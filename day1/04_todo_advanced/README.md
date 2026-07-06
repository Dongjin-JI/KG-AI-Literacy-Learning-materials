# 실습 3-2 - TODO List 앱 고도화하기

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
실습 3-1에서 만든 TODO 앱에 원하는 기능을 추가합니다.
백엔드(FastAPI) + 프론트엔드(HTML) 양쪽을 Continue.dev와 함께 수정하는 경험을 합니다.

---

## 실습 방법

### Step 1. 추가할 기능 선택
아래에서 하나 이상 골라보세요.

| 기능 | 난이도 | 영향 범위 |
|------|--------|----------|
| 우선순위 설정 (높음/중간/낮음) | ⭐ | DB + API + UI |
| 마감일 추가 및 D-day 표시 | ⭐ | DB + API + UI |
| 카테고리/태그 분류 | ⭐⭐ | DB + API + UI |
| 검색 필터 | ⭐⭐ | API + UI |
| 완료 항목 숨기기/보이기 토글 | ⭐ | UI |
| 할 일 수정 (인라인 편집) | ⭐⭐ | API + UI |
| 통계 (전체/완료/미완료 개수) | ⭐ | API + UI |
| 드래그로 순서 변경 | ⭐⭐⭐ | DB + API + UI |

### Step 2. TCCOV 프롬프트 직접 작성
아래 형식으로 직접 프롬프트를 작성해서 Agent에게 요청하세요.

```
[Task] (추가할 기능을 한 줄로)
[Context] 현재 todo-app 구조:
          - main.py: FastAPI 앱, API 엔드포인트 (GET/POST/PATCH/DELETE /todos)
          - database.py: SQLite 연결, todos 테이블 (id, title, done, created_at)
          - static/index.html: fetch API로 백엔드 통신하는 단일 파일 프론트
[Constraints] (지켜야 할 조건)
[Output Format] (UI에서 어떻게 보여야 하는지)
[Validation] (예외 처리할 케이스)
```

### Step 3. 코드 리뷰 요청
기능 추가 후 Continue Chat에 요청해보세요.
```
현재 database.py 코드를 리뷰해줘.
SQL 쿼리에서 개선할 부분이 있으면 알려줘.
```

### Step 4. 리팩토링
```
main.py에서 라우터를 별도 파일로 분리해줘.
FastAPI 구조에 맞게 router 폴더를 만들어줘.
```

---

## 이 실습의 핵심
기능을 추가할 때 **백엔드(API)와 프론트엔드(UI)를 동시에 수정**해야 합니다.
TCCOV 프롬프트에 현재 구조를 명확히 적어줄수록
Continue.dev가 두 파일을 일관성 있게 수정해줍니다.
