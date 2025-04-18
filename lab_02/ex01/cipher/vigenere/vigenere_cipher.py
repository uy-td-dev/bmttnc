class VigenereCipher:
    def __init__(self, key):
        self.key = key
        self.key_length = len(key)

    def encrypt(self, plaintext):
        ciphertext = []
        for i, char in enumerate(plaintext):
            if char.isalpha():
                shift = ord(self.key[i % self.key_length].upper()) - ord('A')
                if char.isupper():
                    ciphertext.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
                else:
                    ciphertext.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            else:
                ciphertext.append(char)
        return ''.join(ciphertext)

    def decrypt(self, ciphertext):
        plaintext = []
        for i, char in enumerate(ciphertext):
            if char.isalpha():
                shift = ord(self.key[i % self.key_length].upper()) - ord('A')
                if char.isupper():
                    plaintext.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
                else:
                    plaintext.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
            else:
                plaintext.append(char)
        return ''.join(plaintext)
    