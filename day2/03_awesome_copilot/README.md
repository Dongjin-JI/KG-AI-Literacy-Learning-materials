# 실습 3 - 컨텍스트 엔지니어링 실습 (awesome-copilot)

## 목표
지금까지는 Custom Instructions와 Agent Skills를 처음부터 직접 만들었습니다.
실무에서는 이미 다른 사람들이 만들어서 공개한 검증된 예시를 **찾아서, 내 프로젝트에 맞게 가져다 쓰는 것**도
중요한 능력입니다. GitHub가 공식 운영하는 커뮤니티 저장소 **awesome-copilot**에서
Instructions 예시와 Skill 예시를 각각 살펴보고, 내 프로젝트에 적용해봅니다.

- 저장소: https://github.com/github/awesome-copilot

## 실습 시간
약 60분

---

## Part 1. Instructions 예시 살펴보고 활용하기

### Step 1. instructions 예시 둘러보기
1. 브라우저에서 [awesome-copilot 저장소](https://github.com/github/awesome-copilot)에 접속합니다.
2. `instructions/` 폴더로 들어가서, 다양한 예시 파일 목록을 살펴봅니다.
3. 내가 실제로 쓰는 언어/프레임워크와 관련된 파일을 1개 찾아서 열어봅니다. (예: `python`, `fastapi`, `security` 등 키워드로 찾아보세요.)
4. 파일 내용을 읽으며 오늘 실습 1(`01_custom_instructions`)에서 만든 형식과 비교해봅니다.
   - frontmatter(`description`, `applyTo` 등)가 있는가?
   - 어떤 규칙/컨벤션을 지시하고 있는가?

### Step 2. 이 프로젝트에 적용해보기
1. 이 폴더(`03_awesome_copilot`)를 VS Code로 엽니다.
   ```bash
   pip3 install -r requirements.txt
   uvicorn main:app --reload
   ```
2. Step 1에서 고른 내용을 복사해서 `.github/copilot-instructions.md` (또는 특정 파일에만 적용하고 싶다면 `.github/instructions/` 아래 새 파일)로 저장합니다.
3. 우리 프로젝트(FastAPI + SQLite + HTML)와 맞지 않는 부분은 직접 수정합니다.
4. Agent 모드에서 관련 기능을 하나 요청해보고, 응답의 References에 방금 추가한 파일이 참조되는지 확인합니다.

---

## Part 2. Skill 예시 살펴보고 적용하기

### Step 3. Skill 예시 둘러보기
1. 같은 저장소에서 Skill 관련 폴더로 들어가서, 다양한 예시 Skill들을 살펴봅니다.
2. 우리 프로젝트에 적용할 만한 Skill을 1개 찾습니다. (예: 테스트 코드 작성, 코드 리뷰, API 문서화 등)
3. 해당 Skill의 `SKILL.md`를 열어서 실습 2(`02_agent_skills`)에서 만든 것과 구조를 비교합니다.
   - `description`이 어떻게 쓰여 있는가? (이 문구로 Copilot이 활성화 여부를 판단합니다)
   - `references/`, `scripts/`, `assets/` 중 어떤 걸 포함하고 있는가?

### Step 4. 이 프로젝트에 적용해보기
1. 고른 Skill 폴더를 통째로 다운로드해서, 이 프로젝트의 `.github/skills/` 아래에 그대로 복사합니다.
2. 우리 프로젝트에 안 맞는 내용(다른 언어/프레임워크 기준으로 쓰여 있는 부분 등)은 직접 수정합니다.
3. Agent 모드에서 그 Skill의 주제와 관련된 요청을 해보고, 실제로 해당 Skill이 발견→활성화되어 동작하는지 확인합니다.

---

## Part 3. (시연) 비개발자를 위한 k-skill 소개
> 🎬 **시연 전용** — 강사가 시연하고, 참가자는 직접 실습하지 않습니다.
> (원한다면 자유 실습 시간에 개인적으로 따라 해봐도 됩니다.)

지금까지는 코드/API 중심의 Skill 예시를 다뤘습니다. Skill 개념은 코딩과 직접
관련 없는 업무에도 그대로 쓰일 수 있다는 것을 보여주기 위해, 한국어 특화
Skill 모음집인 **k-skill**을 시연합니다.

- 저장소: https://github.com/NomaDamas/k-skill
- 이 저장소는 "한국인이라면 유용한" 150개 이상의 Skill을 모아둔 곳으로,
  기차/버스 예매부터 날씨, 문서 처리, 스포츠 결과 조회까지 다양한 실생활
  작업을 다룹니다. 그중 별도 로그인/API 키가 필요 없는 Skill 2개를
  골라 시연합니다. (실제 파일 확인함)

| Skill | 하는 일 | 인증 필요 여부 |
|---|---|---|
| `kakao-map` | 장소 검색, 주소↔좌표 변환, 자동차 길찾기(거리/시간/통행료) | 없음 |
| `naver-shopping-search` | 네이버 쇼핑 최저가 비교, 판매처/리뷰 정보 조회 | 없음 |

두 스킬 모두 그 자리에서 즉흥적으로 질문해도 되는(참가자의 개인 데이터가 필요
없는) 것들이라 라이브 시연에 적합합니다. (예: "OO역에서 OO역까지 차로 가는
길 찾아줘", "이 노트북 모델 최저가 얼마야?") k-skill의 Skill 폴더는 GitHub
Copilot의 Agent Skills(`.github/skills/`)와 동일한 형식(SKILL.md 구조)이라
번역 없이 그대로 다운로드해서 사용할 수 있습니다.

시연 포인트: "코딩을 몰라도, 이미 만들어진 Skill을 가져다 쓰면 AI가 길찾기,
쇼핑 가격 비교 같은 내 업무를 대신 처리해줄 수 있다"는 것을 보여주는 것이 목적입니다.
Part 2에서 살펴본 Skill 구조(이름/설명/본문 지침)가 실제로 이렇게 다양한
곳에 쓰인다는 것도 함께 짚어주면 좋습니다.

---

## 소감 정리
아래 질문에 스스로 답해보며 정리합니다.
- 커뮤니티 예시를 그대로 썼을 때 좋았던 점은 무엇인가요?
- 내 프로젝트에 맞지 않아서 수정해야 했던 부분은 무엇인가요?
- 처음부터 직접 쓰는 것과 비교했을 때, 어떤 상황에서 커뮤니티 예시를 찾아 쓰는 게 더 효율적일까요?

---

## 오늘까지 배운 내용 정리
| 단계 | 이름 | 적용 시점 |
|---|---|---|
| 1 | TCCOV 프롬프트 | 이번 대화 1번만 |
| 2 | Custom Instructions | 프로젝트를 여는 동안 항상 |
| 3 | Agent Skills | 관련된 작업일 때만 선택적으로 |
| 4 | awesome-copilot 활용 | 처음부터 만들지 않고 검증된 예시를 가져와 커스터마이징 |

## 핵심 포인트
> 모든 규칙과 지침을 매번 처음부터 만들 필요는 없습니다.
> 이미 검증된 커뮤니티 예시를 찾아보고, 내 프로젝트에 맞게 다듬어 쓰는 것도
> 훌륭한 컨텍스트 엔지니어링입니다.
