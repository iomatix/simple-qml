import tensorflow as tf
import tensorflow_quantum as tfq
import cirq
import numpy as np
import sympy as mp
from tensorflow.keras import layers, models


# Lib:
    # Quantum Gates: https://www.mathworks.com/discovery/quantum-gates.html
    # Qubits: https://towardsdatascience.com/qubits-explained-everything-you-need-to-know-1c510e6e9f06/

# Goals:
    # Build a parametrized quantum circuit (PQC) that can learn to perform a quantum gate (e.g. XOR, AND, OR, NOT)
    # Teach the QML model to perform the gate by learning the parameters of the PQC.
    
# Steps:
    # Generate data
    # Encode classical data into quantum circuits
        # For each input pair (a,b), create a circuit that prepares the state |a,b>
    # Apply a parametrized quantum circuit (PQC) to teach the QML model.
        # PQC needs to represent the target gate
        # rotation and entangling.
    # Measure the output qubits and compare with expected result using a loss function.
    # Use a classical optimizer (e.g. Adam) to adjust parameters of the PQC.




# Generate data
def generate_data(gate_type):
    input_bits = [[0, 0], [0, 1], [1, 0], [1, 1]] # Pair e.g. [0, 0] needs two qubits in an encoder
    if gate_type == 'XOR':
        labels = [0, 1, 1, 0]
    elif gate_type == 'AND':
        labels = [0, 0, 0, 1]
    elif gate_type == 'OR':
        labels = [0, 1, 1, 1]
    elif gate_type == 'NOT':
        input_bits = [[0], [1]] # Single value e.g. [0] needs one qubit in the encoder
        labels = [1, 0]
    else:
        raise ValueError(f"Unknown gate type: {gate_type}")
    return input_bits, labels 

# Encode data by creating a circuit that prepares the state |a,b>
    # For each bit eq to 1 in the input, apply an X gate to the corresponding qubit to flip it from |0> to |1>
def encode_data(input_bits, qbits):
    circuit = cirq.Circuit() 
    for i, bit in enumerate(input_bits):
        if bit == 1:
            circuit.append(cirq.X(qbits[i])) # flip |0> to |1> by applying Pauli-X Gate
    return circuit

# Function that builds a parametrized circuit (PQC).
# This function should include fixed gates (e.g. Hadamard Gate for superposition), entalnging gates (e.g. CNOT), and learnable gates (like rotation gates with sympy symbols).
def create_pqc(qbits):
    qubits_num = len(qbits)
    qubits = [cirq.LineQubit(i) for i in range(qubits_num)]
    circuit = cirq.Circuit()
    # Apply Hadamard to each qubit to create superposition
    circuit.append(cirq.H.on_each(*qubits))
    # Parametrized rotations for learnable parameters using sympy symbols
        # Rx -> theta, Ry -> phi, Rz -> lambda
    theta, phi = mp.symbols('theta phi')
    circuit.append(cirq.rx(theta).on(qubits[0])) # rotate first qubit on X-axis
    if len(qubits) > 1: # if there are more qubits, rotate second one, and then apply CNOT gates to entangle qubits. In this case sohuld be maximum 2 qubits
        circuit.append(cirq.ry(phi).on(qubits[1]))
        for i in range(qubits_num - 1):
            circuit.append(cirq.CNOT(qubits[i], qubits[i+1])) # entangle each qubit with the next one
    return circuit  

# Setup input
gate_name = 'XOR' # XOR, AND, OR, NOT
input_bits, labels = generate_data(gate_name) 

# Define qubits, default value of qubit is |0>
    # LineQubit(i) = GridQubit(0, i) means that qubits are arranged in a one-dimensional space (line).
qubits = [cirq.LineQubit(i) for i in range(len(input_bits[0]))] # Initialize qubits, one qubit per each input's value. Let's assume symmetry in next values.  

# Encode each sample
circuits = [encode_data(bits, qubits) for bits in input_bits] # Initialize circuit for each input

# Define and apply a parametrized quantum circuit (PQC) to teach the QML model.
# Integrate the PQC into a TF Keras model
pqc_layer = tfq.layers.PQC(create_pqc(qubits), cirq.Z(qubits[0])) # cirq.Z(qubits[0]) is the target gate - Pauli-Z Gate as measurement qubit
model = models.Sequential([ # Sequential in Keras is used for models where layers are stacked linearly, meaning each layer has exactly one input tensor and one output tensor.
    layers.Input(
        shape=(), # scalar input, 0-dimensional tensor. TFQ expects each input to be a serialized quantum circuit, represented as a string.
        dtype=tf.string # Like above note, TFQ expects string
        ),
    pqc_layer
])

# Compile and train the model
X_train = tfq.convert_to_tensor(circuits) # Prepare dataset for the model by converting the list of Cirq circuits to a tensor that TFQ can work with.
y_train = tfq.convert_to_tensor(labels) # Prepare dataset for the model by converting the list of labels to a tensor that TFQ can work with.

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.1), # Define optimizer
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), # Define loss function, the measure
              metrics=['accuracy']) # Define loss function and metrics for the model.
model.fit(X_train, y_train, epochs=200, verbose=1) # Train the model

predictions = model.predict(X_train)
print("Gate: ${gate_name}")
print("Predictions (logits):", predictions)


# Function to test the model
def test_model(model, new_input_bits):
    # Define qubits
    qubits = [cirq.LineQubit(i) for i in range(len(new_input_bits[0]))]
    
    # Encode new input data into quantum circuits
    new_circuits = [encode_data(bits, qubits) for bits in new_input_bits]
    
    # Convert circuits to tensors
    X_test = tfq.convert_to_tensor(new_circuits)
    
    # Use the model to make predictions
    predictions = model.predict(X_test)
    
    # Apply a sigmoid function to convert logits to probabilities
    probabilities = tf.sigmoid(predictions).numpy()
    
    # Convert probabilities to binary predictions (0 or 1)
    binary_predictions = (probabilities > 0.5).astype(int)
    
    return binary_predictions


# Test 
new_input_bits = [[0, 0], [1, 1], [0, 1], [1, 0]]
predictions = test_model(model, new_input_bits)

print("Testing ${gate_name} with new input bits: ${new_input_bits}")
print("Predictions:", predictions)