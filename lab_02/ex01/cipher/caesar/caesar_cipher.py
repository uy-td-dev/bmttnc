from cipher.caesar import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET
    
    def encrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        encrypted_text = []
        for char in text:
            if char in self.alphabet:
                index = (self.alphabet.index(char) + key) % alphabet_len
                encrypted_text.append(self.alphabet[index])
            else:
                encrypted_text.append(char)  # Keep non-alphabet chars unchanged
        return ''.join(encrypted_text)
    
    def decrypt_text(self, text: str, key: int) -> str:
        alphabet_len = len(self.alphabet)
        text = text.upper()
        decrypted_text = []
        for char in text:
            if char in self.alphabet:
                index = (self.alphabet.index(char) - key) % alphabet_len
                decrypted_text.append(self.alphabet[index])
            else:
                decrypted_text.append(char)  # Keep non-alphabet chars unchanged
        return ''.join(decrypted_text)
    