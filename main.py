import streamlit as st

# -------------------- 기본 설정 --------------------
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🌈", layout="wide")

# -------------------- 스타일 --------------------
st.markdown("""
<style>
/* 전체 배경 그라데이션 */
.stApp {
  background: linear-gradient(135deg, #fef7ff 0%, #e7f0ff 50%, #f0fff9 100%);
}

/* 타이틀 */
.hero {
  text-align:center; padding:16px 0 6px 0;
  font-size:42px; font-weight:800; letter-spacing:-0.5px;
}
.subtitle {
  text-align:center; margin-top:-8px; color:#5b5b5b;
}

/* 칩(키워드) */
.chip {
  display:inline-block; padding:6px 12px; margin:6px 6px 0 0;
  border-radius:999px; background:#ffffffaa; backdrop-filter: blur(6px);
  font-size:14px; border:1px solid #e6e6e6;
}

/* 카드 */
.card {
  background:#ffffffdd; border-radius:18px; padding:14px; margin:10px 0 24px;
  box-shadow: 0 8px 28px rgba(0,0,0,0.07);
  border-top:6px solid VAR_COLOR;
}
.card h4 { margin:8px 0 6px; font-size:20px }
.card p { margin:0; color:#444; font-size:15px }

/* 섹션 제목 */
.section-title {
  font-size:24px; font-weight:800; margin:6px 0 12px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- 데이터 --------------------
# 이미지들은 Unsplash 랜덤 소스(무료, 키워드 기반) 사용
mbti_data = {
    "INTJ": {
        "color": "#6C63FF",
        "desc": "🧭 장기전략과 구조화에 강한 분석가 타입",
        "banner": "https://source.unsplash.com/1200x360/?technology,galaxy,code",
        "keywords": ["전략", "분석", "자율", "문제해결", "연구"],
        "jobs": [
            {"name": "🔬 과학자", "img": "https://source.unsplash.com/600x420/?laboratory,science", "blurb": "가설을 세우고 실험·분석으로 검증하는 연구직."},
            {"name": "🧠 전략기획자", "img": "https://source.unsplash.com/600x420/?strategy,planning", "blurb": "시장·데이터 기반으로 회사의 중장기 방향 제시."},
            {"name": "📊 데이터 분석가", "img": "https://source.unsplash.com/600x420/?data,analytics", "blurb": "데이터로 인사이트 도출·의사결정 지원."},
        ],
    },
    "ENTP": {
        "color": "#FF7A59",
        "desc": "🚀 아이디어 폭발, 토론과 실험을 즐기는 발명가",
        "banner": "https://source.unsplash.com/1200x360/?startup,neon,innovation",
        "keywords": ["창의", "도전", "네트워킹", "사업화", "피봇"],
        "jobs": [
            {"name": "🚀 창업가", "img": "https://source.unsplash.com/600x420/?entrepreneur,startup", "blurb": "문제를 기회로 바꿔 비즈니스로 구현."},
            {"name": "📢 마케터", "img": "https://source.unsplash.com/600x420/?marketing,brand", "blurb": "브랜드 전략·캠페인으로 성장 견인."},
            {"name": "💼 컨설턴트", "img": "https://source.unsplash.com/600x420/?consulting,meeting", "blurb": "다양한 산업 문제 해결·성과 혁신."},
        ],
    },
    "INFJ": {
        "color": "#00BFA6",
        "desc": "💫 가치지향, 깊이 있는 통찰로 사람을 돕는 조언자",
        "banner": "https://source.unsplash.com/1200x360/?calm,forest,mentor",
        "keywords": ["공감", "의미", "상담", "글쓰기", "교육"],
        "jobs": [
            {"name": "💬 상담가", "img": "https://source.unsplash.com/600x420/?counseling,therapy", "blurb": "정서·진로·관계의 변화를 돕는 전문 지원."},
            {"name": "✍️ 작가", "img": "https://source.unsplash.com/600x420/?writer,notebook", "blurb": "가치를 언어로 설계해 독자와 연결."},
            {"name": "🧑‍⚕️ 심리전문가", "img": "https://source.unsplash.com/600x420/?psychology,brain", "blurb": "심리 평가·개입을 통한 회복 지원."},
        ],
    },
    "ESFP": {
        "color": "#FFB300",
        "desc": "🎉 사람 중심, 현장에서 빛나는 엔터테이너",
        "banner": "https://source.unsplash.com/1200x360/?festival,event,stage",
        "keywords": ["현장감", "팀워크", "서비스", "표현", "에너지"],
        "jobs": [
            {"name": "🎭 배우/공연가", "img": "https://source.unsplash.com/600x420/?theater,stage", "blurb": "무대에서 감정·메시지를 표현."},
            {"name": "🎪 이벤트 기획", "img": "https://source.unsplash.com/600x420/?event,conference", "blurb": "행사 운영·관객 경험 설계."},
            {"name": "👩‍🏫 교사", "img": "https://source.unsplash.com/600x420/?teacher,classroom", "blurb": "현장 상호작용으로 학습 동기 촉진."},
        ],
    },
    "ISTJ": {
        "color": "#2D9CDB",
        "desc": "🧱 신뢰·정확, 체계로 성과를 만드는 관리자",
        "banner": "https://source.unsplash.com/1200x360/?office,structure",
        "keywords": ["정확성", "책임감", "규정", "안정", "실행력"],
        "jobs": [
            {"name": "📑 회계사", "img": "https://source.unsplash.com/600x420/?accounting,finance", "blurb": "재무·감사로 조직의 신뢰성 보증."},
            {"name": "⚙️ 엔지니어", "img": "https://source.unsplash.com/600x420/?engineering,mechanical", "blurb": "표준·안전·품질을 지키는 기술 구현."},
            {"name": "📋 운영관리자", "img": "https://source.unsplash.com/600x420/?operations,logistics", "blurb": "프로세스 최적화·리스크 관리."},
        ],
    },
    "ENFP": {
        "color": "#EF476F",
        "desc": "🌈 상상력과 사람 사랑으로 변화를 이끄는 촉진자",
        "banner": "https://source.unsplash.com/1200x360/?colors,creative,smile",
        "keywords": ["영감", "스토리", "네트워킹", "학습민첩성", "기획"],
        "jobs": [
            {"name": "🎨 크리에이티브 디렉터", "img": "https://source.unsplash.com/600x420/?creative,design", "blurb": "아이디어를 캠페인·콘텐츠로 연결."},
            {"name": "📰 기자/에디터", "img": "https://source.unsplash.com/600x420/?journalism,newsroom", "blurb": "현장의 이야기를 세상에 전파."},
            {"name": "🤝 커뮤니티 매니저", "img": "https://source.unsplash.com/600x420/?community,people", "blurb": "사람·브랜드·가치를 연결해 성장."},
        ],
    },
}

# -------------------- UI --------------------
st.markdown("<div class='hero'>🌟 MBTI 기반 진로 추천 🌟</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>이모지 + 사진 가득! 나에게 맞는 진로를 한눈에 찾아보세요 👀</div>", unsafe_allow_html=True)
st.write("")

# 사이드바: MBTI 선택
st.sidebar.header("🧩 MBTI 선택")
selected = st.sidebar.selectbox("당신의 MBTI는?", list(mbti_data.keys()), index=0)
data = mbti_data[selected]
accent = data["color"]

# 상단 배너
st.image(data["banner"], use_column_width=True, caption=f"{selected} | {data['desc']}")

# 키워드 칩
st.markdown(f"<div class='section-title'>🔎 {selected} 핵심 키워드</div>", unsafe_allow_html=True)
st.markdown("".join([f"<span class='chip'>{k}</span>" for k in data["keywords"]]), unsafe_allow_html=True)

# 추천 직업 그리드
st.markdown(f"<div class='section-title'>💼 추천 직업</div>", unsafe_allow_html=True)
cols = st.columns(3)
for i, job in enumerate(data["jobs"]):
    with cols[i % 3]:
        # 카드 상단 색상 커스터마이즈
        card_html = f"""
        <div class='card' style='border-top-color:{accent};'>
            <h4>{job['name']}</h4>
            <p>{job['blurb']}</p>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
        st.image(job["img"], use_column_width=True)

# 추가 섹션: 갤러리 & 학과 추천
tab1, tab2 = st.tabs(["🖼️ 직업 사진 모음", "🎓 관련 학과/역량 팁"])

with tab1:
    gcols = st.columns(3)
    for i, job in enumerate(data["jobs"]):
        with gcols[i % 3]:
            st.image(job["img"], use_column_width=True, caption=job["name"])

with tab2:
    st.markdown(f"**{selected}** 유형에게 특히 잘 맞는 공부/역량 팁입니다 ✨")
    if selected in ["INTJ", "ISTJ"]:
        st.markdown("- 📐 논리·수리 훈련(수학, 통계, 알고리즘)\n- 📚 문서화·표준/품질 관리 도구 익히기\n- 🧪 프로젝트에서 가설→실험→검증 사이클 연습")
    elif selected in ["ENTP", "ENFP"]:
        st.markdown("- 🗣️ 스토리텔링·프레젠테이션\n- 📈 시장·사용자 리서치, 그로스 실험\n- 🤝 네트워킹·커뮤니티 운영 경험")
    elif selected == "INFJ":
        st.markdown("- 🧩 상담·코칭 기초 이론\n- ✍️ 글쓰기·콘텐츠 기획\n- 🫶 공감·윤리·다문화 감수성")
    elif selected == "ESFP":
        st.markdown("- 🎙️ 퍼포먼스·스피치 훈련\n- 📅 행사 운영·CS 실습\n- 👥 팀 프로젝트 리더십")
    st.info("팁: 학교 활동/동아리/대회 기록을 **직무 키워드**(예: 문제해결, 데이터분석, 스토리텔링)로 정리하면 학생부·포트폴리오에 좋아요.")

st.caption("⚠️ MBTI는 참고 지표일 뿐, 진로 결정의 유일한 기준이 아닙니다. 흥미·경험과 함께 종합적으로 고려하세요.")


