import streamlit as st
import urllib.parse
from datetime import datetime
from openai import OpenAI

st.set_page_config(page_title="ZOULD", page_icon="⚡", layout="centered")
st.markdown("<style>.stApp{background:linear-gradient(135deg,#0f0c29,#302b63,#24243e);} h1{color:#00ff88;text-align:center;}</style>", unsafe_allow_html=True)
st.title("⚡ ZOULD - الذكاء الخارق")
st.caption(f"Online 24/7 | {datetime.now().strftime('%H:%M')}")

if "messages" not in st.session_state:
    st.session_state.messages = []

api_key = st.secrets.get("POLLINATIONS_API_KEY", "")
if not api_key:
    st.error("المفتاح ما راهش في Secrets!")
    st.stop()

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])
        if "image" in m:
            st.image(m["image"])

def ask_zould(prompt, mode):
    if mode == "🎨 يرسم و يصمم":
        enc = urllib.parse.quote(prompt)
        img_url = f"https://gen.pollinations.ai/image/{enc}?width=1024&height=1024&model=flux&nologo=true&key={api_key}"
        return None, img_url
    else:
        client = OpenAI(base_url="https://gen.pollinations.ai/api/v1", api_key=api_key)
        r = client.chat.completions.create(
            model="openai",
            messages=[
                {"role":"system","content":"انت ZOULD مساعد جزائري ذكي جدا، تهدر بالدارجة الجزائرية، قوي في كلش."},
                {"role":"user","content":prompt}
            ]
        )
        return r.choices[0].message.content, None

mode = st.selectbox("اختار وش يدير ZOULD:", ["💬 يهدر و يجاوب", "🎨 يرسم و يصمم"])
if prompt := st.chat_input("قول لـ ZOULD واش يدير..."):
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        with st.spinner("ZOULD يفكر...🧠⚡"):
            try:
                text, img = ask_zould(prompt, mode)
                if img:
                    st.image(img)
                    st.session_state.messages.append({"role":"assistant","content":"تفضل الصورة ⚡","image":img})
                else:
                    st.markdown(text)
                    st.session_state.messages.append({"role":"assistant","content":text})
            except Exception as e:
                st.error(f"صرا خطأ: {e}")
