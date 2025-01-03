import subprocess
import argparse
import sys
import os

def run_command(command):
    try:
        # Execute the command
        print(f"Running command: {' '.join(command)}...")
        subprocess.run(command, check=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")
    except FileNotFoundError:
        print("Frida command not found. Make sure Frida is installed and accessible.")

def run_codeshare_commands_from_file(codeshare, app_identifier):
    try:
        with open(codeshare, 'r') as file:
            for line in file:
                command = ["frida", "-U", "--codeshare", line.strip(), "-f", app_identifier]
                run_command(command)
    except FileNotFoundError:
        print(f"File {codeshare} not found.")

def run_frida_command(script_path, app_identifier):
    command = ["frida", "-U", "-l", script_path, "-f", app_identifier]
    run_command(command)

def get_scripts_from_folder(folder_path):
    try:
        # List all files in the folder and return their full paths
        return [
            os.path.join(folder_path, file)
            for file in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, file))
        ]
    except FileNotFoundError:
        print(f"Folder {folder_path} not found.")
        return []

def run_codeshare_commands_by_number(number, app_identifier):
    # Map numbers to corresponding file paths
    file_mapping = {
        "1": "Scripts/SSL/SSL.txt",
        "2": "Scripts/Root/Root.txt",
        "3": "Scripts/Both/Both.txt"
    }
    if number not in file_mapping:
        print(f"Invalid number: {number}. Please use 1 for SSL, 2 for Root, or 3 for Both.")
        return

    file_path = file_mapping[number]
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return

    # Run commands from the specified file
    run_codeshare_commands_from_file(file_path, app_identifier)

def main():
    # Define the argument parser with a custom help message
    parser = argparse.ArgumentParser(
        description="Run Frida scripts and optionally codeshare scripts from a file.",
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=False
    )
    parser.add_argument(
        "-n", metavar="NUMBER", 
        help=( 
            "Run codeshare commands by number:\n"
            "  1  Run SSL bypass codeshare commands (Scripts/SSL/SSL.txt)\n"
            "  2  Run Root bypass codeshare commands (Scripts/Root/Root.txt)\n"
            "  3  Run Both combined codeshare commands (Scripts/Both/Both.txt)"
        )
    )
    parser.add_argument("-r", action="store_true", help="Run stored Root scripts")
    parser.add_argument("-s", action="store_true", help="Run stored SSL bypass scripts")
    parser.add_argument("-b", action="store_true", help="Run stored Both combined scripts")
    parser.add_argument("-i", action="store_true", help="Run 'frida-ps -Uai'")
    parser.add_argument("-h", "--help", action="help", help="Show this help message and exit")
    parser.add_argument("app_identifier", nargs='?', help="The app identifier to run the commands on")
    args = parser.parse_args()

    # If -i flag is provided, run frida-ps -Uai
    if args.i:
        run_command(["frida-ps", "-Uai"])
        sys.exit(0)
    
    if not args.app_identifier:
        parser.print_help()
        sys.exit(1)

    app_identifier = args.app_identifier.strip()

    # Handle the -n option
    if args.n:
        run_codeshare_commands_by_number(args.n, app_identifier)
    elif args.r:
        root_folder = os.path.join("Scripts", "Root")
        scripts = get_scripts_from_folder(root_folder)
        for script in scripts:
            run_frida_command(script, app_identifier)
    elif args.s:
        ssl_folder = os.path.join("Scripts", "SSL")
        scripts = get_scripts_from_folder(ssl_folder)
        for script in scripts:
            run_frida_command(script, app_identifier)
    elif args.b:
        both_folder = os.path.join("Scripts", "Both")
        scripts = get_scripts_from_folder(both_folder)
        for script in scripts:
            run_frida_command(script, app_identifier)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
