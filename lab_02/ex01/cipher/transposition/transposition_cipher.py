class TranspositionCipher:
    def __init__(self, key):
        # Ensure the key is a string for sorting purposes
        if isinstance(key, int):
            key = str(key)
        self.key = key
        self.key_length = len(key)

    def encrypt(self, plaintext):
        # Create a list of empty strings for each column
        columns = [''] * self.key_length
        for index, char in enumerate(plaintext):
            column_index = index % self.key_length
            columns[column_index] += char

        # Create a sorted list of tuples (key, column)
        sorted_columns = sorted(zip(self.key, columns))

        # Concatenate the columns to form the ciphertext
        ciphertext = ''.join(column for _, column in sorted_columns)
        return ciphertext

    def decrypt(self, ciphertext):
        # Calculate the number of rows and the number of columns
        num_rows = len(ciphertext) // self.key_length
        num_extra_chars = len(ciphertext) % self.key_length

        # Create a list of empty strings for each column
        columns = [''] * self.key_length

        # Determine the order of columns based on the key
        sorted_key_indices = sorted(range(len(self.key)), key=lambda k: self.key[k])

        # Fill in the columns with the ciphertext
        index = 0
        for i in sorted_key_indices:
            column_length = num_rows + (1 if i < num_extra_chars else 0)
            columns[i] = ciphertext[index:index + column_length]
            index += column_length

        # Create a list to hold the decrypted text
        plaintext = []

        # Decrypt the text by reading it row by row
        for row in range(num_rows + (1 if num_extra_chars > 0 else 0)):
            for col in range(self.key_length):
                if row < len(columns[col]):
                    plaintext.append(columns[col][row])

        return ''.join(plaintext)
