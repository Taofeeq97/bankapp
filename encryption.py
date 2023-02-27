alphabet='abcdefghijklmnopqrstuvwxyz'
alphabet1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number=[0,1, 2, 3, 4, 5, 6, 7, 8, 9, ]

def encrypt(message, shift):
    foremedword = ''
    for letters in message:
        if letters.isalpha():
            if letters.islower():
                index=(alphabet.index(letters)+shift)%26
                encrypted=alphabet[index]
                foremedword+=encrypted.upper()
            if letters.isupper():
                index = (alphabet1.index(letters) + shift) % 26
                encrypted = alphabet1[index]
                foremedword += encrypted.lower()

        elif letters.isdigit():
            index=number.index(int(letters)) + shift
            index1=index % len(number)
            foremedword += str(index1)

        else:
            foremedword+=letters
    return foremedword


def decrypt(message, shift):
    foremedword = ''
    for letters in message:
        if letters.isalpha():
            if letters.islower():
                index = (alphabet.index(letters) - shift) % 26
                encrypted = alphabet[index]
                foremedword += encrypted.upper()
            if letters.isupper():
                index = (alphabet1.index(letters) - shift) % 26
                encrypted = alphabet1[index]
                foremedword += encrypted.lower()
        elif letters.isdigit():
            index = number.index(int(letters)) - shift
            index1 = index % len(number)
            foremedword += str(index1)
        else:
            foremedword += letters
    return foremedword


