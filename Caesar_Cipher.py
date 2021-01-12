alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

decision = True

while decision is True:

    direction = input("Type 'ENCODE' to encrypt, type 'DECODE' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    if shift > 25:
        shift = shift % 25
        if shift == 0:
            shift += 5


    def encrypt(plain_text, shift_amount):  # for encode
        cipher_text = ""
        for letter in plain_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            elif letter not in alphabet:
                cipher_text += letter

        print(f"The Encoded text is: {cipher_text}")


    def decrypt(cipher_text, shift_amount):  # for decode
        plain_text = ""
        for letter in cipher_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position - shift_amount
                plain_text += alphabet[new_position]
            elif letter not in alphabet:
                plain_text += letter
        print(f"The Decoded text is: {plain_text}")


    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    last_dec = input("Type 'Yes' if You want to continue again or Type 'No' to Exit : ").lower()
    if last_dec == "no":
        decision = False
        print("Thanks For Using Caesar Cipher!!")
    else:
        decision = True
