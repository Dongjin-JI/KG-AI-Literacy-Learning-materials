# KG에듀원 AI 리터러시 교육
## GitHub Copilot 활용하기

> 📌 **안내**: 참가자 전원에게 GitHub Copilot Pro 플랜 계정이 제공됩니다.
> 이번 기수는 실습 환경이 **Mac**입니다. 아래 안내도 Mac 기준으로 되어 있습니다.

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
| 폴더 | 실습 내용 | 시간 |
|------|----------|------|
| `01_custom_instructions/` | Custom Instruction 만들기 | 90분 |
| `02_agent_skills/` | Agent Skills 만들기 (Skills) | 90분 |
| `03_awesome_copilot/` | awesome-copilot 탐색하기 (컨텍스트 엔지니어링 심화) | 60분 |
| `04_final_project/` | Copilot을 활용한 나만의 프로젝트 2 + 최종 발표 (자유 실습) | 90분 |

윤리적 AI 활용 가이드는 이론 교육으로 진행합니다 (별도 실습 자료 없음).

---

## 🛠️ 사전 준비 (교육 시작 전 확인)

아래가 설치/준비되어 있는지 확인해주세요. (Mac 기준)

| 항목 | 버전 | 확인 방법 |
|------|------|----------|
| VS Code | 최신 | `code --version` |
| Python | 3.11.8 | `python3 --version` |
| GitHub 계정 | - | github.com 로그인 확인 (Copilot Pro 계정은 당일 안내) |

### Copilot 확장 설치 및 로그인 (교육 당일)
1. VS Code Extensions에서 **GitHub Copilot** 검색 후 설치
2. VS Code 우측 하단(또는 Command Palette)에서 **Sign in to GitHub**로 로그인
3. 안내받은 Copilot Pro 계정으로 로그인되어 있는지 확인 (Copilot Chat 아이콘이 활성화되어 있으면 정상)

### 패키지 설치
```bash
pip3 install fastapi uvicorn openai streamlit
```

---
