import streamlit as st
from cryptography.fernet import Fernet
import base64
import hashlib

# Zero-width character encoding
ZW_SPACE = '\u200b'  # zero-width space
ZW_NON_JOINER = '\u200c'  # represents '1'
ZW_JOINER = '\u200d'      # represents '0'

def derive_key(password: str) -> bytes:
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def encrypt_message(message: str, password: str) -> str:
    key = derive_key(password)
    f = Fernet(key)
    return f.encrypt(message.encode()).decode()

def decrypt_message(token: str, password: str) -> str:
    key = derive_key(password)
    f = Fernet(key)
    return f.decrypt(token.encode()).decode()

def to_zw(text: str) -> str:
    bits = ''.join(format(ord(c), '08b') for c in text)
    return ''.join(ZW_NON_JOINER if b == '1' else ZW_JOINER for b in bits)

def from_zw(zw_text: str) -> str:
    bits = ''.join('1' if c == ZW_NON_JOINER else '0' for c in zw_text if c in [ZW_NON_JOINER, ZW_JOINER])
    chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
    return ''.join(chars)

def embed_secret(cover_text: str, secret_text: str, password: str) -> str:
    encrypted = encrypt_message(secret_text, password)
    hidden = to_zw(encrypted)
    return cover_text + ZW_SPACE + hidden  # Add invisible zero-width encoded text

def extract_secret(stego_text: str, password: str) -> str:
    try:
        hidden_part = stego_text.split(ZW_SPACE)[-1]
        decrypted_token = from_zw(hidden_part)
        return decrypt_message(decrypted_token, password)
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Streamlit App
st.set_page_config(page_title="Steganography App", layout="wide")
st.markdown("<h1 style='text-align: center; color: #2C6E49;'>🕵️‍♂️ Text Steganography with Password</h1>", unsafe_allow_html=True)
st.markdown("---")

col1, col2 = st.columns(2)

# Left: Hide Message
with col1:
    st.markdown("### 🔒 Hide Message")
    cover_text = st.text_area("Enter Cover Text", height=150, key="cover")
    secret_text = st.text_input("Enter Secret Message", key="secret")
    password = st.text_input("Enter Password", type="password", key="hide_pwd")
    if st.button("Hide and Generate", key="hide_btn"):
        if cover_text and secret_text and password:
            stego_result = embed_secret(cover_text, secret_text, password)
            st.success("✅ Message hidden successfully!")
            st.text_area("Stego Text (Copy this)", stego_result, height=200)
            
        else:
            st.error("Please fill in all fields.")

# Right: Reveal Message
with col2:
    st.markdown("### 🔓 Reveal Message")
    stego_input = st.text_area("Paste Stego Text", height=150, key="stego_input")
    reveal_password = st.text_input("Enter Password", type="password", key="reveal_pwd")
    if st.button("Reveal Secret", key="reveal_btn"):
        if stego_input and reveal_password:
            revealed = extract_secret(stego_input, reveal_password)
            if revealed.startswith("❌"):
                st.error(revealed)
            else:
                st.success("✅ Secret recovered!")
                st.text_area("Recovered Secret", revealed)
        else:
            st.error("Please provide stego text and password.")
