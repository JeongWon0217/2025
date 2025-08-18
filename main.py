import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🎨", layout="wide")

# CSS 스타일
st.markdown("""
    <style>
    .main-title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #FF6F61;
        margin-bottom: 30px;
    }
    .job-card {
        background-color: #fff5f5;
        border-radius: 20px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.15);
        text-align: center;
        font-size: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# MBTI별 직업 데이터 + 이미지 + 이모티콘
mbti_jobs = {
    "INTJ": {
        "jobs": ["🔬 과학자", "🧠 전략가", "📊 데이터 분석가"],
        "img": "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
    },
    "ENTP": {
        "jobs": ["🚀 기업가", "📢 마케터", "💼 컨설턴트"],
        "img": "https://cdn-icons-png.flaticon.com/512/3135/3135768.png"
    },
    "INFJ": {
        "jobs": ["💬 상담가", "✍️ 작가", "🧑‍⚕️ 심리학자"],
        "img": "https://cdn-icons-png.flaticon.com/512/2922/2922566.png"
    },
    "ESFP": {
        "jobs": ["🎭 배우", "🎉 이벤트 기획자", "👩‍🏫 교사"],
        "img": "https://cdn-icons-png.flaticon.com/512/2922/2922510.png"
    },
    "ISTJ": {
        "jobs": ["📑 회계사", "⚙️ 엔지니어", "📋 관리자"],
        "img": "https://cdn-icons-png.flaticon.com/512/2922/2922719.png"
    },
    "ENFP": {
        "jobs": ["🎨 광고 기획자", "🎨 디자이너", "📰 기자"],
        "img": "https://cdn-icons-png.flaticon.com/512/2922/2922656.png"
    },
}

# 제목
st.markdown("<div class='main-title'>🌟 MBTI 기반 진로 추천 🌟</div>", unsafe_allow_html=True)

# MBTI 선택
selected_mbti = st.selectbox("👉 당신의 MBTI를 선택하세요:", list(mbti_jobs.keys()))

# 결과 출력
if selected_mbti:
    col1, col2 = st.


