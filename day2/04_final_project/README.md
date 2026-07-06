# 실습 4 — Rules + Prompts를 내 프로젝트에 적용하기 (자유 실습)

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
Day1에서 만든 나만의 TODO 앱(또는 관심 있는 다른 프로젝트)에, 오늘 배운 Rules와
Prompts를 적용해서 최종 결과물을 완성합니다.

> **완전히 새로운 것을 만드는 게 아니라, 실습 1·2에서 이미 해본 패턴을
> 내 프로젝트에 다시 적용하는 것**이 목표입니다. 어려운 실습이 아니라
> "복습하면서 내 것으로 만드는" 실습이라고 생각하세요.

---

## 체크리스트
아래 4가지를 완료하면 이번 실습은 끝입니다. 순서는 자유롭게 진행해도 됩니다.

- [ ] **워크스페이스 Rule 1개 이상** — 실습 1에서 한 것처럼, 내 프로젝트의
      `.continue/rules/`에 프로젝트 전용 규칙 파일을 만듭니다. (프로젝트 개요,
      파일 구조, API 규칙, 지킬 것/하지 말 것 등 — `project-context.md` 템플릿을
      참고해도 됩니다)
- [ ] **전역(Global) Rule 1개 이상** — `~/.continue/rules/`에 내 계정 전체에
      적용할 규칙을 만듭니다. (예: "항상 한국어로 답변해줘", "설명은 간결하게")
- [ ] **invokable Prompt 1개 이상** — 실습 2에서 한 것처럼, 내가 자주 쓸 것 같은
      작업을 `.continue/prompts/`에 Prompt로 만듭니다. (`unit-test-writer.md`를
      참고하거나, 완전히 새로운 걸 만들어도 됩니다. 뭘 만들지 모르겠다면 아래
      "Rule/Prompt 아이디어를 못 정하겠다면" 참고)
- [ ] **실행 확인** — 만든 Rule과 Prompt가 실제로 적용/호출되는지 확인합니다.

---

## Rule/Prompt 아이디어를 못 정하겠다면
각자 만든(또는 만들고 있는) 프로젝트가 전부 다르기 때문에, "이런 Rule/Prompt를
만드세요"라고 미리 정해줄 수 없습니다. 대신 **AI에게 내 프로젝트를 분석시켜서
아이디어를 제안받는 방법**을 씁니다. — 이건 오늘 배운 것과 별개로 실무에서도
그대로 쓸 수 있는 방법입니다.

1. Continue Chat을 **Chat 모드**로 열고, 내 프로젝트 폴더를 연 상태에서 이렇게 물어보세요.
   ```
   이 프로젝트 코드를 보고, 앞으로 작업하면서 반복될 것 같은 요청 3가지를
   추천해줘. 그리고 그중 프로젝트 전체에 항상 적용되면 좋을 규칙(Rule 후보)과,
   가끔 필요할 때만 불러 쓰면 좋을 명령(Prompt 후보)을 구분해서 제안해줘.
   ```
2. 제안받은 것 중 실제로 본인 프로젝트에 맞는 것을 하나씩 골라서 다듬습니다.
   (프로젝트 성격에 따라 완전히 다를 수 있습니다 — 예: 웹 앱이면 "API 응답
   형식 통일", 데이터 분석 코드면 "차트 스타일 통일", 자동화 스크립트면
   "로그 포맷 통일" 등)
3. 고른 아이디어를 실습 1의 `project-context.md`, 실습 2의 `unit-test-writer.md`와
   같은 구조(Rule은 name/alwaysApply 또는 globs, Prompt는 name/description/invokable)로
   옮겨 적으면 됩니다.

---

## 진행 방법

### Step 1. 대상 프로젝트 정하기
- Day1에서 만든 TODO 앱을 이어서 쓰거나
- 관심 있는 다른 프로젝트(사이드 프로젝트 등)를 새로 골라도 됩니다.

### Step 2. 체크리스트 항목을 하나씩 완료하기
실습 1(`01_rules_custom_instruction`)과 실습 2(`02_prompts_skills`)에서 했던
절차를 **그대로 다시 따라 하면 됩니다.** 막히면 그 폴더의 README를 다시
참고하세요.

### Step 3. 실행 확인하기
- Rule이 실제로 적용됐는지: Continue 채팅창 하단 툴바(또는 응답의 References 영역,
  버전에 따라 위치가 다를 수 있음)에서 이번 요청에 어떤 Rule이 참조됐는지 확인
- Prompt가 실제로 호출되는지: `/프롬프트이름`으로 호출해서 결과 확인

---

## 제출 및 발표

### 전원: 양식 작성 및 제출
참가자 전원은 정리 양식(워드 파일)을 작성해서 제출합니다.
프로젝트 개요 → 워크스페이스 Rule → 전역 Rule → invokable Prompt → 실행 확인
결과 → 소감/다음 단계 → 발표 메모 순으로, 위 체크리스트와 동일한 구조입니다.
양식을 채우다 보면 자연스럽게 내용이 정리됩니다.

### 발표자 선정 및 발표
- 참가자 투표로 1~2명을 발표자로 선정합니다.
- 발표 시간은 1인당 2~3분입니다.
- 발표 내용:
  - 어떤 프로젝트를 골랐고, 어떤 Rule/Prompt를 만들었는지 한 줄씩 소개
  - 실제 동작 화면 시연 (Rule 적용 전/후 비교, Prompt 호출 장면)
  - 이틀간 배운 것 중 실무에 가장 먼저 적용해보고 싶은 것 한 가지

## 핵심 포인트
오늘 배운 것은 "새로운 지식"이 아니라 "반복 가능한 패턴"입니다. 실습 1·2에서
연습한 절차를 내 프로젝트에 그대로 다시 적용해보는 것만으로 충분합니다.
