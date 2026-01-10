import streamlit as st
import os
import folium
import base64
from streamlit_folium import st_folium

st.set_page_config(
    page_title="김준태 · 김경미 결혼식",
    page_icon="💍",
    layout="centered"
)

def get_image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ===== CSS =====
st.markdown("""
<style>
.stApp { background-color: #F9F8F6; }

* {
    -webkit-tap-highlight-color: transparent !important;
    -webkit-touch-callout: none !important;
    outline: none !important;
}

/* expander 전체 배경 흰색 고정 */
[data-testid="stExpander"] {
    background: white !important;
    border-radius: 14px;
}

/* expander 내부 */
[data-testid="stExpander"] div,
[data-testid="stExpander"] span,
[data-testid="stExpander"] p {
    color: #333 !important;
    opacity: 1 !important;
}

.eng-title {
    font-family: 'Times New Roman', serif;
    font-style: italic;
    font-size: 26px;
    color: #B2A59B;
    margin: 30px 0 10px;
}

.gallery-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
}

.gallery-grid img {
    width: 100%;
    aspect-ratio: 1/1;
    object-fit: cover;
    border-radius: 6px;
}

.copy-box {
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:16px;
    background:white;
    border-radius:14px;
    margin-bottom:12px;
    cursor:pointer;
}

.copy-btn {
    background:#333;
    color:white;
    border:none;
    padding:8px 16px;
    border-radius:20px;
    font-size:13px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# ===== 메인 이미지 =====
if os.path.exists("main.jpg"):
    st.markdown(
        f'<img src="data:image/jpeg;base64,{get_image_base64("main.jpg")}" style="width:100%;">',
        unsafe_allow_html=True
    )

st.markdown("""
<p class="eng-title">THE WEDDING OF</p>
<h2>김준태 · 김경미</h2>
<p>2026.05.10 SUN PM 1:20</p>
<p>웨딩시티 4층</p>
""", unsafe_allow_html=True)

st.divider()

# ===== 계좌 복사 =====
st.markdown("<h3>마음 전하실 곳</h3>", unsafe_allow_html=True)

def account_row(title, number):
    st.markdown(f"""
    <div class="copy-box"
        onclick="navigator.clipboard.writeText('{number}'); alert('계좌번호가 복사되었습니다');">
        <div>
            <div style="font-size:13px;color:#888;">{title}</div>
            <div style="font-size:16px;font-weight:bold;">{number}</div>
        </div>
        <div class="copy-btn">복사</div>
    </div>
    """, unsafe_allow_html=True)

with st.expander("신랑 측 계좌번호", expanded=False):
    account_row("국민은행 (김준태)", "123-45678-90")

with st.expander("신부 측 계좌번호", expanded=False):
    account_row("신한은행 (김경미)", "987-65432-10")

st.divider()

# ===== 지도 =====
st.markdown("<p class='eng-title'>Location</p>", unsafe_allow_html=True)
st.markdown("<b>웨딩시티 4층</b><br>서울 구로구 구로동 3-25", unsafe_allow_html=True)

m = folium.Map(
    location=[37.5070431, 126.8902185],
    zoom_start=17
)

folium.Marker(
    [37.5070431, 126.8902185],
    icon=folium.DivIcon(
        html='<div style="background:#333;color:white;padding:8px 18px;border-radius:20px;font-weight:bold;">웨딩시티 4층</div>'
    )
).add_to(m)

st_folium(m, width="100%", height=350)