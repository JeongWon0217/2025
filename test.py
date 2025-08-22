import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="응급처치 학습 앱", page_icon="🩺", layout="centered")

st.title("🚑 응급처치 학습 앱")
st.markdown("응급 상황 대처법을 배우고, 그림과 퀴즈로 학습 효과를 확인하세요!")

# --------------------------
# 메뉴 선택
# --------------------------
menu = st.sidebar.radio("메뉴 선택", ["응급처치 가이드", "퀴즈 모드"])

# --------------------------
# 그림 불러오기 (예시: images 폴더)
# --------------------------
def load_image(file_name):
    path = os.path.join("images", file_name)
    if os.path.exists(path):
        return Image.open(path)
    else:
        return None

# --------------------------
# 응급처치 가이드 데이터
# --------------------------
procedures = {
    "화상": [
        "즉시 화상 부위를 차가운 흐르는 물에 10~15분 이상 식힌다.",
        "물집은 터뜨리지 않는다.",
        "깨끗한 거즈로 부위를 덮는다.",
        "연고, 기름, 소독약은 바르지 않는다.",
        "심한 화상은 119에 신고한다."
    ],
    "기도폐쇄(성인)": [
        "기침을 유도한다.",
        "기침 불가 시 하임리히법(복부 밀어 올리기) 시행",
        "의식 없으면 심폐소생술(CPR) 진행"
    ],
    "심정지": [
        "반응과 호흡 확인",
        "즉시 119 신고 및 AED 요청",
        "가슴 압박 30회 + 인공호흡 2회 반복 (30:2 비율)",
        "AED 도착 시 즉시 사용"
    ],
    "출혈": [
        "출혈 부위를 압박한다",
        "심하면 지혈대 사용",
        "환자를 안정시키고 병원으로 이송"
    ],
    "골절": [
        "부러진 부위를 움직이지 않게 고정",
        "부목 등으로 관절 위아래까지 고정",
        "출혈이 있으면 지혈 우선",
        "병원으로 신속히 이송"
    ]
}

procedure_images = {
    "화상": "burn.png",
    "기도폐쇄(성인)": "heimlich.png",
    "심정지": "cpr.png",
    "출혈": "bleeding.png",
    "골절": "fracture.png"
}

# --------------------------
# 퀴즈 데이터
# --------------------------
quiz_data = [
    {
        "question": "화상 응급처치 시 가장 먼저 해야 할 일은?",
        "options": ["연고 바르기", "차가운 물로 식히기", "물집 터뜨리기"],
        "answer": "차가운 물로 식히기"
    },
    {
        "question": "성인 기도폐쇄 시 시행하는 방법은?",
        "options": ["등 두드리기", "하임리히법", "가슴압박"],
        "answer": "하임리히법"
    },
    {
        "question": "심정지 환자에게 가슴 압박은 분당 몇 회가 적절한가?",
        "options": ["40~60회", "80~100회", "100~120회"],
        "answer": "100~120회"
    }
]

# --------------------------
# 응급처치 가이드
# --------------------------
if menu == "응급처치 가이드":
    st.header("📝 상황별 응급처치 단계")
    situation = st.selectbox("상황을 선택하세요", list(procedures.keys()))
    
    img = load_image(procedure_images.get(situation, ""))
    if img:
        st.image(img, use_column_width=True)
    
    st.subheader(f"🚨 {situation} 응급처치 절차")
    for i, step in enumerate(procedures[situation], 1):
        st.write(f"{i}. {step}")

# --------------------------
# 퀴즈 모드
# --------------------------
elif menu == "퀴즈 모드":
    st.header("❓ 응급처치 퀴즈")

    # 세션 상태 초기화
    if "q_num" not in st.session_state:
        st.session_state.q_num = 0
        st.session_state.score = 0
        st.session_state.completed = False

    if not st.session_state.completed:
        q = quiz_data[st.session_state.q_num]
        st.subheader(f"문제 {st.session_state.q_num + 1}: {q['question']}")
        user_answer = st.radio("정답을 선택하세요", q["options"], key=f"q_{st.session_state.q_num}")

        if st.button("정답 확인"):
            if user_answer == q["answer"]:
                st.success("✅ 정답입니다!")
                st.session_state.score += 1
            else:
                st.error(f"❌ 오답입니다. 정답은 '{q['answer']}' 입니다.")

            # 다음 문제
            if st.session_state.q_num < len(quiz_data) - 1:
                st.session_state.q_num += 1
            else:
                st.session_state.completed = True

    else:
        st.info(f"퀴즈 종료! 총 {len(quiz_data)}문제 중 {st.session_state.score}개 맞았습니다.")
        if st.button("다시 시작"):
            st.session_state.q_num = 0
            st.session_state.score = 0
            st.session_state.completed = False


