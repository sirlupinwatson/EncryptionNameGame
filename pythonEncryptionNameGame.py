# Encrypt a name in numbers using a Caesar cipher


def main():
    name = input("Enter your name: ")
    shift = int(input("Enter a shift value: "))
    encrypted_name = encrypt(name, shift)
    print("Your encrypted name is:", encrypted_name)


def encrypt(name, shift):
    """Encrypt a name using a Caesar cipher"""
    encrypted_name = ""
    for letter in name:
        if letter.isalpha():
            encrypted_name += chr(ord(letter) + shift)
        else:
            encrypted_name += letter
    return encrypted_name


main()


# Output: EncryptionNameGame.py