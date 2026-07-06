<!-- TODO: 이 실습 구성은 초안입니다. 실제 진행 전 강사 검토 필요 (미니실습 개수, 난이도 확정 안 됨) -->

# 실습 2 — Prompts로 반복 작업 자동화하기

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
자주 반복하는 작업(예: 단위 테스트 작성)을 Continue의 **Prompts**
(`.continue/prompts/*.md`, `invokable: true`)로 만들어두고,
채팅에서 `/이름`으로 즉시 불러 쓰는 방법을 익힙니다.

## Prompts란?
실습 1의 Rules가 **"항상 켜져 있는 배경 규칙"**이라면,
Prompts는 **"필요할 때 한 번씩 실행하는 재사용 가능한 명령(매크로)"**입니다.

| | Rules | Prompts |
|---|---|---|
| 적용 시점 | 워크스페이스를 여는 동안 항상 자동 적용 | `/이름`으로 호출했을 때만 실행 |
| 목적 | 프로젝트 전체 규칙/컨벤션 | 자주 반복하는 특정 작업(테스트 생성, 리뷰 등) |
| 재사용 방식 | 매번 자동 포함 | 실행할 때마다 재사용, 대상 코드만 바꿔가며 사용 |

---

## 이어서 진행하기
이 실습은 실습 1(`01_rules_custom_instruction`)에서 Rules를 적용한 이후 상태를
이어받아 진행하는 것을 전제로 합니다.
- **이어서 진행한다면**: 실습 1에서 작업하던 폴더를 그대로 계속 사용하세요.
- **새로 시작한다면**: 이 폴더에 있는 기본 앱(우선순위 필드 없는 초기 상태)을 사용해도 됩니다.

## 실습 파일
- `main.py`, `database.py` : FastAPI + SQLite 백엔드
- `static/index.html` : 프론트엔드
- `.continue/prompts/unit-test-writer.md` : 단위 테스트 생성용 Prompt (바로 사용 가능한 예시)

---

## Step 1. 폴더 열기 & 실행 확인
VS Code에서 `02_prompts_skills` 폴더를 열어주세요. (또는 실습 1을 이어서 진행 중인 폴더)
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
`http://localhost:8000` 접속해서 정상 동작하는지 확인하세요.

실습 중 되돌리기 편하도록, 폴더 전체를 백업 복사해두세요 (git은 사용하지 않습니다).

## Step 2. Prompt 없이 반복 요청해보기
Continue Chat을 Agent 모드로 열고 아래처럼 직접 요청해보세요.
> database.py 의 함수들에 대한 단위 테스트를 작성해줘. 빈 입력, 잘못된 타입, 경계값,
> 예외 상황 같은 엣지 케이스도 반드시 포함해줘.

→ 매번 "엣지 케이스도 포함해줘" 같은 조건을 다시 타이핑해야 한다는 점을 확인하세요.

## Step 3. `/unit-test-writer` 로 호출해보기
1. Continue Chat 입력창에 `/`를 입력하면 사용 가능한 Prompt 목록이 나타납니다.
2. `unit-test-writer`를 선택하거나 `/unit-test-writer`라고 직접 입력합니다.
3. 테스트를 만들고 싶은 코드(예: `database.py`)를 이어서 붙여넣거나 참조시킵니다.
4. 결과를 확인합니다.

→ Step 2와 비교했을 때, 엣지 케이스 조건을 매번 다시 타이핑하지 않고도 같은 품질의
요청을 반복할 수 있었는지 확인하세요.

## Step 4. 결과 비교
| | Prompt 없이 | Prompt 사용 |
|---|---|---|
| 엣지 케이스 포함 여부 | | |
| 요청 형식의 일관성 | | |
| 반복 요청 시 타이핑 양 | | |

---

## 심화 실습 (시간이 남는다면, 초안)
<!-- TODO: 강사 검토 필요 - 학생이 직접 두 번째 Prompt를 만들어보는 실습을 추가할지 결정 -->
`unit-test-writer` 외에 스스로 자주 쓸 것 같은 Prompt를 하나 더 만들어보세요.
(예: 커밋 메시지 생성, 코드 리뷰 체크리스트, API 문서 생성 등)

---

## 핵심 포인트
Rules는 "이 프로젝트에서 항상 지킬 규칙", Prompts는 "가끔 하지만 매번 형식이 같은
작업을 저장해둔 명령"입니다. 팀에서 자주 반복하는 요청이 있다면 Prompt로 만들어두면
팀 전체가 같은 품질의 요청을 반복할 수 있습니다.
