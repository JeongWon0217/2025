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
# 앱 제목 + 탭 메뉴
# -------------------------------
st.title("⛑️ 응급처치 교육 앱")
tab1, tab2 = st.tabs(["📘 응급처치 방법", "📝 퀴즈 풀기"])

# -------------------------------
# 탭1: 응급처치 설명
# -------------------------------
with tab1:
    st.header("📘 응급처치 방법")
    choice = st.selectbox("궁금한 응급처치를 선택하세요", list(first_aid_info.keys()))
    st.subheader(choice)
    st.write(first_aid_info[choice])

# -------------------------------
# 탭2: 퀴즈
# -------------------------------
with tab2:
    st.header("📝 응급처치 퀴즈")

    # 세션 초기화
    if "quiz_list" not in st.session_state:
        st.session_state.quiz_list = random.sample(quiz_data, len(quiz_data))
        st.session_state.index = 0
        st.session_state.answered = False
        st.session_state.selected = None
        st.session_state.score = 0

    # 현재 문제
    if st.session_state.index < len(st.session_state.quiz_list):
        quiz = st.session_state.quiz_list[st.session_state.index]
        st.write(f"**❓ Q{st.session_state.index+1}. {quiz['question']}**")
        st.session_state.selected = st.radio("👉 답을 선택하세요:", quiz["options"])

        if st.button("✅ 정답 확인") and not st.session_state.answered:
            st.session_state.answered = True
            if st.session_state.selected == quiz["answer"]:
                st.success("🎉 정답입니다! 👍")
                st.session_state.score += 1
            else:
                st.error(f"❌ 오답입니다. 정답은 **{quiz['answer']}** 입니다.")

        if st.session_state.answered and st.button("➡️ 다음 문제"):
            st.session_state.index += 1
            st.session_state.answered = False
            st.session_state.selected = None

        # 진행률 표시
        st.progress((st.session_state.index) / len(st.session_state.quiz_list))

    else:
        st.success(f"🥳 모든 문제를 다 풀었습니다! 총 점수: **{st.session_state.score} / {len(st.session_state.quiz_list)}**")
        if st.button("🔄 다시 풀기"):
            st.session_state.clear()





