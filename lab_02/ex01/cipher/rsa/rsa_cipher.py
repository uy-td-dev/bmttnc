import binascii

class RSACipher:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = 65537  # Commonly used public exponent
        self.d = self.mod_inverse(self.e, self.phi)

    def mod_inverse(self, a, m):
        m0, x0, x1 = m, 0, 1
        if m == 1:
            return 0
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += m0
        return x1

    def encrypt_block(self, block):
        # Encrypt a single block
        block_int = int(binascii.hexlify(block.encode()), 16)
        return pow(block_int, self.e, self.n)

    def decrypt_block(self, block_int):
        # Decrypt a single block
        plaintext_int = pow(block_int, self.d, self.n)
        hex_plaintext = hex(plaintext_int)[2:]  # Remove the '0x' prefix
        if len(hex_plaintext) % 2 != 0:
            hex_plaintext = '0' + hex_plaintext  # Pad with a leading zero if odd-length
        return binascii.unhexlify(hex_plaintext).decode()

    def encrypt(self, plaintext):
        # Split plaintext into blocks that fit within n
        block_size = (self.n.bit_length() - 1) // 8  # Maximum block size in bytes
        blocks = [plaintext[i:i + block_size] for i in range(0, len(plaintext), block_size)]
        ciphertext = [self.encrypt_block(block) for block in blocks]
        return ciphertext

    def decrypt(self, ciphertext):
        # Decrypt each block and combine the results
        plaintext = ''.join([self.decrypt_block(block) for block in ciphertext])
        return plaintext
