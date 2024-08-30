import streamlit as st
from openai import OpenAI
def chatbot(question):
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "너는 안동의 명물이 아닌지 알려주는 봇이야 맞다면 y 아니면 n으로 대답해줘"},
        {"role": "user", "content": "찜닭!"}
  ]
  )

    return completion.choices[0].message.content


question ="안동에서 유명한것은?"
answer = st.text_input(question)
if st.button("정답 확인하기"):
    result = chatbot(answer)
    if result =='y':
        st.success("정답")
    else:
        st.error("오답")
