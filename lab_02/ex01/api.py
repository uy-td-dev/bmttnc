from flask import Flask, jsonify, render_template, request
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayfairCipher
from cipher.transposition.transposition_cipher import TranspositionCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.rsa import RSACipher
app = Flask(__name__)

casear_cipher = CaesarCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    text = data.get('text')
    key = int(data.get('key'))
    if not text or not key:
        return jsonify({'error': 'Invalid input'}), 400
    try:
        encrypted_text = casear_cipher.encrypt_text(text, key)
        return jsonify({'encrypted_text': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/caesar/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    text = data.get('text')
    key = int(data.get('key'))
    if not text or not key:
        return jsonify({'error': 'Invalid input'}), 400
    try:
        decrypted_text = casear_cipher.decrypt_text(text, key)
        return jsonify({'decrypted_text': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/playfair/creatematrix', methods=['POST'])
def create_matrix():
    data = request.get_json()
    key = data.get('key')
    if not key:
        return jsonify({'error': 'Invalid input'}), 400
    try:
        playfair_cipher = PlayfairCipher(key)
        matrix = playfair_cipher.create_table(key)
        return jsonify({'matrix': matrix})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    plaintext = data.get('plaintext')
    key = data.get('key')
    if not plaintext or not key:
        return jsonify({'error': 'Invalid input'}), 400
    try:
        playfair_cipher = PlayfairCipher(key)
        ciphertext = playfair_cipher.encrypt(plaintext)
        return jsonify({'ciphertext': ciphertext})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    ciphertext = data.get('ciphertext')
    key = data.get('key')
    if not ciphertext or not key:
        return jsonify({'error': 'Invalid input'}), 400
    try:
        playfair_cipher = PlayfairCipher(key)
        plaintext = playfair_cipher.decrypt(ciphertext)
        return jsonify({'plaintext': plaintext})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    plaintext = data.get('plaintext')
    key = str(data.get('key'))  # Convert key to string
    if not plaintext or not key:
        return jsonify({'error': 'Invalid input'}), 400
    try:
        transposition_cipher = TranspositionCipher(key)
        ciphertext = transposition_cipher.encrypt(plaintext)
        return jsonify({'ciphertext': ciphertext})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    ciphertext = data.get('plaintext')
    key = str(data.get('key'))  # Convert key to string
    if not ciphertext or not key:
        return jsonify({'error': 'Invalid input'}), 400
    try:
        transposition_cipher = TranspositionCipher(key)
        plaintext = transposition_cipher.decrypt(ciphertext)
        return jsonify({'ciphertext': plaintext})
    except Exception as e:
        return jsonify({'error': str(e)}), 500   
    
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    plaintext = data.get('plaintext')
    key = data.get('key')
    if not plaintext or not key:
        return jsonify({'error': 'Invalid input'}), 400
    try:
        vigenere_cipher = VigenereCipher(key)
        ciphertext = vigenere_cipher.encrypt(plaintext)
        return jsonify({'ciphertext': ciphertext})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    ciphertext = data.get('ciphertext')
    key = data.get('key')
    if not ciphertext or not key:
        return jsonify({'error': 'Invalid input'}), 400
    try:
        vigenere_cipher = VigenereCipher(key)
        plaintext = vigenere_cipher.decrypt(ciphertext)
        return jsonify({'plaintext': plaintext})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json()
    plaintext = data.get('plaintext')
    key = int(data.get('key'))
    if not plaintext or not key:
        return jsonify({'error': 'Invalid input'}), 400
    try:
        railfence_cipher = RailFenceCipher(key)
        ciphertext = railfence_cipher.encrypt(plaintext)
        return jsonify({'ciphertext': ciphertext})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    ciphertext = data.get('ciphertext')
    key = int(data.get('key'))
    if not ciphertext or not key:
        return jsonify({'error': 'Invalid input'}), 400
    try:
        railfence_cipher = RailFenceCipher(key)
        plaintext = railfence_cipher.decrypt(ciphertext)
        return jsonify({'plaintext': plaintext})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/api/rsa/encrypt', methods=['POST'])
def rsa_encrypt():
    data = request.get_json()
    plaintext = data.get('plaintext')
    p = int(data.get('p'))
    q = int(data.get('q'))
    if not plaintext or not p or not q:
        return jsonify({'error': 'Invalid input'}), 400
    try:
        rsa_cipher = RSACipher(p, q)
        ciphertext = rsa_cipher.encrypt(plaintext)
        return jsonify({'ciphertext': ciphertext})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/api/rsa/decrypt', methods=['POST'])
def rsa_decrypt():
    data = request.get_json()
    ciphertext = data.get('ciphertext')
    p = int(data.get('p'))
    q = int(data.get('q'))
    if not ciphertext or not p or not q:
        return jsonify({'error': 'Invalid input'}), 400
    try:
        rsa_cipher = RSACipher(p, q)
        plaintext = rsa_cipher.decrypt(ciphertext)
        return jsonify({'plaintext': plaintext})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# web with return file tempalates/index.html
@app.route('/')
def index():
    return  render_template('index.html')
@app.route('/caesar')
def caesar():
    return  render_template('caesar.html')
@app.route('/playfair')
def playfair():
    return  render_template('playfair.html')
@app.route('/transposition')
def transposition():
    return  render_template('transposition.html')
@app.route('/vigenere')
def vigenere():
    return  render_template('vigenere.html')
@app.route('/railfence')
def railfence():
    return  render_template('railfence.html')


# Run the Flask app

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)