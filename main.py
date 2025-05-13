import streamlit as st

# MBTI별 추천 직업 데이터 (예시)
# 실제 진로 교육에는 더 다양하고 전문적인 정보가 필요합니다.
# 각 직업에 간단한 '선호도 키워드'를 연결하여 후속 질문과 연동합니다.
mbti_careers = {
    "ISTJ": {"name": "세상의 소금형", "emoji": "🧂", "careers": [
        {"name": "회계사", "keywords": ["규칙/절차", "데이터", "안정적"], "explanation": "정확하고 체계적인 성향이 강하며, 데이터 분석과 규칙 준수가 중요한 회계 업무에 적합합니다."},
        {"name": "공무원", "keywords": ["규칙/절차", "안정적", "사회봉사"], "explanation": "안정적인 환경에서 정해진 규칙에 따라 일하며 사회에 기여하는 공무원 직무에 잘 맞을 수 있습니다."},
        {"name": "은행원", "keywords": ["규칙/절차", "사람들과 소통", "안정적"], "explanation": "규칙적인 업무 환경에서 고객과 소통하며 안정적으로 일하는 은행 업무에 강점을 보일 수 있습니다."},
        {"name": "시스템 관리자", "keywords": ["데이터", "문제 해결", "안정적"], "explanation": "시스템 데이터를 관리하고 문제를 해결하는 기술적인 업무를 안정적으로 수행하는 데 능숙합니다."}
    ]},
    "ISFJ": {"name": "임금 뒷편의 권력형", "emoji": "🛡️", "careers": [
        {"name": "간호사", "keywords": ["사람들과 소통", "사회봉사", "규칙/절차"], "explanation": "타인을 돕는 사회봉사 성향과 규칙적인 의료 절차 준수가 중요한 간호 업무에 적합합니다."},
        {"name": "사회복지사", "keywords": ["사람들과 소통", "사회봉사", "문제 해결"], "explanation": "사람들과 소통하며 그들의 문제를 해결하고 사회에 기여하는 사회복지 분야에 잘 맞을 수 있습니다."},
        {"name": "초등학교 교사", "keywords": ["사람들과 소통", "사회봉사", "창의적"], "explanation": "아이들과 소통하며 그들의 성장을 돕고, 창의적인 교육 방식을 활용하는 초등 교육에 강점을 보일 수 있습니다."},
        {"name": "사서", "keywords": ["규칙/절차", "데이터", "안정적"], "explanation": "자료를 체계적으로 관리하고 규칙에 따라 운영하는 사서 업무를 안정적으로 수행하는 데 능숙합니다."}
    ]},
    "INFJ": {"name": "예언자형", "emoji": "🔮", "careers": [
        {"name": "심리학자", "keywords": ["사람들과 소통", "문제 해결", "창의적"], "explanation": "인간 심리에 대한 깊은 이해를 바탕으로 사람들의 문제를 해결하고 새로운 이론을 탐구하는 심리학 분야에 적합합니다."},
        {"name": "상담사", "keywords": ["사람들과 소통", "문제 해결", "사회봉사"], "explanation": "타인과 깊이 소통하며 그들의 어려움을 듣고 해결을 돕는 상담 분야에 잘 맞을 수 있습니다."},
        {"name": "작가", "keywords": ["창의적", "혼자 집중", "아이디어"], "explanation": "내면의 아이디어를 바탕으로 창의적인 글쓰기에 집중하는 작가 활동에 강점을 보일 수 있습니다."},
        {"name": "예술가", "keywords": ["창의적", "혼자 집중", "아이디어"], "explanation": "독창적인 아이디어를 시각적 또는 다른 형태로 표현하는 예술 분야에 능숙합니다."}
    ]},
    "INTJ": {"name": "과학자형", "emoji": "🔬", "careers": [
        {"name": "연구원", "keywords": ["데이터", "문제 해결", "혼자 집중", "아이디어"], "explanation": "데이터를 분석하고 문제를 해결하며 새로운 아이디어를 탐구하는 연구 분야에 적합합니다."},
        {"name": "대학교수", "keywords": ["데이터", "사람들과 소통", "아이디어"], "explanation": "전문 분야의 데이터를 연구하고 새로운 아이디어를 학생들에게 전달하는 대학교수 직무에 잘 맞을 수 있습니다."},
        {"name": "엔지니어", "keywords": ["데이터", "문제 해결", "규칙/절차"], "explanation": "데이터와 규칙을 바탕으로 기술적인 문제를 해결하고 시스템을 설계하는 엔지니어링 분야에 강점을 보일 수 있습니다."},
        {"name": "건축가", "keywords": ["창의적", "문제 해결", "규칙/절차"], "explanation": "창의적인 아이디어로 공간 문제를 해결하고 건축 규칙에 따라 설계하는 건축 분야에 능숙합니다."}
    ]},
    "ISTP": {"name": "백과사전형", "emoji": "🛠️", "careers": [
        {"name": "기술자", "keywords": ["문제 해결", "몸을 움직임", "규칙/절차"], "explanation": "실질적인 문제를 파악하고 몸을 움직여 해결하는 기술 분야에 적합합니다."},
        {"name": "경찰관", "keywords": ["몸을 움직임", "문제 해결", "안정적"], "explanation": "활동적으로 움직이며 사건을 해결하고 사회 질서를 유지하는 경찰 직무에 잘 맞을 수 있습니다."},
        {"name": "소방관", "keywords": ["몸을 움직임", "문제 해결", "사회봉사"], "explanation": "위험한 상황에서 몸을 움직여 사람들을 돕고 문제를 해결하는 소방 분야에 강점을 보일 수 있습니다."},
        {"name": "파일럿", "keywords": ["규칙/절차", "안정적", "혼자 집중"], "explanation": "정해진 규칙에 따라 비행을 안정적으로 수행하며 고도의 집중력을 발휘하는 파일럿 직무에 능숙합니다."}
    ]},
    "ISFP": {"name": "성인군자형", "emoji": "🎨", "careers": [
        {"name": "디자이너", "keywords": ["창의적", "혼자 집중", "몸을 움직임"], "explanation": "자신의 감각과 창의성을 발휘하여 결과물을 만들어내는 디자인 분야에 적합합니다."},
        {"name": "음악가", "keywords": ["창의적", "혼자 집중"], "explanation": "내면의 감정을 음악으로 표현하고 연주에 집중하는 음악 분야에 잘 맞을 수 있습니다."},
        {"name": "요리사", "keywords": ["창의적", "몸을 움직임", "규칙/절차"], "explanation": "창의적인 레시피를 개발하고 손을 사용하여 요리를 만들며 규칙적인 주방 업무를 수행하는 요리 분야에 강점을 보일 수 있습니다."},
        {"name": "수의사", "keywords": ["사람들과 소통", "문제 해결", "사회봉사"], "explanation": "동물 및 보호자와 소통하며 동물의 건강 문제를 해결하고 생명을 구하는 수의학 분야에 능숙합니다."}
    ]},
    "INFP": {"name": "잔 다르크형", "emoji": "🌟", "careers": [
        {"name": "시인", "keywords": ["창의적", "혼자 집중", "아이디어"], "explanation": "추상적인 아이디어를 시적인 언어로 창의적으로 표현하는 시 쓰기에 적합합니다."},
        {"name": "소설가", "keywords": ["창의적", "혼자 집중", "아이디어"], "explanation": "상상력을 발휘하여 이야기를 만들고 글쓰기에 집중하는 소설 창작에 잘 맞을 수 있습니다."},
        {"name": "그래픽 디자이너", "keywords": ["창의적", "혼자 집중", "데이터"], "explanation": "창의적인 아이디어를 시각적인 데이터로 구현하는 그래픽 디자인 분야에 강점을 보일 수 있습니다."},
        {"name": "편집자", "keywords": ["창의적", "규칙/절차", "혼자 집중"], "explanation": "창의적인 관점으로 글을 다듬고 출판 규칙에 따라 작업하는 편집 업무에 능숙합니다."}
    ]},
    "INTP": {"name": "아이디어 뱅크형", "emoji": "💡", "careers": [
        {"name": "프로그래머", "keywords": ["데이터", "문제 해결", "혼자 집중", "아이디어"], "explanation": "데이터와 논리를 사용하여 문제를 해결하고 새로운 프로그램을 개발하는 프로그래밍 분야에 적합합니다."},
        {"name": "수학자", "keywords": ["데이터", "문제 해결", "혼자 집중", "규칙/절차"], "explanation": "데이터와 규칙을 바탕으로 추상적인 문제를 깊이 탐구하는 수학 연구에 잘 맞을 수 있습니다."},
        {"name": "철학자", "keywords": ["아이디어", "혼자 집중"], "explanation": "추상적이고 이론적인 아이디어를 깊이 탐구하고 사색하는 철학 분야에 강점을 보일 수 있습니다."},
        {"name": "데이터 과학자", "keywords": ["데이터", "문제 해결", "아이디어"], "explanation": "데이터를 분석하여 문제를 해결하고 새로운 통찰을 발견하는 데이터 과학 분야에 능숙합니다."}
    ]},
    "ESTP": {"name": "활동가형", "emoji": "🏄", "careers": [
        {"name": "영업원", "keywords": ["사람들과 소통", "몸을 움직임", "아이디어"], "explanation": "사람들과 적극적으로 소통하고 활동적으로 움직이며 새로운 영업 전략을 시도하는 영업 분야에 적합합니다."},
        {"name": "사업가", "keywords": ["사람들과 소통", "문제 해결", "아이디어", "몸을 움직임"], "explanation": "다양한 사람들과 소통하며 문제를 해결하고 새로운 사업 아이디어를 실행하는 사업 분야에 잘 맞을 수 있습니다."},
        {"name": "스포츠 선수", "keywords": ["몸을 움직임", "규칙/절차", "문제 해결"], "explanation": "규칙에 따라 몸을 움직여 경기에 참여하고 문제를 해결하는 스포츠 분야에 강점을 보일 수 있습니다."},
        {"name": "탐정", "keywords": ["문제 해결", "몸을 움직임", "데이터"], "explanation": "현장을 직접 조사하고 데이터를 분석하여 사건을 해결하는 탐정 직무에 능숙합니다."}
    ]},
    "ESFP": {"name": "사교적인 유형", "emoji": "🥳", "careers": [
        {"name": "연예인", "keywords": ["사람들과 소통", "창의적", "몸을 움직임"], "explanation": "사람들 앞에서 자신의 끼를 발산하고 활동적으로 표현하는 연예 분야에 적합합니다."},
        {"name": "이벤트 기획자", "keywords": ["사람들과 소통", "창의적", "몸을 움직임", "규칙/절차"], "explanation": "사람들과 소통하며 창의적인 아이디어로 이벤트를 기획하고 실행하는 이벤트 기획 분야에 잘 맞을 수 있습니다."},
        {"name": "승무원", "keywords": ["사람들과 소통", "규칙/절차", "안정적"], "explanation": "다양한 승객과 소통하며 안전 및 서비스 규칙에 따라 안정적으로 일하는 승무원 직무에 강점을 보일 수 있습니다."},
        {"name": "유치원 교사", "keywords": ["사람들과 소통", "사회봉사", "창의적"], "explanation": "아이들과 소통하며 그들의 성장을 돕고 창의적인 활동을 통해 교육하는 유치원 교육에 능숙합니다."}
    ]},
    "ENFP": {"name": "스파크형", "emoji": "✨", "careers": [
        {"name": "마케터", "keywords": ["사람들과 소통", "창의적", "아이디어", "데이터"], "explanation": "사람들의 마음을 움직이는 창의적인 아이디어를 내고 데이터를 활용하여 홍보 전략을 세우는 마케팅 분야에 적합합니다."},
        {"name": "홍보 전문가", "keywords": ["사람들과 소통", "창의적", "아이디어"], "explanation": "사람들과 소통하며 창의적인 아이디어로 조직이나 개인을 홍보하는 분야에 잘 맞을 수 있습니다."},
        {"name": "강사", "keywords": ["사람들과 소통", "창의적", "아이디어"], "explanation": "사람들과 소통하며 자신의 지식과 아이디어를 창의적으로 전달하는 강사 직무에 강점을 보일 수 있습니다."},
        {"name": "크리에이터", "keywords": ["창의적", "아이디어", "혼자 집중", "몸을 움직임"], "explanation": "새로운 아이디어를 바탕으로 다양한 콘텐츠를 창의적으로 만들고 활동하는 크리에이터 분야에 능숙합니다."}
    ]},
    "ENTP": {"name": "발명가형", "emoji": "🧠", "careers": [
        {"name": "기업가", "keywords": ["아이디어", "문제 해결", "사람들과 소통", "몸을 움직임"], "explanation": "새로운 아이디어로 사업을 시작하고 문제를 해결하며 다양한 사람들과 소통하는 기업가 활동에 적합합니다."},
        {"name": "변호사", "keywords": ["문제 해결", "규칙/절차", "사람들과 소통", "데이터"], "explanation": "법률 규칙을 바탕으로 문제를 분석하고 해결하며 의뢰인과 소통하는 변호사 직무에 잘 맞을 수 있습니다."},
        {"name": "컨설턴트", "keywords": ["문제 해결", "데이터", "사람들과 소통", "아이디어"], "explanation": "데이터 분석과 새로운 아이디어를 바탕으로 기업의 문제를 해결하고 고객과 소통하는 컨설팅 분야에 강점을 보일 수 있습니다."},
        {"name": "발명가", "keywords": ["아이디어", "문제 해결", "혼자 집중", "규칙/절차"], "explanation": "새로운 아이디어를 바탕으로 문제를 해결하고 규칙에 따라 결과물을 만들어내는 발명 분야에 능숙합니다."}
    ]},
    "ESTJ": {"name": "사업가형", "emoji": "💼", "careers": [
        {"name": "경영자", "keywords": ["규칙/절차", "사람들과 소통", "문제 해결", "데이터"], "explanation": "조직의 규칙을 정하고 사람들과 소통하며 문제를 해결하여 성과를 이끌어내는 경영 분야에 적합합니다."},
        {"name": "관리자", "keywords": ["규칙/절차", "사람들과 소통", "문제 해결", "안정적"], "explanation": "정해진 규칙에 따라 조직을 관리하고 사람들과 소통하며 문제를 해결하는 관리직에 잘 맞을 수 있습니다."},
        {"name": "군인", "keywords": ["규칙/절차", "몸을 움직임", "안정적"], "explanation": "규칙과 체계에 따라 움직이며 국가 안보를 위해 헌신하는 군인 직무에 강점을 보일 수 있습니다."},
        {"name": "판사", "keywords": ["규칙/절차", "문제 해결", "데이터", "혼자 집중"], "explanation": "법률 규칙과 데이터를 바탕으로 사건을 분석하고 문제를 해결하며 공정한 판단을 내리는 판사 직무에 능숙합니다."}
    ]},
    "ESFJ": {"name": "친선도모형", "emoji": "🤝", "careers": [
        {"name": "교사", "keywords": ["사람들과 소통", "사회봉사", "규칙/절차", "안정적"], "explanation": "학생들과 소통하며 그들의 성장을 돕고 교육 규칙에 따라 안정적으로 교육하는 교사 직무에 적합합니다."},
        {"name": "영업 관리자", "keywords": ["사람들과 소통", "문제 해결", "규칙/절차"], "explanation": "영업팀원과 소통하며 문제를 해결하고 영업 규칙에 따라 팀을 관리하는 분야에 잘 맞을 수 있습니다."},
        {"name": "사회복지사", "keywords": ["사람들과 소통", "사회봉사", "문제 해결"], "explanation": "타인과 소통하며 그들의 문제를 해결하고 사회에 기여하는 사회복지 분야에 강점을 보일 수 있습니다."},
        {"name": "행정가", "keywords": ["규칙/절차", "사람들과 소통", "안정적"], "explanation": "정해진 규칙에 따라 행정 업무를 수행하고 사람들과 소통하며 안정적으로 일하는 행정 분야에 능숙합니다."}
    ]},
    "ENFJ": {"name": "언변능숙형", "emoji": "🗣️", "careers": [
        {"name": "정치인", "keywords": ["사람들과 소통", "아이디어", "문제 해결", "몸을 움직임"], "explanation": "사람들과 소통하며 자신의 아이디어를 바탕으로 사회 문제를 해결하기 위해 활동하는 정치 분야에 적합합니다."},
        {"name": "외교관", "keywords": ["사람들과 소통", "규칙/절차", "데이터"], "explanation": "다양한 국가의 사람들과 소통하며 국제 규칙과 데이터를 바탕으로 외교 업무를 수행하는 분야에 잘 맞을 수 있습니다."},
        {"name": "리더십 코치", "keywords": ["사람들과 소통", "문제 해결", "아이디어"], "explanation": "사람들과 소통하며 그들의 문제를 파악하고 새로운 아이디어를 제시하여 성장을 돕는 리더십 코칭 분야에 강점을 보일 수 있습니다."},
        {"name": "성직자", "keywords": ["사람들과 소통", "사회봉사", "아이디어"], "explanation": "사람들과 소통하며 그들의 정신적인 문제를 돕고 공동체에 긍정적인 아이디어를 전달하는 성직 분야에 능숙합니다."}
    ]},
    "ENTJ": {"name": "지도자형", "emoji": "👑", "careers": [
        {"name": "최고 경영자 (CEO)", "keywords": ["문제 해결", "아이디어", "사람들과 소통", "데이터", "몸을 움직임"], "explanation": "조직의 문제를 해결하고 새로운 아이디어를 제시하며 다양한 사람들과 소통하여 조직을 이끌어가는 CEO 직무에 적합합니다."},
        {"name": "프로젝트 매니저", "keywords": ["규칙/절차", "문제 해결", "사람들과 소통", "데이터"], "explanation": "정해진 규칙에 따라 프로젝트를 관리하고 문제를 해결하며 팀원들과 소통하는 프로젝트 관리 분야에 잘 맞을 수 있습니다."},
        {"name": "전략 기획가", "keywords": ["아이디어", "문제 해결", "데이터", "혼자 집중"], "explanation": "데이터 분석과 깊은 사고를 통해 새로운 전략 아이디어를 제시하고 문제를 해결하는 전략 기획 분야에 강점을 보일 수 있습니다."},
        {"name": "컨설턴트", "keywords": ["문제 해결", "데이터", "사람들과 소통", "아이디어"], "explanation": "데이터 분석과 새로운 아이디어를 바탕으로 기업의 문제를 해결하고 고객과 소통하는 컨설팅 분야에 능숙합니다."}
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
        for i, option in enumerate(current_question_data['options']):
            # 고유한 키 생성
            checkbox_key = f"q{st.session_state.question_index}_opt{i}"
            # 체크박스가 선택되었는지 확인하고, 선택된 경우 해당 키워드를 추가
            if st.checkbox(option['text'], key=checkbox_key, value=checkbox_key in st.session_state.get(f'q{st.session_state.question_index}_selected', [])):
                 selected_options_for_current_q.extend(option['keywords'])

        # '다음 질문' 버튼
        if st.button("다음 질문", key=f"next_q_button_{st.session_state.question_index}"):
            # 현재 질문에서 선택된 키워드들을 세션 상태에 추가
            st.session_state.selected_preferences.extend(selected_options_for_current_q)
            # 현재 질문에서 선택된 옵션의 키를 저장 (페이지 새로고침 후에도 체크박스 상태 유지)
            st.session_state[f'q{st.session_state.question_index}_selected'] = [f"q{st.session_state.question_index}_opt{i}" for i, option in enumerate(current_question_data['options']) if st.session_state[f"q{st.session_state.question_index}_opt{i}"]]

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

        # 상위 직업 추천 (최대 5개, 선호도 점수가 0점 이상인 경우만)
        recommended_count = 0
        for career, score in sorted_careers:
            # 최소 1개 이상의 선호도 키워드가 일치하고, 아직 5개 미만으로 추천한 경우
            if score > 0 and recommended_count < 5:
                # 해당 직업 정보 찾기 (설명 포함)
                career_detail = next((item for item in mbti_info['careers'] if item['name'] == career), None)
                if career_detail:
                    st.markdown(f"**{career}** 👍")
                    st.write(f"*{career_detail['explanation']}*") # 상담 내용 형식으로 설명 제시
                    st.write(f"(선호도 일치도: {score}개)")
                    st.markdown("") # 줄바꿈
                    recommended_count += 1
            elif recommended_count >= 5:
                break # 5개 추천했으면 중단

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
