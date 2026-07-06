<!-- TODO: 이 실습 구성은 초안입니다. 실제 진행 전 강사 검토 필요 (미니실습 개수, 난이도 확정 안 됨) -->

# 실습 3 — 컨텍스트 엔지니어링 심화 (awesome-copilot 탐색 → Continue.dev로 번역)

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
GitHub가 공식 운영하는 커뮤니티 저장소 **awesome-copilot**에서 Instructions/Skills
예시를 직접 찾아보고, 그 내용을 **Continue.dev의 Rules/Prompts 문법으로 "번역"**해봅니다.
Copilot 전용 예시라도 문법만 바꾸면 Continue.dev에서 그대로 활용할 수 있다는 것을
체감하는 것이 목표입니다.

- 저장소: https://github.com/github/awesome-copilot

> ⚠️ 이 저장소는 계속 업데이트되는 커뮤니티 저장소라, 폴더 구성(`instructions/`,
> `skills/`, `agents/`, `plugins/`, `hooks/`, `workflows/` 등)이나 파일 목록이
> 실습 시점에 지금과 다를 수 있습니다. 아래 예시가 안 보이면 비슷한 다른 파일로
> 대체해서 진행하세요.

---

## Part 1. Instructions 예시 찾아보고 번역하기

### Step 1. 예시 살펴보기 (미리 골라둔 예시 — 직접 확인함)
<!-- TODO: 원래 요청은 "커밋 메시지 생성 스킬" 예시였으나, 저장소 전체 검색 결과
     "commit"이 포함된 파일이 실제로 존재하지 않아(2026-07 기준 확인) 대신
     이번 실습 주제와 가장 잘 맞는 실제 존재하는 파일로 교체함. 강사 검토 시
     원하시는 다른 예시로 바꿔도 됩니다. -->

`instructions/context-engineering.instructions.md`
(https://github.com/github/awesome-copilot/blob/main/instructions/context-engineering.instructions.md)

실제 파일의 frontmatter는 아래와 같습니다. (2026-07 기준 확인)
```yaml
---
description: 'Guidelines for structuring code and projects to maximize GitHub Copilot effectiveness through better context management'
applyTo: '**'
---
```
본문은 프로젝트 구조/코드 패턴/Copilot과 작업하는 법/컨텍스트 힌트/여러 파일
동시 수정/트러블슈팅 6개 항목으로 구성된 컨텍스트 엔지니어링 가이드입니다.

### Step 2. 본인 언어/프레임워크 예시 직접 찾아보기
1. 저장소의 `instructions/` 폴더로 들어가서, 본인이 쓰는 언어/프레임워크 관련
   파일을 하나 찾아봅니다.
2. 파일을 열어서 frontmatter(`description`, `applyTo`)와 본문 내용을 확인합니다.

### Step 3. Continue Rules 문법으로 번역하기
위 예시(`context-engineering.instructions.md`)를 Continue Rules로 바꾸면 이런 형태가 됩니다.

```yaml
---
name: Context Engineering
globs: "**/*"
alwaysApply: true
description: 프로젝트 구조와 코드를 컨텍스트 관리에 유리하게 구성하기 위한 가이드
---
(본문 내용은 원본을 그대로 옮기거나 우리 프로젝트에 맞게 요약)
```

> 번역 포인트: Copilot의 `applyTo: '**'`(모든 파일에 적용)는 Continue에서
> `globs`로 전체를 지정하는 대신 **`alwaysApply: true`**로 표현하는 것이 더
> 자연스럽습니다. `globs`는 "특정 파일에만" 적용하고 싶을 때 쓰는 조건이기
> 때문입니다.

Step 2에서 본인이 찾은 예시도 같은 방식으로 `.continue/rules/*.md` 형식으로
직접 번역해봅니다.

---

## Part 2. Skills 예시 찾아보고 번역하기

### Step 4. Skills 예시 찾아보기
저장소의 Skill 관련 폴더(`skills/` 등, 위 경고 참고)에서 예시를 하나 찾아
`SKILL.md`의 구조(이름, 설명, 본문 지침)를 확인합니다.

### Step 5. Continue Prompts 문법으로 번역하기
Skill의 이름/설명/지침을 Continue Prompts 형식으로 옮겨봅니다.
```yaml
---
name: (Skill 이름)
description: (Skill 설명 — 언제 이 Prompt를 써야 하는지)
invokable: true
---
(Skill 본문 지침을 우리 프로젝트에 맞게 옮기거나 요약)
```

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
  골라 시연합니다. (2026-07 기준, 실제 파일 확인함)

| Skill | 하는 일 | 인증 필요 여부 |
|---|---|---|
| `korea-weather` | 기상청 단기예보를 조회해 요약 (프록시 경유) | 없음 |
| `hwp` | 한글(HWP/HWPX) 문서를 AI가 읽고 다루도록 변환 (Node.js 18+ 필요) | 없음 |

시연 포인트: "코딩을 몰라도, 이미 만들어진 Skill을 가져다 쓰면 AI가 날씨 확인,
문서 정리 같은 내 업무를 대신 처리해줄 수 있다"는 것을 보여주는 것이 목적입니다.
Part 2에서 살펴본 Skill 구조(이름/설명/본문 지침)가 실제로 이렇게 다양한
곳에 쓰인다는 것도 함께 짚어주면 좋습니다.

---

## 소감 정리
- 다른 도구(Copilot)용으로 만들어진 예시를 그대로 가져다 쓸 때 좋았던 점은?
- 문법을 번역하면서 어색하거나 애매했던 부분은?
- `applyTo`/`globs`, "항상 적용"/`alwaysApply` 처럼 서로 다른 도구의 개념을
  대응시켜보니 어떤 공통점이 보였나요?

## 핵심 포인트
도구마다 문법은 다르지만, "컨텍스트를 어떻게 구조화해서 AI에게 전달할 것인가"라는
사고방식은 동일합니다. 커뮤니티 예시를 찾아 번역하는 능력은 어떤 AI 코딩 툴을
쓰든 재사용할 수 있습니다.
