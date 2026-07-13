# 실습 2 - Agent Skills 만들기 (Skills)

## 목표
`.github/skills/` 아래에 나만의 Agent Skill을 만들어서, Copilot이 작업 내용에 맞는 Skill을 스스로
**발견(Discovery) → 활성화(Activation) → 실행(Execution)** 하는 과정을 체감합니다.

> ⚠️ Agent Skills는 최근에 추가된 기능입니다. 사용 중인 Copilot/VS Code 버전에 따라 아직 지원되지
> 않을 수 있으니, 먼저 확장 프로그램을 최신 버전으로 업데이트한 뒤 실습을 시작하세요.

## Agent Skills란?
Copilot이 특정 작업을 수행할 때 사용할 수 있는 **지침 + 스크립트 + 참고자료가 하나로 묶인 폴더**입니다.
실습 1의 Custom Instructions와 비교하면 다음과 같은 차이가 있습니다.

| | Custom Instructions | Agent Skills |
|---|---|---|
| 구성 | 파일 1개 (`copilot-instructions.md`) | 여러 개의 독립된 폴더 (Skill마다 1개) |
| 로드 방식 | 워크스페이스를 여는 동안 **항상 전체**가 로드됨 | 필요한 Skill의 **이름+설명만 먼저** 로드되고, 관련 있을 때만 전체 내용이 로드됨 |
| 적합한 상황 | 프로젝트 전체에 항상 적용되는 규칙 | 특정 도메인 작업(테스트 작성, API 추가, 배포 등)별로 나눠진 전문 지침 |

### 동작 방식 (3단계)
1. **발견**: Copilot이 시작될 때 각 Skill의 이름과 설명(description)만 가볍게 읽어둡니다. (전체 내용은 아직 안 읽음)
2. **활성화**: 사용자의 요청이 특정 Skill의 설명과 관련 있다고 판단되면, 그 Skill의 `SKILL.md` 전체를 컨텍스트에 불러옵니다.
3. **실행**: 불러온 지침을 따라 작업을 수행합니다. 필요하면 `references/`의 문서를 더 읽거나, `scripts/`의 코드를 직접 실행합니다.

→ 이 방식 덕분에 Skill을 아무리 많이 만들어둬도, 매번 관련 없는 Skill까지 전부 컨텍스트에 넣지 않아
**컨텍스트를 효율적으로 사용**할 수 있습니다.

## 폴더 구조
```
.github/
└── skills/
    ├── add-api-endpoint/
    │   ├── SKILL.md          # 핵심 지침 (실습에서 직접 채울 템플릿)
    │   └── references/
    │       └── checklist.md  # 상세 체크리스트 (필요할 때만 추가로 로드됨)
    └── code-style-check/
        ├── SKILL.md          # 핵심 지침
        └── scripts/
            └── check_style.py # 실제로 실행 가능한 점검 스크립트
```

---

## 실습 순서

### Step 1. 폴더 열기 & 실행 확인
VS Code에서 `02_agent_skills` 폴더를 열어주세요.
```bash
pip3 install -r requirements.txt
uvicorn main:app --reload
```
`http://localhost:8000` 접속해서 정상 동작하는지 확인하세요.

되돌리기 편하도록, 폴더 전체를 `02_agent_skills_backup`으로 복사해두세요
(Finder에서 복사-붙여넣기면 충분합니다. git은 사용하지 않습니다).

### Step 2. Skill 없이 반복 작업 요청해보기
Agent 모드에서 아래처럼 새 엔드포인트 추가를 요청해보세요.
```
todo id로 특정 항목 하나를 조회하는 GET /todos/{id} 엔드포인트를 추가해줘.
존재하지 않는 id가 오면 적절한 에러를 반환해줘.
```
→ 결과를 확인하세요. 존재하지 않는 id를 요청했을 때 몇 번 상태 코드로 응답하나요
   (404? 200+null? 500?)? 기존 파일 역할 분리(main.py/database.py), 응답 형식이
   일관되게 지켜졌나요?

> 💡 왜 "통계 API" 대신 이 프롬프트인가요? 이전엔 개수만 세는 단순 GET
> 요청이라 입력 검증도, id 조회도 필요 없어서 `references/checklist.md`의
> 체크리스트 항목("존재하지 않는 id → 404" 등)이 애초에 적용될 여지가 없었습니다.
> id로 단건 조회하는 이 시나리오는 "없는 id면 어떻게 응답할지"를 모델이
> 자체 판단해야 해서, Skill 유무에 따라 실제로 다르게 처리될 가능성이 큽니다.

