import os
import streamlit as st
import requests
import base64

# ---------------- CONFIG ----------------
API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    st.error("❌ OPENROUTER_API_KEY not found.")
    st.stop()

# ---------------- HELPERS ----------------
def image_to_base64(uploaded_file):
    return base64.b64encode(uploaded_file.read()).decode("utf-8")

def ask_chatbot(prompt, image_base64=None):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Coding Doubt Solver"
    }

    user_content = [{"type": "text", "text": prompt}]

    if image_base64:
        user_content.append({
            "type": "image_url",
            "image_url": {"url": f"data:image/png;base64,{image_base64}"}
        })

    payload = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {
                "role": "system",
                "content": "You are a coding doubt solver. Explain the problem clearly and provide an optimized solution with code."
            },
            {
                "role": "user",
                "content": user_content
            }
        ],
        "max_tokens": 800
    }

    response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]

# ---------------- UI ----------------
st.set_page_config(page_title="Coding Doubt Solver", page_icon="🤖")

st.title("🤖 Coding Doubt Solver")
st.write("Upload a coding problem image and get explanation + solution.")

uploaded_image = st.file_uploader(
    "Upload an image (optional)",
    type=["png", "jpg", "jpeg"]
)

question = st.text_area("Your question", "Solve this coding problem:")

if st.button("Ask Chatbot"):
    with st.spinner("Thinking..."):
        try:
            img_base64 = image_to_base64(uploaded_image) if uploaded_image else None
            answer = ask_chatbot(question, img_base64)
            st.success("✅ Response")
            st.markdown(answer)
        except Exception as e:
            st.error(f"❌ Error: {e}")





