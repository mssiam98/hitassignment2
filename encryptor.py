def encrypt_char(char, s1, s2):
    if 'a' <= char <= 'm':
        # Shift forward by (s1 * s2)
        return chr((ord(char) - ord('a') + (s1 * s2)) % 26 + ord('a'))
    elif 'n' <= char <= 'z':
        # Shift backward by (s1 + s2)
        return chr((ord(char) - ord('a') - (s1 + s2)) % 26 + ord('a'))
    elif 'A' <= char <= 'M':
        # Shift backward by s1
        return chr((ord(char) - ord('A') - s1) % 26 + ord('A'))
    elif 'N' <= char <= 'Z':
        # Shift forward by s2 squared
        return chr((ord(char) - ord('A') + (s2 ** 2)) % 26 + ord('A'))
    return char

def run_encryption(s1, s2):
    try:
        with open("raw_text.txt", "r") as f_in, open("encrypted_text.txt", "w") as f_out:
            content = f_in.read()
            encrypted_content = "".join(encrypt_char(c, s1, s2) for c in content)
            f_out.write(encrypted_content)
        print("Encryption complete: 'encrypted_text.txt' created.")
    except FileNotFoundError:
        print("Error: 'raw_text.txt' not found.")

if __name__ == "__main__":
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))
    run_encryption(shift1, shift2)
