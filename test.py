import streamlit as st
from PIL import Image

st.set_page_config(page_title="🧍 신체 모형 교육 앱", layout="centered")

st.title("🧍 신체 모형 교육용 웹 앱")
st.write("신체 모형의 특정 부위를 선택하면 설명을 볼 수 있습니다.")

# 이미지 업로드 기능
uploaded_file = st.file_uploader("신체 모형 이미지를 업로드하세요", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    body_img = Image.open(uploaded_file)
    st.image(body_img, use_column_width=True)
else:
    st.warning("⚠️ 신체 모형 이미지를 업로드해주세요!")

# 신체 기관 데이터 (예시)
organs = {
    "뇌 🧠": "뇌는 신체의 모든 활동을 조절하고 사고, 감정, 기억을 담당합니다.",
    "심장 ❤️": "심장은 혈액을 전신에 순환시키는 펌프 역할을 합니다.",
    "폐 🫁": "폐는 산소와 이산화탄소를 교환하는 호흡 기관입니다.",
    "간 🧬": "간은 해독, 단백질 합성, 에너지 저장 등 대사 작용을 담당합니다.",
    "신장 💧": "신장은 혈액 속 노폐물을 걸러내고 소변을 생성합니다.",
    "뼈 🦴": "뼈는 신체를 지지하고 내장을 보호하며 혈액 세포를 생성합니다."
}

selected = st.selectbox("궁금한 신체 부위를 선택하세요 👇", list(organs.keys()))
if selected:
    st.subheader(f"{selected} 설명")
    st.write(organs[selected])



