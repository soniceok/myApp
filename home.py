import streamlit as st

st.title("Streamlit Course :sun_with_face:")
st.code("pip install streamlit")
st.header("streamlit 설치")
st.write("Termainal에 streamlit 패키지 설치")
st.write("home.py 만들기")
with st.echo():
    import streamlit
    st.write("Hello, There!")
st.header("streamlit 웹 실행하기")