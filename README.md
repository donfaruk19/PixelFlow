# 🎨 PixelFlow: CLI Image Encryption Tool

## Overview
PixelFlow is a command-line interface (CLI) tool designed for image encryption and decryption through pixel manipulation. Developed as a task for Prodigy Infotech, this tool provides a secure and intuitive way to protect your images using advanced encryption techniques.

## Features
* **🔧 Self-Setup Environment:** Automatically creates a Python virtual environment and installs all necessary dependencies (`Pillow`, `numpy`, `colorama`) upon first run, ensuring a smooth setup process.
* **💻 Interactive CLI:** A user-friendly command-line interface with clear prompts, color-coded output, and options to quit (`q`) or go back (`b`) at almost any step.
* **📁 Dynamic File Selection:** Allows users to browse directories and select image files directly from the CLI, simplifying input and key image selection.
* **🔐 Multiple Encryption Methods:**
    * **Shift Cipher:** A simple pixel-shifting technique where a numerical key (1-255) is added to or subtracted from each RGB color component.
    * **XOR Cipher:** Performs a bitwise XOR operation on pixel values. Supports both a numerical key (1-255) or another image as a key.
    * **Shuffle Cipher:** Rearranges image blocks based on a numerical seed (1-255). Requires image dimensions to be perfectly divisible by the predefined block size (16x16 pixels).
* **🔑 Flexible Key Management:**
    * Direct numerical input for keys (1-255).
    * Generate numerical keys from a user-provided passphrase using SHA-256 hashing.
    * Option to use a separate image as a key for XOR encryption.
* **💾 Output File Handling:** Prompts for output file name, includes an overwrite warning, and automatically saves in common image formats (PNG, JPG, BMP). Defaults to PNG if an unknown format is specified.
* **👁️ Open Output File:** After successful processing, offers to open the resulting image directly in the system's default image viewer.
* **📖 Comprehensive Help Guide:** An integrated help section provides detailed explanations of all features, encryption methods, key types, and usage instructions.
* **⚠️ Robust Error Handling:** Provides informative messages for file not found errors, invalid inputs, and method-specific requirements (e.g., image dimensions for shuffle).

## Installation & Setup
PixelFlow is designed to be self-setting up. Follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/donfaruk19/PixelFlow.git
    cd PixelFlow
    ```

2.  **Run the Script:**
    Open your terminal or command prompt and run:
    ```bash
    python pixelflow.py
    ```
    The script will automatically check for a virtual environment (`.venv`) and required dependencies. If not found, it will create the virtual environment and install `Pillow`, `numpy`, and `colorama`.

## How to Use

Upon running the script, you'll be greeted by an interactive command-line interface:

1.  **Main Menu:**
    Choose to `e`ncrypt, `d`ecrypt, or get `h`elp.
    ```
    Enter mode (e/encrypt, d/decrypt, h/help):
    ```

2.  **Select Input Image:**
    You can either enter the full path to your image manually (`1`) or browse through the current directory and its subdirectories (`2`) to select an image (`.jpg`, `.png`, `.jpeg`, `.bmp`).
    ```
    Select input image (1: Enter path manually, 2: Select from current directory/subdirectories):
    ```

3.  **Specify Output File Name:**
    Enter the desired name for your processed image. The tool will warn you if the file already exists and ask for confirmation to overwrite.
    ```
    Enter the output file name (e.g., encrypted_output.png):
    ```

4.  **Choose Encryption Method:**
    Select your preferred method:
    * `s` / `shift` (Shift Cipher)
    * `x` / `xor` (XOR Cipher)
    * `f` / `shuffle` (Shuffle Cipher)
    ```
    Choose encryption method (s/shift, x/xor, f/shuffle):
    ```

5.  **Provide Key Information:**
    The key prompt will vary based on the chosen method:
    * **Shift/Shuffle:** You'll choose between `d`irect numerical input (1-255) or generating a key `p`from a passphrase.
    * **XOR:** You'll choose between a `n`umerical key (1-255) or an `i`mage key. If selecting an image key, you'll go through the file selection process again for the key image.

6.  **Process and Save:**
    The tool will process the image and save it to the specified output path.

7.  **Open Output:**
    After saving, you'll be asked if you wish to open the newly created image in your system's default viewer.
    ```
    Do you want to open the output file? (y: Yes, n: No):
    ```

### Global Commands
At most prompts, you can enter:
* `q` or `quit`: To exit the program entirely.
* `b` or `back`: To return to the previous step in the process.

## Requirements
- Python 3.7 or higher
- The script will automatically install these packages if they are not found:
  * `Pillow` (PIL Fork) - Image processing
  * `numpy` - Numerical operations
  * `colorama` - Colored terminal output

## Project Structure
```
PixelFlow/
├── pixelflow.py          # Main application script
├── README.md             # This file
├── LICENSE               # GNU General Public License
└── requirements.txt      # Python dependencies (optional)
```

## Encryption Methods Explained

### 1. Shift Cipher
- **How it works:** Adds or subtracts a numerical key from each RGB value of every pixel.
- **Best for:** Quick, simple encryption.
- **Key range:** 1-255

### 2. XOR Cipher
- **How it works:** Performs bitwise XOR operation on pixel values.
- **Best for:** Moderate security with good performance.
- **Key options:** Numerical key or image-based key
- **Key range:** 1-255 (for numerical key)

### 3. Shuffle Cipher
- **How it works:** Rearranges image blocks (16x16 pixels) based on a seed value.
- **Best for:** Visual scrambling of image content.
- **Requirements:** Image dimensions must be divisible by 16
- **Key range:** 1-255

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Author
**Abdullahi Umar Faruk**

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Support
If you encounter any issues or have questions, please open an issue on the [GitHub repository](https://github.com/donfaruk19/PixelFlow/issues).
