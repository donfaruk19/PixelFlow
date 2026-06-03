import subprocess
import sys
import os
import platform
import re
import hashlib

# Define the virtual environment directory name
VENV_DIR = ".venv"
# List of required packages
REQUIRED_PACKAGES = ["Pillow", "numpy", "colorama"]

# --- Self-Setup Virtual Environment and Dependencies ---
def setup_environment():
    """
    Checks if running in a venv and if packages are installed.
    Creates venv and installs packages if necessary, then re-executes.
    """
    in_venv = (sys.prefix != sys.base_prefix)
    all_packages_installed = True
    
    # Check if packages are installed
    for package in REQUIRED_PACKAGES:
        try:
            if package == "Pillow":
                __import__("PIL")
            else:
                __import__(package.lower().replace('-', '_'))
        except ImportError:
            all_packages_installed = False
            break

    # If already in venv and all packages installed, proceed
    if in_venv and all_packages_installed:
        return

    # Print colored output without colorama import yet
    print("--- Setting up environment ---")

    venv_path = os.path.join(os.getcwd(), VENV_DIR)
    
    if platform.system() == "Windows":
        python_executable = os.path.join(venv_path, "Scripts", "python.exe")
        pip_executable = os.path.join(venv_path, "Scripts", "pip.exe")
    else:
        python_executable = os.path.join(venv_path, "bin", "python")
        pip_executable = os.path.join(venv_path, "bin", "pip")

    # Create virtual environment if it doesn't exist
    if not os.path.exists(venv_path):
        print(f"Creating virtual environment at '{venv_path}'...")
        try:
            subprocess.check_call([sys.executable, "-m", "venv", venv_path])
            print("Virtual environment created successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error creating virtual environment: {e}")
            print("Please ensure 'python3 -m venv' is available on your system.")
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred while creating venv: {e}")
            sys.exit(1)
    else:
        print(f"Virtual environment already exists at '{venv_path}'.")

    # Install packages if not already installed
    if not all_packages_installed:
        print(f"Installing required packages: {', '.join(REQUIRED_PACKAGES)}...")
        try:
            # Use python -m pip for better cross-platform compatibility (especially on Windows)
            install_command = [python_executable, "-m", "pip", "install", "--upgrade", "pip"]
            subprocess.check_call(install_command)
            print("Pip upgraded successfully.")
            
            install_command = [python_executable, "-m", "pip", "install"] + REQUIRED_PACKAGES
            subprocess.check_call(install_command)
            print("All required packages installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing packages: {e}")
            print(f"Please try installing manually within the venv: '{python_executable} -m pip install {' '.join(REQUIRED_PACKAGES)}'")
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred while installing packages: {e}")
            sys.exit(1)
    else:
        print("All required packages are already installed.")

    # Relaunch script in virtual environment
    print("Relaunching script in virtual environment...")
    try:
        # Use subprocess instead of os.execv to properly handle paths with spaces
        subprocess.call([python_executable, sys.argv[0]] + sys.argv[1:])
        sys.exit(0)
    except Exception as e:
        print(f"Error relaunching script: {e}")
        sys.exit(1)

setup_environment()

# Now import colorama after virtual environment is set up
from colorama import init, Fore, Style
from PIL import Image
import numpy as np

init()

ANSI_ESCAPE_PATTERN = re.compile(r'\x1b\[[0-9;]*m')

# --- Unique CLI Header Design ---
BORDER_COLOR = Fore.MAGENTA
TITLE_COLOR = Fore.CYAN
SUB_TITLE_COLOR = Fore.LIGHTCYAN_EX
AUTHOR_COLOR = Fore.GREEN
HEADER_WIDTH = 50

def center_header_text(text, width, color=None):
    visible_text = ANSI_ESCAPE_PATTERN.sub('', text)
    text_len = len(visible_text)
    
    padding_left = (width - text_len) // 2
    padding_right = width - text_len - padding_left
    
    formatted_text = " " * padding_left + text + " " * padding_right
    
    if color:
        return color + formatted_text + Style.RESET_ALL
    return formatted_text

