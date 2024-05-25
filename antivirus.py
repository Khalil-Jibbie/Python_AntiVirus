import os

def scan_directory(directory):
    suspicious_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if is_suspicious(file):
                suspicious_files.append(os.path.join(root, file))
    return suspicious_files

def is_suspicious(file):
    suspicious_extensions = ['.exe', '.dll', '.bat', '.vbs', '.scr'] # Add more extensions as needed
    file_extension = os.path.splitext(file)[1]
    if file_extension in suspicious_extensions:
        return True
    else:
        return False

def main():
    directory_to_scan = input("Enter the directory to scan: ")
    suspicious_files = scan_directory(directory_to_scan)
    if suspicious_files:
        print("Potentially suspicious files found:")
        for file in suspicious_files:
            print(file)
    else:
        print("No suspicious files found.")

if __name__ == "__main__":
    main()