확인 후 백업해둔 폴더의 `main.py`, `database.py`로 다시 덮어써서 원상복구하세요.
(정교하게 되돌리는 게 목적이 아니라 "Skill 적용 전/후 비교"가 목적이므로 대략만
복구해도 무방합니다)

### Step 3. `add-api-endpoint` Skill 채우기
1. `.github/skills/add-api-endpoint/SKILL.md` 파일을 엽니다.
2. frontmatter의 `description`을 최대한 구체적으로 채웁니다. **이 설명이 Copilot이 "언제 이 Skill을 써야 할지" 판단하는 유일한 단서**이므로 대충 쓰면 활성화가 잘 안 될 수 있습니다.
3. 본문의 빈칸(**존재하지 않는 리소스 처리**, 파일 역할 분리, 응답 형식, 반드시 지킬 것)을 채웁니다.
   특히 "존재하지 않는 리소스 처리"가 이번 실습에서 가장 중요한 항목입니다 — 나머지는
   기존 코드를 보고 모델이 어느 정도 알아서 따라할 가능성이 있지만, 이건 지금 코드에
   참고할 선례가 없어서 Skill이 있고 없고에 따라 실제로 다르게 처리될 확률이 높습니다.
4. `references/checklist.md` 도 함께 채웁니다.

> 💡 **초안 작성이 막막하다면**: Copilot Chat에게 코드를 분석시켜서 초안을
> 받아보세요.
> ```
> 이 프로젝트에서 새 API 엔드포인트를 추가하는 작업을 처리할 Agent Skill을
> 만들려고 해. main.py, database.py의 기존 패턴(파일 역할 분리, 응답 형식,
> id 조회 실패 시 에러 처리 방식)을 분석해서, .github/skills/add-api-endpoint/
> SKILL.md의 description과 본문 초안을 작성해줘. description에는 "언제 이
> Skill을 써야 하는지"가 명확히 드러나야 해.
> ```
> 생성된 초안을 그대로 쓰지 말고, description이 실제로 활성화 판단 기준으로
> 쓸 만큼 구체적인지 직접 검토하세요.

### Step 4. 같은 요청 다시 해보기
Step 2와 동일한 요청을 다시 보내봅니다.
```
todo id로 특정 항목 하나를 조회하는 GET /todos/{id} 엔드포인트를 추가해줘.
존재하지 않는 id가 오면 적절한 에러를 반환해줘.
```
→ Copilot 응답의 References(참조 파일 목록)에 `SKILL.md`가 떴는지 확인하세요.
→ Step 2 결과와 비교해서 무엇이 달라졌나요?

### Step 5. 결과 비교
| | Skill 없이 | Skill 적용 후 |
|---|---|---|
| 존재하지 않는 id 요청 시 404 반환 | | |
| 파일 역할 분리 유지 | | |
| 응답 형식 일관성 | | |

---

## 심화 실습 (시간이 남는다면) - scripts/ 활용
`.github/skills/code-style-check/` 에는 이미 동작하는 점검 스크립트(`scripts/check_style.py`)가 들어있습니다.
1. `SKILL.md`를 읽고 어떤 상황에서 이 Skill이 활성화되도록 설계되어 있는지 확인합니다.
2. Agent 모드에 아래처럼 요청해봅니다.
   ```
   database.py 코드 스타일 점검해줘
   ```
3. Copilot이 `code-style-check` Skill을 발견하고, `scripts/check_style.py`를 직접 실행해서 결과를 알려주는지 관찰합니다.
4. 터미널에서 직접 실행해서 결과를 비교해볼 수도 있습니다.
   ```bash
   python3 .github/skills/code-style-check/scripts/check_style.py database.py
   ```

→ 이렇게 여러 개의 Skill을 만들어두면, Copilot은 요청 내용에 맞는 Skill "만" 선택적으로 불러와 사용합니다.
   (`add-api-endpoint`를 물어보면 그 Skill만, 코드 점검을 물어보면 `code-style-check`만 로드됨)

## 핵심 포인트
> Custom Instructions는 "프로젝트 전체에 항상 적용되는 규칙 1벌"이라면,
> Agent Skills는 "작업 종류별로 나눠진 여러 개의 전문 지침 모음"입니다.
> Skill이 많아져도 관련 있는 것만 골라 불러오기 때문에 컨텍스트 낭비 없이
> 테스트 작성, 배포, 디버깅처럼 서로 다른 작업에 특화된 Copilot을 만들 수 있습니다.
