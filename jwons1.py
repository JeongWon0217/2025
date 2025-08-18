import streamlit as st

st.set_page_config(page_title="의학 교육용 사이트", page_icon="🩺", layout="wide")

st.title("🩺 신체 기관과 현상 교육 사이트 🌟")
st.markdown("궁금한 신체 기관이나 현상을 선택하면 설명과 이미지를 제공합니다!")

# 선택 박스
organ = st.selectbox(
    "알고 싶은 신체 기관/현상을 선택하세요 🔍",
    ["심장 ❤️", "폐 🫁", "뇌 🧠", "소화기관 🍽️", "혈액순환 💉"]
)

info = {
    "심장 ❤️": ("심장은 혈액을 전신에 공급하는 펌프 역할을 합니다.", 
                "https://cdn-icons-png.flaticon.com/512/616/616493.png"),
    "폐 🫁": ("폐는 산소를 들이마시고 이산화탄소를 내보내는 호흡 기관입니다.", 
             "https://cdn-icons-png.flaticon.com/512/616/616408.png"),
    "뇌 🧠": ("뇌는 신체의 모든 활동을 조절하고 사고와 감정을 담당합니다.", 
             "https://cdn-icons-png.flaticon.com/512/616/616430.png"),
    "소화기관 🍽️": ("소화기관은 음식물을 분해해 영양분을 흡수합니다.", 
                 "https://cdn-icons-png.flaticon.com/512/1046/1046786.png"),
    "혈액순환 💉": ("혈액순환은 산소와 영양분을 세포에 전달합니다.", 
                 "https://cdn-icons-png.flaticon.com/512/1046/1046857.png"),
}

desc, img = info[organ]
st.image(img, width=200)
st.info(desc)
