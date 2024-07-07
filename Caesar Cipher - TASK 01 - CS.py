def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Algorithm")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ")
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))
    
    if choice.lower() == 'e':
        encrypted_text = caesar_cipher_encrypt(text, shift)
        print(f"Encrypted text: {encrypted_text}")
    elif choice.lower() == 'd':
        decrypted_text = caesar_cipher_decrypt(text, shift)
        print(f"Decrypted text: {decrypted_text}")
    else:
        print("Invalid choice. Please select 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()
