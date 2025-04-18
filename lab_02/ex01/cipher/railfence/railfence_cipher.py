class RailFenceCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        # Create a 2D array to represent the rail fence
        rail = [['\n' for _ in range(len(plaintext))]
                for _ in range(self.key)]
        dir_down = False
        row, col = 0, 0

        # Place characters in the rail fence pattern
        for char in plaintext:
            if row == 0:
                dir_down = True
            if row == self.key - 1:
                dir_down = False

            rail[row][col] = char
            col += 1

            row += 1 if dir_down else -1

        # Read the characters row by row to form the ciphertext
        result = []
        for i in range(self.key):
            for j in range(len(plaintext)):
                if rail[i][j] != '\n':
                    result.append(rail[i][j])
        return ''.join(result)

    def decrypt(self, ciphertext):
        # Create a 2D array to represent the rail fence
        rail = [['\n' for _ in range(len(ciphertext))]
                for _ in range(self.key)]
        dir_down = None
        row, col = 0, 0

        # Mark the positions in the rail fence
        for _ in range(len(ciphertext)):
            if row == 0:
                dir_down = True
            if row == self.key - 1:
                dir_down = False

            rail[row][col] = '*'
            col += 1

            row += 1 if dir_down else -1

        # Fill the rail fence with the ciphertext
        index = 0
        for i in range(self.key):
            for j in range(len(ciphertext)):
                if rail[i][j] == '*' and index < len(ciphertext):
                    rail[i][j] = ciphertext[index]
                    index += 1

        # Read the characters in a zigzag pattern to form the plaintext
        result = []
        row, col = 0, 0
        for _ in range(len(ciphertext)):
            if row == 0:
                dir_down = True
            if row == self.key - 1:
                dir_down = False

            if rail[row][col] != '\n':
                result.append(rail[row][col])
                col += 1

            row += 1 if dir_down else -1
        return ''.join(result)
