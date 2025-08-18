import streamlit as st

# MBTI별 추천 직업 데이터 (예시)
mbti_jobs = {
    "INTJ": ["과학자", "전략가", "데이터 분석가"],
    "ENTP": ["기업가", "마케터", "컨설턴트"],
    "INFJ": ["상담가", "작가", "심리학자"],
    "ESFP": ["배우", "이벤트 기획자", "교사"],
    "ISTJ": ["회계사", "엔지니어", "관리자"],
    "ENFP": ["광고 기획자", "디자이너", "기자"],
    # 필요한 만큼 추가
}

st.title("MBTI 기반 직업 추천 웹 앱 🎯")

# MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_jobs.keys()))

# 결과 출력
if selected_mbti:
    st.subheader(f"{selected_mbti} 유형에게 추천하는 직업은:")
    for job in mbti_jobs[selected_mbti]:
        st.write(f"- {job}")

