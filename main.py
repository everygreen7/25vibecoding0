import streamlit as st

# MBTI별 추천 직업 데이터 (예시)
# 실제 진로 교육에는 더 다양하고 전문적인 정보가 필요합니다.
# 각 직업에 간단한 '선호도 키워드', '설명', '준비 사항'을 연결합니다.
mbti_careers = {
    "ISTJ": {"name": "세상의 소금형", "emoji": "🧂", "careers": [
        {"name": "회계사", "keywords": ["규칙/절차", "데이터", "안정적"], "explanation": "정확하고 체계적인 성향이 강하며, 데이터 분석과 규칙 준수가 중요한 회계 업무에 적합합니다.", "preparation": "경영학, 회계학 전공, 회계 관련 자격증(AICPA, KICPA 등) 취득, 재무 및 세무 관련 지식 습득"},
        {"name": "공무원", "keywords": ["규칙/절차", "안정적", "사회봉사"], "explanation": "안정적인 환경에서 정해진 규칙에 따라 일하며 사회에 기여하는 공무원 직무에 잘 맞을 수 있습니다.", "preparation": "공무원 시험 준비 (국어, 영어, 한국사 등 공통 과목 및 직렬별 전문 과목), 관련 분야 전공 (행정학 등), 봉사활동 경험"},
        {"name": "은행원", "keywords": ["규칙/절차", "사람들과 소통", "안정적"], "explanation": "규칙적인 업무 환경에서 고객과 소통하며 안정적으로 일하는 은행 업무에 강점을 보일 수 있습니다.", "preparation": "경영학, 경제학, 금융학 전공, 금융 관련 자격증(AFPK, CFP 등) 취득, 고객 응대 및 소통 능력 향상"},
        {"name": "시스템 관리자", "keywords": ["데이터", "문제 해결", "안정적"], "explanation": "시스템 데이터를 관리하고 문제를 해결하는 기술적인 업무를 안정적으로 수행하는 데 능숙합니다.", "preparation": "컴퓨터공학, 정보통신학 전공, 서버/네트워크 관련 지식 및 실습, 정보처리기사 등 자격증 취득"}
    ]},
    "ISFJ": {"name": "임금 뒷편의 권력형", "emoji": "🛡️", "careers": [
        {"name": "간호사", "keywords": ["사람들과 소통", "사회봉사", "규칙/절차"], "explanation": "타인을 돕는 사회봉사 성향과 규칙적인 의료 절차 준수가 중요한 간호 업무에 적합합니다.", "preparation": "간호학과 전공, 간호사 국가고시 합격, 의료 관련 지식 및 실습 능력, 환자와의 공감 및 소통 능력"},
        {"name": "사회복지사", "keywords": ["사람들과 소통", "사회봉사", "문제 해결"], "explanation": "사람들과 소통하며 그들의 문제를 해결하고 사회에 기여하는 사회복지 분야에 잘 맞을 수 있습니다.", "preparation": "사회복지학과 전공, 사회복지사 자격증 취득, 상담 및 문제 해결 능력, 다양한 사람들에 대한 이해와 공감 능력"},
        {"name": "초등학교 교사", "keywords": ["사람들과 소통", "사회봉사", "창의적"], "explanation": "아이들과 소통하며 그들의 성장을 돕고, 창의적인 교육 방식을 활용하는 초등 교육에 강점을 보일 수 있습니다.", "preparation": "초등교육과 전공 (사범대 또는 교대), 교원 임용고시 합격, 아동 발달 및 교육 과정 이해, 창의적인 수업 구성 능력"},
        {"name": "사서", "keywords": ["규칙/절차", "데이터", "안정적"], "explanation": "자료를 체계적으로 관리하고 규칙에 따라 운영하는 사서 업무를 안정적으로 수행하는 데 능숙합니다.", "preparation": "문헌정보학과 전공, 사서 자격증 취득, 자료 분류 및 관리 시스템 이해, 이용자에 대한 서비스 마인드"}
    ]},
    "INFJ": {"name": "예언자형", "emoji": "🔮", "careers": [
        {"name": "심리학자", "keywords": ["사람들과 소통", "문제 해결", "창의적"], "explanation": "인간 심리에 대한 깊은 이해를 바탕으로 사람들의 문제를 해결하고 새로운 이론을 탐구하는 심리학 분야에 적합합니다.", "preparation": "심리학과 전공 (대학원 진학 필수), 연구 방법론 학습, 상담 및 분석 능력, 인간 행동에 대한 깊은 통찰력"},
        {"name": "상담사", "keywords": ["사람들과 소통", "문제 해결", "사회봉사"], "explanation": "타인과 깊이 소통하며 그들의 어려움을 듣고 해결을 돕는 상담 분야에 잘 맞을 수 있습니다.", "preparation": "심리학, 상담학, 사회복지학 등 전공 (대학원 또는 전문 교육 과정 이수), 상담 관련 자격증 취득, 경청 및 공감 능력"},
        {"name": "작가", "keywords": ["창의적", "혼자 집중", "아이디어"], "explanation": "내면의 아이디어를 바탕으로 창의적인 글쓰기에 집중하는 작가 활동에 강점을 보일 수 있습니다.", "preparation": "문예창작학과 등 관련 전공 또는 꾸준한 글쓰기 연습, 다양한 분야에 대한 폭넓은 독서, 자신만의 독창적인 아이디어 발굴 능력"},
        {"name": "예술가", "keywords": ["창의적", "혼자 집중", "아이디어"], "explanation": "독창적인 아이디어를 시각적 또는 다른 형태로 표현하는 예술 분야에 능숙합니다.", "preparation": "미술, 음악, 디자인 등 관련 전공 또는 전문적인 실기 훈련, 자신만의 예술 세계 구축, 포트폴리오 제작 및 전시/공연 경험"}
    ]},
    "INTJ": {"name": "과학자형", "emoji": "🔬", "careers": [
        {"name": "연구원", "keywords": ["데이터", "문제 해결", "혼자 집중", "아이디어"], "explanation": "데이터를 분석하고 문제를 해결하며 새로운 아이디어를 탐구하는 연구 분야에 적합합니다.", "preparation": "관련 분야 학사 및 석/박사 학위 취득, 연구 방법론 및 데이터 분석 능력, 논문 작성 및 발표 경험, 끊임없는 학습 자세"},
        {"name": "대학교수", "keywords": ["데이터", "사람들과 소통", "아이디어"], "explanation": "전문 분야의 데이터를 연구하고 새로운 아이디어를 학생들에게 전달하는 대학교수 직무에 잘 맞을 수 있습니다.", "preparation": "관련 분야 박사 학위 취득, 연구 실적 및 강의 능력, 학생 지도 및 소통 능력, 교육자로서의 사명감"},
        {"name": "엔지니어", "keywords": ["데이터", "문제 해결", "규칙/절차"], "explanation": "데이터와 규칙을 바탕으로 기술적인 문제를 해결하고 시스템을 설계하는 엔지니어링 분야에 강점을 보일 수 있습니다.", "preparation": "공학 계열 전공, 관련 분야 전문 지식 및 기술 습득, 문제 해결 능력, 팀워크 및 협업 능력"},
        {"name": "건축가", "keywords": ["창의적", "문제 해결", "규칙/절차"], "explanation": "창의적인 아이디어로 공간 문제를 해결하고 건축 규칙에 따라 설계하는 건축 분야에 능숙합니다.", "preparation": "건축학과 전공, 건축 관련 자격증 취득, 설계 프로그램 활용 능력, 공간 지각 능력 및 창의적인 아이디어"}
    ]},
    "ISTP": {"name": "백과사전형", "emoji": "🛠️", "careers": [
        {"name": "기술자", "keywords": ["문제 해결", "몸을 움직임", "규칙/절차"], "explanation": "실질적인 문제를 파악하고 몸을 움직여 해결하는 기술 분야에 적합합니다.", "preparation": "공업고등학교 또는 전문대학/대학교 관련 학과 졸업, 해당 분야 기술 자격증 취득, 실무 경험 및 문제 해결 능력, 꼼꼼함과 정확성"},
        {"name": "경찰관", "keywords": ["몸을 움직임", "문제 해결", "안정적"], "explanation": "활동적으로 움직이며 사건을 해결하고 사회 질서를 유지하는 경찰 직무에 잘 맞을 수 있습니다.", "preparation": "경찰행정학과 등 관련 학과 전공 또는 경찰 시험 준비, 체력 단련, 법률 지식 습득, 위기 대처 능력"},
        {"name": "소방관", "keywords": ["몸을 움직임", "문제 해결", "사회봉사"], "explanation": "위험한 상황에서 몸을 움직여 사람들을 돕고 문제를 해결하는 소방 분야에 강점을 보일 수 있습니다.", "preparation": "소방 관련 학과 전공 또는 소방 시험 준비, 강인한 체력과 정신력, 응급 처치 능력, 희생정신"},
        {"name": "파일럿", "keywords": ["규칙/절차", "안정적", "혼자 집중"], "explanation": "정해진 규칙에 따라 비행을 안정적으로 수행하며 고도의 집중력을 발휘하는 파일럿 직무에 능숙합니다.", "preparation": "항공운항학과 전공 또는 항공 교육 기관 이수, 비행 훈련 및 자격증 취득, 뛰어난 상황 판단 능력 및 집중력, 건강한 신체"}
    ]},
    "ISFP": {"name": "성인군자형", "emoji": "🎨", "careers": [
        {"name": "디자이너", "keywords": ["창의적", "혼자 집중", "몸을 움직임"], "explanation": "자신의 감각과 창의성을 발휘하여 결과물을 만들어내는 디자인 분야에 적합합니다.", "preparation": "디자인 관련 학과 전공, 디자인 툴 활용 능력, 자신만의 개성 있는 디자인 스타일 구축, 포트폴리오 제작"},
        {"name": "음악가", "keywords": ["창의적", "혼자 집중"], "explanation": "내면의 감정을 음악으로 표현하고 연주에 집중하는 음악 분야에 잘 맞을 수 있습니다.", "preparation": "음악 관련 학과 전공 또는 전문적인 음악 교육, 악기 연주 또는 작/편곡 능력, 자신만의 음악 세계 구축, 공연 및 음반 활동"},
        {"name": "요리사", "keywords": ["창의적", "몸을 움직임", "규칙/절차"], "explanation": "창의적인 레시피를 개발하고 손을 사용하여 요리를 만들며 규칙적인 주방 업무를 수행하는 요리 분야에 강점을 보일 수 있습니다.", "preparation": "조리학과 전공 또는 요리 학원 수료, 다양한 요리 레시피 습득 및 실습, 위생 및 안전 지식, 창의적인 레시피 개발 능력"},
        {"name": "수의사", "keywords": ["사람들과 소통", "문제 해결", "사회봉사"], "explanation": "동물 및 보호자와 소통하며 동물의 건강 문제를 해결하고 생명을 구하는 수의학 분야에 능숙합니다.", "preparation": "수의예과 및 수의학과 전공, 수의사 국가고시 합격, 동물에 대한 깊은 이해와 사랑, 보호자와의 원활한 소통 능력"}
    ]},
    "INFP": {"name": "잔 다르크형", "emoji": "🌟", "careers": [
        {"name": "시인", "keywords": ["창의적", "혼자 집중", "아이디어"], "explanation": "추상적인 아이디어를 시적인 언어로 창의적으로 표현하는 시 쓰기에 적합합니다.", "preparation": "문예창작학과 등 관련 전공 또는 꾸준한 시 쓰기 연습, 폭넓은 독서와 사색, 자신만의 감수성 표현 능력"},
        {"name": "소설가", "keywords": ["창의적", "혼자 집중", "아이디어"], "explanation": "상상력을 발휘하여 이야기를 만들고 글쓰기에 집중하는 소설 창작에 잘 맞을 수 있습니다.", "preparation": "문예창작학과 등 관련 전공 또는 꾸준한 소설 쓰기 연습, 다양한 경험과 상상력, 탄탄한 스토리 구성 능력"},
        {"name": "그래픽 디자이너", "keywords": ["창의적", "혼자 집중", "데이터"], "explanation": "창의적인 아이디어를 시각적인 데이터로 구현하는 그래픽 디자인 분야에 강점을 보일 수 있습니다.", "preparation": "그래픽 디자인 관련 학과 전공, 디자인 툴 활용 능력, 시각적인 감각과 창의성, 포트폴리오 제작"},
        {"name": "편집자", "keywords": ["창의적", "규칙/절차", "혼자 집중"], "explanation": "창의적인 관점으로 글을 다듬고 출판 규칙에 따라 작업하는 편집 업무에 능숙합니다.", "preparation": "국어국문학과, 문예창작학과 등 관련 전공, 뛰어난 문장력 및 교정/교열 능력, 출판 시장 및 독자 이해, 꼼꼼함과 책임감"}
    ]},
    "INTP": {"name": "아이디어 뱅크형", "emoji": "💡", "careers": [
        {"name": "프로그래머", "keywords": ["데이터", "문제 해결", "혼자 집중", "아이디어"], "explanation": "데이터와 논리를 사용하여 문제를 해결하고 새로운 프로그램을 개발하는 프로그래밍 분야에 적합합니다.", "preparation": "컴퓨터공학, 소프트웨어학과 등 전공, 다양한 프로그래밍 언어 학습, 알고리즘 및 자료구조 이해, 코딩 실력 향상"},
        {"name": "수학자", "keywords": ["데이터", "문제 해결", "혼자 집중", "규칙/절차"], "explanation": "데이터와 규칙을 바탕으로 추상적인 문제를 깊이 탐구하는 수학 연구에 잘 맞을 수 있습니다.", "preparation": "수학과 전공 (대학원 진학 필수), 깊이 있는 수학 이론 학습, 논리적 사고력 및 문제 해결 능력, 추상적인 개념 이해 능력"},
        {"name": "철학자", "keywords": ["아이디어", "혼자 집중"], "explanation": "추상적이고 이론적인 아이디어를 깊이 탐구하고 사색하는 철학 분야에 강점을 보일 수 있습니다.", "preparation": "철학과 전공 (대학원 진학 필수), 다양한 철학 사상 학습, 비판적 사고력 및 논리력, 깊이 있는 사색 능력"},
        {"name": "데이터 과학자", "keywords": ["데이터", "문제 해결", "아이디어"], "explanation": "데이터를 분석하여 문제를 해결하고 새로운 통찰을 발견하는 데이터 과학 분야에 능숙합니다.", "preparation": "컴퓨터공학, 통계학, 수학 등 전공, 데이터 분석 툴 및 프로그래밍 언어 학습, 통계적 지식 및 모델링 능력, 새로운 통찰 발굴 능력"}
    ]},
    "ESTP": {"name": "활동가형", "emoji": "🏄", "careers": [
        {"name": "영업원", "keywords": ["사람들과 소통", "몸을 움직임", "아이디어"], "explanation": "사람들과 적극적으로 소통하고 활동적으로 움직이며 새로운 영업 전략을 시도하는 영업 분야에 적합합니다.", "preparation": "마케팅, 경영학 등 관련 전공 또는 영업 관련 교육 이수, 뛰어난 커뮤니케이션 능력 및 설득력, 적극적인 태도와 긍정적인 마인드"},
        {"name": "사업가", "keywords": ["사람들과 소통", "문제 해결", "아이디어", "몸을 움직임"], "explanation": "다양한 사람들과 소통하며 문제를 해결하고 새로운 사업 아이디어를 실행하는 사업 분야에 잘 맞을 수 있습니다.", "preparation": "경영학, 경제학 등 전공 또는 사업 관련 경험, 시장 분석 능력, 문제 해결 능력, 리더십 및 추진력"},
        {"name": "스포츠 선수", "keywords": ["몸을 움직임", "규칙/절차", "문제 해결"], "explanation": "규칙에 따라 몸을 움직여 경기에 참여하고 문제를 해결하는 스포츠 분야에 강점을 보일 수 있습니다.", "preparation": "해당 종목에 대한 전문적인 훈련, 강인한 체력과 기술, 경기 규칙 및 전략 이해, 정신력 강화 훈련"},
        {"name": "탐정", "keywords": ["문제 해결", "몸을 움직임", "데이터"], "explanation": "현장을 직접 조사하고 데이터를 분석하여 사건을 해결하는 탐정 직무에 능숙합니다.", "preparation": "경찰학, 법학 등 관련 학과 전공 또는 탐정 관련 교육 이수, 뛰어난 관찰력 및 분석력, 추리 및 문제 해결 능력, 강인한 체력"}
    ]},
    "ESFP": {"name": "사교적인 유형", "emoji": "🥳", "careers": [
        {"name": "연예인", "keywords": ["사람들과 소통", "창의적", "몸을 움직임"], "explanation": "사람들 앞에서 자신의 끼를 발산하고 활동적으로 표현하는 연예 분야에 적합합니다.", "preparation": "연기, 노래, 춤 등 전문적인 훈련, 자신만의 매력 개발, 대중과의 소통 능력, 끊임없는 노력과 자기 관리"},
        {"name": "이벤트 기획자", "keywords": ["사람들과 소통", "창의적", "몸을 움직임", "규칙/절차"], "explanation": "사람들과 소통하며 창의적인 아이디어로 이벤트를 기획하고 실행하는 이벤트 기획 분야에 잘 맞을 수 있습니다.", "preparation": "이벤트, 홍보, 광고 등 관련 학과 전공, 창의적인 아이디어 기획 능력, 실행력 및 문제 해결 능력, 다양한 사람들과의 협업 능력"},
        {"name": "승무원", "keywords": ["사람들과 소통", "규칙/절차", "안정적"], "explanation": "다양한 승객과 소통하며 안전 및 서비스 규칙에 따라 안정적으로 일하는 승무원 직무에 강점을 보일 수 있습니다.", "preparation": "항공운항과, 관광경영학과 등 관련 학과 전공, 외국어 능력, 서비스 마인드 및 고객 응대 능력, 건강한 신체 및 단정한 용모"},
        {"name": "유치원 교사", "keywords": ["사람들과 소통", "사회봉사", "창의적"], "explanation": "아이들과 소통하며 그들의 성장을 돕고 창의적인 활동을 통해 교육하는 유치원 교육에 능숙합니다.", "preparation": "유아교육과 전공, 유치원 정교사 자격증 취득, 아동 발달 및 심리 이해, 창의적인 교육 프로그램 구성 능력, 아이들에 대한 사랑과 인내심"}
    ]},
    "ENFP": {"name": "스파크형", "emoji": "✨", "careers": [
        {"name": "마케터", "keywords": ["사람들과 소통", "창의적", "아이디어", "데이터"], "explanation": "사람들의 마음을 움직이는 창의적인 아이디어를 내고 데이터를 활용하여 홍보 전략을 세우는 마케팅 분야에 적합합니다.", "preparation": "마케팅, 경영학, 광고홍보학 등 전공, 시장 분석 능력, 창의적인 아이디어 발상 능력, 데이터 분석 및 활용 능력"},
        {"name": "홍보 전문가", "keywords": ["사람들과 소통", "창의적", "아이디어"], "explanation": "사람들과 소통하며 창의적인 아이디어로 조직이나 개인을 홍보하는 분야에 잘 맞을 수 있습니다.", "preparation": "홍보, 광고, 언론정보학 등 전공, 뛰어난 글쓰기 및 발표 능력, 위기 관리 능력, 다양한 사람들과의 네트워킹 능력"},
        {"name": "강사", "keywords": ["사람들과 소통", "창의적", "아이디어"], "explanation": "사람들과 소통하며 자신의 지식과 아이디어를 창의적으로 전달하는 강사 직무에 강점을 보일 수 있습니다.", "preparation": "자신이 가르칠 분야에 대한 전문 지식, 뛰어난 설명 및 전달 능력, 청중과의 상호작용 능력, 자신감과 열정"},
        {"name": "크리에이터", "keywords": ["창의적", "아이디어", "혼자 집중", "몸을 움직임"], "explanation": "새로운 아이디어를 바탕으로 다양한 콘텐츠를 창의적으로 만들고 활동하는 크리에이터 분야에 능숙합니다.", "preparation": "콘텐츠 기획 및 제작 능력 (영상 편집, 디자인 등), 자신만의 개성 있는 아이디어, 트렌드 파악 능력, 꾸준한 콘텐츠 생산 능력"}
    ]},
    "ENTP": {"name": "발명가형", "emoji": "🧠", "careers": [
        {"name": "기업가", "keywords": ["아이디어", "문제 해결", "사람들과 소통", "몸을 움직임"], "explanation": "새로운 아이디어로 사업을 시작하고 문제를 해결하며 다양한 사람들과 소통하는 기업가 활동에 적합합니다.", "preparation": "경영학, 경제학 등 전공 또는 사업 관련 경험, 시장 분석 및 사업 기획 능력, 문제 해결 능력, 리더십 및 위험 감수 능력"},
        {"name": "변호사", "keywords": ["문제 해결", "규칙/절차", "사람들과 소통", "데이터"], "explanation": "법률 규칙을 바탕으로 문제를 분석하고 해결하며 의뢰인과 소통하는 변호사 직무에 잘 맞을 수 있습니다.", "preparation": "법학 전문대학원(로스쿨) 진학 및 변호사 시험 합격, 법률 지식 및 논리적 사고력, 뛰어난 분석 및 문제 해결 능력, 의뢰인과의 신뢰 구축 능력"},
        {"name": "컨설턴트", "keywords": ["문제 해결", "데이터", "사람들과 소통", "아이디어"], "explanation": "데이터 분석과 새로운 아이디어를 바탕으로 기업의 문제를 해결하고 고객과 소통하는 컨설팅 분야에 강점을 보일 수 있습니다.", "preparation": "경영학, 경제학 등 전공 또는 관련 분야 전문성, 데이터 분석 능력, 논리적 사고력 및 문제 해결 능력, 고객과의 소통 및 프레젠테이션 능력"},
        {"name": "발명가", "keywords": ["아이디어", "문제 해결", "혼자 집중", "규칙/절차"], "explanation": "새로운 아이디어를 바탕으로 문제를 해결하고 규칙에 따라 결과물을 만들어내는 발명 분야에 능숙합니다.", "preparation": "관련 분야 전문 지식 및 기술, 창의적인 아이디어 발상 능력, 문제 해결 능력, 특허 출원 및 기술 사업화 지식"}
    ]},
    "ESTJ": {"name": "사업가형", "emoji": "💼", "careers": [
        {"name": "경영자", "keywords": ["규칙/절차", "사람들과 소통", "문제 해결", "데이터"], "explanation": "조직의 규칙을 정하고 사람들과 소통하며 문제를 해결하여 성과를 이끌어내는 경영 분야에 적합합니다.", "preparation": "경영학 등 관련 전공, 조직 관리 및 리더십 능력, 문제 해결 능력, 데이터 기반 의사결정 능력"},
        {"name": "관리자", "keywords": ["규칙/절차", "사람들과 소통", "문제 해결", "안정적"], "explanation": "정해진 규칙에 따라 조직을 관리하고 사람들과 소통하며 문제를 해결하는 관리직에 잘 맞을 수 있습니다.", "preparation": "경영학 등 관련 전공 또는 실무 경험, 조직 관리 및 소통 능력, 문제 해결 능력, 책임감과 성실함"},
        {"name": "군인", "keywords": ["규칙/절차", "몸을 움직임", "안정적"], "explanation": "규칙과 체계에 따라 움직이며 국가 안보를 위해 헌신하는 군인 직무에 강점을 보일 수 있습니다.", "preparation": "사관학교 또는 부사관/장교 임관 과정 이수, 강인한 체력과 정신력, 군사 지식 및 전술 이해, 리더십과 희생정신"},
        {"name": "판사", "keywords": ["규칙/절차", "문제 해결", "데이터", "혼자 집중"], "explanation": "법률 규칙과 데이터를 바탕으로 사건을 분석하고 문제를 해결하며 공정한 판단을 내리는 판사 직무에 능숙합니다.", "preparation": "법학 전문대학원(로스쿨) 졸업 및 판사 임용 절차 통과, 깊이 있는 법률 지식 및 논리적 사고력, 공정하고 객관적인 판단 능력, 책임감과 윤리의식"}
    ]},
    "ESFJ": {"name": "친선도모형", "emoji": "🤝", "careers": [
        {"name": "교사", "keywords": ["사람들과 소통", "사회봉사", "규칙/절차", "안정적"], "explanation": "학생들과 소통하며 그들의 성장을 돕고 교육 규칙에 따라 안정적으로 교육하는 교사 직무에 적합합니다.", "preparation": "사범대학 또는 교직 이수, 교원 임용고시 합격, 학생 지도 및 상담 능력, 교육 과정 및 교수법 이해"},
        {"name": "영업 관리자", "keywords": ["사람들과 소통", "문제 해결", "규칙/절차"], "explanation": "영업팀원과 소통하며 문제를 해결하고 영업 규칙에 따라 팀을 관리하는 분야에 잘 맞을 수 있습니다.", "preparation": "마케팅, 경영학 등 관련 전공 또는 영업 경험, 팀 관리 및 리더십 능력, 문제 해결 능력, 목표 달성 능력"},
        {"name": "사회복지사", "keywords": ["사람들과 소통", "사회봉사", "문제 해결"], "explanation": "타인과 소통하며 그들의 문제를 해결하고 사회에 기여하는 사회복지 분야에 강점을 보일 수 있습니다.", "preparation": "사회복지학과 전공, 사회복지사 자격증 취득, 상담 및 문제 해결 능력, 봉사정신과 타인에 대한 이해"},
        {"name": "행정가", "keywords": ["규칙/절차", "사람들과 소통", "안정적"], "explanation": "정해진 규칙에 따라 행정 업무를 수행하고 사람들과 소통하며 안정적으로 일하는 행정 분야에 능숙합니다.", "preparation": "행정학과 등 관련 전공 또는 행정 경험, 문서 작성 및 관리 능력, 다양한 사람들과의 소통 능력, 꼼꼼함과 책임감"}
    ]},
    "ENFJ": {"name": "언변능숙형", "emoji": "🗣️", "careers": [
        {"name": "정치인", "keywords": ["사람들과 소통", "아이디어", "문제 해결", "몸을 움직임"], "explanation": "사람들과 소통하며 자신의 아이디어를 바탕으로 사회 문제를 해결하기 위해 활동하는 정치 분야에 적합합니다.", "preparation": "정치외교학과, 행정학과 등 전공 또는 관련 분야 경험, 뛰어난 연설 및 설득 능력, 사회 문제에 대한 깊은 이해, 리더십과 추진력"},
        {"name": "외교관", "keywords": ["사람들과 소통", "규칙/절차", "데이터"], "explanation": "다양한 국가의 사람들과 소통하며 국제 규칙과 데이터를 바탕으로 외교 업무를 수행하는 분야에 잘 맞을 수 있습니다.", "preparation": "외교학과, 정치외교학과 등 전공, 뛰어난 외국어 능력, 국제 정세 및 문화 이해, 협상 및 소통 능력"},
        {"name": "리더십 코치", "keywords": ["사람들과 소통", "문제 해결", "아이디어"], "explanation": "사람들과 소통하며 그들의 문제를 파악하고 새로운 아이디어를 제시하여 성장을 돕는 리더십 코칭 분야에 강점을 보일 수 있습니다.", "preparation": "심리학, 교육학 등 관련 전공 또는 코칭 전문 교육 이수, 뛰어난 경청 및 공감 능력, 리더십 이론 및 실제 경험, 사람들의 잠재력 개발 능력"},
        {"name": "성직자", "keywords": ["사람들과 소통", "사회봉사", "아이디어"], "explanation": "사람들과 소통하며 그들의 정신적인 문제를 돕고 공동체에 긍정적인 아이디어를 전달하는 성직 분야에 능숙합니다.", "preparation": "신학대학원 졸업, 종교 관련 지식 및 영성, 사람들과의 소통 및 상담 능력, 봉사정신과 희생정신"}
    ]},
    "ENTJ": {"name": "지도자형", "emoji": "👑", "careers": [
        {"name": "최고 경영자 (CEO)", "keywords": ["문제 해결", "아이디어", "사람들과 소통", "데이터", "몸을 움직임"], "explanation": "조직의 문제를 해결하고 새로운 아이디어를 제시하며 다양한 사람들과 소통하여 조직을 이끌어가는 CEO 직무에 적합합니다.", "preparation": "경영학 등 관련 전공 및 다양한 실무 경험, 뛰어난 리더십 및 의사결정 능력, 시장 분석 및 전략 수립 능력, 문제 해결 능력"},
        {"name": "프로젝트 매니저", "keywords": ["규칙/절차", "문제 해결", "사람들과 소통", "데이터"], "explanation": "정해진 규칙에 따라 프로젝트를 관리하고 문제를 해결하며 팀원들과 소통하는 프로젝트 관리 분야에 잘 맞을 수 있습니다.", "preparation": "관련 분야 전문 지식 및 프로젝트 관리 방법론 학습, 뛰어난 조직 및 계획 능력, 팀원과의 소통 및 협업 능력, 문제 해결 능력"},
        {"name": "전략 기획가", "keywords": ["아이디어", "문제 해결", "데이터", "혼자 집중"], "explanation": "데이터 분석과 깊은 사고를 통해 새로운 전략 아이디어를 제시하고 문제를 해결하는 전략 기획 분야에 강점을 보일 수 있습니다.", "preparation": "경영학, 경제학 등 전공 또는 관련 분야 경험, 데이터 분석 능력, 논리적 사고력 및 전략 수립 능력, 시장 및 경쟁 환경 분석 능력"},
        {"name": "컨설턴트", "keywords": ["문제 해결", "데이터", "사람들과 소통", "아이디어"], "explanation": "데이터 분석과 새로운 아이디어를 바탕으로 기업의 문제를 해결하고 고객과 소통하는 컨설팅 분야에 능숙합니다.", "preparation": "경영학, 경제학 등 전공 또는 관련 분야 전문성, 데이터 분석 능력, 논리적 사고력 및 문제 해결 능력, 고객과의 소통 및 프레젠테이션 능력"}
    ]}
}


