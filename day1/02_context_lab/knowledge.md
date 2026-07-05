# 나의 개발 지식 베이스

============================================================

이 파일을 채울수록 챗봇이 나의 업무에 맞는 답변을 줍니다.
아래 항목을 본인 기준으로 직접 작성해보세요.

[목적/사용 시점]
이 파일은 오늘(Day1) 챗봇 실습에서만 쓰고 끝나는 파일이 아닙니다.
여기에 정리한 내용은 Day2 "Custom Instructions" 실습에서
.github/copilot-instructions.md 로 그대로 옮겨질 원본 재료입니다.
오늘 최대한 구체적으로 작성해둘수록 Day2 실습이 수월해집니다.

[보안 안내]
실제 사내 시스템명, DB 스키마명, API 엔드포인트 경로 등
민감한 정보는 그대로 적지 말고, 패턴만 일반화해서 작성하세요.
(예: "결제시스템-PG연동-v3" (X) → "외부 결제 연동 시스템" (O))

============================================================

## 나의 개발 환경 (필수)
- 주력 언어:         # 예: Java 17 (또는 Python 3.11, TypeScript 등)
- 프레임워크:        # 예: Spring Boot 3.x (또는 FastAPI, Django, Express 등)
- DB:               # 예: MySQL 8.0, Redis (또는 PostgreSQL, MongoDB 등)
- 빌드 도구:         # 예: Gradle (또는 pip/poetry, npm/yarn 등)
- IDE:              # 예: IntelliJ IDEA (또는 VS Code, PyCharm 등)

## 현재 프로젝트 (선택)
- 프로젝트 설명:     # 예: 사내 인사 관리 시스템 백엔드 개발 (또는 개인 사이드 프로젝트, 오픈소스 기여 등)
- 팀 규모:          # 예: 백엔드 3명, 프론트 2명 (또는 1인 개발 등)
- 주요 도메인:      # 예: 결제, 회원, 정산 (또는 커머스, 콘텐츠, 데이터 파이프라인 등)

## 코딩 컨벤션 (필수)
- 네이밍 규칙:      # 예: camelCase, 클래스는 PascalCase (또는 snake_case, kebab-case 등)
- 패키지 구조:      # 예: controller / service / repository / entity / dto (또는 routes / services / models 등)
- 예외 처리:        # 예: CustomException 클래스 사용, GlobalExceptionHandler로 처리 (또는 try/except + 커스텀 에러 클래스 등)
- 주석 스타일:      # 예: Javadoc 형식, 복잡한 비즈니스 로직에만 주석 (또는 docstring, JSDoc 등)

## 자주 쓰는 패턴 (필수)
예시:
- Service 레이어에서 트랜잭션 처리 (또는 Python: 데코레이터로 트랜잭션 처리)
- DTO ↔ Entity 변환은 MapStruct 사용 (또는 TypeScript: DTO 타입은 zod로 검증)
- API 응답은 CommonResponse<T> 래퍼 클래스로 통일 (또는 공통 응답 스키마 객체로 통일)

## AI에게 원하는 답변 방식 (필수)
예시:
- 코드는 항상 전체 클래스 단위로 보여줘 (또는 전체 함수/모듈 단위로 보여줘)
- 의존성 주입은 생성자 주입 방식으로 해줘
- 테스트 코드도 같이 작성해줘 (JUnit5, Mockito 등 / 또는 pytest, Jest 등)

## 자주 겪는 문제 유형 (선택)
예시:
- JPA N+1 문제 (또는 다른 ORM에서의 유사 이슈: SQLAlchemy, TypeORM 등)
- 트랜잭션 롤백 이슈
- 복잡한 동적 쿼리 (QueryDSL) (또는 복잡한 쿼리 빌더 사용 이슈)

============================================================

[다음 단계 연결]
이 내용을 Day2 Custom Instructions 실습에서
.github/copilot-instructions.md 에 그대로 옮겨,
Copilot이 이 규칙들을 실제로 지키는지 확인합니다.

============================================================
