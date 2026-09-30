import streamlit as st
import requests
import time
from datetime import datetime

st.set_page_config(page_title="ZOULD - Super AI", page_icon="⚡", layout="wide")

st.markdown("""
<style>
.stApp {background: linear-gradient(135deg, #0f0f0f 0%, #1a1a2e 100%);}
h1 {color: #00ff88; text-align: center;}
</style>
""", unsafe_allow_html=True)

st.title("⚡ ZOULD - الذكاء الخارق")
st.caption(f"يخدم وحدو 24/7 | {datetime.now().strftime('%H:%M:%S')}")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"assistant","content":"أنا ZOULD ⚡ نحكي، نبحث، نرسم، نفكر، نخدم حتى وانت مش فاتح! واش حاب نديرلك ضرك؟"}]

with st.sidebar:
    st.header("🧠 قدرات ZOULD")
    mode = st.radio("اختار:", ["💬 يحكي و يفكر", "🔍 يبحث", "🎨 يرسم و يصمم", "🤖 يخدم وحدو"])
    if st.button("🗑️ مسح"):
        st.session_state.messages = []
        st.rerun()
    st.success("✅ Online 24/7")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "image" in msg:
            st.image(msg["image"])

def ask_zould(prompt, mode):
    try:
        if mode == "🎨 يرسم و يصمم":
            return None, f"https://image.pollinations.ai/prompt/{requests.utils.quote(prompt)}?width=1024&height=1024&nologo=true"
        else:
            system = "انت ZOULD ذكاء خارق جزائري، تحكي بالدارجة خفيف، ذكي جدا"
            full = f"{system}\nالمستخدم: {prompt}\nMode: {mode}"
            r = requests.get(f"https://text.pollinations.ai/{requests.utils.quote(full)}", timeout=30)
            return r.text, None
    except Exception as e:
        return f"صبر ⚡ {e}", None

if prompt := st.chat_input("قول لـ ZOULD واش يدير..."):
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("ZOULD يفكر...🧠"):
            text, img = ask_zould(prompt, mode)
            if img:
                st.image(img, caption=prompt)
                st.session_state.messages.append({"role":"assistant","content":f"رسمت: {prompt}", "image": img})
            else:
                st.markdown(text)
                st.session_state.messages.append({"role":"assistant","content":text})
