import streamlit as st
from datetime import datetime

st.set_page_config(page_title="ZOULD", page_icon="⚡", layout="centered")

st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #1a1a2e, #16213e); color: white; }
h1 { text-align: center; }
</style>
""", unsafe_allow_html=True)

st.title("⚡ ZOULD - الذكاء الخارق")
st.caption(f"Online 24/7 | {datetime.now().strftime('%H:%M')}")

mode = st.selectbox("ZOULD اختار وش يدير:", ["💬 يهدر و يجاوب", "🎨 يرسم و يصمم", "💻 يكتب كود"])

user_input = st.chat_input("واش يدير ZOULD قول لـ...")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        if "يهدر" in mode:
            response = f"سمعتك خويا! قلت: '{user_input}'\n\nأنا ZOULD، وراني واجد نجاوبك على أي سؤال. هذا مثال لرد ذكي، وتقدر تطورني لاحقاً بـ API Key."
        elif "يرسم" in mode:
            response = f"لو كان عندي رسم، كنت نرسملك: '{user_input}'\n\nحاليا نقدر نوصفلك الصورة بالتفصيل باش تستخدمها في أي مولد صور."
        else:
            response = f"طلبت كود لـ: '{user_input}'\n\n```python\n# مثال كود\ndef zould_example():\n    print('{user_input}')\n    return 'ZOULD جاهز!'\n```"
        st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
