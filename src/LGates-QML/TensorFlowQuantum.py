import tensorflow as tf
import tensorflow_quantum as tfq
import cirq
import numpy as np
import sympy as mp
from tensorflow.keras import layers, models


# Lib:
    # Quantum Gates: https://www.mathworks.com/discovery/quantum-gates.html
    
    
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
def encode_data(input_bits, qubits):
    circuit = cirq.Circuit() 
    for i, bit in enumerate(input_bits):
        if bit == 1:
            circuit.append(cirq.X(qubits[i])) # flip |0> to |1> by applying Pauli-X Gate
    return circuit

# Function that builds a parametrized circuit (PQC).
# This function should include fixed gates (e.g. Hadamard Gate for superposition), entalnging gates (e.g. CNOT), and learnable gates (like rotation gates with sympy symbols).
def create_pqc(qubits_num):
    # qubits = [circq.LineQubit(1) for i in range(qubits_num)]
    # TODO
    

# Setup input
input_bits, labels = generate_data('XOR') # XOR, AND, OR, NOT

# Define qubits, default value of qubit is |0>
    # LineQubit(i) = GridQubit(0, i) means that qubits are arranged in a one-dimensional space (line).
qubits = [cirq.LineQubit(i) for i in range(len(input_bits[0]))] # Initialize qubits, one qubit per each input's value. Let's assume symmetry in next values.  

# Encode each sample
circuits = [encode_data(bits, qubits) for bits in input_bits] # Initialize circuit for each input

# Define and apply a parametrized quantum circuit (PQC) to teach the QML model.
tfq.convert_to_tensor(circuits) # Prepare dataset for the model by converting the list of Cirq circuits to a tensor that TFQ can work with.
