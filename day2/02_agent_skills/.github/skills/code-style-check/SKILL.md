---
name: code-style-check
description: 파이썬 코드에서 SQL 인젝션 위험이나 DB 커넥션 미종료 같은 흔한 문제를 스캔할 때 사용한다. "코드 점검해줘", "스타일 체크해줘", "이 파일 검사해줘" 같은 요청에서 사용
---

# 코드 스타일/안전성 점검

이 Skill이 활성화되면, `scripts/check_style.py` 를 실행해서 프로젝트의 `.py` 파일을 스캔합니다.

## 실행 방법
```bash
python .github/skills/code-style-check/scripts/check_style.py <검사할 파일 경로>
```

## 점검 항목
- SQL 쿼리를 f-string/포맷 문자열로 조합하는 패턴 (SQL Injection 위험)
- `sqlite3.connect()` 이후 `conn.close()` 가 없는 경우 (리소스 누수)

## 결과 활용
스크립트가 출력한 경고 목록을 바탕으로, 해당 위치를 안전한 방식(파라미터 바인딩, 커넥션 close)으로 고쳐줍니다.
