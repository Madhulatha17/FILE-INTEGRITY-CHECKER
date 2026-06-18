import hashlib
import os

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()

def check_file_integrity(file_path):
    if not os.path.exists(file_path):
        print("File not found!")
        return

    original_hash = calculate_hash(file_path)

    print("\nFile Integrity Checker")
    print("----------------------")
    print("Original Hash:", original_hash)

    input("\nModify the file if you want, then press Enter...")

    new_hash = calculate_hash(file_path)

    print("New Hash:", new_hash)

    if original_hash == new_hash:
        print("\n✓ File Integrity Maintained")
    else:
        print("\n⚠ File Has Been Modified!")

file_name = input("Enter file name: ")
check_file_integrity(file_name)
