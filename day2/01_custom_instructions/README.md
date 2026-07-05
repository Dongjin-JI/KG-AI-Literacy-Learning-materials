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

---

## 실습 순서

### Step 1. 폴더 열기 & 실행 확인
VS Code에서 `01_custom_instructions` 폴더를 열어주세요.
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
`http://localhost:8000` 접속해서 정상 동작하는지 확인하세요.

실습 중 되돌리기 편하도록 git으로 현재 상태를 체크포인트로 남겨두세요.
```bash
git init
git add -A
git commit -m "checkpoint"
```

### Step 2. Custom Instructions 없이 먼저 기능 추가 요청
Copilot Chat을 **Agent 모드**로 열고 아래처럼 짧게 요청해보세요.
```
할 일에 우선순위(높음/중간/낮음) 필드를 추가해줘
```
→ 결과를 확인하세요. 기존 파일 구조(main.py/database.py 역할 분리)를 지켰나요?
   SQL 쿼리 작성 방식, 에러 처리는 기존 코드와 일관성이 있나요?

확인이 끝났으면 변경사항을 되돌립니다.
```bash
git reset --hard
```

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

## 심화 실습 (시간이 남는다면)
파일 종류별로 다른 규칙을 적용하고 싶다면, `.github/instructions/` 폴더 아래
`applyTo` 프론트매터를 가진 파일을 여러 개 만들 수 있습니다.

`.github/instructions/backend.instructions.md`
```markdown
---
applyTo: "**/*.py"
---
- 함수는 database.py 에만 작성하고 main.py 는 라우팅만 담당해줘
- 모든 SQL 쿼리는 파라미터 바인딩만 사용해줘
```

`.github/instructions/frontend.instructions.md`
```markdown
---
applyTo: "static/**"
---
- 외부 프레임워크(React, Vue 등) 없이 순수 HTML/CSS/JS로만 작성해줘
- 기존 UI 톤(심플한 리스트형)을 유지해줘
```
→ Python 파일을 수정할 때와 HTML 파일을 수정할 때 서로 다른 규칙이 적용되는지 확인해보세요.

---

## 핵심 포인트
> TCCOV가 **"이번 한 번만" 주는 컨텍스트**라면,
> Custom Instructions는 **"항상 켜져 있는" 컨텍스트**입니다.
> 반복적으로 알려주는 게 지겨웠던 규칙일수록 Custom Instructions로 옮기고,
> 이번 요청에만 필요한 세부 지시는 TCCOV로 그때그때 주는 것이 가장 효율적입니다.
