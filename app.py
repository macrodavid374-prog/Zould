import streamlit as st
st.set_page_config(page_title="ZOULD", page_icon="⚡")
st.title("⚡ ZOULD")
st.success("مرحبا بيك في ZOULD - الموقع خدام!")
st.write("هذا هو موقعك الرسمي ZOULD")
name = st.text_input("اسمك:")
if st.button("دخول"):
    st.balloons()
    st.write(f"مرحبا {name}!")
