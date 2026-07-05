"""
[Agent Skill: code-style-check]
지정한 파이썬 파일에서 흔한 문제 패턴을 스캔하는 간단한 정적 점검 스크립트.

사용법: python check_style.py <파일 경로>
"""

import re
import sys
from pathlib import Path


SQL_FSTRING_PATTERN = re.compile(r'(f"[^"]*"|f\'[^\']*\')\s*\)?\s*$')
EXECUTE_PATTERN = re.compile(r'\.execute\(')


def check_file(path: Path):
    warnings = []
    lines = path.read_text(encoding="utf-8").splitlines()

    connect_count = 0
    close_count = 0

    for i, line in enumerate(lines, start=1):
        if "connect(" in line:
            connect_count += 1
        if "close()" in line:
            close_count += 1

        if EXECUTE_PATTERN.search(line):
            # 같은 줄 또는 바로 다음 줄에 f-string으로 SQL을 조합하는지 확인
            window = " ".join(lines[max(0, i - 2):i])
            if re.search(r'f"[^"]*(\{[^}]+\})', window) or re.search(r"f'[^']*(\{[^}]+\})", window):
                warnings.append(f"[{i}줄] SQL 쿼리에 f-string 조합 사용 의심 (SQL Injection 위험): {line.strip()}")

    if connect_count > close_count:
        warnings.append(
            f"커넥션 open({connect_count}) 대비 close({close_count})가 적습니다. "
            f"conn.close() 누락 여부를 확인하세요."
        )

    return warnings


def main():
    if len(sys.argv) != 2:
        print("사용법: python check_style.py <파일 경로>")
        sys.exit(1)

    target = Path(sys.argv[1])
    if not target.exists():
        print(f"파일을 찾을 수 없습니다: {target}")
        sys.exit(1)

    warnings = check_file(target)

    if not warnings:
        print(f"[OK] {target} 에서 특별한 문제를 찾지 못했습니다.")
    else:
        print(f"[WARN] {target} 에서 {len(warnings)}건의 의심 항목을 찾았습니다:")
        for w in warnings:
            print(f"  - {w}")


if __name__ == "__main__":
    main()
