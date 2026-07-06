# 실습 1 — Rules(지침) 만들기

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
`.continue/rules/project-context.md` 파일을 작성해서, 매번 프롬프트에 반복 입력하던
프로젝트 컨텍스트를 한 번만 설정하면 계속 적용되는 상시 컨텍스트로 만듭니다.

## Rules란?
어제 배운 TCCOV 프롬프트는 그때그때 Context를 입력하는 방식이었습니다.
Rules는 워크스페이스에 `.continue/rules/` 폴더 안에 파일을 만들어두면,
그 폴더를 여는 동안 모든 채팅/Agent 요청에 자동으로 포함되는 방식입니다.

| | TCCOV 프롬프트 | Rules |
|---|---|---|
| 적용 범위 | 그 대화 1번 | 워크스페이스를 여는 동안 항상 |
| 입력 위치 | 매번 채팅창에 직접 입력 | `.continue/rules/` 파일 1번 작성 |
| 적합한 내용 | 이번 요청에만 필요한 세부 지시 | 프로젝트 전체에 항상 적용되는 규칙/컨벤션 |

⚠️ **헷갈리기 쉬운 부분**: `.continue/rules/` 폴더는 워크스페이스(프로젝트) 루트에
만듭니다. 이 파일은 프로젝트 폴더 안에 있으므로 git에 커밋하면 팀원 전체가 공유합니다.
즉 "이 프로젝트를 여는 사람이라면 누구든" 똑같이 적용되는 프로젝트 단위 공유 규칙입니다.

(참고로 `~/.continue/rules/` — 내 컴퓨터 홈 디렉토리에 있는 전역(Global) Rules도
별도로 존재합니다. 이건 내가 어떤 프로젝트를 열든 항상 나에게만 적용되는 설정이라,
오늘 실습하는 프로젝트 단위 지침과는 다릅니다.)

## 실습 파일
- `main.py`, `database.py` : FastAPI + SQLite 백엔드
- `static/index.html` : 프론트엔드
- `.continue/rules/project-context.md` : 실습에서 직접 채울 템플릿

## Step 1. 폴더 열기 & 실행 확인
VS Code에서 `01_rules_custom_instruction` 폴더를 열어주세요.
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
`http://localhost:8000` 접속해서 정상 동작하는지 확인하세요.
실습 중 되돌리기 편하도록, 폴더 전체를 `01_rules_custom_instruction_backup`으로
복사해두세요 (탐색기에서 복사-붙여넣기면 충분합니다. git은 사용하지 않습니다).

## Step 2. Rules 없이 먼저 기능 추가 요청
Continue Chat을 Agent 모드로 열고 아래처럼 짧게 요청해보세요.
> 할 일에 우선순위(높음/중간/낮음) 필드를 추가해줘

결과를 확인하세요. 기존 파일 구조(main.py/database.py 역할 분리)를 지켰나요?
SQL 쿼리 작성 방식, 에러 처리는 기존 코드와 일관성이 있나요?
확인이 끝났으면 백업해둔 폴더의 `main.py`, `database.py`로 다시 덮어써서 원상복구하세요.
(정교하게 되돌리는 게 목적이 아니라 "Rules 적용 전/후 비교"가 목적이므로 대략만
복구해도 무방합니다)

## Step 3. `.continue/rules/project-context.md` 작성
템플릿의 빈칸을 채워보세요.
- 프로젝트 개요, 파일 구조, API 규칙
- 반드시 지킬 것 (예: SQL 파라미터 바인딩, DB 커넥션 close 등)
- 하지 말아야 할 것 (예: 임의로 새 라이브러리 추가 금지 등)

최대한 구체적으로 적을수록 다음 단계 결과가 달라집니다.

## Step 4. 같은 요청 다시 해보기
Step 2와 동일한 프롬프트로 다시 요청해보세요.
> 할 일에 우선순위(높음/중간/낮음) 필드를 추가해줘

Continue 하단 툴바의 Rules 아이콘을 눌러 이번 요청에 어떤 rule이 적용됐는지 확인하세요.
Step 2 결과와 비교했을 때 무엇이 달라졌나요?

## Step 5. 결과 비교
| | Rules 없이 | Rules 적용 후 |
|---|---|---|
| 파일 역할 분리 유지 | ? | ? |
| SQL 작성 방식 | ? | ? |
| 에러/예외 처리 | ? | ? |
| 프론트엔드 스타일 일관성 | ? | ? |

## 심화 실습 (시간이 남는다면)
파일 종류별로 다른 규칙을 적용하려면, `.continue/rules/` 안에 `globs` 프론트매터를
가진 파일을 여러 개 만들 수 있습니다.

`.continue/rules/backend.md`
```yaml
---
name: Backend Rules
globs: "**/*.py"
alwaysApply: false
---
- 함수는 database.py 에만 작성하고 main.py 는 라우팅만 담당해줘
- 모든 SQL 쿼리는 파라미터 바인딩만 사용해줘
```

`.continue/rules/frontend.md`
```yaml
---
name: Frontend Rules
globs: "static/**"
alwaysApply: false
---
- 외부 프레임워크(React, Vue 등) 없이 순수 HTML/CSS/JS로만 작성해줘
- 기존 UI 톤(심플한 리스트형)을 유지해줘
```

## 핵심 포인트
TCCOV가 "이번 한 번만" 주는 컨텍스트라면, Rules는 "항상 켜져 있는" 컨텍스트입니다.
반복적으로 알려주는 게 지겨웠던 규칙일수록 Rules로 옮기고, 이번 요청에만 필요한
세부 지시는 TCCOV로 그때그때 주는 것이 가장 효율적입니다.
