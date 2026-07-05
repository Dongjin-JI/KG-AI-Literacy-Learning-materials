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
# 대화 세션 관리 (새 대화 / 대화 히스토리)
# ============================================================
def new_session() -> dict:
    return {"title": "새 대화", "messages": []}


if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = [new_session()]
    st.session_state.current_session = 0


def current_messages() -> list:
    return st.session_state.chat_sessions[st.session_state.current_session]["messages"]


# ============================================================
# Streamlit UI
# ============================================================
st.set_page_config(page_title="나만의 코딩 어시스턴트", page_icon="🤖")
st.title("🤖 나만의 코딩 어시스턴트")
st.caption("knowledge.md 를 채울수록 더 똑똑한 어시스턴트가 됩니다.")

# 사이드바: 시스템 프롬프트 확인 + 대화 관리
with st.sidebar:
    st.subheader("📄 현재 시스템 프롬프트")
    try:
        st.text_area(
            label="system_prompt.md + knowledge.md",
            value=load_system_prompt(),
            height=280,
            disabled=True,
        )
    except FileNotFoundError as e:
        st.error(f"파일을 찾을 수 없습니다: {e}")

    if st.button("🔄 프롬프트 새로고침", use_container_width=True):
        st.rerun()

    st.divider()

    if st.button("🆕 새 대화", use_container_width=True):
        st.session_state.chat_sessions.append(new_session())
        st.session_state.current_session = len(st.session_state.chat_sessions) - 1
        st.rerun()

    st.subheader("🕘 대화 히스토리")
    for i, session in enumerate(st.session_state.chat_sessions):
        label = ("👉 " if i == st.session_state.current_session else "") + session["title"]
        if st.button(label, key=f"session_{i}", use_container_width=True):
            st.session_state.current_session = i
            st.rerun()

# 현재 선택된 대화의 메시지 목록
messages = current_messages()

# 이전 대화 출력
for msg in messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 사용자 입력
if prompt := st.chat_input("코드 관련 질문을 입력하세요..."):

    # 이 대화의 첫 질문이면, 질문 내용으로 히스토리 제목을 정해줌
    is_first_message = not messages
    if is_first_message:
        title = prompt.strip()
        st.session_state.chat_sessions[st.session_state.current_session]["title"] = (
            title[:20] + "..." if len(title) > 20 else title
        )

    # 사용자 메시지 추가
    messages.append({"role": "user", "content": prompt})
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
                    *messages,
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

    messages.append({"role": "assistant", "content": result})

    # 히스토리 제목이 방금 바뀌었다면, 사이드바에 새 제목이 바로 보이도록 다시 그림
    if is_first_message:
        st.rerun()
