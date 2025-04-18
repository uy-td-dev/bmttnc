import ast
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from api_client import call_api

class RSAView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.input_text = QLineEdit()
        self.encrypt_button = QPushButton("Encrypt RSA")
        self.decrypt_button = QPushButton("Decrypt RSA")
        self.output_text = QTextEdit()

        layout.addWidget(QLabel("Text:"))
        layout.addWidget(self.input_text)
        layout.addWidget(self.encrypt_button)
        layout.addWidget(self.decrypt_button)
        layout.addWidget(QLabel("Output:"))
        layout.addWidget(self.output_text)

        self.setLayout(layout)

        self.encrypt_button.clicked.connect(lambda: self.call_rsa("encrypt"))
        self.decrypt_button.clicked.connect(lambda: self.call_rsa("decrypt"))

    def call_rsa(self, action):
        import requests  # Import requests for API calls

        # Define the API endpoint based on the action
        url = f"http://127.0.0.1:5000/api/rsa/{action}"

        # Get the input text and RSA parameters
        text = self.input_text.text()
        p = 61  # Example value for p
        q = 53  # Example value for q

        # Prepare the payload
        if action == "encrypt":
            payload = {
                "plaintext": text,
                "p": p,
                "q": q
            }
        elif action == "decrypt":
            try:
                ciphertext = text # Convert input text to an integer for decryption
            except ValueError:
                self.output_text.setPlainText("Error: Ciphertext must be a valid integer.")
                return
            payload = {
                "ciphertext": ast.literal_eval(ciphertext),
                "p": p,
                "q": q
            }

        try:
            # Make the API request
            response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
            response.raise_for_status()  # Raise an error for HTTP errors

            # Parse the response and display the result
            result = response.json()
            print(action)
            if action == "encrypt":
                print(f"Response JSON: {result}")
                encrypted_text = result.get("ciphertext")
                self.output_text.setPlainText(str(encrypted_text))
            elif action == "decrypt":
                print(f"Response JSON: {result}")
                decrypted_text = result.get("plaintext", "No result returned")
                self.output_text.setPlainText(str(decrypted_text))
            # self.output_text.setPlainText(result.get("result", "No result returned"))
        except requests.exceptions.RequestException as e:
            # Handle errors and display them in the output text area
            self.output_text.setPlainText(f"Error: {e}")