print(BORDER_COLOR + "╔" + "═" * HEADER_WIDTH + "╗" + Style.RESET_ALL)
print(BORDER_COLOR + "║" + center_header_text("", HEADER_WIDTH) + "║" + Style.RESET_ALL)
# --- MODIFIED ASCII ART TITLE FOR CLARITY: "IMAGE" ---
print(BORDER_COLOR + "║" + center_header_text(TITLE_COLOR + "█  █ █ ███ ███ ███", HEADER_WIDTH, None) + BORDER_COLOR + "║" + Style.RESET_ALL) # IMAGE top part
print(BORDER_COLOR + "║" + center_header_text(TITLE_COLOR + "█  ███ █ █ █ █ ███", HEADER_WIDTH, None) + BORDER_COLOR + "║" + Style.RESET_ALL) # IMAGE bottom part
# --- END MODIFIED ASCII ART TITLE ---
print(BORDER_COLOR + "║" + center_header_text("", HEADER_WIDTH) + "║" + Style.RESET_ALL)
print(BORDER_COLOR + "║" + center_header_text(SUB_TITLE_COLOR + "E N C R Y P T I O N   T O O L", HEADER_WIDTH, None) + BORDER_COLOR + "║" + Style.RESET_ALL)
print(BORDER_COLOR + "║" + center_header_text("", HEADER_WIDTH) + "║" + Style.RESET_ALL)
print(BORDER_COLOR + "║" + center_header_text(AUTHOR_COLOR + "By Abdullahi Umar Faruk", HEADER_WIDTH, None) + BORDER_COLOR + "║" + Style.RESET_ALL)
print(BORDER_COLOR + "║" + center_header_text("", HEADER_WIDTH) + "║" + Style.RESET_ALL)
print(BORDER_COLOR + "╚" + "═" * HEADER_WIDTH + "╝" + Style.RESET_ALL)

print(Fore.YELLOW + "Task: Pixel Manipulation for Image Encryption")
print(Fore.RED + "Copyright © 2025 Prodigy Infotech. All rights reserved.")
print("WARNING: Unauthorized use or distribution is prohibited.")
print(Fore.RESET + "═" * (HEADER_WIDTH + 2) + "\n")

# --- Helper function for consistent user input and flow control ---
def get_user_choice(prompt_text, valid_options=None, allow_back=True):
    while True:
        back_option = ", b: Back" if allow_back else ""
        user_input = input(f"{Fore.BLUE}{prompt_text} (q: Quit{back_option}): {Style.RESET_ALL}").strip().lower()

        if user_input == 'q':
            return 'QUIT' # Sentinel value for quitting the entire program
        if allow_back and user_input == 'b':
            return 'BACK' # Sentinel value for going back one step

        if valid_options is None: # No specific validation needed, just return input
            return user_input
        elif user_input in valid_options:
            return user_input
        else:
            print(f"{Fore.RED}Invalid input. Please choose from the valid options: {', '.join(valid_options)}.{Style.RESET_ALL}\n")