# 순차 질문 정의
# 각 질문은 딕셔너리 형태로, 'question'과 'options'를 포함합니다.
# 'options'는 다시 딕셔너리 리스트로, 'text'와 해당 옵션 선택 시 추가될 'keywords'를 가집니다.
sequential_questions = [
    {
        "question": "어떤 환경에서 일하는 것을 선호하시나요? 🤔",
        "options": [
            {"text": "사람들과 함께 소통하며 일하는 것 🤝", "keywords": ["사람들과 소통"]},
            {"text": "혼자 집중하여 깊이 파고드는 것 🤫", "keywords": ["혼자 집중"]}
        ]
    },
    {
        "question": "일의 성격은 어떠해야 할까요? ✨",
        "options": [
            {"text": "정해진 규칙과 절차에 따라 안정적으로 일하는 것 📝", "keywords": ["규칙/절차", "안정적"]},
            {"text": "새롭고 다양한 아이디어를 탐색하며 창의적으로 일하는 것 💡", "keywords": ["창의적", "아이디어"]}
        ]
    },
    {
        "question": "주로 어떤 종류의 활동에 흥미를 느끼나요? 📊💪",
        "options": [
            {"text": "정보나 데이터를 분석하고 활용하는 것 📊", "keywords": ["데이터"]},
            {"text": "몸을 움직이며 활동적으로 일하는 것 💪", "keywords": ["몸을 움직임"]}
        ]
    },
    {
        "question": "일에서 중요하다고 생각하는 가치는 무엇인가요? 👍",
        "options": [
            {"text": "문제를 파악하고 해결하여 성과를 내는 것 🔧", "keywords": ["문제 해결"]},
            {"text": "타인을 돕고 사회에 기여하는 것 💖", "keywords": ["사회봉사"]}
        ]
    }
]

