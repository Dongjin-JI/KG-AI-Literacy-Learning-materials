# 실습 2 - 나만의 코딩 튜터봇 만들기

## GitHub Copilot ↔ Continue.dev 대응표

| 개념 | GitHub Copilot | Continue.dev |
|---|---|---|
| 상시 지침 (Custom Instructions) | Custom Instructions | **Rules** |
| 프로젝트 공유 지침 파일 위치 | `.github/copilot-instructions.md` | `.continue/rules/*.md` |
| 파일 종류별 조건부 지침 | `.github/instructions/*.instructions.md` + `applyTo` | `.continue/rules/*.md` + `globs` |
| 항상 적용 여부 지정 | (기본이 항상 적용) | `alwaysApply: true/false` |
| 개인 전역 지침 | 계정 설정 > Personal custom instructions | `~/.continue/rules/*.md` |
| 재사용 가능한 호출형 프롬프트 (Skill) | Skills / Prompt files | **Prompts** (`.continue/prompts/*.md`, `invokable: true`) |
| Chat / Agent 모드 | Copilot Chat / Agent mode | Continue Chat / Agent mode |
| 모델 접근 방식 | GitHub 계정 인증 | Elice API (`apiBase` + `apiKey`, `openai/` 프리픽스 필요) |

> 오늘 실습은 Continue.dev로 진행하지만, 여기서 배우는 개념(지침 자동 적용, 재사용 프롬프트)은 Copilot을 포함한 모든 AI 코딩 툴에 공통으로 존재합니다. 도구 이름만 다를 뿐 사고방식은 동일합니다.

---

## 목표
시스템 프롬프트와 지식 파일을 직접 작성해서,
**학생 자율학습을 도와주는 AI 코딩 튜터봇**을 만들어봅니다.

## 상황
당신은 코딩 과외를 하고 있는 선생님입니다. 학생이 자율학습 할 때
도움이 되는 코딩 튜터 챗봇을 간단하게 만들고자 합니다.
기초 코딩 문법과 기초 코딩테스트(알고리즘) 관련 자료를 학생 수준에 맞게
잘 전달해주는 것이 목표입니다.

## 파일 구조
```
02_context_lab/
├── app.py            # 튜터봇 앱 (수정 불필요, 새 대화/히스토리 기능 포함)
├── system_prompt.md  # 튜터봇 페르소나 및 답변 방식 정의
├── knowledge.md      # 튜터링 대상/커리큘럼/지도 방식 (직접 작성)
└── README.md         # 실습 가이드
```

## 실습 순서

### Step 1. 설치 및 실행
```bash
pip install openai streamlit
streamlit run app.py
```

### Step 2. 지식 파일 없이 먼저 질문해보기
`knowledge.md` 를 비워둔 채로 아래 질문을 해보세요.
```
이진 탐색 알고리즘이 뭔지 알려줘
```
→ 결과를 기억해두세요. 학생 수준을 고려한 설명인가요, 아니면 전문가용 설명인가요?

### Step 3. knowledge.md 직접 작성 (Continue Chat 모드 활용)
1. VS Code에서 Continue Chat을 **Chat 모드**로 엽니다.
2. `knowledge.md` 파일을 열고, 안내된 [작성 방법]에 따라 Chat 모드와 대화하며 항목을 채워봅니다.
   막막하면 이렇게 물어보세요.
   ```
   나는 코딩 과외 선생님이고, 학생 자율학습용 코딩 튜터 챗봇을 만들려고 해.
   knowledge.md 의 각 항목(튜터링 대상, 커리큘럼 범위, 설명 스타일,
   자주 쓰는 지도 패턴, AI에게 원하는 답변 방식, 학생들이 자주 헷갈려하는 부분)을
   같이 채워줘.
   ```
3. Chat 모드가 제안한 초안을 그대로 쓰지 말고, 실제 가르치는(또는 가르친다고 가정한) 상황에 맞게 직접 다듬어서 `knowledge.md`에 채워 넣습니다.
   최대한 구체적으로 작성할수록 좋습니다.

### Step 4. 같은 질문 다시 해보기
사이드바의 **🔄 프롬프트 새로고침** 버튼을 누르고 같은 질문을 해보세요.
```
이진 탐색 알고리즘이 뭔지 알려줘
```
→ Step 2와 어떻게 달라졌나요? 학생 수준에 맞춰 개념 → 힌트 순서로 설명하나요?

### Step 5. system_prompt.md 수정해보기
`system_prompt.md` 하단의 자유 수정 구역을 바꿔보세요.
- 튜터봇 이름 바꾸기
- 답변 규칙 추가하기 (예: "힌트 3번 줘도 못 풀면 그때 정답을 보여줘")

### Step 6. 새 대화 / 대화 히스토리 사용해보기
- 사이드바의 **🆕 새 대화** 버튼을 누르면 새로운 대화가 시작됩니다. 질문 주제가 바뀔 때 활용해보세요.
- **🕘 대화 히스토리** 목록에서 이전 대화를 클릭하면 그 대화로 다시 돌아갈 수 있습니다.
- 대화의 첫 질문 내용이 자동으로 히스토리 제목이 됩니다.

### Step 7. 도전 과제
아래 질문들로 튜터봇을 테스트해보세요.
- "재귀 함수가 뭔지 완전 처음 배우는 사람도 이해하게 설명해줘"
- "이 코드가 왜 안 되는지 알려줘 (학생이 짠 것처럼 오류 있는 코드 붙여넣기)"
- "방금 문제랑 비슷한 연습 문제 하나만 더 줘"

---

## 핵심 포인트
knowledge.md 를 더 구체적으로 쓸수록 → 학생 수준에 맞는 더 좋은 답변이 나옵니다.
이것이 바로 **컨텍스트 엔지니어링**입니다.
그리고 이 knowledge.md 를 채우는 방식(Chat 모드로 상황을 설명하고 함께 정리하기)은
Day2 Rules 실습에서도 그대로 이어집니다.
