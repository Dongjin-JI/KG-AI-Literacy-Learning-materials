# 실습 1 - 버그 찾기 & 수정하기

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
실무에서 자주 발생하는 버그가 심어진 코드를 Continue.dev로 찾아서 수정합니다.
**나쁜 프롬프트 vs TCCOV 프롬프트**의 결과 차이를 직접 체감합니다.

---

## 실습 파일
- `buggy_todo.py` : 버그가 숨어있는 TODO 앱 코드

---

## 실습 순서

### Step 1. 나쁜 프롬프트로 먼저 시도
Continue 사이드바에서 Chat을 열고(단축키 `Ctrl/Cmd+L`, 버전에 따라 다를 수 있음) 아래처럼 요청해보세요.
```
이 코드 문제 찾아줘
```
→ 어떤 답변이 나오는지 확인하세요.

### Step 2. TCCOV 프롬프트로 다시 시도
아래 형식으로 코드를 붙여넣어서 요청해보세요.
```
[Task] 아래 Python 코드에서 버그를 찾아서 수정된 코드로 고쳐줘
[Context] SQLite 기반 TODO 앱 백엔드 코드야.
          add/get/update/delete 기능이 있고,
          실제 서비스에 배포할 예정이야.
[Constraints] 보안 취약점, 예외 처리 누락, 리소스 관리 문제를 모두 찾아줘.
              수정 시 기존 함수 시그니처는 유지해줘.
[Output Format] 버그 목록을 먼저 나열하고,
                수정된 전체 코드를 제공해줘.
[Validation] SQL Injection, None 반환, 커넥션 미종료 케이스도 확인해줘.

(코드 붙여넣기)
```
→ Step 1 결과와 비교해보세요.

### Step 3. 결과 비교
| | 나쁜 프롬프트 | TCCOV 프롬프트 |
|---|---|---|
| 버그 탐지 개수 | ? | ? |
| 수정 코드 품질 | ? | ? |
| 보안 이슈 언급 | ? | ? |

---

## 숨어있는 버그 (실습 후 확인)
<details>
<summary>정답 보기 (실습 먼저 해보세요!)</summary>

1. **SQL Injection** - `add_todo()`: f-string으로 쿼리 직접 조합
2. **리소스 누수** - `get_all_todos()`: `conn.close()` 누락
3. **파라미터 순서 오류** - `mark_done()`: done=True가 id 자리에 들어감
4. **튜플 누락** - `delete_todo()`: 파라미터가 튜플이 아님 + `conn.close()` 누락
5. **None 예외 처리 누락** - `get_todo_by_id()`: 결과 없을 때 `result[0]`에서 TypeError

</details>
