# 실습 2 - TODO List 앱 만들기

## 목표
GitHub Copilot **Agent 모드**로 Python 백엔드 + HTML 프론트엔드 구조의
TODO List 웹 앱을 처음부터 만들어봅니다.

---

## 실습 방법

### Step 1. 빈 폴더 열기
VS Code에서 `02_todo_app` 폴더를 열어주세요.

### Step 2. Agent 모드 열기
- `Ctrl+Shift+I` (Mac: `Cmd+Shift+I`) 로 Copilot Chat 열기
- 상단 드롭다운에서 **Agent** 선택

### Step 3. 아래 PRD를 그대로 붙여넣어서 요청하세요

```
아래 PRD를 기반으로 Python 백엔드 + HTML 프론트엔드 구조의
TODO List 웹 앱을 만들어줘.

## 프로젝트 개요
- 이름: todo-app
- 백엔드: Python FastAPI
- 프론트엔드: HTML + CSS + JavaScript (fetch API)
- DB: SQLite (sqlite3 표준 라이브러리 사용)
- 실행: uvicorn main:app --reload

## 핵심 기능
1. 할 일 추가: 입력창에 텍스트 입력 후 추가 버튼 클릭
2. 할 일 목록 조회: 전체 목록을 카드 형태로 표시
3. 완료 처리: 체크박스 클릭으로 완료/미완료 토글
4. 삭제: 삭제 버튼 클릭으로 항목 제거

## API 명세
- GET    /todos          전체 할 일 목록 조회
- POST   /todos          새 할 일 추가 { "title": str }
- PATCH  /todos/{id}     완료 상태 토글
- DELETE /todos/{id}     할 일 삭제

## 기술 요구사항
- DB는 SQLite, 테이블명 todos (id, title, done, created_at)
- 프론트엔드는 static/index.html 단일 파일로 구성
- fetch API로 백엔드와 통신 (페이지 새로고침 없이 동작)
- CORS 설정 포함
- 깔끔하고 직관적인 UI

## 파일 구조
main.py          - FastAPI 앱 및 API 엔드포인트
database.py      - SQLite 연결 및 쿼리 처리
requirements.txt - 필요 패키지
static/
  index.html     - 프론트엔드 (HTML + CSS + JS 단일 파일)
```

### Step 4. Agent 동작 관찰
Agent가 파일을 하나씩 생성하는 과정을 지켜보세요.
- 어떤 순서로 파일을 만드는지
- 백엔드와 프론트엔드를 어떻게 연결하는지
- 오류가 생기면 스스로 수정하는지

### Step 5. 설치 및 실행
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
브라우저에서 `http://localhost:8000` 접속

### Step 6. 동작 확인
- 할 일 추가 → 목록에 바로 뜨는지
- 체크박스 클릭 → 완료 처리되는지
- 삭제 버튼 → 목록에서 사라지는지

---

## 막혔을 때
- 에러 메시지를 그대로 Copilot Chat에 붙여넣기
- "이 에러 고쳐줘" 한 마디면 Agent가 직접 수정함
- CORS 에러 → "CORS 설정 추가해줘"

---

## 관찰 포인트
> Agent 모드의 핵심은 **코드를 받아서 내가 붙여넣는 게 아니라**
> Agent가 직접 파일을 생성하고 수정한다는 점입니다.
> 이것이 "검색처럼 쓰는 AI"와 "코드를 짜는 AI"의 차이입니다.
