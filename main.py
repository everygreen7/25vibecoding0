import streamlit as st

# MBTI별 추천 직업 데이터 (예시)
# 실제 진로 교육에는 더 다양하고 전문적인 정보가 필요합니다.
# 각 직업에 간단한 '선호도 키워드'를 연결하여 후속 질문과 연동합니다.
mbti_careers = {
    "ISTJ": {"name": "세상의 소금형", "emoji": "🧂", "careers": [
        {"name": "회계사", "keywords": ["규칙/절차", "데이터", "안정적"]},
        {"name": "공무원", "keywords": ["규칙/절차", "안정적", "사회봉사"]},
        {"name": "은행원", "keywords": ["규칙/절차", "사람들과 소통", "안정적"]},
        {"name": "시스템 관리자", "keywords": ["데이터", "문제 해결", "안정적"]}
    ]},
    "ISFJ": {"name": "임금 뒷편의 권력형", "emoji": "🛡️", "careers": [
        {"name": "간호사", "keywords": ["사람들과 소통", "사회봉사", "규칙/절차"]},
        {"name": "사회복지사", "keywords": ["사람들과 소통", "사회봉사", "문제 해결"]},
        {"name": "초등학교 교사", "keywords": ["사람들과 소통", "사회봉사", "창의적"]},
        {"name": "사서", "keywords": ["규칙/절차", "데이터", "안정적"]}
    ]},
    "INFJ": {"name": "예언자형", "emoji": "🔮", "careers": [
        {"name": "심리학자", "keywords": ["사람들과 소통", "문제 해결", "창의적"]},
        {"name": "상담사", "keywords": ["사람들과 소통", "문제 해결", "사회봉사"]},
        {"name": "작가", "keywords": ["창의적", "혼자 집중", "아이디어"]},
        {"name": "예술가", "keywords": ["창의적", "혼자 집중", "아이디어"]}
    ]},
    "INTJ": {"name": "과학자형", "emoji": "🔬", "careers": [
        {"name": "연구원", "keywords": ["데이터", "문제 해결", "혼자 집중", "아이디어"]},
        {"name": "대학교수", "keywords": ["데이터", "사람들과 소통", "아이디어"]},
        {"name": "엔지니어", "keywords": ["데이터", "문제 해결", "규칙/절차"]},
        {"name": "건축가", "keywords": ["창의적", "문제 해결", "규칙/절차"]}
    ]},
    "ISTP": {"name": "백과사전형", "emoji": "🛠️", "careers": [
        {"name": "기술자", "keywords": ["문제 해결", "몸을 움직임", "규칙/절차"]},
        {"name": "경찰관", "keywords": ["몸을 움직임", "문제 해결", "안정적"]},
        {"name": "소방관", "keywords": ["몸을 움직임", "문제 해결", "사회봉사"]},
        {"name": "파일럿", "keywords": ["규칙/절차", "안정적", "혼자 집중"]}
    ]},
    "ISFP": {"name": "성인군자형", "emoji": "🎨", "careers": [
        {"name": "디자이너", "keywords": ["창의적", "혼자 집중", "몸을 움직임"]},
        {"name": "음악가", "keywords": ["창의적", "혼자 집중"]},
        {"name": "요리사", "keywords": ["창의적", "몸을 움직임", "규칙/절차"]},
        {"name": "수의사", "keywords": ["사람들과 소통", "문제 해결", "사회봉사"]}
    ]},
    "INFP": {"name": "잔 다르크형", "emoji": "🌟", "careers": [
        {"name": "시인", "keywords": ["창의적", "혼자 집중", "아이디어"]},
        {"name": "소설가", "keywords": ["창의적", "혼자 집중", "아이디어"]},
        {"name": "그래픽 디자이너", "keywords": ["창의적", "혼자 집중", "데이터"]},
        {"name": "편집자", "keywords": ["창의적", "규칙/절차", "혼자 집중"]}
    ]},
    "INTP": {"name": "아이디어 뱅크형", "emoji": "💡", "careers": [
        {"name": "프로그래머", "keywords": ["데이터", "문제 해결", "혼자 집중", "아이디어"]},
        {"name": "수학자", "keywords": ["데이터", "문제 해결", "혼자 집중", "규칙/절차"]},
        {"name": "철학자", "keywords": ["아이디어", "혼자 집중"]},
        {"name": "데이터 과학자", "keywords": ["데이터", "문제 해결", "아이디어"]}
    ]},
    "ESTP": {"name": "활동가형", "emoji": "🏄", "careers": [
        {"name": "영업원", "keywords": ["사람들과 소통", "몸을 움직임", "아이디어"]},
        {"name": "사업가", "keywords": ["사람들과 소통", "문제 해결", "아이디어", "몸을 움직임"]},
        {"name": "스포츠 선수", "keywords": ["몸을 움직임", "규칙/절차", "문제 해결"]},
        {"name": "탐정", "keywords": ["문제 해결", "몸을 움직임", "데이터"]}
    ]},
    "ESFP": {"name": "사교적인 유형", "emoji": "🥳", "careers": [
        {"name": "연예인", "keywords": ["사람들과 소통", "창의적", "몸을 움직임"]},
        {"name": "이벤트 기획자", "keywords": ["사람들과 소통", "창의적", "몸을 움직임", "규칙/절차"]},
        {"name": "승무원", "keywords": ["사람들과 소통", "규칙/절차", "안정적"]},
        {"name": "유치원 교사", "keywords": ["사람들과 소통", "사회봉사", "창의적"]}
    ]},
    "ENFP": {"name": "스파크형", "emoji": "✨", "careers": [
        {"name": "마케터", "keywords": ["사람들과 소통", "창의적", "아이디어", "데이터"]},
        {"name": "홍보 전문가", "keywords": ["사람들과 소통", "창의적", "아이디어"]},
        {"name": "강사", "keywords": ["사람들과 소통", "창의적", "아이디어"]},
        {"name": "크리에이터", "keywords": ["창의적", "아이디어", "혼자 집중", "몸을 움직임"]}
    ]},
    "ENTP": {"name": "발명가형", "emoji": "🧠", "careers": [
        {"name": "기업가", "keywords": ["아이디어", "문제 해결", "사람들과 소통", "몸을 움직임"]},
        {"name": "변호사", "keywords": ["문제 해결", "규칙/절차", "사람들과 소통", "데이터"]},
        {"name": "컨설턴트", "keywords": ["문제 해결", "데이터", "사람들과 소통", "아이디어"]},
        {"name": "발명가", "keywords": ["아이디어", "문제 해결", "혼자 집중", "규칙/절차"]}
    ]},
    "ESTJ": {"name": "사업가형", "emoji": "💼", "careers": [
        {"name": "경영자", "keywords": ["규칙/절차", "사람들과 소통", "문제 해결", "데이터"]},
        {"name": "관리자", "keywords": ["규칙/절차", "사람들과 소통", "문제 해결", "안정적"]},
        {"name": "군인", "keywords": ["규칙/절차", "몸을 움직임", "안정적"]},
        {"name": "판사", "keywords": ["규칙/절차", "문제 해결", "데이터", "혼자 집중"]}
    ]},
    "ESFJ": {"name": "친선도모형", "emoji": "🤝", "careers": [
        {"name": "교사", "keywords": ["사람들과 소통", "사회봉사", "규칙/절차", "안정적"]},
        {"name": "영업 관리자", "keywords": ["사람들과 소통", "문제 해결", "규칙/절차"]},
        {"name": "사회복지사", "keywords": ["사람들과 소통", "사회봉사", "문제 해결"]},
        {"name": "행정가", "keywords": ["규칙/절차", "사람들과 소통", "안정적"]}
    ]},
    "ENFJ": {"name": "언변능숙형", "emoji": "🗣️", "careers": [
        {"name": "정치인", "keywords": ["사람들과 소통", "아이디어", "문제 해결", "몸을 움직임"]},
        {"name": "외교관", "keywords": ["사람들과 소통", "규칙/절차", "데이터"]},
        {"name": "리더십 코치", "keywords": ["사람들과 소통", "문제 해결", "아이디어"]},
        {"name": "성직자", "keywords": ["사람들과 소통", "사회봉사", "아이디어"]}
    ]},
    "ENTJ": {"name": "지도자형", "emoji": "👑", "careers": [
        {"name": "최고 경영자 (CEO)", "keywords": ["문제 해결", "아이디어", "사람들과 소통", "데이터", "몸을 움직임"]},
        {"name": "프로젝트 매니저", "keywords": ["규칙/절차", "문제 해결", "사람들과 소통", "데이터"]},
        {"name": "전략 기획가", "keywords": ["아이디어", "문제 해결", "데이터", "혼자 집중"]},
        {"name": "컨설턴트", "keywords": ["문제 해결", "데이터", "사람들과 소통", "아이디어"]}
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
            if st.checkbox(option['text'], key=checkbox_key):
                selected_options_for_current_q.extend(option['keywords'])

        # '다음 질문' 버튼
        if st.button("다음 질문", key=f"next_q_button_{st.session_state.question_index}"):
            # 현재 질문에서 선택된 키워드들을 세션 상태에 추가
            st.session_state.selected_preferences.extend(selected_options_for_current_q)
            # 다음 질문으로 인덱스 이동
            st.session_state.question_index += 1
            st.rerun() # 페이지 새로고침하여 다음 질문 표시

    else: # 모든 질문 완료 후
        st.write("모든 질문에 답변하셨습니다! 결과를 바탕으로 추천 직업을 알려드릴게요. 👇")

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

        st.subheader("당신의 선호도를 바탕으로 추천하는 직업은... 👇")

        # 상위 1-2개 직업 추천 (선호도 점수가 0점 이상인 경우만)
        recommended_count = 0
        for career, score in sorted_careers:
            # 최소 1개 이상의 선호도 키워드가 일치하는 직업만 추천
            if score > 0 and recommended_count < 2:
                st.markdown(f"**{career}** 👍 (선호도 일치도: {score}개)")
                recommended_count += 1
            elif recommended_count >= 2:
                break # 2개 추천했으면 중단

        if recommended_count == 0:
            st.write("선택하신 선호도와 일치하는 추천 직업을 찾기 어렵습니다. 다른 선호도를 선택해 보세요! 🤔")

        st.markdown("---") # 구분선 추가
        # 다시 시작 버튼
        if st.button("다시 시작하기 🔄", key="restart_button"):
            st.session_state.question_index = 0
            st.session_state.selected_preferences = []
            st.session_state.mbti_selected = None # MBTI 선택도 초기화
            st.rerun() # 페이지 새로고침

st.markdown("""
---
**참고:** 이 추천은 참고용이며, 당신의 미래를 결정하는 절대적인 기준이 아닙니다.
다양한 경험을 통해 당신에게 가장 잘 맞는 길을 찾으시길 바랍니다! 응원합니다! 🎉
""")
