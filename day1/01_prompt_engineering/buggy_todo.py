"""
[실습] 버그 찾기 & 수정하기

아래 코드에는 실무에서 자주 발생하는 버그가 숨어있습니다.
Continue Chat에 아래 미션을 요청해서 버그를 찾고 수정해보세요.

[미션]
이 코드에서 발생할 수 있는 보안 취약점, 예외 처리 누락,
리소스 관리 문제를 찾아서 수정된 코드로 고쳐줘.

[힌트 - 막혔을 때만 확인]
- 코드를 Continue Chat에 붙여넣을 때 어떤 맥락을 같이 주면 더 정확한 답변이 나올까?
- TCCOV 형식으로 요청해보세요.
"""

import sqlite3


# ================================================
# DB 초기화
# ================================================
def init_db():
    conn = sqlite3.connect("todos.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()


# ================================================
# 할 일 추가
# Bug 1: SQL Injection 취약점
# ================================================
def add_todo(title):
    conn = sqlite3.connect("todos.db")
    cursor = conn.cursor()
    query = f"INSERT INTO todos (title) VALUES ('{title}')"  # 위험
    cursor.execute(query)
    conn.commit()
    conn.close()


# ================================================
# 전체 조회
# Bug 2: 커넥션 미종료 (리소스 누수)
# ================================================
def get_all_todos():
    conn = sqlite3.connect("todos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todos")
    return cursor.fetchall()  # conn.close() 없음


# ================================================
# 완료 처리
# Bug 3: 파라미터 순서 오류 + 예외 처리 누락
# ================================================
def mark_done(todo_id):
    conn = sqlite3.connect("todos.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE todos SET done = ? WHERE id = ?",
        (True, todo_id)  # done=True가 id 자리에 들어감
    )
    conn.commit()
    conn.close()


# ================================================
# 삭제
# Bug 4: 입력값 검증 없음 + 커넥션 미종료
# ================================================
def delete_todo(todo_id):
    conn = sqlite3.connect("todos.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE id = ?", todo_id)  # 튜플 아님
    conn.commit()
    # conn.close() 없음


# ================================================
# 특정 항목 조회
# Bug 5: 결과 없을 때 예외 처리 누락
# ================================================
def get_todo_by_id(todo_id):
    conn = sqlite3.connect("todos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todos WHERE id = ?", (todo_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0]  # None일 때 TypeError 발생


# ================================================
# 실행
# ================================================
if __name__ == "__main__":
    init_db()

    add_todo("Continue.dev 설치")
    add_todo("버그 찾기 실습")

    todos = get_all_todos()
    for todo in todos:
        print(todo)

    mark_done(1)
    delete_todo(2)