# Streamlit session state 초기화
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
if 'selected_preferences' not in st.session_state:
    st.session_state.selected_preferences = []
if 'mbti_selected' not in st.session_state:
    st.session_state.mbti_selected = None

# 웹 앱 타이틀 설정
st.set_page_config(page_title="MBTI 기반 직업 추천 🚀", page_icon="👍")
st.title("나에게 맞는 직업은 무엇일까? 🤔")

st.markdown("""
안녕하세요! 당신의 MBTI 유형을 선택하시면, 해당 유형에게 어울릴 만한 직업들을 추천해 드립니다.
이 추천은 일반적인 경향이며, 개인의 흥미와 강점에 따라 얼마든지 달라질 수 있습니다. 😊
""")

# MBTI 선택 드롭다운
mbti_options = list(mbti_careers.keys())
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", mbti_options, key="mbti_select")

# MBTI 선택이 변경되면 세션 상태 초기화
if st.session_state.mbti_selected != selected_mbti:
    st.session_state.mbti_selected = selected_mbti
    st.session_state.question_index = 0
    st.session_state.selected_preferences = []
    # 이전 질문 선택 상태 초기화
    for i in range(len(sequential_questions)):
        st.session_state.pop(f'q{i}_selected', None)
        for j in range(len(sequential_questions[i]['options'])):
             st.session_state.pop(f'q{i}_opt{j}', None)

    st.rerun() # MBTI 변경 시 페이지 새로고침하여 질문 초기화

