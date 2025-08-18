import streamlit as st

st.set_page_config(page_title="의료 교육 검색", page_icon="🩺", layout="centered")

st.title("🔍 신체 기관 & 현상 검색")
st.markdown("궁금한 신체 부위를 검색해보세요! 😊")

# 데이터 (신체 기관과 관련된 이모지 & 이미지 업데이트)
info = {
    "심장": ("❤️ 심장은 혈액을 온몸으로 보내는 중요한 펌프 역할을 합니다.", 
            "https://cdn-icons-png.flaticon.com/512/2913/2913464.png"),  # 심장 그림
    "폐": ("🫁 폐는 산소와 이산화탄소를 교환하는 호흡 기관입니다.", 
          "https://cdn-icons-png.flaticon.com/512/1995/1995565.png"),  # 폐 그림
    "뇌": ("🧠 뇌는 신체와 정신 활동을 조절하는 중추 기관입니다.", 
          "https://cdn-icons-png.flaticon.com/512/1995/1995530.png"),  # 뇌 그림
    "소화": ("🍏 소화 기관은 음식물을 분해하고 영양분을 흡수합니다.", 
            "https://cdn-icons-png.flaticon.com/512/1995/1995557.png"),  # 위 그림
    "혈액순환": ("🩸 혈액순환은 산소와 영양분을 세포에 전달하고 노폐물을 제거합니다.", 
               "https://cdn-icons-png.flaticon.com/512/616/616408.png"),  # 혈액 관련 그림
    "간": ("🫀 간은 해독과 영양소 저장 등 다양한 기능을 수행합니다.", 
           "https://cdn-icons-png.flaticon.com/512/1995/1995528.png"),  # 간 그림
    "신장": ("🫙 신장은 혈액을 걸러 소변을 생성하며 체내 수분과 전해질을 조절합니다.", 
            "https://cdn-icons-png.flaticon.com/512/1995/1995537.png"),  # 신장 그림
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

