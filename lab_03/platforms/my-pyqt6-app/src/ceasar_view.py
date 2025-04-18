from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QFormLayout, QHBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import requests
from api_client import call_api

class CeasarView(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        # Set up the main layout
        main_layout = QVBoxLayout()

        # Title Label
        title_label = QLabel("Caesar Cipher")
        title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #4CAF50; margin-bottom: 20px;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        # Form Layout for Input Fields
        form_layout = QFormLayout()
        form_layout.setSpacing(10)

        self.input_text = QLineEdit()
        self.input_text.setPlaceholderText("Enter text to encrypt or decrypt")
        self.input_text.setStyleSheet("padding: 5px; border: 1px solid #ccc; border-radius: 5px;")
        form_layout.addRow(QLabel("Text:"), self.input_text)

        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("Enter key (number)")
        self.key_input.setStyleSheet("padding: 5px; border: 1px solid #ccc; border-radius: 5px;")
        form_layout.addRow(QLabel("Key (number):"), self.key_input)

        main_layout.addLayout(form_layout)

        # Buttons Layout
        button_layout = QHBoxLayout()

        # Define buttons before adding them to the layout
        self.encrypt_button = QPushButton("Encrypt")
        self.encrypt_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 10px; border-radius: 5px;")
        self.decrypt_button = QPushButton("Decrypt")
        self.decrypt_button.setStyleSheet("background-color: #2196F3; color: white; padding: 10px; border-radius: 5px;")

        button_layout.addWidget(self.encrypt_button)
        button_layout.addWidget(self.decrypt_button)
        main_layout.addLayout(button_layout)

        # Output Text
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setStyleSheet("padding: 5px; border: 1px solid #ccc; border-radius: 5px; background-color: #f9f9f9;, text-color: #333;")
        main_layout.addWidget(QLabel("Output:"))
        main_layout.addWidget(self.output_text)

        # Set the main layout
        self.setLayout(main_layout)

        # Connect buttons to actions
        self.encrypt_button.clicked.connect(lambda: self.call_ceasar("encrypt"))
        self.decrypt_button.clicked.connect(lambda: self.call_ceasar("decrypt"))

    def call_ceasar(self, action):
        try:
            print(f"Button clicked: {action}")  # Debug print

            # Get the input text and key
            text = self.input_text.text()
            key = self.key_input.text()
            print(f"Input Text: {text}")  # Debug print
            print(f"Key: {key}")  # Debug print

            # Validate input
            if not text or not key:
                self.output_text.setPlainText("Error: Text and key must not be empty.")
                return

            # Prepare the payload
            payload = {
                "text": text,
                "key": key
            }
            print(f"Payload: {payload}")  # Debug print

            # Define the API endpoint based on the action
            url = f"http://localhost:5000/api/caesar/{action}"

            # Make the API request
            response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})
            response.raise_for_status()  # Raise an error for HTTP errors
            print(f"Response status code: {response.status_code}")  # Debug print
            print(f"Response content: {response.content}")  # Debug print

            # Parse the response and display the result
            result = response.json()
            print(f"Response JSON: {result}")  # Debug print

            if action == "encrypt":
                encrypted_text = result.get("encrypted_text", "No result returned")
                print(f"Encrypted text: {encrypted_text}")  # Debug print
                self.output_text.setText(encrypted_text)
            elif action == "decrypt":
                decrypted_text = result.get("decrypted_text", "No result returned")
                print(f"Decrypted text: {decrypted_text}")  # Debug print
                self.output_text.setText(decrypted_text)
        except requests.exceptions.RequestException as e:
            # Handle errors and display them in the output text area
            self.output_text.setText(f"Error: {e}")
            print(f"RequestException: {e}")  # Debug print
        except Exception as e:
            print(f"Error in call_ceasar: {e}")
