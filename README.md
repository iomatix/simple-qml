# Simple QML

## Environment Setup: [TensorFlow Quantum Installation Guide](https://www.tensorflow.org/quantum/install)

### Requirements:
- **Python 3.11** (TensorFlow Quantum supports Python 3.9–3.11)
- **GPU with TensorFlow 2.15 support** *(Ensure proper CUDA and cuDNN setup)*
- **Note for Windows Users:** TensorFlow Quantum isn’t officially supported on Windows. It’s recommended to use Windows Subsystem for Linux (WSL).

---

## Native Installation on Linux/macOS (or via WSL on Windows)

### Step-by-Step Setup:

1. **Install Python 3.11:**  
   [Download Python 3.11](https://www.python.org/downloads/release/python-31111/) (skip if already installed)

2. **Create a Virtual Environment for Python 3.11:**

   ```bash
   python3.11 -m venv .venv
   ```

3. **Activate the Environment:**
   - Linux/macOS (or WSL on Windows):

       ```bash
       source .venv/bin/activate
       ```

4. **Verify the Environment is Active:**

   ```bash
    which python  # Should output a path like ".venv/bin/python"
   ```

5. **Upgrade and Ensure pip:**

   ```bash
    python -m pip install --upgrade pip
    python -m pip --version
   ```

6. **Install TensorFlow and TensorFlow Quantum:**

   ```bash
    python -m pip install tensorflow==2.15.0
    python -m pip install tensorflow-quantum==0.7.3
   ```

7. **Install Qiskit:**
    [Qiskit Installation Guide](https://docs.quantum.ibm.com/guides/install-qiskit)

   ```bash
    python -m pip install qiskit
   ```

8. **Optional - Install Qiskit Runtime (for Quantum Hardware Jobs):**

   ```bash
    python -m pip install qiskit-ibm-runtime
   ```

## Windows Native Setup (Using WSL)

Since TensorFlow Quantum isn’t officially supported on native Windows, you should use Windows Subsystem for Linux (WSL).

1. **Enable WSL and Install a Linux Distribution:**
   - Open PowerShell as Administrator and run:

       ```powershell
        wsl --install
       ```

   - Restart your computer when prompted, then set up your preferred Linux distribution (e.g., Ubuntu).

2. **Open Your WSL Terminal and Follow the Instructions:**
    - Inside the WSL terminal, create and activate your virtual environment, and install the required packages using the Linux/macOS commands provided above.

### Note for Visual Studio Code users on Windows

- Open the integrated terminal in VS Code (e.g. via `Ctrl + ~`), and open WSL terminal in current project using `wsl` command.
- Alternatively, in VS Code, press `Ctrl + Shift + P` and from Command Pallette find `WSL` and select `Remote-WSL: Reopen Folder in WSL`. This will open current project in a WSL environment.
