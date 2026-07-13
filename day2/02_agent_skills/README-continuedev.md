# 실습 2 - Rules(alwaysApply: false)로 나만의 자동 활성화 지침 만들기 (Continue.dev 버전)

> ⚠️ **이 파일은 백업용입니다.** 이 실습은 원래 GitHub Copilot 기준(`README.md`,
> Agent Skills)으로 진행합니다. Copilot 계정/플랜 문제로 실습을 진행할 수 없는
> 경우에만 이 문서를 사용하세요.

## GitHub Copilot ↔ Continue.dev 대응표

| 개념 | GitHub Copilot | Continue.dev |
|---|---|---|
| 작업별 자동 활성화 지침 (Skill) | **Agent Skills** (`.github/skills/`) | **Rules + `alwaysApply: false`** (`.continue/rules/*.md`) |
| 활성화 근거 | `description` | `description` (+ `globs`가 있으면 파일 매칭도 함께 판단) |
| 활성화 방식 | Copilot이 요청 내용과 description을 비교해 **자동으로** 판단 | agent가 요청 내용과 description을 비교해 **자동으로** 판단 |
| 참고자료·스크립트 번들 | `references/`, `scripts/` 폴더 | 없음 — Rule 본문에 스크립트 경로를 적어 실행을 지시 |

> ✅ **바로잡습니다**: Continue.dev의 "Prompts"(`invokable: true`)는 `/이름`으로
> **수동으로만** 호출되기 때문에, description을 보고 자동으로 발견·활성화되는
> Copilot Agent Skills와는 동작 방식이 다릅니다. Skill의 "자동 활성화" 감각을
> 재현하려면 Prompts가 아니라 **Rules를 `alwaysApply: false`로 설정**하는 것이
> 맞습니다. Continue 공식 문서: *"Included if globs exist AND match file context,
> or the agent decides to pull the rule into context based on its description"*
> (`alwaysApply: false`일 때).

---

## 목표
`.continue/rules/`에 **작업 종류별로 나뉜 여러 개의 Rule**을 `alwaysApply: false`로
만들어서, agent가 요청 내용에 맞는 Rule을 스스로 **발견 → 컨텍스트에 끌어오기 →
실행** 하는 과정을 체감합니다.

## Rules(alwaysApply: false)란?
실습 1에서 만든 `project-context.md`는 `alwaysApply: true`라서 워크스페이스를
여는 동안 **항상** 켜져 있었습니다. 이번에는 `alwaysApply: false`로 설정한 Rule을
만듭니다 — 항상 켜져 있는 대신, **관련 있는 요청일 때만** agent가 스스로 판단해서
불러옵니다.

| | Rules (`alwaysApply: true`) | Rules (`alwaysApply: false`) |
|---|---|---|
| 로드 방식 | 워크스페이스를 여는 동안 **항상 전체**가 로드됨 | 이름/`description`만 먼저 참고되고, 관련 있을 때만 agent가 전체 내용을 컨텍스트에 끌어옴 |
| 적합한 상황 | 프로젝트 전체에 항상 적용되는 규칙 | 특정 도메인 작업(엔드포인트 추가, 코드 점검 등)별로 나눠진 전문 지침 |
| 추가 조건 | 없음 | `globs`를 함께 지정하면 특정 파일이 컨텍스트에 있을 때도 자동 적용됨 |

### 동작 방식 (Copilot Agent Skills와 동일한 3단계)
1. **발견**: agent가 `alwaysApply: false`인 각 Rule의 `name`/`description`을 가볍게 참고해둡니다.
2. **활성화**: 사용자의 요청이 특정 Rule의 description(또는 `globs`로 지정한 파일 패턴)과
   관련 있다고 판단되면, 그 Rule의 본문 전체를 컨텍스트에 불러옵니다.
3. **실행**: 불러온 지침을 따라 작업을 수행합니다. 필요하면 본문에서 안내한 스크립트를 직접 실행합니다.