# 선택된 MBTI 정보 표시
if selected_mbti:
    mbti_info = mbti_careers[selected_mbti]
    st.subheader(f"선택하신 MBTI는 {selected_mbti} ({mbti_info['name']}) 입니다! {mbti_info['emoji']}")

    st.write("이 MBTI 유형에게 일반적으로 추천되는 직업 목록입니다:")
    # 일반 추천 목록은 항상 표시
    for career_info in mbti_info['careers']:
        st.markdown(f"- {career_info['name']} ✨")

    st.markdown("---") # 구분선 추가

    st.subheader("조금 더 자세히 알아볼까요? 🤔")

    # 순차 질문 표시 로직
    if st.session_state.question_index < len(sequential_questions):
        current_question_data = sequential_questions[st.session_state.question_index]
        st.write(f"**질문 {st.session_state.question_index + 1}.** {current_question_data['question']}")

        # 각 질문의 옵션에 대한 체크박스 생성
        selected_options_for_current_q = []
        # 현재 질문의 체크박스 상태를 저장할 리스트 초기화
        current_q_selected_keys = []
        for i, option in enumerate(current_question_data['options']):
            # 고유한 키 생성
            checkbox_key = f"q{st.session_state.question_index}_opt{i}"
            # 세션 상태에 저장된 이전 선택 상태를 불러와 체크박스 초기값 설정
            initial_value = checkbox_key in st.session_state.get(f'q{st.session_state.question_index}_selected', [])
            if st.checkbox(option['text'], key=checkbox_key, value=initial_value):
                 selected_options_for_current_q.extend(option['keywords'])
                 current_q_selected_keys.append(checkbox_key) # 현재 선택된 옵션 키 저장

        # '다음 질문' 버튼
        if st.button("다음 질문", key=f"next_q_button_{st.session_state.question_index}"):
            # 현재 질문에서 선택된 키워드들을 세션 상태에 추가
            st.session_state.selected_preferences.extend(selected_options_for_current_q)
            # 현재 질문에서 선택된 옵션의 키를 세션 상태에 저장
            st.session_state[f'q{st.session_state.question_index}_selected'] = current_q_selected_keys

            # 다음 질문으로 인덱스 이동
            st.session_state.question_index += 1
            st.rerun() # 페이지 새로고침하여 다음 질문 표시

    else: # 모든 질문 완료 후
        st.write("모든 질문에 답변하셨습니다! 당신의 MBTI 특성과 선호도를 바탕으로 추천 직업을 알려드릴게요. 👇")

        # 선택된 선호도와 직업 키워드를 매칭하여 점수 계산
        career_scores = {}
        for career_info in mbti_info['careers']:
            score = 0
            for keyword in career_info['keywords']:
                if keyword in st.session_state.selected_preferences:
                    score += 1
            career_scores[career_info['name']] = score

        # 점수가 높은 순서대로 정렬
        sorted_careers = sorted(career_scores.items(), key=lambda item: item[1], reverse=True)

        st.markdown("---") # 구분선 추가

        st.subheader("당신에게 추천하는 직업은... 👇")

        # 상위 3개 직업 추천 (선호도 점수가 0점 이상인 경우만)
        recommended_count = 0
        for career, score in sorted_careers:
            # 최소 1개 이상의 선호도 키워드가 일치하고, 아직 3개 미만으로 추천한 경우
            if score > 0 and recommended_count < 3:
                # 해당 직업 정보 찾기 (설명 및 준비 사항 포함)
                career_detail = next((item for item in mbti_info['careers'] if item['name'] == career), None)
                if career_detail:
                    st.markdown(f"**{career}** 👍")
                    st.write(f"*{career_detail['explanation']}*") # 상담 내용 형식으로 설명 제시
                    st.write(f"(선호도 일치도: {score}개)")
                    st.markdown("**이 직업을 위해 준비해야 할 사항:**") # 준비 사항 제목
                    st.write(f"{career_detail['preparation']}") # 준비 사항 내용
                    st.markdown("") # 줄바꿈
                    recommended_count += 1
            elif recommended_count >= 3:
                break # 3개 추천했으면 중단

        if recommended_count == 0:
            st.write("선택하신 선호도와 일치하는 추천 직업을 찾기 어렵습니다. 다른 선호도를 선택해 보세요! 🤔")

        st.markdown("---") # 구분선 추가
        # 다시 시작 버튼
        if st.button("다시 시작하기 🔄", key="restart_button"):
            st.session_state.question_index = 0
            st.session_state.selected_preferences = []
            st.session_state.mbti_selected = None # MBTI 선택도 초기화
            # 질문별 선택 상태도 초기화
            for i in range(len(sequential_questions)):
                st.session_state.pop(f'q{i}_selected', None)
                for j in range(len(sequential_questions[i]['options'])):
                     st.session_state.pop(f'q{i}_opt{j}', None)

            st.rerun() # 페이지 새로고침

st.markdown("""
---
**참고:** 이 추천은 참고용이며, 당신의 미래를 결정하는 절대적인 기준이 아닙니다.
다양한 경험을 통해 당신에게 가장 잘 맞는 길을 찾으시길 바랍니다! 응원합니다! 🎉
""")
