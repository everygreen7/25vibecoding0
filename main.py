import streamlit as st

# MBTI별 추천 직업 데이터 (예시)
# 실제 진로 교육에는 더 다양하고 전문적인 정보가 필요합니다.
mbti_careers = {
    "ISTJ": {"name": "세상의 소금형", "emoji": "🧂", "careers": ["회계사", "공무원", "은행원", "시스템 관리자"]},
    "ISFJ": {"name": "임금 뒷편의 권력형", "emoji": "🛡️", "careers": ["간호사", "사회복지사", "초등학교 교사", "사서"]},
    "INFJ": {"name": "예언자형", "emoji": "🔮", "careers": ["심리학자", "상담사", "작가", "예술가"]},
    "INTJ": {"name": "과학자형", "emoji": "🔬", "careers": ["연구원", "대학교수", "엔지니어", "건축가"]},
    "ISTP": {"name": "백과사전형", "emoji": "🛠️", "careers": ["기술자", "경찰관", "소방관", "파일럿"]},
    "ISFP": {"name": "성인군자형", "emoji": "🎨", "careers": ["디자이너", "음악가", "요리사", "수의사"]},
    "INFP": {"name": "잔 다르크형", "emoji": "🌟", "careers": ["시인", "소설가", "그래픽 디자이너", "편집자"]},
    "INTP": {"name": "아이디어 뱅크형", "emoji": "💡", "careers": ["프로그래머", "수학자", "철학자", "데이터 과학자"]},
    "ESTP": {"name": "활동가형", "emoji": "🏄", "careers": ["영업원", "사업가", "스포츠 선수", "탐정"]},
    "ESFP": {"name": "사교적인 유형", "emoji": "🥳", "careers": ["연예인", "이벤트 기획자", "승무원", "유치원 교사"]},
    "ENFP": {"name": "스파크형", "emoji": "✨", "careers": ["마케터", "홍보 전문가", "강사", "크리에이터"]},
    "ENTP": {"name": "발명가형", "emoji": "🧠", "careers": ["기업가", "변호사", "컨설턴트", "발명가"]},
    "ESTJ": {"name": "사업가형", "emoji": "💼", "careers": ["경영자", "관리자", "군인", "판사"]},
    "ESFJ": {"name": "친선도모형", "emoji": "🤝", "careers": ["교사", "영업 관리자", "사회복지사", "행정가"]},
    "ENFJ": {"name": "언변능숙형", "emoji": "🗣️", "careers": ["정치인", "외교관", "리더십 코치", "성직자"]},
    "ENTJ": {"name": "지도자형", "emoji": "👑", "careers": ["최고 경영자 (CEO)", "프로젝트 매니저", "전략 기획가", "컨설턴트"]}
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

# 선택된 MBTI에 따른 직업 추천 표시
if selected_mbti:
    mbti_info = mbti_careers[selected_mbti]
    st.subheader(f"선택하신 MBTI는 {selected_mbti} ({mbti_info['name']}) 입니다! {mbti_info['emoji']}")
    st.write("추천 직업 목록:")
    for career in mbti_info['careers']:
        st.markdown(f"- {career} ✨")

st.markdown("""
**참고:** 이 추천은 참고용이며, 당신의 미래를 결정하는 절대적인 기준이 아닙니다.
다양한 경험을 통해 당신에게 가장 잘 맞는 길을 찾으시길 바랍니다! 응원합니다! 🎉
""")
