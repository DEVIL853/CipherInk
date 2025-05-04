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
