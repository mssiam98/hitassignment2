def decrypt_char(char, s1, s2):
    # Reverse lowercase logic
    if 'a' <= char <= 'z':
        # We need to determine if the ORIGINAL was a-m or n-z. 
        # Since the shift might land a char anywhere, we test the reverse shift.
        
        # Try reversing the 'a-m' shift
        orig_attempt = chr((ord(char) - ord('a') - (s1 * s2)) % 26 + ord('a'))
        if 'a' <= orig_attempt <= 'm': return orig_attempt
        
        # Try reversing the 'n-z' shift
        orig_attempt = chr((ord(char) - ord('a') + (s1 + s2)) % 26 + ord('a'))
        return orig_attempt

    # Reverse uppercase logic
    elif 'A' <= char <= 'Z':
        # Try reversing the 'A-M' shift (backward s1 becomes forward s1)
        orig_attempt = chr((ord(char) - ord('A') + s1) % 26 + ord('A'))
        if 'A' <= orig_attempt <= 'M': return orig_attempt
        
        # Try reversing the 'N-Z' shift (forward s2^2 becomes backward s2^2)
        orig_attempt = chr((ord(char) - ord('A') - (s2 ** 2)) % 26 + ord('A'))
        return orig_attempt
        
    return char

def verify_decryption():
    try:
        with open("raw_text.txt", "r") as f1, open("decrypted_text.txt", "r") as f2:
            if f1.read() == f2.read():
                print("Verification SUCCESS: The files match perfectly.")
            else:
                print("Verification FAILED: The files do not match.")
    except FileNotFoundError:
        print("Error: Files missing for verification.")

def run_decryption(s1, s2):
    try:
        with open("encrypted_text.txt", "r") as f_in, open("decrypted_text.txt", "w") as f_out:
            content = f_in.read()
            decrypted_content = "".join(decrypt_char(c, s1, s2) for c in content)
            f_out.write(decrypted_content)
        print("Decryption complete: 'decrypted_text.txt' created.")
        verify_decryption()
    except FileNotFoundError:
        print("Error: 'encrypted_text.txt' not found.")

if __name__ == "__main__":
    shift1 = int(input("Enter shift1 used for encryption: "))
    shift2 = int(input("Enter shift2 used for encryption: "))
    run_decryption(shift1, shift2)