# --- Modified get_file_path to integrate 'QUIT' and 'BACK' ---
def get_file_path(prompt, allow_back=True):
    while True:
        choice = get_user_choice(f"{prompt} (1: Enter path manually, 2: Select from current directory/subdirectories)", 
                                 valid_options=['1', '2'], allow_back=allow_back)
        
        if choice == 'QUIT':
            return 'QUIT'
        if choice == 'BACK':
            return 'BACK' # Indicate that we need to go back to the previous step in the main flow
        
        if choice == "1":
            path = get_user_choice(f"Enter the full path (e.g., image.jpg or /path/to/image.jpg)", allow_back=True)
            if path in ['QUIT', 'BACK']: return path # Propagate QUIT/BACK from sub-prompt
            return path
        
        elif choice == "2":
            current_dir = os.getcwd()
            print(f"{Fore.BLUE}Scanning: {current_dir}{Style.RESET_ALL}")
            
            all_entries = sorted(os.listdir(current_dir))
            
            selectable_paths = [] 
            
            if os.path.dirname(current_dir) != current_dir:
                selectable_paths.append(("[DIR] ..", os.path.dirname(current_dir), True))

            for entry_name in all_entries:
                full_path = os.path.join(current_dir, entry_name)
                if os.path.isdir(full_path):
                    selectable_paths.append((f"[DIR] {entry_name}", full_path, True))
                elif os.path.isfile(full_path) and entry_name.lower().endswith(('.jpg', '.png', '.jpeg', '.bmp')):
                    selectable_paths.append((f"[IMG] {entry_name}", full_path, False))
            
            if not selectable_paths:
                print(f"{Fore.RED}No relevant items (directories or images) found in current directory! Please use manual entry or go back.{Style.RESET_ALL}\n")
                continue

            print(f"{Fore.BLUE}Available items (select by number):{Style.RESET_ALL}")
            for i, (display_name, _, _) in enumerate(selectable_paths):
                print(f"{i+1}. {display_name}")
            
            try:
                selection_input = get_user_choice("Select an item (enter number)", allow_back=True)
                if selection_input in ['QUIT', 'BACK']: return selection_input # Propagate QUIT/BACK
                
                selection_index = int(selection_input) - 1
                
                if 0 <= selection_index < len(selectable_paths):
                    selected_display_name, selected_full_path, is_dir = selectable_paths[selection_index]
                    
                    if is_dir:
                        os.chdir(selected_full_path)
                        print(f"{Fore.GREEN}Changed directory to: {os.getcwd()}{Style.RESET_ALL}")
                        # If directory is changed, re-run get_file_path from current dir
                        # This recursive call will handle its own QUIT/BACK
                        result = get_file_path(prompt, allow_back)
                        if result in ['QUIT', 'BACK']: return result # Propagate if quit/back from recursive call
                        return result
                    else:
                        return selected_full_path
                else:
                    print(f"{Fore.RED}Invalid selection number! Please choose a number from the list.{Style.RESET_ALL}\n")
            except ValueError:
                print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}\n")
            except IndexError:
                print(f"{Fore.RED}An unexpected selection error occurred. Please try again.{Style.RESET_ALL}\n")
            except Exception as e:
                print(f"{Fore.RED}An error occurred during selection: {e}{Style.RESET_ALL}\n")

def generate_key_from_passphrase(passphrase_str):
    """Generates a numerical key (1-255) from a passphrase using SHA-256."""
    if not passphrase_str:
        return None
    try:
        passphrase_bytes = passphrase_str.encode('utf-8')
        hash_digest = hashlib.sha256(passphrase_bytes).hexdigest()
        numerical_key = (int(hash_digest, 16) % 255) + 1
        return numerical_key
    except Exception as e:
        print(f"{Fore.RED}Error generating key from passphrase: {e}{Style.RESET_ALL}")
        return None

# --- CONSTANT FOR SHUFFLE BLOCK SIZE ---
SHUFFLE_BLOCK_SIZE = 16 # Pixels per side of a square block (e.g., 16x16 pixels)

def open_file_in_default_viewer(filepath):
    """
    Opens a file using the default viewer for the current operating system.
    """
    try:
        if platform.system() == "Windows":
            os.startfile(filepath)
        elif platform.system() == "Darwin":  # macOS
            subprocess.call(['open', filepath])
        else:  # Linux and other Unix-like systems
            subprocess.call(['xdg-open', filepath])
        print(f"{Fore.GREEN}Opened '{os.path.basename(filepath)}' in default viewer.{Style.RESET_ALL}")
    except FileNotFoundError:
        print(f"{Fore.RED}Error: Default viewer not found or file path is incorrect.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Could not open file automatically: {e}{Style.RESET_ALL}")


