import streamlit as st
from openai import OpenAI
from pathlib import Path

# ============================================================
# 엘리스 API 설정
# ============================================================
API_KEY = "YOUR_ELICE_API_KEY"   # 발급받은 API 키로 교체하세요
BASE_URL = "YOUR_ELICE_BASE_URL" # 엘리스 플랫폼 base_url로 교체하세요
MODEL = "YOUR_MODEL_NAME"        # 사용할 모델명으로 교체하세요

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL,
)

# ============================================================
# 시스템 프롬프트 로드
# system_prompt.md + knowledge.md 를 합쳐서 최종 시스템 프롬프트 생성
# ============================================================
def load_system_prompt() -> str:
    system = Path("system_prompt.md").read_text(encoding="utf-8")
    knowledge = Path("knowledge.md").read_text(encoding="utf-8")
    return f"{system}\n\n---\n\n## 사용자 지식 베이스\n{knowledge}"


# ============================================================
# Streamlit UI
# ============================================================
st.set_page_config(page_title="나만의 코딩 어시스턴트", page_icon="🤖")
st.title("🤖 나만의 코딩 어시스턴트")
st.caption("knowledge.md 를 채울수록 더 똑똑한 어시스턴트가 됩니다.")

# 사이드바: 현재 시스템 프롬프트 확인
with st.sidebar:
    st.subheader("📄 현재 시스템 프롬프트")
    try:
        st.text_area(
            label="system_prompt.md + knowledge.md",
            value=load_system_prompt(),
            height=400,
            disabled=True,
        )
    except FileNotFoundError as e:
        st.error(f"파일을 찾을 수 없습니다: {e}")

    if st.button("🔄 프롬프트 새로고침"):
        st.rerun()

# 채팅 히스토리 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 대화 출력
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 사용자 입력
if prompt := st.chat_input("코드 관련 질문을 입력하세요..."):

    # 사용자 메시지 추가
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 어시스턴트 응답 생성
    with st.chat_message("assistant"):
        try:
            system_prompt = load_system_prompt()
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    *st.session_state.messages,
                ],
                stream=True,
            )

            result = st.write_stream(
                chunk.choices[0].delta.content or ""
                for chunk in response
                if chunk.choices and chunk.choices[0].delta.content
            )

        except Exception as e:
            result = f"❌ 오류가 발생했습니다: {e}"
            st.error(result)

    st.session_state.messages.append({"role": "assistant", "content": result})
