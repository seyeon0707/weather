import streamlit as st

# 페이지 기본 설정 (브라우저 탭 이름과 아이콘)
st.set_page_config(page_title="맞춤형 코디 가이드 앱", page_icon="🧥", layout="centered")

# [필수 조건 1: 함수(def) 사용]
def get_outfit_guide(temp):
    # [필수 조건 2: 선택구조(if-elif-else) & 리스트(list) 사용]
    if -20 <= temp <= 0:
        warmth_index = "따뜻지수 [1] ❄️"
        clothes = ["🧥 포근한 롱패딩", "👖 따뜻한 기모바지", "👢 푹신한 어그"]
        extra_msg = "추운 날씨이므로 감기에 걸리지않게 따뜻하게 입는게 중요하겠습니다."
       
    elif 1 <= temp <= 13:
        warmth_index = "따뜻지수 [2] 🍂"
        clothes = ["🧥 가벼운 경량패딩", "🧶 포근한 니트", "👖 편한 트레이닝 바지", "🧣 따뜻한 목도리"]
        extra_msg = ""
       
    elif 14 <= temp <= 20:
        warmth_index = "따뜻지수 [3] 🌼"
        clothes = ["👕 산뜻한 롱슬리브", "🩳 트렌디한 버뮤다 팬츠", "👟 귀여운 크록스"]
        extra_msg = ""
       
    elif 21 <= temp <= 30:
        warmth_index = "따뜻지수 [4] ☀️"
        clothes = ["🎽 시원한 나시", "🩳 가벼운 반바지", "🩴 쿨한 쪼리 신발"]
        extra_msg = "매우 더운 날씨이므로 열사병에 걸리지 않게 시원하게 입는게 중요하겠습니다"
       
    else:
        warmth_index = "범위 초과 ❓"
        clothes = []
        extra_msg = "-20도 ~ 30도 사이의 온도를 입력해주세요."
       
    return warmth_index, clothes, extra_msg


# --- 화면(Streamlit UI) 구성 ---
st.title("🧸 [ 맞춤형 코디 가이드 앱]")
st.caption("오늘 기온에 딱 맞는 귀여운 데일리룩을 추천해 드려요! ✨")

# 온도 구간 안내를 2열 카드 형태로 깔끔하게 배치
with st.container(border=True):
    st.markdown("#### 🌡️ 온도 구간 안내")
    col1, col2 = st.columns(2)
    with col1:
        st.write("❄️ **1.** -20도 ~ 0도")
        st.write("🍂 **2.** 1도 ~ 13도")
    with col2:
        st.write("🌼 **3.** 14도 ~ 20도")
        st.write("☀️ **4.** 21도 ~ 30도")

st.write("") # 여백

# 오늘의 온도 입력받기
temp = st.number_input("🌡️ 오늘의 온도를 입력하세요 (-20도 ~ 30도)", min_value=-20, max_value=30, value=15, step=1)

# 꽉 차는 귀여운 버튼
if st.button("✨ 오늘의 코디 추천받기 ✨", use_container_width=True, type="primary"):
    # 함수 호출
    warmth, outfit_list, message = get_outfit_guide(temp)
   
    st.write("")
    # 결과 영역을 깔끔한 테두리 박스로 묶기
    with st.container(border=True):
        st.subheader(f"🎀 {temp}도일때의 코디 추천")
        st.info(f"**{warmth}**")
       
        st.markdown("#### 👗 추천 코디 아이템")
        # [필수 조건 3: 반복구조(for) 사용]
        for item in outfit_list:
            st.success(item)
           
        # 추운 날(-20~0도) 또는 더운 날(21~30도) 추가 멘트 출력
        if message != "":
            st.warning(f"📢 {message}")
