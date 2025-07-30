import streamlit as st
import math

# --- Encryption Algorithms ---

# Rail Fence Cipher
def rail_fence_encrypt(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    dir_down = False
    row, col = 0, 0
    for char in text:
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        rail[row][col] = char
        col += 1
        row += 1 if dir_down else -1
    result = ''.join(''.join(r).replace('\n', '') for r in rail)
    return result

# Row Transposition Cipher
def row_transposition_encrypt(text, key):
    cols = len(key)
    rows = math.ceil(len(text) / cols)

    # Fill matrix with message
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    index = 0
    for r in range(rows):
        for c in range(cols):
            matrix[r][c] = text[index] if index < len(text) else 'X'
            index += 1

    # Create (char, index) pair and sort it
    key_pairs = sorted([(char.lower(), i) for i, char in enumerate(key)])
    order = [pair[1] for pair in key_pairs]

    # Read columns by sorted order
    encrypted = ''.join(matrix[r][c] for c in order for r in range(rows))
    return encrypted


# --- Ocean Drift Theme Styling ---
st.markdown("""
    <style>
    html, body, [class*="css"] {
        background: linear-gradient(to right, #e0f7fa, #ffffff);
        font-family: 'Courier New', monospace;
        color: #004d4d;
    }
    .stTextInput>div>div>input, .stTextArea textarea {
        background-color: #f0faff !important;
        color: #004d4d !important;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }
    .stSlider {
        color: #006064 !important;
    }
    .stButton>button {
        background-color: #00acc1;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        font-size: 16px;
        transition: all 0.3s ease;
        box-shadow: 1px 1px 5px #bbb;
    }
    .stButton>button:hover {
        background-color: #00838f;
        transform: scale(1.03);
    }
    .stSuccess {
        background-color: #e0f2f1;
        border-left: 5px solid #00acc1;
        padding: 10px;
        border-radius: 10px;
        font-size: 16px;
        margin-top: 10px;
    }
    h1 {
        color: #006064;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- App UI ---
st.title("🌊 ROW AND RAIL Cipher Encryptor")

st.markdown("#### Select your encryption method:")

method = st.selectbox("🔧 Choose Cipher Technique:", ["Rail Fence Cipher", "Row Transposition Cipher"])

message = st.text_input("✉️ Enter your message:", value="OCEANFLOW")

if method == "Rail Fence Cipher":
    rail_key = st.slider("🔢 Enter number of rails (Key):", min_value=2, max_value=10, value=3)
    if st.button("🔐 Encrypt Now"):
        msg = message.replace(" ", "").upper()
        encrypted = rail_fence_encrypt(msg, rail_key)
        st.success(f"🔷 **Rail Fence Output:** `{encrypted}` 🌊")
        st.markdown('<div style="text-align:center; font-size:30px;">🌸🌊🌸💙🌸🌊🌸</div>', unsafe_allow_html=True)

elif method == "Row Transposition Cipher":
    row_key = st.text_input("🔑 Enter Row Transposition Key (String or Numbers):", value="3142")
    if st.button("🔐 Encrypt Now"):
        msg = message.replace(" ", "").upper()
        encrypted = row_transposition_encrypt(msg, row_key)
        st.success(f"🔷 **Row Transposition Output:** `{encrypted}` 💙")
        st.markdown('<div style="text-align:center; font-size:30px;">🌊🌀🌼🌊</div>', unsafe_allow_html=True)
