# KG에듀원 AI 리터러시 교육
## AI 코딩 툴 활용하기 (실습: Continue.dev / 시연: GitHub Copilot)

> 📌 **안내**: 이 교육은 원래 GitHub Copilot 기준으로 설계되었지만,
> Copilot 개인 플랜 신규 가입 이슈로 **참가자 실습은 Continue.dev**로 진행합니다.
> GitHub Copilot은 강사가 시연할 때만 사용합니다.
> 각 실습 폴더 README 상단의 "GitHub Copilot ↔ Continue.dev 대응표"를 참고하면
> 두 도구의 개념이 어떻게 대응되는지 확인할 수 있습니다.

---

## 📌 실습 파일 받는 방법

### git 사용 시
```bash
git clone https://github.com/Dongjin-JI/KG-AI-Literacy-Learning-materials.git
```

### git 모를 경우
우측 상단 **Code → Download ZIP** 클릭 후 압축 해제

---

## 📂 실습 구성

### Day 1
| 폴더 | 실습 내용 | 시간 |
|------|----------|------|
| `01_prompt_engineering/` | 프롬프트 엔지니어링 미니 실습 (TCCOV) | 30분 |
| `02_context_lab/` | 나만의 코딩 어시스턴트 만들기 | 30분 |
| `03_todo_app/` | TODO List 앱 만들기 (Agent 모드) | 60분 |
| `04_todo_advanced/` | TODO List 앱 고도화하기 | 60분 |
| `05_final_project/` | Copilot을 활용한 나만의 프로젝트 1 (자유 실습) | 150분 |

### Day 2
| 폴더 | 실습 내용 | 시간 | 상태 |
|------|----------|------|------|
| `01_rules_custom_instruction/` | Rules(지침) 만들기 | 90분 | 확정 |
| `02_prompts_skills/` | Prompts로 반복 작업 자동화하기 | 90분 | ⚠️ 초안 |
| `03_context_engineering/` | 컨텍스트 엔지니어링 심화 (awesome-copilot 탐색·번역) | 60분 | ⚠️ 초안 |
| `04_final_project/` | Rules + Prompts를 내 프로젝트에 적용하기 (자유 실습) | 90분 | ⚠️ 초안 |

윤리적 AI 활용 가이드는 이론 교육으로 진행합니다 (별도 실습 자료 없음).

---

## 🛠️ 사전 준비 (교육 시작 전 확인)

아래가 설치되어 있는지 확인해주세요.

| 항목 | 버전 | 확인 방법 |
|------|------|----------|
| VS Code | 최신 | `code --version` |
| Python | 3.11.8 | `python --version` |

> GitHub 계정은 필요하지 않습니다. 실습 파일은 익명으로 클론하거나 ZIP으로
> 받으며, Continue.dev는 Elice API로 연결하므로 GitHub 로그인이 필요 없습니다.

### Continue.dev 확장 설치 및 연결 (교육 당일)
1. VS Code Extensions에서 **Continue** 검색 후 설치
2. Continue 설정에서 아래처럼 모델을 연결합니다. (안내받은 API 키로 교체)
   ```yaml
   models:
     - name: GPT-5 mini (Elice)
       provider: openai
       model: openai/gpt-5-mini
       apiBase: <안내받은 Elice API Base URL>
       apiKey: <안내받은 Elice API Key>
   ```
   - 모델명 앞에 `openai/` 프리픽스를 꼭 붙여야 합니다.
   - GitHub Copilot은 강사 시연 전용이며, 참가자는 설치/로그인하지 않습니다.

### 패키지 설치
```bash
pip install fastapi uvicorn openai streamlit
```

---
