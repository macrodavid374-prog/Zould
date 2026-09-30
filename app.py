import streamlit as st
import requests
import urllib.parse
import time
from datetime import datetime

st.set_page_config(page_title="ZOULD - الذكاء الخارق", page_icon="⚡")

st.markdown("""
<style>
.stApp {background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);}
h1 {color: #00ff88; text-align: center;}
</style>
""", unsafe_allow_html=True)

st.title("⚡ ZOULD - الذكاء الخارق")
st.caption(f"يخدم وحدو 24/7 | {datetime.now().strftime('%H:%M')}")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.success("✅ Online 24/7")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "image" in msg:
            st.image(msg["image"])

def ask_zould(prompt, mode):
    try:
        if mode == "🎨 يرسم و يصمم":
            encoded = urllib.parse.quote(prompt)
            img_url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1024&nologo=true&enhance=true"
            return None, img_url
        else:
            system = "انت ZOULD ذكي جدا، مساعد جزائري يهدر بالدارجة"
            full = f"{system}\nالمستخدم: {prompt}\nZOULD:"
            encoded = urllib.parse.quote(full)
            r = requests.get(f"https://text.pollinations.ai/{encoded}", timeout=90)
            return r.text, None
    except Exception as e:
        return f"صبر ⚡ {e}", None

mode = st.selectbox("اختار:", ["💬 يهدر و يجاوب", "🎨 يرسم و يصمم"])

if prompt := st.chat_input("قول لـ ZOULD واش يدير..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("ZOULD يفكر...🧠"):
            text, img = ask_zould(prompt, mode)
            if img:
                st.image(img, caption=prompt)
                st.session_state.messages.append({"role": "assistant", "content": prompt, "image": img})
            else:
                st.markdown(text)
                st.session_state.messages.append({"role": "assistant", "content": text})
