# 실습 1 - 버그 찾기 & 수정하기

## 목표
실무에서 자주 발생하는 버그가 심어진 코드를 Copilot으로 찾아서 수정합니다.
**나쁜 프롬프트 vs TCCOV 프롬프트**의 결과 차이를 직접 체감합니다.

---

## 실습 파일
- `buggy_todo.py` : 버그가 숨어있는 TODO 앱 코드

---

## 실습 순서

### Step 1. 나쁜 프롬프트로 먼저 시도
Copilot Chat을 열고 아래처럼 요청해보세요.
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
