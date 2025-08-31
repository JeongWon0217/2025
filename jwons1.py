import streamlit as st
import random

st.set_page_config(page_title="🚑 응급처치 학습", layout="centered")

# --- 세션 상태 초기화 ---
if "page" not in st.session_state:
    st.session_state.page = "응급처치 방법"
if "quiz_index" not in st.session_state:
    st.session_state.quiz_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False

# --- 퀴즈 데이터 ---
quizzes = [
    {"q": "심폐소생술(CPR) 시 가슴 압박의 깊이는?", "a": ["약 2cm", "약 5cm", "약 10cm"], "correct": 1},
    {"q": "코피가 날 때 올바른 응급처치는?", "a": ["머리를 뒤로 젖힌다", "머리를 앞으로 숙이고 콧등을 누른다", "찬물로 얼굴을 씻는다"], "correct": 1},
    {"q": "화상 응급처치 첫 단계는?", "a": ["연고 바르기", "흐르는 차가운 물로 식히기", "붕대로 감싸기"], "correct": 1},
]

# --- 사이드 메뉴 ---
st.title("🚨 응급처치 학습 앱")
menu = st.radio("메뉴를 선택하세요:", ["응급처치 방법", "퀴즈 풀기"], horizontal=True)

# --- 응급처치 방법 ---
if menu == "응급처치 방법":
    st.header("🩹 기본 응급처치 방법")
    st.write("1. 코피: 머리를 앞으로 숙이고 콧등을 10분간 압박합니다.")
    st.write("2. 화상: 흐르는 찬물로 10분 이상 식힙니다.")
    st.write("3. 기도 폐쇄: 하임리히법을 실시합니다.")
    st.write("4. 심정지: 119 신고 후 심폐소생술(CPR)을 시작합니다.")

# --- 퀴즈 풀기 ---
elif menu == "퀴즈 풀기":
    st.header("📝 응급처치 퀴즈")

    # 현재 문제 가져오기
    quiz = quizzes[st.session_state.quiz_index]

    # 문제 출력
    st.subheader(quiz["q"])
    choice = st.radio("정답을 고르세요:", quiz["a"], key=f"choice_{st.session_state.quiz_index}")

    # 정답 확인
    if st.button("정답 확인"):
        if not st.session_state.answered:
            if quiz["a"].index(choice) == quiz["correct"]:
                st.success("정답입니다! ✅")
                st.session_state.score += 1
            else:
                st.error(f"틀렸습니다 ❌ 정답은 '{quiz['a'][quiz['correct']]}' 입니다.")
            st.session_state.answered = True

    # 다음 문제
    if st.session_state.answered:
        if st.button("다음 문제"):
            if st.session_state.quiz_index < len(quizzes) - 1:
                st.session_state.quiz_index += 1
                st.session_state.answered = False
            else:
                st.write(f"🎉 퀴즈 완료! 총 점수: {st.session_state.score}/{len(quizzes)}")

