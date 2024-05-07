def caesar_cipher(text, shift, decrypt=False):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift
            if decrypt:
                shift_amount = -shift_amount
            shifted_char = chr((ord(char.lower()) - ord('a') + shift_amount) % 26 + ord('a'))
            if char.isupper():
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char
    return result

def main():
    while True:
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            plaintext = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = caesar_cipher(plaintext, shift)
            print("Encrypted text:", encrypted_text)
        elif choice == '2':
            ciphertext = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = caesar_cipher(ciphertext, shift, decrypt=True)
            print("Decrypted text:", decrypted_text)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

