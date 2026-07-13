# 실습 3 - 컨텍스트 엔지니어링 심화 (awesome-copilot 탐색 → Continue.dev로 번역) (Continue.dev 버전)

> ⚠️ **이 파일은 백업용입니다.** 이 실습은 원래 GitHub Copilot 기준(`README.md`)으로
> 진행합니다. Copilot 계정/플랜 문제로 실습을 진행할 수 없는 경우에만 이 문서를
> 사용하세요.

## GitHub Copilot ↔ Continue.dev 대응표

| 개념 | GitHub Copilot | Continue.dev |
|---|---|---|
| 상시 지침 (Custom Instructions) | Custom Instructions | **Rules** (`alwaysApply: true`) |
| 프로젝트 공유 지침 파일 위치 | `.github/copilot-instructions.md` | `.continue/rules/*.md` |
| 작업별 자동 활성화 지침 (Skill) | **Agent Skills** (`.github/skills/`) | **Rules** (`alwaysApply: false`) |
| 활성화 방식 | description 기반 **자동** 발견·활성화 | description(+`globs`) 기반 **자동** 발견·활성화 |
| Chat / Agent 모드 | Copilot Chat / Agent mode | Continue Chat / Agent mode |

> awesome-copilot 저장소의 예시는 전부 GitHub Copilot 문법(frontmatter, 폴더 구조)으로
> 작성돼 있습니다. 오늘은 이 예시를 그대로 베끼는 게 아니라, **Continue.dev의
> Rules 문법(`alwaysApply: true/false`)으로 "번역"**하는 연습을 합니다. 도구가
> 달라도 컨텍스트를 구조화하는 사고방식은 똑같다는 걸 체감하는 것이 목표입니다.

- 저장소: https://github.com/github/awesome-copilot

> ⚠️ 이 저장소는 계속 업데이트되는 커뮤니티 저장소라, 폴더 구성(`instructions/`,
> `skills/`, `agents/`, `plugins/`, `hooks/`, `workflows/` 등)이나 파일 목록이
> 실습 시점에 지금과 다를 수 있습니다. 아래 예시가 안 보이면 비슷한 다른 파일로
> 대체해서 진행하세요.

## 실습 시간
약 60분

---

## Part 1. Instructions 예시 찾아보고 Rules로 번역하기

