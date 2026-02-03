import streamlit as st

# Page config
st.set_page_config(
    page_title="Valentine 💖",
    page_icon="💖",
    layout="centered"
)

# Background & button styling
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
}
.stButton > button {
    background-color: #ff4d6d;
    color: white;
    border-radius: 25px;
    padding: 10px 20px;
    border: none;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

st.title("💘 Valentine Special 💘")

name = st.text_input("Enter your name 💕")

if name:
    st.markdown(f"## 💖 {name}, will you be my Valentine? 💖")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes ❤️"):
            st.success("💖 Yayyy betuuuuu ❤️! I knew it 😍💖")
            st.image(
                "https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif",
                width=300
            )

    with col2:
        st.button("No 😢")
