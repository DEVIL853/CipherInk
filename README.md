# ✒️ CipherInk - Text Steganography App

CipherInk is a secure and user-friendly web app that allows you to **hide** and **reveal** secret messages within plain text using **zero-width characters** and **password-protected encryption**. Built with **Streamlit** and **Fernet encryption**, CipherInk ensures your messages are safely concealed and only accessible to those with the correct password.

## 🛠️ Features

- **Invisible Text Steganography**: Hide secret messages within ordinary text using invisible zero-width characters (such as zero-width space, non-joiner, and joiner).
- **Password-Based Encryption**: Encrypt messages with a user-defined password, ensuring that the message is protected and can only be decrypted by someone with the correct password.
- **Easy-to-Use Interface**: A simple and clean layout with two main actions: hide and reveal.
- **Cross-Platform**: Can be deployed on any platform that supports Streamlit.

## 🚀 Getting Started

### Prerequisites

To run this app locally, ensure you have Python 3.6+ and the following dependencies installed:

- `streamlit`
- `cryptography`

You can install the required packages using `pip`:

```bash
pip install streamlit cryptography

Running the App Locally
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/CipherInk.git
cd CipherInk
Run the app with Streamlit:

bash
Copy
Edit
streamlit run app.py
Open the provided URL in your browser, and you are ready to hide and reveal messages securely!

🎨 How It Works
1. Hide a Secret Message:
Enter your cover text (the text in which you want to hide the secret message).

Type your secret message.

Provide a password for encryption to keep the message secure.

Click "Hide and Generate". The app will encrypt your secret message and embed it invisibly in the cover text using zero-width characters.

2. Reveal a Hidden Message:
Paste the stego-text (cover text with the hidden message).

Enter the password used to encrypt the message.

Click "Reveal Secret" to extract and decrypt the hidden message.

🧩 How It Works Internally
Encryption: The secret message is encrypted using Fernet encryption, making it unreadable without the correct password.

Zero-Width Encoding: The encrypted message is converted into binary and encoded into zero-width characters (\u200b, \u200c, \u200d), making the message invisible in the cover text.

Embedding: The encoded hidden message is appended to the cover text, leaving no visible trace.

Extraction: CipherInk decodes the zero-width characters back into binary and decrypts the secret message using the password provided.

🔒 Security
CipherInk uses Fernet encryption to securely encrypt and decrypt the secret messages.

Password protection: The encryption key is derived from a user-provided password using SHA-256 and base64, ensuring that only the correct password can decrypt the hidden message.

🖥️ Screenshots


📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

📢 Contributing
We welcome contributions! Feel free to open issues or submit pull requests to improve the app or fix bugs. Please follow the standard GitHub workflow for contributing.

👤 Author
Your Name - Your GitHub Profile

📝 Additional Notes
CipherInk is intended to demonstrate the use of steganography and encryption techniques for hiding messages. It’s not designed for high-security applications but is ideal for educational purposes or low-risk applications.

Zero-width characters are invisible in most text viewers but may appear in some code editors or when copied into certain applications. Use caution when sharing encrypted stego-text.


