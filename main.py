import streamlit as st
# from streamlit_chat import message # If you use streamlit-chat

st.title("삼각함수 챗봇")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("삼각함수에 대해 무엇이 궁금하신가요?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 여기에 챗봇의 응답 로직을 구현합니다.
    # 예시:
    response = f"당신이 '{prompt}'라고 질문했군요. 아직 학습 중입니다."
    # 실제로는 규칙 기반, LLM 기반, 또는 수학 라이브러리 연동 로직이 들어갑니다.

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
