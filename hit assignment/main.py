def encrypt_content(content, s1, s2):
    encrypted = ""
    for char in content:
        if 'a' <= char <= 'm':
            # Shift forward by (s1 * s2)
            encrypted += chr((ord(char) - ord('a') + (s1 * s2)) % 26 + ord('a'))
        elif 'n' <= char <= 'z':
            # Shift backward by (s1 + s2)
            encrypted += chr((ord(char) - ord('a') - (s1 + s2)) % 26 + ord('a'))
        elif 'A' <= char <= 'M':
            # Shift backward by s1
            encrypted += chr((ord(char) - ord('A') - s1) % 26 + ord('A'))
        elif 'N' <= char <= 'Z':
            # Shift forward by s2 squared
            encrypted += chr((ord(char) - ord('A') + (s2 ** 2)) % 26 + ord('A'))
        else:
            # Non-alphabetic characters remain unchanged
            encrypted += char
    return encrypted

def decrypt_content(content, s1, s2):
    decrypted = ""
    for char in content:
        if 'a' <= char <= 'z':
            # Attempt to reverse the 'a-m' logic first
            orig = chr((ord(char) - ord('a') - (s1 * s2)) % 26 + ord('a'))
            if 'a' <= orig <= 'm':
                decrypted += orig
            else:
                # If it wasn't a-m, it must have been n-z
                decrypted += chr((ord(char) - ord('a') + (s1 + s2)) % 26 + ord('a'))
        
        elif 'A' <= char <= 'Z':
            # Attempt to reverse the 'A-M' logic first
            orig = chr((ord(char) - ord('A') + s1) % 26 + ord('A'))
            if 'A' <= orig <= 'M':
                decrypted += orig
            else:
                # If it wasn't A-M, it must have been N-Z
                decrypted += chr((ord(char) - ord('A') - (s2 ** 2)) % 26 + ord('A'))
        else:
            decrypted += char
    return decrypted

def verify_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        if f1.read() == f2.read():
            return True
        return False

def main():
    # 1. Prompt for user input
    try:
        shift1 = int(input("Enter value for shift1: "))
        shift2 = int(input("Enter value for shift2: "))
    except ValueError:
        print("Please enter valid integers.")
        return

    # 2. Encrypt the contents of raw_text.txt
    try:
        with open("raw_text.txt", "r") as f:
            raw_data = f.read()
        
        encrypted_data = encrypt_content(raw_data, shift1, shift2)
        
        with open("encrypted_text.txt", "w") as f:
            f.write(encrypted_data)
        print("Step 1: Encryption successful. 'encrypted_text.txt' created.")

        # 3. Decrypt the encrypted file
        decrypted_data = decrypt_content(encrypted_data, shift1, shift2)
        
        with open("decrypted_text.txt", "w") as f:
            f.write(decrypted_data)
        print("Step 2: Decryption successful. 'decrypted_text.txt' created.")

        # 4. Verify the decryption
        if verify_files("raw_text.txt", "decrypted_text.txt"):
            print("Step 3: Verification SUCCESS! The files match.")
        else:
            print("Step 3: Verification FAILED! The files do not match.")

    except FileNotFoundError:
        print("Error: 'raw_text.txt' not found in the directory.")
3
if __name__ == "__main__":
    main()