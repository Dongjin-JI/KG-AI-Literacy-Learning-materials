# 실습 3 - TODO List 앱 고도화하기

## 목표
실습 2에서 만든 TODO 앱에 원하는 기능을 추가합니다.
백엔드(FastAPI) + 프론트엔드(HTML) 양쪽을 Copilot과 함께 수정하는 경험을 합니다.

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
기능 추가 후 Copilot Chat에 요청해보세요.
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
Copilot이 두 파일을 일관성 있게 수정해줍니다.
