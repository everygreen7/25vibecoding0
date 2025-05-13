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

# 웹 앱 타이틀 설정
st.set_page_config(page_title="MBTI 기반 직업 추천 🚀", page_icon="👍")
st.title("나에게 맞는 직업은 무엇일까? 🤔")

st.markdown("""
안녕하세요! 당신의 MBTI 유형을 선택하시면, 해당 유형에게 어울릴 만한 직업들을 추천해 드립니다.
이 추천은 일반적인 경향이며, 개인의 흥미와 강점에 따라 얼마든지 달라질 수 있습니다. 😊
""")

# MBTI 선택 드롭다운
mbti_options = list(mbti_careers.keys())
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", mbti_options)

# 선택된 MBTI에 따른 직업 추천 표시 및 후속 질문
if selected_mbti:
    mbti_info = mbti_careers[selected_mbti]
    st.subheader(f"선택하신 MBTI는 {selected_mbti} ({mbti_info['name']}) 입니다! {mbti_info['emoji']}")

    st.write("이 MBTI 유형에게 일반적으로 추천되는 직업 목록입니다:")
    for career_info in mbti_info['careers']:
        st.markdown(f"- {career_info['name']} ✨")

    st.markdown("---") # 구분선 추가

    st.subheader("조금 더 자세히 알아볼까요? 🤔")
    st.write("아래 항목들 중 당신의 흥미나 선호에 해당하는 것을 모두 선택해주세요.")

    # 후속 질문 (선호도 체크박스)
    # 각 체크박스의 key를 고유하게 설정하여 오류 방지
    pref_people = st.checkbox("사람들과 소통하고 돕는 일 🤝", key="pref_people")
    pref_data = st.checkbox("데이터를 분석하고 활용하는 일 📊", key="pref_data")
    pref_creative = st.checkbox("새롭고 창의적인 아이디어를 내는 일 💡", key="pref_creative")
    pref_rules = st.checkbox("규칙과 절차에 따라 안정적으로 일하는 것 📝", key="pref_rules")
    pref_active = st.checkbox("몸을 움직이며 활동적으로 일하는 것 💪", key="pref_active")
    pref_problem = st.checkbox("문제를 파악하고 해결하는 일 🔧", key="pref_problem")
    pref_alone = st.checkbox("혼자 집중하여 깊이 파고드는 일 🤫", key="pref_alone") # 혼자 집중 추가
    pref_idea = st.checkbox("추상적이거나 이론적인 아이디어를 다루는 일 ✨", key="pref_idea") # 아이디어 추가


    # 선택된 선호도에 따라 직업 추천 필터링
    selected_preferences = []
    if pref_people: selected_preferences.append("사람들과 소통")
    if pref_data: selected_preferences.append("데이터")
    if pref_creative: selected_preferences.append("창의적")
    if pref_rules: selected_preferences.append("규칙/절차")
    if pref_active: selected_preferences.append("몸을 움직임")
    if pref_problem: selected_preferences.append("문제 해결")
    if pref_alone: selected_preferences.append("혼자 집중")
    if pref_idea: selected_preferences.append("아이디어")


    # 선택된 선호도와 직업 키워드를 매칭하여 점수 계산
    career_scores = {}
    for career_info in mbti_info['careers']:
        score = 0
        for keyword in career_info['keywords']:
            if keyword in selected_preferences:
                score += 1
        career_scores[career_info['name']] = score

    # 점수가 높은 순서대로 정렬
    sorted_careers = sorted(career_scores.items(), key=lambda item: item[1], reverse=True)

    st.markdown("---") # 구분선 추가

    st.subheader("당신의 선호도를 바탕으로 추천하는 직업은... 👇")

    # 상위 1-2개 직업 추천 (선호도 점수가 0점 이상인 경우만)
    recommended_count = 0
    for career, score in sorted_careers:
        if score > 0 and recommended_count < 2:
            st.markdown(f"**{career}** 👍 (선호도 일치도: {score}개)")
            recommended_count += 1
        elif recommended_count >= 2:
            break # 2개 추천했으면 중단

    if recommended_count == 0:
        st.write("선택하신 선호도와 일치하는 추천 직업을 찾기 어렵습니다. 다른 선호도를 선택해 보세요! 🤔")


st.markdown("""
---
**참고:** 이 추천은 참고용이며, 당신의 미래를 결정하는 절대적인 기준이 아닙니다.
다양한 경험을 통해 당신에게 가장 잘 맞는 길을 찾으시길 바랍니다! 응원합니다! 🎉
""")
