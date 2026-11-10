
import streamlit as st
import ollama

# 웹페이지 설정
st.set_page_config(
    page_title="Open Source LLM",
    page_icon="🤖",
    layout="centered"
)

# 제목
st.title("🤖 Open Source LLM Chat")
st.write("Qwen 2.5 기반 오픈소스 AI 대화 프로그램")

# 사용할 모델
MODEL = "qwen2.5:1.5b"

# 대화 기록 저장
if "messages" not in st.session_state:
    st.session_state.messages = []

# 기존 대화 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 질문 입력
prompt = st.chat_input("AI에게 질문해 보세요.")

if prompt:

    # 사용자 질문 저장
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # AI 답변 생성
    with st.chat_message("assistant"):
        with st.spinner("AI가 생각하고 있습니다..."):

            try:
                response = ollama.chat(
                    model=MODEL,
                    messages=st.session_state.messages
                )

                answer = response["message"]["content"]

                st.markdown(answer)

                # 답변 저장
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")

# 사이드바
with st.sidebar:
    st.header("프로그램 정보")
    st.write("모델: Qwen 2.5")
    st.write("크기: 1.5B")
    st.write("실행 환경: Ollama")

    if st.button("대화 초기화"):
        st.session_state.messages = []
        st.rerun()
