# 실습 1 - Custom Instruction 만들기

## 목표
`.github/copilot-instructions.md` 파일을 작성해서, 매번 프롬프트에 반복 입력하던
프로젝트 컨텍스트를 **한 번만 설정하면 계속 적용되는** 상시 컨텍스트로 만듭니다.

## Custom Instructions란?
어제 배운 TCCOV 프롬프트는 **그때그때** Context를 입력하는 방식이었습니다.
Custom Instructions는 워크스페이스에 `.github/copilot-instructions.md` 파일을 만들어두면,
**그 폴더를 여는 동안 모든 Copilot Chat 요청에 자동으로 포함**되는 방식입니다.

| | TCCOV 프롬프트 | Custom Instructions |
|---|---|---|
| 적용 범위 | 그 대화 1번 | 워크스페이스를 여는 동안 항상 |
| 입력 위치 | 매번 채팅창에 직접 입력 | `.github/copilot-instructions.md` 파일 1번 작성 |
| 적합한 내용 | 이번 요청에만 필요한 세부 지시 | 프로젝트 전체에 항상 적용되는 규칙/컨벤션 |

> ⚠️ **헷갈리기 쉬운 부분**: `.github/copilot-instructions.md`는 "나만의 개인 지침"이 아닙니다.
> 이 파일은 **깃 레포 안에 들어있는 파일**이라서, git에 커밋하면 팀원 전체가 공유합니다.
> 즉 "이 프로젝트를 여는 사람이라면 누구든" 똑같이 적용되는 **프로젝트 단위 공유 규칙**입니다.
>
> (참고로 GitHub 계정 설정에 등록하는 "개인(Personal) custom instructions"도 별도로 존재합니다.
> 이건 내 계정으로 로그인했을 때 **모든 레포에 걸쳐 나에게만** 적용되는 설정이라, 오늘 실습하는
> 프로젝트 단위 지침과는 다릅니다.)

---

## 실습 파일
이 폴더에는 이미 동작하는 미니 TODO 앱이 들어있습니다.
- `main.py`, `database.py` : FastAPI + SQLite 백엔드
- `static/index.html` : 프론트엔드
- `.github/copilot-instructions.md` : 실습에서 직접 채울 템플릿
- `templates/ai-service-instructions-developer.md`, `templates/ai-service-instructions-non-developer.md` :
  심화 실습에서 본인 AI 서비스용으로 채울 템플릿

---

## 실습 순서

### Step 1. 폴더 열기 & 실행 확인
VS Code에서 `01_custom_instructions` 폴더를 열어주세요.
```bash
pip3 install -r requirements.txt
uvicorn main:app --reload
```
`http://localhost:8000` 접속해서 정상 동작하는지 확인하세요.

실습 중 되돌리기 편하도록, 폴더 전체를 `01_custom_instructions_backup`으로
복사해두세요 (Finder에서 복사-붙여넣기면 충분합니다. git은 사용하지 않습니다).

### Step 2. Custom Instructions 없이 먼저 기능 추가 요청
Copilot Chat을 **Agent 모드**로 열고 아래처럼 짧게 요청해보세요.
```
할 일에 우선순위(높음/중간/낮음) 필드를 추가해줘
```
→ 결과를 확인하세요. 기존 파일 구조(main.py/database.py 역할 분리)를 지켰나요?
   SQL 쿼리 작성 방식, 에러 처리는 기존 코드와 일관성이 있나요?

확인이 끝났으면 백업해둔 폴더의 `main.py`, `database.py`로 다시 덮어써서 원상복구하세요.
(정교하게 되돌리는 게 목적이 아니라 "Custom Instructions 적용 전/후 비교"가 목적이므로
대략만 복구해도 무방합니다)

### Step 3. `.github/copilot-instructions.md` 작성
`.github/copilot-instructions.md` 파일을 열어서 템플릿의 빈칸을 채워보세요.
- 프로젝트 개요, 파일 구조, API 규칙
- 반드시 지킬 것 (예: SQL 파라미터 바인딩, DB 커넥션 close 등)
- 하지 말아야 할 것 (예: 임의로 새 라이브러리 추가 금지 등)

최대한 구체적으로 적을수록 다음 단계 결과가 달라집니다.

### Step 4. 같은 요청 다시 해보기
Step 2와 **동일한 프롬프트**로 다시 요청해보세요.
```
할 일에 우선순위(높음/중간/낮음) 필드를 추가해줘
```
→ Copilot Chat 응답에 `copilot-instructions.md`가 참조(reference)되었는지 확인하세요.
→ Step 2 결과와 비교했을 때 무엇이 달라졌나요?

### Step 5. 결과 비교
| | Custom Instructions 없이 | Custom Instructions 적용 후 |
|---|---|---|
| 파일 역할 분리 유지 | ? | ? |
| SQL 작성 방식 | ? | ? |
| 에러/예외 처리 | ? | ? |
| 프론트엔드 스타일 일관성 | ? | ? |

---

## 심화 실습 (시간이 남는다면) — 본인 AI 서비스에 맞는 지침 작성해보기
지금까지는 오늘 실습용 TODO 앱을 대상으로 Custom Instructions를 연습했습니다.
이번에는 **실제 여러분이 업무에서 쓰는(또는 쓰고 싶은) AI 서비스**를 대상으로
지침을 직접 작성해보는 시간입니다.

1. 아래 두 양식 중 본인 상황에 맞는 것을 하나 고르세요. (`templates/` 폴더)
   - `templates/ai-service-instructions-developer.md` — 코드/API/기술 스택이 있는 개발 업무용
   - `templates/ai-service-instructions-non-developer.md` — 보고서 작성, 데이터 정리,
     고객 응대 등 코딩 외 업무용
2. 템플릿을 복사해서 본인 상황에 맞게 채워보세요. 실제 사내 시스템명이나
   민감 정보는 적지 말고, 패턴만 일반화해서 작성하세요.
3. 관련 프로젝트(또는 새 폴더)를 열고 `.github/copilot-instructions.md`로
   저장한 뒤, 관련 요청을 해서 실제로 어떻게 다르게 동작하는지 확인해보세요.
4. 시간이 되면 옆 사람과 서로의 지침을 비교해보세요. 같은 "개발자용"이어도
   업무에 따라 반드시 지킬 것/하지 말아야 할 것이 얼마나 다른지 확인할 수 있습니다.

## 핵심 포인트
> TCCOV가 **"이번 한 번만" 주는 컨텍스트**라면,
> Custom Instructions는 **"항상 켜져 있는" 컨텍스트**입니다.
> 반복적으로 알려주는 게 지겨웠던 규칙일수록 Custom Instructions로 옮기고,
> 이번 요청에만 필요한 세부 지시는 TCCOV로 그때그때 주는 것이 가장 효율적입니다.
