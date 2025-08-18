import streamlit as st

st.set_page_config(page_title="의료 교육 검색", page_icon="🩺", layout="centered")

st.title("🔍 신체 기관 & 현상 검색")
st.markdown("궁금한 신체 부위를 검색해보세요! 😊")

# 데이터 (간단 버전)
info = {
    "심장": ("💖 혈액을 온몸에 공급하는 펌프 역할을 하는 기관입니다.", 
            "https://cdn-icons-png.flaticon.com/512/4151/4151022.png"),
    "폐": ("🌬️ 산소와 이산화탄소 교환을 담당하는 호흡 기관입니다.", 
          "https://cdn-icons-png.flaticon.com/512/616/616408.png"),
    "뇌": ("🧠 신체와 정신 활동을 조절하는 중추 기관입니다.", 
          "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"),
    "소화": ("🍽️ 음식물을 분해해 영양분을 흡수하는 과정입니다.", 
            "https://cdn-icons-png.flaticon.com/512/1046/1046784.png"),
    "혈액순환": ("🩸 산소와 영양분을 세포에 전달하고 노폐물을 제거하는 과정입니다.", 
               "https://cdn-icons-png.flaticon.com/512/2966/2966486.png"),
}

# 검색창
query = st.text_input("궁금한 신체 기관을 입력하세요 (예: 심장, 뇌) 📝")

if query:
    if query in info:
        desc, img = info[query]
        st.image(img, width=150)
        st.success(desc)
    else:
        st.warning("❗ 해당 기관은 아직 등록되지 않았습니다.")

