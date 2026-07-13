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

### Step 2. Custom Instructions 없이 먼저 리팩토링 요청
Copilot Chat을 **Agent 모드**로 열고 아래처럼 요청해보세요.
```
프로젝트 전체 코드(main.py, database.py)를 검토해서, 더 견고하고
유지보수하기 좋은 구조로 자유롭게 리팩토링해줘.
```
→ 결과를 확인하세요. DB 커넥션 방식(`get_connection()`, 파라미터 바인딩)이
   그대로 유지됐나요? API 요청/응답 형식(JSON 스키마)이 바뀌지 않았나요?
   새 라이브러리(ORM 등)를 임의로 추가하진 않았나요? main.py/database.py의
   역할 분리가 유지됐나요?

> 💡 왜 "필드 추가" 대신 "자유 리팩토링"인가요? 필드를 추가하는 정도의 작업은
> 기존 코드 패턴을 보고 대부분 잘 따라합니다(모델이 이미 있는 코드를 참고하니까요).
> 반대로 "자유롭게 리팩토링해줘"처럼 재량을 많이 주는 요청은, 모델이 일반적인
> 모범 사례(예: ORM 도입, 응답 형식 표준화)를 따르고 싶어 해서 **이 프로젝트만의
> 규칙과 충돌할 가능성이 훨씬 큽니다.** 그래서 Custom Instructions의 효과가
> 훨씬 뚜렷하게 드러납니다.

확인이 끝났으면 백업해둔 폴더의 `main.py`, `database.py`로 다시 덮어써서 원상복구하세요.
(정교하게 되돌리는 게 목적이 아니라 "Custom Instructions 적용 전/후 비교"가 목적이므로
대략만 복구해도 무방합니다)

### Step 3. `.github/copilot-instructions.md` 작성
`.github/copilot-instructions.md` 파일을 열어서 템플릿의 빈칸을 채워보세요.
- 프로젝트 개요, 파일 구조, API 규칙
- 반드시 지킬 것 (예: SQL 파라미터 바인딩, DB 커넥션 close 등)
- 하지 말아야 할 것 (예: 임의로 새 라이브러리 추가 금지 등)

최대한 구체적으로 적을수록 다음 단계 결과가 달라집니다.

> 💡 **초안 작성이 막막하다면**: Copilot Chat에게 코드를 분석시켜서 초안을
> 받아보세요.
> ```
> 이 프로젝트(main.py, database.py, static/index.html)를 분석해서
> .github/copilot-instructions.md 초안을 작성해줘. 파일 구조, API 규칙,
> 코딩 컨벤션, 반드시 지킬 것, 하지 말아야 할 것을 포함하고, 특히 DB
> 커넥션 획득 방식과 SQL 쿼리 작성 패턴처럼 지금 코드에 이미 있는
> 컨벤션을 구체적으로 반영해줘.
> ```
> 생성된 초안을 그대로 쓰지 말고, 실제로 맞는 내용인지 직접 읽고 다듬으세요.

### Step 4. 같은 요청 다시 해보기
Step 2와 **동일한 프롬프트**로 다시 요청해보세요.
```
프로젝트 전체 코드(main.py, database.py)를 검토해서, 더 견고하고
유지보수하기 좋은 구조로 자유롭게 리팩토링해줘.
```
→ Copilot Chat 응답에 `copilot-instructions.md`가 참조(reference)되었는지 확인하세요.
→ Step 2 결과와 비교했을 때 무엇이 달라졌나요?

### Step 5. 워크스페이스 범위 확인 — 지침이 "이 폴더"에만 묶여있다는 것 체감하기
Custom Instructions는 **지금 VS Code로 열어놓은 폴더(워크스페이스)** 기준으로 적용됩니다.
폴더를 벗어나면 똑같은 지침이라도 적용되지 않는다는 것을 직접 확인해봅니다.

1. VS Code에서 **파일 > 새 창**(Mac: `Cmd+Shift+N`, Windows: `Ctrl+Shift+N`)을 열고,
   이번엔 `01_custom_instructions`의 **상위 폴더**(`day2/` 또는 레포 최상위 폴더)를 엽니다.
2. 새 창에서 Copilot Chat을 Agent 모드로 열고, Step 4와 **동일한 프롬프트**를 보냅니다.
   ```
   프로젝트 전체 코드(main.py, database.py)를 검토해서, 더 견고하고
   유지보수하기 좋은 구조로 자유롭게 리팩토링해줘.
   ```
3. 응답의 References에 `copilot-instructions.md`가 뜨는지 확인하세요.
   (뜨지 않거나, 지침 없이 진행했던 Step 2와 비슷한 결과가 나올 가능성이 높습니다)
4. 다시 원래 `01_custom_instructions` 창(또는 폴더)으로 돌아와 같은 요청을 반복해보고,
   이번엔 References에 참조되는지 다시 확인합니다.

→ **완전히 똑같은 질문**인데, 어느 폴더를 열고 있느냐에 따라 결과가 달라진다는 것을
확인하세요. Custom Instructions는 "이 워크스페이스를 여는 동안만" 적용되는,
**폴더에 종속된** 설정입니다. (그래서 오늘 실습 파일들이 레포 루트가 아니라
각 실습 폴더 안에 들어있는 것입니다)

### Step 6. 결과 비교
| | Custom Instructions 없이 | Custom Instructions 적용 후 |
|---|---|---|
| DB 커넥션/쿼리 방식(`get_connection()`, 파라미터 바인딩) 유지 | ? | ? |
| API 요청/응답 형식(JSON 스키마) 그대로 유지 | ? | ? |
| 새 라이브러리(ORM 등) 임의 추가 여부 | ? | ? |
| main.py/database.py 파일 역할 분리 유지 | ? | ? |

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
