<!-- TODO: 이 실습 구성은 초안입니다. 실제 진행 전 강사 검토 필요 (발표 시간/형식 미확정) -->

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
      참고하거나, 완전히 새로운 걸 만들어도 됩니다)
- [ ] **실행 확인** — 만든 Rule과 Prompt가 실제로 적용/호출되는지 확인합니다.

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
- Rule이 실제로 적용됐는지: Continue 하단 툴바에서 이번 요청에 어떤 Rule이
  참조됐는지 확인
- Prompt가 실제로 호출되는지: `/프롬프트이름`으로 호출해서 결과 확인

---

## 발표 준비 (초안)
<!-- TODO: 발표 시간/형식 강사 확정 필요 -->
- 어떤 프로젝트를 골랐고, 어떤 Rule/Prompt를 만들었는지 한 줄씩 소개
- 실제 동작 화면 시연 (Rule 적용 전/후 비교, Prompt 호출 장면)
- 이틀간 배운 것 중 실무에 가장 먼저 적용해보고 싶은 것 한 가지

## 핵심 포인트
오늘 배운 것은 "새로운 지식"이 아니라 "반복 가능한 패턴"입니다. 실습 1·2에서
연습한 절차를 내 프로젝트에 그대로 다시 적용해보는 것만으로 충분합니다.
