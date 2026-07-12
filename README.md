# KG에듀원 AI 리터러시 교육
## GitHub Copilot 활용하기

> 📌 **안내**: 참가자 전원에게 GitHub Copilot Pro 플랜 계정이 제공됩니다.
> 실습 환경(OS)은 기수마다 다를 수 있어, 사전 준비 항목은 Mac/Windows 둘 다
> 안내합니다. 본인 노트북 OS에 맞는 항목만 따라 하시면 됩니다.

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

아래 5가지를 준비해주세요. Mac / Windows 각각의 설치 방법을 안내합니다.
참가자 전원에게 **GitHub Copilot Pro 플랜 계정**이 제공되며, 로그인은 교육 당일 진행합니다.

### 1. Git 설치
**Mac**
- 터미널을 열고 `git --version` 입력 → 이미 설치돼 있으면 버전이 바로 나옵니다.
- 없다면 터미널에 `xcode-select --install` 입력 후 안내에 따라 설치 (Xcode Command Line Tools에 Git 포함)
- 또는 Homebrew가 있다면 `brew install git`

**Windows**
- https://git-scm.com/download/win 접속 → 자동으로 다운로드되는 설치 파일 실행
- 설치 옵션은 기본값 그대로 두고 진행(Next 계속)해도 무방합니다.
- 설치 후 확인: Git Bash 또는 PowerShell/명령 프롬프트에서 `git --version`

### 2. VS Code 설치
**Mac**
1. https://code.visualstudio.com/ 접속 → **Download for macOS** 클릭
2. 다운로드된 `.zip` 압축 해제 → `Visual Studio Code.app`을 **응용 프로그램(Applications)** 폴더로 이동
3. Applications 폴더 또는 Spotlight(Cmd+Space)에서 실행

**Windows**
1. https://code.visualstudio.com/ 접속 → **Download for Windows** 클릭 (System Installer 권장)
2. 다운로드된 설치 파일 실행 → 기본 옵션으로 설치 진행
   - "Add to PATH" 체크박스는 켜진 상태로 진행하세요.
3. 설치 후 시작 메뉴에서 "Visual Studio Code" 실행

### 3. Python 3.12.3 설치
**Mac**
1. https://www.python.org/downloads/release/python-3123/ 접속 → **macOS 64-bit universal2 installer** 다운로드
2. 설치 파일 실행 후 안내에 따라 설치
3. 확인: 터미널에서 `python3 --version` → `Python 3.12.3` 확인
   - Mac은 `python`이 아니라 `python3`, `pip`이 아니라 `pip3`를 사용합니다. (이 레포의 모든 실습 안내도 `python3`/`pip3` 기준입니다)

**Windows**
1. https://www.python.org/downloads/release/python-3123/ 접속 → **Windows installer (64-bit)** 다운로드
2. 설치 파일 실행 시 하단의 **"Add python.exe to PATH"** 체크박스를 반드시 체크한 뒤 설치
3. 확인: 명령 프롬프트/PowerShell에서 `python --version` → `Python 3.12.3` 확인

### 4. GitHub Copilot 확장 설치 (Mac/Windows 공통, 교육 당일)
1. VS Code 실행 → 좌측 사이드바 Extensions 아이콘 클릭 (단축키 Mac: `Cmd+Shift+X`, Windows: `Ctrl+Shift+X`)
2. 검색창에 **GitHub Copilot** 입력 → **Install** 클릭
   - 최신 버전은 설치 시 **GitHub Copilot Chat**도 함께 설치됩니다.

### 5. Copilot 로그인 (Mac/Windows 공통, 교육 당일)
1. VS Code 우측 하단 계정 아이콘을 클릭하거나, Command Palette(Mac: `Cmd+Shift+P`, Windows: `Ctrl+Shift+P`)를 열고 **"GitHub Copilot: Sign in"** 입력 후 선택
2. 브라우저가 열리면 안내받은 **GitHub Copilot Pro 계정**으로 로그인
3. VS Code로 돌아와 로그인이 완료됐는지 확인 (Copilot Chat 아이콘이 활성화되어 있으면 정상)

### 패키지 설치
**Mac**
```bash
pip3 install fastapi uvicorn openai streamlit
```

**Windows**
```powershell
pip install fastapi uvicorn openai streamlit
```

---