def process_image(input_path, output_path, method, mode, key_value=None, key_image_path=None):
    """
    Generic function to encrypt or decrypt an image using specified method.
    method: 'shift', 'xor', or 'shuffle'
    mode: 'encrypt' or 'decrypt' (expected to be exact strings 'encrypt' or 'decrypt')
    key_value: integer key for 'shift', 'xor' numerical, or 'shuffle' (as seed)
    key_image_path: path to an image file to use as a key for 'xor' with image key
    """
    print(f"\n{Fore.CYAN}--- Starting image processing ---{Style.RESET_ALL}")
    try:
        print(f"{Fore.CYAN}Loading image '{os.path.basename(input_path)}'...{Style.RESET_ALL}")
        img = Image.open(input_path)
        img = img.convert('RGB')
        img_array = np.array(img, dtype=np.uint8)
        print(f"{Fore.GREEN}Image loaded successfully.{Style.RESET_ALL}")

        height, width, channels = img_array.shape
        processed_array = None

        print(f"{Fore.CYAN}Applying {mode} with {method} method...{Style.RESET_ALL}")

        if method == 'shift':
            if key_value is None:
                raise ValueError("Numerical key must be provided for 'shift' method.")
            
            temp_array = img_array.astype(np.int16) 
            if mode == 'encrypt':
                processed_array = (temp_array + key_value) % 256
            elif mode == 'decrypt':
                processed_array = (temp_array - key_value) % 256
            else:
                 raise ValueError(f"Invalid mode for shift method: {mode}. Expected 'encrypt' or 'decrypt'.")
            processed_array = processed_array.astype(np.uint8)

        elif method == 'xor':
            if key_image_path:
                print(f"{Fore.BLUE}Loading key image from '{os.path.basename(key_image_path)}'...{Style.RESET_ALL}")
                key_img = Image.open(key_image_path)
                key_img = key_img.convert('RGB')

                if key_img.size != img.size:
                    print(f"{Fore.YELLOW}Warning: Key image dimensions ({key_img.size}) do not match input image ({img.size}). Resizing key image.{Style.RESET_ALL}")
                    key_img = key_img.resize(img.size)
                
                key_array = np.array(key_img, dtype=np.uint8)
                processed_array = (img_array ^ key_array).astype(np.uint8)
                print(f"{Fore.GREEN}Key image loaded and processed.{Style.RESET_ALL}")

            elif key_value is not None:
                processed_array = (img_array ^ key_value).astype(np.uint8)
            else:
                raise ValueError("Either a numerical key or a key image path must be provided for 'xor' method.")
            
        elif method == 'shuffle':
            if key_value is None:
                raise ValueError("Numerical key (seed) must be provided for 'shuffle' method.")
            
            if height % SHUFFLE_BLOCK_SIZE != 0 or width % SHUFFLE_BLOCK_SIZE != 0:
                raise ValueError(f"Image dimensions ({width}x{height}) must be perfectly divisible by BLOCK_SIZE ({SHUFFLE_BLOCK_SIZE}) for shuffling. Please choose another image or method.")
            
            num_blocks_h = height // SHUFFLE_BLOCK_SIZE
            num_blocks_w = width // SHUFFLE_BLOCK_SIZE
            total_blocks = num_blocks_h * num_blocks_w

            blocks = img_array.reshape(num_blocks_h, SHUFFLE_BLOCK_SIZE, 
                                       num_blocks_w, SHUFFLE_BLOCK_SIZE, channels)
            blocks = blocks.swapaxes(1, 2)
            blocks = blocks.reshape(total_blocks, SHUFFLE_BLOCK_SIZE, SHUFFLE_BLOCK_SIZE, channels)

            np.random.seed(key_value)
            
            permutation = np.random.permutation(total_blocks)

            if mode == 'encrypt':
                processed_blocks = blocks[permutation]
            elif mode == 'decrypt':
                inverse_permutation = np.argsort(permutation)
                processed_blocks = blocks[inverse_permutation]
            else:
                raise ValueError(f"Invalid mode for shuffle method: {mode}. Expected 'encrypt' or 'decrypt'.")
            
            processed_array = processed_blocks.reshape(num_blocks_h, num_blocks_w,
                                                       SHUFFLE_BLOCK_SIZE, SHUFFLE_BLOCK_SIZE, channels)
            processed_array = processed_array.swapaxes(1, 2)
            processed_array = processed_array.reshape(height, width, channels)

        else:
            raise ValueError("Invalid encryption method specified. Must be 'shift', 'xor', or 'shuffle'.")
        
        print(f"{Fore.GREEN}Processing complete. Generating image from array.{Style.RESET_ALL}")
        processed_img = Image.fromarray(processed_array)
        
        print(f"{Fore.CYAN}Saving processed image to '{os.path.basename(output_path)}'...{Style.RESET_ALL}")
        output_format = output_path.split('.')[-1].upper()
        if output_format not in ['PNG', 'JPG', 'JPEG', 'BMP']:
            output_format = 'PNG'
            print(f"{Fore.YELLOW}Warning: Unknown output format '{output_path.split('.')[-1]}'. Saving as PNG.{Style.RESET_ALL}")
            if '.' not in output_path:
                output_path += ".png"
        
        processed_img.save(output_path, format=output_format)
        
        action_text = "Encrypted" if mode == 'encrypt' else "Decrypted"
        print(f"{Fore.GREEN}{action_text} image saved as {output_path}{Style.RESET_ALL}")
        
        # --- NEW: Ask to open output file ---
        open_choice = get_user_choice(f"Do you want to open the output file?", 
                                      valid_options=['y', 'yes', 'n', 'no'], allow_back=False)
        if open_choice in ['y', 'yes']:
            open_file_in_default_viewer(output_path)
        # --- END NEW ---

        print(f"{Fore.CYAN}--- Image processing finished ---{Style.RESET_ALL}\n")
        return True # Indicate success
    except FileNotFoundError:
        print(f"{Fore.RED}Error: File not found at specified path.{Style.RESET_ALL}\n")
        return False
    except ValueError as ve:
        print(f"{Fore.RED}Error processing image (ValueError): {ve}. Ensure image is valid and meets requirements (e.g., dimensions for shuffle).{Style.RESET_ALL}\n")
        return False
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}{Style.RESET_ALL}\n")
        return False

