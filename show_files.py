import os
import sys

def list_files(startpath, exclude_folders):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
        dirs[:] = [d for d in dirs if d not in exclude_folders]

def print_file_contents(startpath, exclude_files, exclude_folders):
    text_extensions = ['.txt', '.py', '.css', '.js', '.html']
    for root, dirs, files in os.walk(startpath):
        for file in files:
            if file not in exclude_files and any(file.endswith(ext) for ext in text_extensions):
                print("File: ", os.path.join(root, file))
                with open(os.path.join(root, file), 'r') as f:
                    try:
                        print(f.read())
                    except UnicodeDecodeError:
                        print("Could not decode file contents.")
        dirs[:] = [d for d in dirs if d not in exclude_folders]

def create_log_dir():
    log_dir = os.path.join(os.getcwd(), "logs")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    return log_dir

def log_to_file(log_dir):
    file_name = f"log_{len(os.listdir(log_dir)) + 1}.txt"
    file_path = os.path.join(log_dir, file_name)
    return file_path

startpath = '/Users/charlesfletcher/agentJeans'
exclude_files = ['log.txt']  # Add more filenames here as required
exclude_folders = ['logs', 'venv']  # Add more folder names here as required

log_dir = create_log_dir()
log_file = log_to_file(log_dir)

with open(log_file, 'w') as log:
    # Redirect stdout to the log file
    original_stdout = sys.stdout
    sys.stdout = log

    # List files and directories
    list_files(startpath, exclude_folders)

    # Print file contents
    print_file_contents(startpath, exclude_files, exclude_folders)

    # Restore original stdout
    sys.stdout = original_stdout
