# PinRooter

PinRooter is a dynamic Frida script execution tool designed to automate the process of running root and SSL bypass scripts on mobile applications. It supports both predefined and codeshare scripts, as well as real-time script execution for debugging, penetration testing, or app analysis.

---

## Features

- **Run Predefined Scripts**: Easily execute root, SSL bypass, or combined scripts.
- **Dynamic Codeshare Support**: Run Frida Codeshare scripts directly from a file.
- **Interactive Process**: List installed applications or attach to a specific app.
- **Script Management**: Organize and execute scripts from the `Root`, `SSL`, or `Both` directories.
- **Error Handling**: Provides clear feedback for common issues like missing files or incorrect configurations.

---

## Prerequisites

1. **Python 3.6 or above** installed.
2. **Frida Toolkit**:
   - Install Frida using pip:
     ```bash
     pip install frida-tools
     ```
   - Make sure Frida is compatible with your target device (Android/iOS).
3. **Rooted or Jailbroken Device**: Required for bypassing SSL and root restrictions.

---

## Folder Structure

   ```bash
Scripts/
├── Root/    # Root bypass scripts
├── SSL/     # SSL bypass scripts
└── Both/    # Combined scripts
|__ PinRooter.py
   ```

Place your custom Frida scripts in the respective directories.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/PinRooter.git
   cd PinRooter
   ```


## Usage

### General Syntax

```bash
python frida_tool.py [OPTIONS] app_identifier
```

### Options

- `-n <NUMBER>` : Run scripts based on the number:
  - `1` for Root bypass scripts.
  - `2` for SSL bypass scripts.
  - `3` for both Root and SSL bypass scripts combined.
- `-r` : Run all scripts in the `Root/` folder.
- `-s` : Run all scripts in the `SSL/` folder.
- `-b` : Run all scripts in the `Both/` folder.
- `-i` : List all installed applications using `frida-ps -Uai`.
- `-h` : Display help information.

---

### Examples

1. **List Installed Applications**:
   ```bash
   python frida_tool.py -i
   ```

2. **Run a Codeshare Script**:
   ```bash
   python frida_tool.py -n 1 com.example.app
   ```

3. **Run All Root Scripts**:
   ```bash
   python frida_tool.py -r com.example.app
   ```

4. **Run Combined Scripts**:
   ```bash
   python frida_tool.py -b com.example.app
   ```




