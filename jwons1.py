import streamlit as st
import random

st.set_page_config(page_title="⛑️ 응급처치 학습", page_icon="⛑️", layout="centered")

# ---------------------------
# 세션 상태 초기화
# ---------------------------
if "page" not in st.session_state:
    st.session_state.page = "설명"
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "quiz_order" not in st.session_state:
    st.session_state.quiz_order = []

# ---------------------------
# 데이터
# ---------------------------
first_aid_info = {
    "심폐소생술": "🫀 의식과 호흡이 없는 환자에게 가슴압박과 인공호흡을 시행하는 방법입니다.",
    "기도 폐쇄": "🍎 음식물 등으로 기도가 막혔을 때 하임리히법 등을 이용해 기도를 확보합니다.",
    "출혈": "🩸 출혈 부위에 압박을 가해 지혈하고 필요시 압박 붕대를 사용합니다.",
    "화상": "🔥 화상 부위를 흐르는 물에 10분 이상 식히고 물집은 터뜨리지 않습니다.",
    "골절": "🦴 골절 부위를 움직이지 않게 고정하고 병원으로 이송합니다."
}

quiz_data = [
    {
        "question": "심폐소생술에서 가슴압박과 인공호흡의 비율은?",
        "options": ["15:2", "30:2", "10:1", "50:5"],
        "answer": "30:2"
    },
    {
        "question": "기도가 막혔을 때 사용하는 응급처치법은?",
        "options": ["하임리히법", "심폐소생술", "지혈법", "골절 고정"],
        "answer": "하임리히법"
    },
    {
        "question": "심한 출혈이 있을 때 가장 먼저 해야 할 응급처치는?",
        "options": ["심폐소생술", "압박 지혈", "하임리히법", "물 붓기"],
        "answer": "압박 지혈"
    },
    {
        "question": "화상을 입었을 때 올바른 응급처치는?",
        "options": ["흐르는 물에 10분 이상 식히기", "물집을 터뜨리기", "소독약 바르기", "붕대로 감기"],
        "answer": "흐르는 물에 10분 이상 식히기"
    },
    {
        "question": "골절이 의심될 때 가장 중요한 응급처치는?",
        "options": ["부목으로 고정", "심폐소생술", "냉찜질만 하기", "운동시키기"],
        "answer": "부목으로 고정"
    }
]

# ---------------------------
# 사이드 메뉴
# ---------------------------
st.title("⛑️ 응급처치 학습 앱")

page = st.radio("메뉴 선택", ["설명", "퀴즈"], horizontal=True, index=0)
st.session_state.page = page

# ---------------------------
# 설명 페이지
# ---------------------------
if st.session_state.page == "설명":
    st.subheader("📖 응급처치 방법")
    for k, v in first_aid_info.items():
        st.write(f"**{k}**: {v}")

# ---------------------------
# 퀴즈 페이지
# ---------------------------
elif st.session_state.page == "퀴즈":
    # 문제 순서 섞기 (처음 들어올 때만)
    if not st.session_state.quiz_order:
        st.session_state.quiz_order = random.sample(range(len(quiz_data)), len(quiz_data))

    current_index = st.session_state.current_q
    if current_index < len(quiz_data):
        q = quiz_data[st.session_state.quiz_order[current_index]]

        st.subheader(f"Q{current_index+1}. {q['question']}")
        selected = st.radio("정답을 고르세요:", q["options"], key=f"q_{current_index}")

        if st.button("✅ 답 확인"):
            if selected == q["answer"]:
                st.success("정답입니다! 🎉")
                st.session_state.score += 1
            else:
                st.error(f"틀렸습니다. 정답은 '{q['answer']}' 입니다.")

            # 👉 여기서 바로 다음 문제로 넘어감
            st.session_state.current_q += 1
            st.experimental_rerun()

    else:
        st.success(f"퀴즈 완료! 최종 점수: {st.session_state.score} / {len(quiz_data)}")
        if st.button("🔄 다시 풀기"):
            st.session_state.current_q = 0
            st.session_state.score = 0
            st.session_state.quiz_order = []
            st.experimental_rerun()
