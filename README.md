
# Simple QML

## Table of Contents

- [Simple QML](#simple-qml)
  - [Table of Contents](#table-of-contents)
    - [Installation Guide](#installation-guide)
      - [Requirements](#requirements)
    - [Native Installation on Linux/macOS](#native-installation-on-linuxmacos)
      - [Step-by-Step Setup](#step-by-step-setup)
        - [1. **Install Python 3.11:**](#1-install-python-311)
        - [2. **Create a Virtual Environment for Python 3.11:**](#2-create-a-virtual-environment-for-python-311)
        - [3. **Activate the Environment:**](#3-activate-the-environment)
        - [4. **Verify the Environment is Active:**](#4-verify-the-environment-is-active)
        - [5. **Upgrade and Ensure pip:**](#5-upgrade-and-ensure-pip)
        - [6. **Install TensorFlow and TensorFlow Quantum:**](#6-install-tensorflow-and-tensorflow-quantum)
        - [7. **Install Qiskit:**](#7-install-qiskit)
        - [8. **Optional - Install Qiskit Runtime (for Quantum Hardware Jobs):**](#8-optional---install-qiskit-runtime-for-quantum-hardware-jobs)
    - [Windows Native Setup (Using WSL)](#windows-native-setup-using-wsl)
        - [1. **Enable WSL and Install a Linux Distribution:**](#1-enable-wsl-and-install-a-linux-distribution)
        - [2. **Open Your WSL Terminal and Follow the Instructions:**](#2-open-your-wsl-terminal-and-follow-the-instructions)
      - [Note for Visual Studio Code users on Windows](#note-for-visual-studio-code-users-on-windows)

---

### Installation Guide

[TensorFlow Quantum Installation Guide](https://www.tensorflow.org/quantum/install)

#### Requirements
  
- **Python 3.11** (TensorFlow Quantum supports Python 3.9–3.11)

- **GPU with TensorFlow 2.15 support**  *(Ensure proper [CUDA](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html) and [cuDNN](https://developer.nvidia.com/cudnn) setup)*

- **Note for Windows Users:** TensorFlow Quantum isn’t officially supported on Windows. It’s recommended to use Windows Subsystem for Linux (WSL).

---

### Native Installation on Linux/macOS

#### Step-by-Step Setup

##### 1. **Install Python 3.11:**

[Download Python 3.11](https://www.python.org/downloads/release/python-31111/) and [install it](INSTRUCTIONS_PYTHON.md#Python-installation-on-Ubuntu).

##### 2. **Create a Virtual Environment for Python 3.11:**

```bash

python3.11 -m venv .venv

```

##### 3. **Activate the Environment:**

- Linux/macOS (or WSL on Windows):

```bash

source .venv/bin/activate

```

##### 4. **Verify the Environment is Active:**

```bash

which python # Should output a path like ".venv/bin/python"

```

##### 5. **Upgrade and Ensure pip:**

```bash

python -m pip install --upgrade pip

python -m pip --version

```

##### 6. **Install TensorFlow and TensorFlow Quantum:**

```bash

python -m pip install tensorflow==2.15.0

python -m pip install tensorflow-quantum==0.7.3

```

##### 7. **Install Qiskit:**

[Qiskit Installation Guide](https://docs.quantum.ibm.com/guides/install-qiskit)

```bash

python -m pip install qiskit

```

##### 8. **Optional - Install Qiskit Runtime (for Quantum Hardware Jobs):**

```bash

python -m pip install qiskit-ibm-runtime

```

### Windows Native Setup (Using WSL)

Since TensorFlow Quantum isn’t officially supported on native Windows, you should use Windows Subsystem for Linux (WSL).

##### 1. **Enable WSL and Install a Linux Distribution:**

- Personally I recommend Ubuntu or Fedora. Important note is that the distribution should be supported by [CUDA](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu).

- Example below shows installation of Ubuntu distribution (24.04 LTS).

- Open PowerShell as Administrator and run:

```powershell

wsl --update

wsl --install -d Ubuntu-24.04

wsl --setdefault Ubuntu-24.04

wsl --status

wsl -l -v

```

##### 2. **Open Your WSL Terminal and Follow the Instructions:**

- Within the WSL terminal, [create and activate your virtual environment, and install the required packages using the Linux/macOS commands provided above](#native-installation-on-linuxmacos).

#### Note for Visual Studio Code users on Windows

- Open the integrated terminal in VS Code (e.g. via `Ctrl + ~`), and open WSL terminal in current project using `wsl` command.

- Alternatively, in VS Code, press `Ctrl + Shift + P` and from Command Pallette find `WSL` and select `Remote-WSL: Reopen Folder in WSL`. This will open current project in a WSL environment.
