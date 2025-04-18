class PlayfairCipher:
    def __init__(self, key):
        self.key = key
        self.table = self.create_table(key)

    def create_table(self, key):
        # Create a 5x5 table for the Playfair cipher
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' is omitted
        table = []
        used_chars = set()

        # Add characters from the key to the table
        for char in key.upper():
            if char in alphabet and char not in used_chars:
                used_chars.add(char)
                table.append(char)

        # Add remaining characters from the alphabet
        for char in alphabet:
            if char not in used_chars:
                used_chars.add(char)
                table.append(char)

        return [table[i:i + 5] for i in range(0, 25, 5)]  # Create 5x5 grid

    def encrypt(self, plaintext):
        # Encrypt the plaintext using the Playfair cipher
        plaintext = self.prepare_text(plaintext)
        ciphertext = ""

        for i in range(0, len(plaintext), 2):
            a, b = plaintext[i], plaintext[i + 1]
            row_a, col_a = self.find_position(a)
            row_b, col_b = self.find_position(b)

            if row_a is None or col_a is None or row_b is None or col_b is None:
                raise ValueError(f"Character '{a}' or '{b}' not found in the cipher table.")

            if row_a == row_b:  # Same row
                ciphertext += self.table[row_a][(col_a + 1) % 5]
                ciphertext += self.table[row_b][(col_b + 1) % 5]
            elif col_a == col_b:  # Same column
                ciphertext += self.table[(row_a + 1) % 5][col_a]
                ciphertext += self.table[(row_b + 1) % 5][col_b]
            else:  # Rectangle swap
                ciphertext += self.table[row_a][col_b]
                ciphertext += self.table[row_b][col_a]

        return ciphertext

    def decrypt(self, ciphertext):
        # Decrypt the ciphertext using the Playfair cipher
        plaintext = ""

        for i in range(0, len(ciphertext), 2):
            a, b = ciphertext[i], ciphertext[i + 1]
            row_a, col_a = self.find_position(a)
            row_b, col_b = self.find_position(b)

            if row_a is None or col_a is None or row_b is None or col_b is None:
                raise ValueError(f"Character '{a}' or '{b}' not found in the cipher table.")

            if row_a == row_b:  # Same row
                plaintext += self.table[row_a][(col_a - 1) % 5]
                plaintext += self.table[row_b][(col_b - 1) % 5]
            elif col_a == col_b:  # Same column
                plaintext += self.table[(row_a - 1) % 5][col_a]
                plaintext += self.table[(row_b - 1) % 5][col_b]
            else:  # Rectangle swap
                plaintext += self.table[row_a][col_b]
                plaintext += self.table[row_b][col_a]

        return plaintext

    def find_position(self, char):
        # Find the position of a character in the table
        for i, row in enumerate(self.table):
            if char in row:
                return i, row.index(char)
        return None, None
    
    def prepare_text(self, text):
        # Prepare the text for encryption/decryption
        text = text.upper().replace("J", "I")  # Replace 'J' with 'I'
        text = text.replace(" ", "")  # Remove spaces
        prepared_text = ""
        i = 0
        while i < len(text):
            a = text[i]
            if i + 1 < len(text):
                b = text[i + 1]
                if a == b:
                    prepared_text += a + "X"
                    i += 1
                else:
                    prepared_text += a + b
                    i += 2
            else:
                prepared_text += a + "X"
                i += 1
        return prepared_text