# Help function
def display_help():
    print(Fore.CYAN + "\n=== Help Section ===")
    print(Fore.GREEN + "About the Tool:")
    print("This Image Encryption Tool uses pixel manipulation to encrypt and decrypt images.")
    print("It allows selection of different encryption methods and key types.")
    print(Fore.YELLOW + "Author: Abdullahi Umar Faruk")
    print(Fore.RESET + "Encryption Methods:")
    print("  - " + Fore.CYAN + "Shift Cipher:" + Fore.RESET + " Adds/subtracts a 'shift' value to each RGB component (pixel_value ± shift) % 256.")
    print("    This uses a numerical key (1-255). The key must be the same for both encryption and decryption.")
    print("  - " + Fore.CYAN + "XOR Cipher:" + Fore.RESET + " Performs a bitwise XOR operation (pixel_value ^ key) on each RGB component.")
    print("    This is a simple bit-flipping cipher. Applying XOR with the same key twice reverses the operation.")
    print("    Supports two key types:")
    print("      - " + Fore.CYAN + "Numerical Key:" + Fore.RESET + " A single number (1-255) applied to all pixels.")
    print("      - " + Fore.CYAN + "Image Key:" + Fore.RESET + " Uses another image as the key. Each pixel of the input image is XORed with the corresponding pixel of the key image. The key image must have the same dimensions as the input image.")
    print("  - " + Fore.CYAN + "Shuffle Cipher:" + Fore.RESET + " Rearranges image blocks to scramble the image visually.")
    print(f"    Uses a numerical key (1-255) as a seed for random permutation of {SHUFFLE_BLOCK_SIZE}x{SHUFFLE_BLOCK_SIZE} pixel blocks.")
    print("    IMPORTANT: Image dimensions (width and height) must be perfectly divisible by the block size.")
    print("    The key must be the same for encryption and decryption to reverse the shuffle.")
    print(Fore.RESET + "Key Generation:")
    print("  - " + Fore.CYAN + "Direct Numerical Input:" + Fore.RESET + " Manually enter a number between 1 and 255.")
    print("  - " + Fore.CYAN + "From Passphrase:" + Fore.RESET + " Enter a text phrase. This tool will convert it into a numerical key (1-255) using a secure hashing algorithm (SHA-256).")
    print(Fore.RESET + "Global Options (available at most prompts):")
    print("  q/quit     - Exit the program at any point.")
    print("  b/back     - Go back to the previous step in the process.")
    print(Fore.RESET + "Main Menu Options:")
    print("  e/encrypt  - Encrypt an image")
    print("  d/decrypt  - Decrypt an image")
    print("  h/help     - Display this help message")
    print(Fore.CYAN + "===================\n")

