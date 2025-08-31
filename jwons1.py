import streamlit as st
import random

st.set_page_config(page_title="응급처치 앱", page_icon="⛑️")

# 세션 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = "방법"
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "questions" not in st.session_state:
    st.session_state.questions = [
        {"q": "심폐소생술 시 가슴압박의 깊이는?", "a": "약 5cm"},
        {"q": "화상 응급처치로 옳은 것은?", "a": "찬물로 식히기"},
        {"q": "기도가 막혔을 때 사용하는 방법은?", "a": "하임리히법"},
    ]
    random.shuffle(st.session_state.questions)

# 상단 탭
menu = st.radio("메뉴 선택", ["응급처치 방법 🩺", "퀴즈 ❓"], horizontal=True)

if menu == "응급처치 방법 🩺":
    st.subheader("응급처치 방법 모음")
    st.write("🚑 심폐소생술: 30회 압박 후 2회 인공호흡")
    st.write("🔥 화상: 흐르는 찬물로 10분 이상 식히기")
    st.write("😮‍💨 기도폐쇄: 하임리히법 실시")

elif menu == "퀴즈 ❓":
    q_idx = st.session_state.current_q
    if q_idx < len(st.session_state.questions):
        q = st.session_state.questions[q_idx]
        st.subheader(f"문제 {q_idx+1}: {q['q']}")
        answer = st.text_input("정답을 입력하세요:", key=f"answer_{q_idx}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("정답 확인"):
                if answer.strip() == q['a']:
                    st.success("정답입니다! 🎉")
                    st.session_state.score += 1
                else:
                    st.error(f"틀렸습니다. 정답은 {q['a']} 입니다.")

        with col2:
            if st.button("다음 문제로 ➡️"):
                # 버튼 클릭 시 즉시 다음 문제로 이동
                st.session_state.current_q += 1
                st.rerun()   # 👈 rerun으로 즉시 반영
    else:
        st.success(f"퀴즈 완료! 총점: {st.session_state.score}/{len(st.session_state.questions)}")
        if st.button("다시 풀기 🔄"):
            st.session_state.current_q = 0
            st.session_state.score = 0
            random.shuffle(st.session_state.questions)
            st.rerun()