## 폴더 구조
```
.continue/
└── rules/
    ├── project-context.md      # 실습 1에서 만든 항상 켜진 Rule (alwaysApply: true)
    ├── add-api-endpoint.md     # 작업별 Rule (alwaysApply: false, 실습에서 직접 채울 템플릿)
    └── code-style-check.md     # 작업별 Rule (alwaysApply: false, 바로 사용 가능한 예시)
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

### Step 2. Rule 없이 반복 작업 요청해보기
Continue Chat을 Agent 모드로 열고 아래처럼 새 엔드포인트 추가를 요청해보세요.
```
todo id로 특정 항목 하나를 조회하는 GET /todos/{id} 엔드포인트를 추가해줘.
존재하지 않는 id가 오면 적절한 에러를 반환해줘.
```
→ 결과를 확인하세요. 존재하지 않는 id를 요청했을 때 몇 번 상태 코드로 응답하나요
   (404? 200+null? 500?)? 기존 파일 역할 분리(main.py/database.py), 응답 형식이
   일관되게 지켜졌나요?

> 💡 왜 "통계 API" 대신 이 프롬프트인가요? 이전엔 개수만 세는 단순 GET
> 요청이라 입력 검증도, id 조회도 필요 없어서 체크리스트 항목("존재하지 않는
> id → 404" 등)이 애초에 적용될 여지가 없었습니다. id로 단건 조회하는 이
> 시나리오는 "없는 id면 어떻게 응답할지"를 모델이 자체 판단해야 해서, Rule
> 유무에 따라 실제로 다르게 처리될 가능성이 큽니다.

확인 후 백업해둔 폴더의 `main.py`, `database.py`로 다시 덮어써서 원상복구하세요.
(정교하게 되돌리는 게 목적이 아니라 "Rule 적용 전/후 비교"가 목적이므로 대략만
복구해도 무방합니다)

### Step 3. `add-api-endpoint` Rule 채우기
1. `.continue/rules/add-api-endpoint.md` 파일을 엽니다.
2. frontmatter의 `description`을 최대한 구체적으로 채웁니다. **이 설명이 agent가
   "언제 이 Rule을 자동으로 끌어올지" 판단하는 유일한 단서**이므로 대충 쓰면
   활성화가 잘 안 될 수 있습니다.
3. 본문의 빈칸(파일 역할 분리, 응답 형식, 반드시 지킬 것, 상세 체크리스트)을 채웁니다.
4. `alwaysApply: false`가 그대로 있는지 확인합니다. (실수로 지우면 실습 1처럼 항상 켜지는 Rule이 됩니다)

### Step 4. 같은 요청 다시 해보기
Step 2와 동일한 요청을 다시 보내봅니다.
```
todo id로 특정 항목 하나를 조회하는 GET /todos/{id} 엔드포인트를 추가해줘.
존재하지 않는 id가 오면 적절한 에러를 반환해줘.
```
→ Continue 채팅창 하단 툴바(또는 응답의 References 영역, 버전에 따라 위치가 다를 수 있음)에서
`add-api-endpoint` Rule이 자동으로 참조됐는지 확인하세요. (사용자가 직접 호출하지
않았는데도 컨텍스트에 들어왔다는 점이 핵심입니다)
→ Step 2 결과와 비교해서 무엇이 달라졌나요?

### Step 5. 결과 비교
| | Rule 없이 | Rule 적용 후 |
|---|---|---|
| 존재하지 않는 id 요청 시 404 반환 | | |
| 파일 역할 분리 유지 | | |
| 응답 형식 일관성 | | |

---

## 심화 실습 (시간이 남는다면) - `code-style-check` Rule 활용
`.continue/rules/code-style-check.md`는 `globs: "*.py"`도 함께 지정돼 있어서,
description 판단과 파일 패턴 매칭 **두 가지 방식** 모두로 자동 활성화될 수 있습니다.
실행 대상은 이미 동작하는 점검 스크립트(`.github/skills/code-style-check/scripts/check_style.py`)
입니다. 이 스크립트는 파이썬 표준 라이브러리만 사용해서 Copilot/Continue 어느
쪽에서도 그대로 재사용할 수 있습니다.

1. `.continue/rules/code-style-check.md`를 읽고 어떤 상황에서 자동 활성화되도록 설계되어 있는지 확인합니다.
2. Continue Chat Agent 모드에 아래처럼 요청해봅니다.
   ```
   database.py 코드 스타일 점검해줘
   ```
3. agent가 `code-style-check` Rule을 스스로 끌어와서, `scripts/check_style.py`를 직접 실행해
   결과를 알려주는지 관찰합니다.
4. 터미널에서 직접 실행해서 결과를 비교해볼 수도 있습니다.
   ```bash
   python3 .github/skills/code-style-check/scripts/check_style.py database.py
   ```

→ 이렇게 여러 개의 `alwaysApply: false` Rule을 만들어두면, agent는 요청 내용에
   맞는 Rule "만" 선택적으로 끌어와 사용합니다. (엔드포인트 추가를 물어보면 그
   Rule만, 코드 점검을 물어보면 `code-style-check`만 컨텍스트에 들어옴)

## 핵심 포인트
> `alwaysApply: true` Rule이 "프로젝트 전체에 항상 적용되는 규칙 1벌"이라면,
> `alwaysApply: false` Rule은 "작업 종류별로 나눠진 여러 개의 전문 지침 모음"입니다.
> Rule이 많아져도 관련 있는 것만 골라 불러오기 때문에 컨텍스트 낭비 없이
> 테스트 작성, 배포, 디버깅처럼 서로 다른 작업에 특화된 자동 활성화 지침을
> 만들 수 있습니다 — Copilot Agent Skills와 동일한 사고방식입니다.