# --- Main Program Logic (State Machine Style) ---
def main_program_loop():
    current_step = 'MAIN_MENU'
    session_data = {} # To store data like input_path, output_path, etc. between steps

    while True:
        if current_step == 'MAIN_MENU':
            mode_input = get_user_choice(f"Enter mode (e/encrypt, d/decrypt, h/help)", 
                                         valid_options=['e', 'encrypt', 'd', 'decrypt', 'h', 'help'], allow_back=False)
            if mode_input == 'QUIT':
                print(Fore.CYAN + "Exiting PixelFlow. Goodbye!")
                sys.exit()
            elif mode_input in ['h', 'help']:
                display_help()
                continue # Stay in main menu after help
            else:
                session_data['action_mode'] = 'encrypt' if mode_input in ['e', 'encrypt'] else 'decrypt'
                current_step = 'GET_INPUT_IMAGE'
        
        elif current_step == 'GET_INPUT_IMAGE':
            input_path = get_file_path("Select input image", allow_back=True)
            if input_path == 'QUIT': sys.exit()
            if input_path == 'BACK':
                current_step = 'MAIN_MENU'
                continue # Restart loop to go back

            # Check if path is valid (e.g., file exists)
            if not os.path.isfile(input_path):
                print(f"{Fore.RED}Error: Input file not found or is not a valid file: '{input_path}'{Style.RESET_ALL}\n")
                continue # Stay in GET_INPUT_IMAGE step
            
            session_data['input_path'] = input_path
            current_step = 'GET_OUTPUT_PATH'

        elif current_step == 'GET_OUTPUT_PATH':
            output_path_input = get_user_choice(f"Enter the output file name (e.g., encrypted_output.png)", allow_back=True)
            if output_path_input == 'QUIT': sys.exit()
            if output_path_input == 'BACK':
                current_step = 'GET_INPUT_IMAGE'
                continue # Restart loop to go back
            
            if not output_path_input:
                print(f"{Fore.RED}Output file name cannot be empty!{Style.RESET_ALL}\n")
                continue

            # --- OVERWRITE CHECK ---
            if os.path.exists(output_path_input):
                print(f"{Fore.YELLOW}Warning: Output file '{output_path_input}' already exists!{Style.RESET_ALL}")
                overwrite_choice = get_user_choice(f"Do you want to overwrite it?", valid_options=['y', 'yes', 'n', 'no'], allow_back=True)
                
                if overwrite_choice == 'QUIT': sys.exit()
                if overwrite_choice == 'BACK':
                    current_step = 'GET_INPUT_IMAGE' # Go back to input image selection
                    continue
                if overwrite_choice in ['n', 'no']:
                    print(f"{Fore.BLUE}Please enter a different output file name.{Style.RESET_ALL}\n")
                    current_step = 'GET_OUTPUT_PATH' # Stay in this step to re-enter new name
                    continue
                # If 'y' or 'yes', flow continues normally
            # --- END OVERWRITE CHECK ---

            session_data['output_path'] = output_path_input
            current_step = 'GET_ENCRYPTION_METHOD'

        elif current_step == 'GET_ENCRYPTION_METHOD':
            method_choice = get_user_choice(f"Choose encryption method (s/shift, x/xor, f/shuffle)", 
                                            valid_options=['s', 'shift', 'x', 'xor', 'f', 'shuffle'], allow_back=True)
            if method_choice == 'QUIT': sys.exit()
            if method_choice == 'BACK':
                current_step = 'GET_OUTPUT_PATH'
                continue # Restart loop to go back

            if method_choice in ['s', 'shift']:
                session_data['encryption_method'] = 'shift'
            elif method_choice in ['x', 'xor']:
                session_data['encryption_method'] = 'xor'
            elif method_choice in ['f', 'shuffle']:
                session_data['encryption_method'] = 'shuffle'
            
            current_step = 'GET_KEY_INFO'

        elif current_step == 'GET_KEY_INFO':
            encryption_method = session_data['encryption_method']
            key_val = None
            key_img_path = None
            
            if encryption_method == 'shift' or encryption_method == 'shuffle':
                key_source_choice = get_user_choice(f"How to get numerical key for '{encryption_method}'? (d/direct input, p/from passphrase)", 
                                                    valid_options=['d', 'direct', 'p', 'passphrase'], allow_back=True)
                if key_source_choice == 'QUIT': sys.exit()
                if key_source_choice == 'BACK':
                    current_step = 'GET_ENCRYPTION_METHOD'
                    continue
                
                if key_source_choice in ['d', 'direct']:
                    key_str_input = get_user_choice(f"Enter the numerical key value (1-255)", allow_back=True)
                    if key_str_input == 'QUIT': sys.exit()
                    if key_str_input == 'BACK': continue # Stay in GET_KEY_INFO, re-prompt for key source

                    try:
                        key_val = int(key_str_input)
                        if not (0 < key_val < 256):
                            print(f"{Fore.RED}Key value must be between 1 and 255!{Style.RESET_ALL}\n")
                            continue # Stay in GET_KEY_INFO, re-prompt for key value
                    except ValueError:
                        print(f"{Fore.RED}Invalid input. Please enter an integer for the key value.{Style.RESET_ALL}\n")
                        continue # Stay in GET_KEY_INFO, re-prompt for key value

                elif key_source_choice in ['p', 'passphrase']:
                    passphrase = get_user_choice(f"Enter your passphrase", allow_back=True)
                    if passphrase == 'QUIT': sys.exit()
                    if passphrase == 'BACK': continue # Stay in GET_KEY_INFO, re-prompt for key source

                    key_val = generate_key_from_passphrase(passphrase)
                    if key_val is None:
                        print(f"{Fore.RED}Failed to generate key from passphrase. Please try again.{Style.RESET_ALL}\n")
                        continue # Stay in GET_KEY_INFO, re-prompt for passphrase or source
                    print(f"{Fore.GREEN}Generated numerical key: {key_val}{Style.RESET_ALL}")
                
                session_data['key_value'] = key_val
                session_data['key_image_path'] = None # Ensure it's clear
                current_step = 'PROCESS_IMAGE'

            elif encryption_method == 'xor':
                key_type_choice = get_user_choice(f"Choose XOR key type (n/numerical, i/image)", 
                                                  valid_options=['n', 'numerical', 'i', 'image'], allow_back=True)
                if key_type_choice == 'QUIT': sys.exit()
                if key_type_choice == 'BACK':
                    current_step = 'GET_ENCRYPTION_METHOD'
                    continue

                if key_type_choice in ['n', 'numerical']:
                    key_source_choice = get_user_choice(f"How to get numerical key? (d/direct input, p/from passphrase)", 
                                                        valid_options=['d', 'direct', 'p', 'passphrase'], allow_back=True)
                    if key_source_choice == 'QUIT': sys.exit()
                    if key_source_choice == 'BACK': continue # Stay in GET_KEY_INFO, re-prompt for XOR key type
                    
                    if key_source_choice in ['d', 'direct']:
                        key_str_input = get_user_choice(f"Enter the numerical key value (1-255)", allow_back=True)
                        if key_str_input == 'QUIT': sys.exit()
                        if key_str_input == 'BACK': continue # Stay in GET_KEY_INFO, re-prompt for key source

                        try:
                            key_val = int(key_str_input)
                            if not (0 < key_val < 256):
                                print(f"{Fore.RED}Key value must be between 1 and 255!{Style.RESET_ALL}\n")
                                continue
                        except ValueError:
                            print(f"{Fore.RED}Invalid input. Please enter an integer for the key value.{Style.RESET_ALL}\n")
                            continue
                    elif key_source_choice in ['p', 'passphrase']:
                        passphrase = get_user_choice(f"Enter your passphrase", allow_back=True)
                        if passphrase == 'QUIT': sys.exit()
                        if passphrase == 'BACK': continue

                        key_val = generate_key_from_passphrase(passphrase)
                        if key_val is None:
                            print(f"{Fore.RED}Failed to generate key from passphrase. Please try again.{Style.RESET_ALL}\n")
                            continue
                        print(f"{Fore.GREEN}Generated numerical key: {key_val}{Style.RESET_ALL}")
                    
                    session_data['key_value'] = key_val
                    session_data['key_image_path'] = None
                    current_step = 'PROCESS_IMAGE'

                elif key_type_choice in ['i', 'image']:
                    key_img_path = get_file_path("Select key image", allow_back=True)
                    if key_img_path == 'QUIT': sys.exit()
                    if key_img_path == 'BACK': continue # Stay in GET_KEY_INFO, re-prompt for XOR key type

                    # Validate key image path if needed (e.g., file exists)
                    if not os.path.isfile(key_img_path):
                        print(f"{Fore.RED}Error: Key image file not found or is not a valid file: '{key_img_path}'{Style.RESET_ALL}\n")
                        continue # Stay in GET_KEY_INFO, re-prompt for image path
                        
                    session_data['key_value'] = None
                    session_data['key_image_path'] = key_img_path
                    current_step = 'PROCESS_IMAGE'
            else: # Should not happen if method validation is correct
                print(f"{Fore.RED}Unexpected error in key info step. Returning to main menu.{Style.RESET_ALL}\n")
                current_step = 'MAIN_MENU'

        elif current_step == 'PROCESS_IMAGE':
            success = process_image(
                input_path=session_data['input_path'],
                output_path=session_data['output_path'],
                method=session_data['encryption_method'],
                mode=session_data['action_mode'],
                key_value=session_data.get('key_value'),
                key_image_path=session_data.get('key_image_path')
            )
            # After processing, reset for next operation
            if success:
                print(f"{Fore.GREEN}Operation complete. Returning to main menu.{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Operation failed. Returning to main menu.{Style.RESET_ALL}")
            current_step = 'MAIN_MENU'
            session_data = {} # Clear session data

# Run the main program loop
if __name__ == "__main__":
    try:
        main_program_loop()
    except KeyboardInterrupt:
        print(f"\n{Fore.CYAN}Operation interrupted by user. Exiting.{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}An unhandled error occurred: {e}{Style.RESET_ALL}")
        sys.exit(1)

print(Style.RESET_ALL)
