# Caesar Cipher (IS493Project)

# encrypt a message
def encrypt(text, key):
    result = ""  # Hold the encrypted message
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + key) % 26 + 65)  # shift uppercase letter forward
        elif char.islower():
            result += chr((ord(char) - 97 + key) % 26 + 97)  # shift lowercase letter forward
        else:
            result += char
    return result


# decrypt a message
def decrypt(text, key):
    result = ""  # Hold the decrypted message
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 - key) % 26 + 65)  # shift uppercase letter back
        elif char.islower():
            result += chr((ord(char) - 97 - key) % 26 + 97)  # shift lowercase letter back
        else:
            result += char
    return result


# find the key from known plaintext
def crack_key(plain, cipher):
    if len(plain) != len(cipher):
        return "Error: Plaintext and ciphertext must have the same length."

    key = None

    for p, c in zip(plain, cipher):
        if (('A' <= p <= 'Z' and 'A' <= c <= 'Z') or
                ('a' <= p <= 'z' and 'a' <= c <= 'z')):  # both letters with the same case
            current_key = (ord(c) - ord(p)) % 26  # the gap between them is the key

            if key is None:
                key = current_key  # first key found
            elif current_key != key:
                return "Error: The texts do not match the Caesar cipher."

        elif p != c:  # non-letters must stay the same
            return "Error: The texts do not match the Caesar cipher."

    if key is None:
        return "Error: No letters found in the texts."

    return key


# ask for a valid key (0-25)
def get_key():
    while True:
        try:
            key = int(input("Enter the key (0-25): "))
            if 0 <= key <= 25:
                return key
            else:
                print("Invalid key! Please enter a number from 0 to 25.")
        except ValueError:  # if the user types letters instead of numbers
            print("Invalid input! Please enter a number, not letters.")


# main program
while True:
    print()
    print("      Caesar Cipher      ")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Cryptanalysis")
    print("4. Exit")

    choice = input("Choose your option (1-4): ")

    if choice == "1":
        text = input("Enter your message: ")
        key = get_key()
        print("Encrypted message:", encrypt(text, key))

    elif choice == "2":
        text = input("Enter the encrypted message: ")
        key = get_key()
        print("Decrypted message:", decrypt(text, key))

    elif choice == "3":
        plain = input("Enter the plaintext: ")
        cipher = input("Enter the ciphertext: ")
        result = crack_key(plain, cipher)

        # Display the key if found; otherwise, display the error message
        if isinstance(result, int):
            print("The key is:", result)
        else:
            print(result)

    elif choice == "4":
        print("Program closed. Stay secure!")
        break

    else:
        print("Invalid option, please try again.")