### Step 1. instructions 예시 둘러보기
1. 브라우저에서 [awesome-copilot 저장소](https://github.com/github/awesome-copilot)에 접속합니다.
2. `instructions/` 폴더로 들어가서, 다양한 예시 파일 목록을 살펴봅니다.
3. 내가 실제로 쓰는 언어/프레임워크와 관련된 파일을 1개 찾아서 열어봅니다.
   (예: `python`, `fastapi`, `security` 등 키워드로 찾아보세요. 미리 확인해둔
   예시로 `instructions/context-engineering.instructions.md`도 참고할 만합니다.)
4. 파일 내용을 읽으며 오늘 실습 1(`01_custom_instructions`)에서 만든 형식과 비교해봅니다.
   - frontmatter(`description`, `applyTo` 등)가 있는가?
   - 어떤 규칙/컨벤션을 지시하고 있는가?

### Step 2. Continue Rules 문법으로 번역하기
Copilot Instructions 파일은 보통 아래와 같은 형태입니다.
```yaml
---
description: 'Guidelines for structuring code and projects to maximize GitHub Copilot effectiveness through better context management'
applyTo: '**'
---
(본문 지침)
```

이걸 Continue Rules로 바꾸면 이런 형태가 됩니다.
```yaml
---
name: Context Engineering
alwaysApply: true
description: 프로젝트 구조와 코드를 컨텍스트 관리에 유리하게 구성하기 위한 가이드
---
(본문 내용은 원본을 그대로 옮기거나 우리 프로젝트에 맞게 요약)
```

> 번역 포인트: Copilot의 `applyTo: '**'`(모든 파일에 적용)는 Continue에서
> **`alwaysApply: true`**로 표현하는 것이 자연스럽습니다. 특정 파일에만
> 적용하고 싶을 때는 `globs`를 대신 씁니다.

### Step 3. 이 프로젝트에 적용해보기
1. 이 폴더(`03_awesome_copilot`)를 VS Code로 엽니다.
   ```bash
   pip3 install -r requirements.txt
   uvicorn main:app --reload
   ```
2. Step 2에서 번역한 내용을 `.continue/rules/` 아래 새 파일로 저장합니다.
3. 우리 프로젝트(FastAPI + SQLite + HTML)와 맞지 않는 부분은 직접 수정합니다.
4. Continue Chat Agent 모드에서 관련 기능을 하나 요청해보고, 이번 요청에 방금
   추가한 Rule이 적용됐는지 확인합니다.

---

## Part 2. Skill 예시 찾아보고 Rules(alwaysApply: false)로 번역하기

### Step 4. Skill 예시 둘러보기
1. 같은 저장소에서 Skill 관련 폴더(`skills/` 등, 위 경고 참고)로 들어가서, 다양한
   예시 Skill들을 살펴봅니다.
2. 우리 프로젝트에 적용할 만한 Skill을 1개 찾습니다. (예: 테스트 코드 작성, 코드 리뷰, API 문서화 등)
3. 해당 Skill의 `SKILL.md`를 열어서 실습 2(`02_agent_skills`)에서 만든 것과 구조를 비교합니다.
   - `description`이 어떻게 쓰여 있는가? (Copilot에서는 이 문구로 자동 활성화 여부를 판단합니다)
   - `references/`, `scripts/`, `assets/` 중 어떤 걸 포함하고 있는가?

### Step 5. Continue Rules(alwaysApply: false) 문법으로 번역하기
Skill의 이름/설명/지침을 Continue Rules 형식으로 옮겨봅니다.
```yaml
---
name: (Skill 이름)
alwaysApply: false
description: (Skill 설명 — 언제 이 Rule을 자동으로 끌어와야 하는지)
---
(Skill 본문 지침을 우리 프로젝트에 맞게 옮기거나 요약)
```

> 번역 포인트: Copilot Agent Skills와 Continue의 `alwaysApply: false` Rule은
> **둘 다 description을 보고 agent가 자동으로 판단해서 활성화**합니다 — 이 부분은
> 번역이라기보다 거의 그대로 대응됩니다. 다만 특정 파일 종류에서만 적용하고
> 싶다면 `globs`를 추가로 지정할 수 있습니다(예: `globs: "*.py"`). `scripts/`에
> 있던 실행 스크립트는 파이썬 표준 스크립트라면 Continue 쪽에서도 경로만 맞춰
> 그대로 재사용할 수 있습니다 (Rule 본문에 실행 방법을 적어두면 됩니다).

### Step 6. 이 프로젝트에 적용해보기
1. 번역한 Rule을 이 프로젝트의 `.continue/rules/` 아래에 새 파일로 저장합니다.
2. 우리 프로젝트에 안 맞는 내용(다른 언어/프레임워크 기준으로 쓰여 있는 부분 등)은 직접 수정합니다.
3. Continue Chat Agent 모드에서 관련 요청을 보내보고, 사용자가 직접 호출하지
   않았는데도 이 Rule이 자동으로 컨텍스트에 들어왔는지 확인합니다.

---

## Part 3. (시연) 비개발자를 위한 k-skill 소개
> 🎬 **시연 전용** — 강사가 시연하고, 참가자는 직접 실습하지 않습니다.
> (원한다면 자유 실습 시간에 개인적으로 따라 해봐도 됩니다.)

지금까지는 코드/API 중심의 Skill 예시를 다뤘습니다. Skill 개념은 코딩과 직접
관련 없는 업무에도 그대로 쓰일 수 있다는 것을 보여주기 위해, 한국어 특화
Skill 모음집인 **k-skill**을 시연합니다.

- 저장소: https://github.com/NomaDamas/k-skill
- 이 저장소는 "한국인이라면 유용한" 150개 이상의 Skill을 모아둔 곳으로,
  기차/버스 예매부터 날씨, 문서 처리, 스포츠 결과 조회까지 다양한 실생활
  작업을 다룹니다. 그중 별도 로그인/API 키가 필요 없는 Skill 2개를
  골라 시연합니다. (실제 파일 확인함)

| Skill | 하는 일 | 인증 필요 여부 |
|---|---|---|
| `kakao-map` | 장소 검색, 주소↔좌표 변환, 자동차 길찾기(거리/시간/통행료) | 없음 |
| `naver-shopping-search` | 네이버 쇼핑 최저가 비교, 판매처/리뷰 정보 조회 | 없음 |

k-skill의 Skill 폴더는 GitHub Copilot의 Agent Skills(`.github/skills/`)와 동일한
형식(SKILL.md 구조)입니다. 이 시연은 **Copilot으로 진행**합니다 — Continue.dev로
그대로 옮기려면 Part 2에서 연습한 것과 같은 방식(Rules `alwaysApply: false`
문법으로 번역)이 필요하다는 점만 짚어주면 충분합니다.

시연 포인트: "코딩을 몰라도, 이미 만들어진 Skill을 가져다 쓰면 AI가 길찾기,
쇼핑 가격 비교 같은 내 업무를 대신 처리해줄 수 있다"는 것을 보여주는 것이 목적입니다.

---

## 소감 정리
아래 질문에 스스로 답해보며 정리합니다.
- 다른 도구(Copilot)용으로 만들어진 예시를 Continue.dev로 번역하면서 좋았던 점은?
- 문법을 번역하면서 어색하거나 애매했던 부분은? (`applyTo`/`globs`, `alwaysApply` 값 결정 등)
- 처음부터 직접 쓰는 것과 비교했을 때, 어떤 상황에서 커뮤니티 예시를 찾아 번역해 쓰는 게 더 효율적일까요?

---

## 오늘까지 배운 내용 정리
| 단계 | 이름 | 적용 시점 |
|---|---|---|
| 1 | TCCOV 프롬프트 | 이번 대화 1번만 |
| 2 | Rules (`alwaysApply: true`) | 프로젝트를 여는 동안 항상 |
| 3 | Rules (`alwaysApply: false`) | 관련된 작업일 때만 agent가 자동으로 선택 |
| 4 | awesome-copilot 번역 활용 | 처음부터 만들지 않고 검증된 예시를 가져와 문법만 바꿔 커스터마이징 |

## 핵심 포인트
> 도구마다 문법은 다르지만, "컨텍스트를 어떻게 구조화해서 AI에게 전달할 것인가"라는
> 사고방식은 동일합니다. 커뮤니티 예시를 찾아 번역하는 능력은 어떤 AI 코딩 툴을
> 쓰든 재사용할 수 있습니다.
