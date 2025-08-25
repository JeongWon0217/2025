import streamlit as st
import random

st.set_page_config(page_title="응급처치 교육 앱", page_icon="⛑️", layout="centered")

# -------------------------------
# 데이터 정의
# -------------------------------
first_aid_info = {
    "💓 심폐소생술(CPR)": "심장이 멈춘 환자에게 가슴 압박과 인공호흡을 시행하여 생명을 유지하는 응급처치 방법입니다.",
    "🫁 기도폐쇄(하임리히법)": "이물질로 기도가 막혔을 때 배를 압박하여 기도를 확보하는 방법입니다.",
    "🔥 화상 응급처치": "화상을 입은 부위는 흐르는 찬물에 10~15분 이상 식혀주고, 물집은 터뜨리지 않습니다.",
    "🩸 출혈 응급처치": "출혈 부위를 직접 압박하여 지혈하고, 가능하다면 환부를 심장보다 높게 올립니다.",
    "🦴 골절 응급처치": "골절 부위는 움직이지 않도록 고정하고, 부목 등을 사용하여 추가 손상을 방지합니다."
}

quiz_data = [
    {
        "question": "심장이 멈췄을 때 시행하는 응급처치는?",
        "options": ["기도폐쇄 처치 🫁", "심폐소생술 💓", "지혈법 🩸", "화상처치 🔥", "골절 고정 🦴"],
        "answer": "심폐소생술 💓"
    },
    {
        "question": "기도폐쇄 환자에게 가장 적절한 응급처치는?",
        "options": ["심폐소생술 💓", "출혈 지혈 🩸", "하임리히법 🫁", "골절 부목 🦴", "화상 냉각 🔥"],
        "answer": "하임리히법 🫁"
    },
    {
        "question": "화상을 입었을 때 올바른 응급처치는?",
        "options": ["바로 연고 바르기", "흐르는 찬물로 냉각 🔥", "물집 터뜨리기", "붕대로 압박", "불에 탄 부위 문지르기"],
        "answer": "흐르는 찬물로 냉각 🔥"
    },
    {
        "question": "출혈 환자에게 가장 먼저 시행해야 할 처치는?",
        "options": ["심폐소생술 💓", "하임리히법 🫁", "지혈을 위한 직접 압박 🩸", "골절 부목 고정 🦴", "화상 냉각 🔥"],
        "answer": "지혈을 위한 직접 압박 🩸"
    },
    {
        "question": "뼈가 부러졌을 때 올바른 응급처치는?",
        "options": ["움직이지 않도록 고정 🦴", "냉찜질만 하기", "심폐소생술 💓", "지혈 압박 🩸", "기도 확보 🫁"],
        "answer": "움직이지 않도록 고정 🦴"
    }
]

# -------------------------------
# 사이드바 메뉴
# -------------------------------
st.sidebar.title("⛑️ 응급처치 교육")
menu = st.sidebar.radio("📌 메뉴 선택", ["🏠 소개", "📘 응급처치 설명", "📝 퀴즈 풀기"])

# -------------------------------
# 소개 페이지
# -------------------------------
if menu == "🏠 소개":
    st.title("⛑️ 응급처치 교육 앱")
    st.markdown("""
    🚑 이 앱은 응급상황에서 필요한 **응급처치 방법**을 배우고,  
    ✍️ 간단한 **퀴즈**를 통해 복습할 수 있도록 제작되었습니다.  
    """)

# -------------------------------
# 설명 페이지
# -------------------------------
elif menu == "📘 응급처치 설명":
    st.title("📘 응급처치 설명")
    choice = st.selectbox("궁금한 응급처치를 선택하세요", list(first_aid_info.keys()))
    st.subheader(choice)
    st.write(first_aid_info[choice])

# -------------------------------
# 퀴즈 페이지
# -------------------------------
elif menu == "📝 퀴즈 풀기":
    st.title("📝 응급처치 퀴즈")

    # 랜덤 문제 하나 선택
    if "quiz" not in st.session_state:
        st.session_state.quiz = random.choice(quiz_data)
        st.session_state.selected = None
        st.session_state.answered = False

    quiz = st.session_state.quiz

    st.write(f"**❓ Q. {quiz['question']}**")
    st.session_state.selected = st.radio("👉 답을 선택하세요:", quiz["options"])

    if st.button("✅ 정답 확인"):
        st.session_state.answered = True

    if st.session_state.answered:
        if st.session_state.selected == quiz["answer"]:
            st.success("🎉 정답입니다! 👍")
        else:
            st.error(f"❌ 오답입니다. 정답은 **{quiz['answer']}** 입니다.")

        if st.button("➡️ 다음 문제"):
            st.session_state.quiz = random.choice(quiz_data)
            st.session_state.selected = None
            st.session_state.answered = False



