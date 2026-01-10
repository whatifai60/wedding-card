import streamlit as st
import os
import folium
import base64
from streamlit_folium import st_folium

# 1. 페이지 설정
st.set_page_config(
    page_title="김준태 · 김경미 결혼식",
    page_icon="💍",
    layout="centered"
)

# 2. 이미지 Base64 변환 함수
def get_image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 3. 디자인 CSS
st.markdown("""
<style>
/* 전체 배경 */
.stApp {
    background-color: #F9F8F6;
}

/* 기본 텍스트 */
div.stMarkdown {
    text-align: center;
    color: #333333;
}

/* 클릭 하이라이트 제거 */
* {
    -webkit-tap-highlight-color: transparent !important;
    -webkit-touch-callout: none !important;
    outline: none !important;
}

/* expander 내부 텍스트 색상 고정 */
[data-testid="stExpander"] div,
[data-testid="stExpander"] span,
[data-testid="stExpander"] p {
    color: #333333 !important;
    opacity: 1 !important;
}

/* 타이틀 */
.eng-title {
    font-family: 'Times New Roman', serif;
    font-style: italic;
    font-size: 26px;
    color: #B2A59B;
    margin-top: 30px;
    margin-bottom: 10px;
}

/* 갤러리 */
.gallery-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    width: 100%;
    margin-top: 20px;
}
.gallery-grid img {
    width: 100%;
    aspect-ratio: 1 / 1;
    object-fit: cover;
    border-radius: 5px;
}

/* 연락처 */
.contact-row {
    display: flex;
    justify-content: space-around;
    align-items: center;
    width: 100%;
    margin: 20px 0;
}

/* 복사 버튼 */
.copy-btn {
    background-color: #333333;
    color: white;
    border: none;
    padding: 8px 15px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: bold;
    cursor: pointer;
}

.leaflet-marker-icon,
.leaflet-marker-shadow {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# 4. 메인 이미지
if os.path.exists("main.jpg"):
    main_b64 = get_image_base64("main.jpg")
    st.markdown(
        f'<img src="data:image/jpeg;base64,{main_b64}" style="width:100%; height:auto;">',
        unsafe_allow_html=True
    )

# 타이틀
st.markdown("""
<div style="text-align: center;">
    <p class="eng-title">THE WEDDING OF</p>
    <h1 style="color:#333; font-weight:400;">김준태 · 김경미</h1>
    <p style="font-size:17px; font-weight:500;">2026.05.10 SUN PM 1:20</p>
    <p style="font-size:17px; font-weight:500;">웨딩시티 4층</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# 5. 인사말
st.markdown('<p class="eng-title">Our Wedding</p>', unsafe_allow_html=True)
st.markdown("""
<div style="font-size:16px; line-height:2.2; color:#444;">
오랜 시간 소중한 이야기를 쌓아온<br>
우리 두 사람, 결혼합니다.<br><br>
변함없이 서로를 아끼며 살겠습니다.<br>
서로를 향한 사랑과 믿음으로<br>
하나가 되는 자리에 함께해 주세요.
</div>
""", unsafe_allow_html=True)

st.divider()

# 6. 혼주 정보
st.markdown("""
<div class="contact-row">
    <div>
        <p style="font-size:18px; font-weight:bold;">신랑</p>
        <p>김준태</p>
        <p style="font-size:14px; color:#777;">부 김종우<br>모 김미나</p>
    </div>
    <div>
        <p style="font-size:18px; font-weight:bold;">신부</p>
        <p>김경미</p>
        <p style="font-size:14px; color:#777;">부 김봉욱<br>모 남회숙</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# 7. 갤러리
st.markdown('<p class="eng-title">Gallery</p>', unsafe_allow_html=True)
photos = [f"photo ({i}).jpg" for i in range(1, 31) if os.path.exists(f"photo ({i}).jpg")]

if photos:
    imgs = ""
    for p in photos:
        imgs += f'<img src="data:image/jpeg;base64,{get_image_base64(p)}">'
    st.markdown(f'<div class="gallery-grid">{imgs}</div>', unsafe_allow_html=True)

st.divider()

# 8. 위치
st.markdown('<p class="eng-title">Location</p>', unsafe_allow_html=True)
st.markdown("""
<p style="font-size:18px; font-weight:bold;">웨딩시티 4층</p>
<p style="color:#666;">서울 구로구 구로동 3-25 (신도림 테크노마트)</p>
""", unsafe_allow_html=True)

m = folium.Map(location=[37.5070431, 126.8902185], zoom_start=17)
folium.Marker(
    [37.5070431, 126.8902185],
    icon=folium.DivIcon(
        html="""
        <div style="
            background:#333;
            color:white;
            padding:8px 20px;
            border-radius:20px;
            font-weight:bold;
            font-size:14px;
        ">
        웨딩시티 4층
        </div>
        """
    )
).add_to(m)

st_folium(m, width="100%", height=350, returned_objects=[])

st.markdown("""
<div style="text-align:center; margin-top:15px;">
<a href="https://naver.me/5Rh0OxaM" target="_blank" style="text-decoration:none;">
<div style="background:#03C75A; color:white; padding:12px 20px;
border-radius:5px; font-weight:bold;">
N 네이버 지도 / 길찾기
</div>
</a>
</div>
""", unsafe_allow_html=True)

st.divider()

# 9. 계좌 복사
st.markdown('<p style="font-size:20px;">마음 전하실 곳</p>', unsafe_allow_html=True)

def account_row(title, number):
    st.markdown(f"""
    <div style="display:flex; justify-content:space-between;
                align-items:center; padding:15px;
                background:white; border-radius:12px;
                margin-bottom:12px;">
        <div>
            <span style="font-size:13px; color:#888;">{title}</span><br>
            <span style="font-size:16px; font-weight:bold;">{number}</span>
        </div>
        <button class="copy-btn"
            onclick="navigator.clipboard.writeText('{number}')
            .then(()=>alert('계좌번호가 복사되었습니다!'))">
            복사
        </button>
    </div>
    """, unsafe_allow_html=True)

with st.expander("신랑 측 계좌번호"):
    account_row("국민은행 (김준태)", "123-45678-90")

with st.expander("신부 측 계좌번호"):
    account_row("신한은행 (김경미)", "987-65432-10")