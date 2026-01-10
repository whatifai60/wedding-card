import streamlit as st
import os
import folium
from streamlit_folium import st_folium

# 1. 페이지 설정
st.set_page_config(page_title="김준태 · 김경미 결혼식", page_icon="💍", layout="centered")

# 2. 기기별 레이아웃 최적화 CSS
st.markdown("""
    <style>
    /* 공통 스타일 */
    .stApp { background-color: #F9F8F6; }
    div.stMarkdown { text-align: center; color: #333333; }
    .eng-title {
        font-family: 'Times New Roman', serif;
        font-style: italic;
        font-size: 26px;
        color: #B2A59B;
        margin-top: 30px;
        margin-bottom: 10px;
    }
    
    /* [핵심] 클릭 시 회색 하이라이트 제거 */
    * { -webkit-tap-highlight-color: transparent !important; outline: none !important; }

    /* [핵심] 모바일/PC 판별 및 갤러리 3열 강제 고정 */
    .gallery-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr); /* 무조건 3열 */
        gap: 8px;
        width: 100%;
        margin-top: 20px;
    }
    .gallery-grid img {
        width: 100%;
        aspect-ratio: 1 / 1; /* 정사각형 유지 */
        object-fit: cover;
        border-radius: 5px;
    }

    /* 연락처 섹션 모바일 대응 (옆으로 나란히) */
    .contact-row {
        display: flex;
        justify-content: space-around;
        align-items: center;
        width: 100%;
        margin: 20px 0;
    }

    /* 복사 버튼 스타일 */
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
    
    /* 지도 마커 깨짐 방지 */
    .leaflet-marker-icon, .leaflet-marker-shadow { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. 메인 이미지
if os.path.exists("main.jpg"):
    st.image("main.jpg", use_container_width=True)

st.markdown("""
    <div style="text-align: center;">
        <p class="eng-title">THE WEDDING OF</p>
        <h1 style="color: #333333; margin-top: -10px; font-weight: 400;">김준태 &nbsp; · &nbsp; 김경미</h1>
        <p style="color: #333333; font-size: 17px; margin-bottom: 5px; font-weight: 500;">2026.05.10 SUN PM 1:20</p>
        <p style="color: #333333; font-size: 17px; font-weight: 500;">웨딩시티 4층</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# 3. 인사말
st.markdown('<p class="eng-title">Our Wedding</p>', unsafe_allow_html=True)
st.markdown('<div style="font-size: 16px; line-height: 2.2; color: #444;">오랜 시간 소중한 이야기를 쌓아온<br>우리 두 사람, 결혼합니다.<br><br>변함없이 서로를 아끼며 살겠습니다.<br>서로를 향한 사랑과 믿음으로<br>하나가 되는 자리에 함께해 주세요.</div>', unsafe_allow_html=True)

st.divider()

# 4. 연락처 (HTML 직접 구성으로 모바일 2열 고정)
st.markdown("""
    <div class="contact-row">
        <div style="text-align: center;">
            <p style="font-weight: bold; font-size: 18px;">신랑</p>
            <p style="font-size: 16px;">김준태</p>
            <p style="font-size: 14px; color: #777;">부 김종우<br>모 김미나</p>
        </div>
        <div style="text-align: center;">
            <p style="font-weight: bold; font-size: 18px;">신부</p>
            <p style="font-size: 16px;">김경미</p>
            <p style="font-size: 14px; color: #777;">부 김봉욱<br>모 남회숙</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# 5. 갤러리 (HTML Grid 방식으로 무조건 3열 유지)
st.markdown('<p class="eng-title">Gallery</p>', unsafe_allow_html=True)
existing_photos = [f"photo ({i}).jpg" for i in range(1, 31) if os.path.exists(f"photo ({i}).jpg")]

if existing_photos:
    # Streamlit 기본 image 대신 직접 HTML 태그를 생성하여 3열 고정
    import base64
    def get_image_base64(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()

    gallery_items = ""
    for photo in existing_photos:
        b64 = get_image_base64(photo)
        gallery_items += f'<img src="data:image/jpeg;base64,{b64}">'
    
    st.markdown(f'<div class="gallery-grid">{gallery_items}</div>', unsafe_allow_html=True)

st.divider()

# 6. 장소
st.markdown('<p class="eng-title">Location</p>', unsafe_allow_html=True)
st.markdown('<p style="font-size: 18px; font-weight: bold; color: #333333;">웨딩시티 4층</p><p style="color: #666;">서울 구로구 구로동 3-25 (신도림 테크노마트)</p>', unsafe_allow_html=True)

m = folium.Map(location=[37.5070431, 126.8902185], zoom_start=17)
folium.Marker([37.5070431, 126.8902185], icon=folium.DivIcon(icon_size=(150,36), icon_anchor=(75,18), html='<div style="background-color: #333333; color: white; text-align: center; line-height: 34px; font-size: 14px; font-weight: bold; border-radius: 18px; border: 2px solid white; box-shadow: 0 2px 8px rgba(0,0,0,0.3); width: 150px;">웨딩시티 4층</div>')).add_to(m)
st_folium(m, width="100%", height=350, returned_objects=[])

st.markdown('<div style="text-align: center; margin-top: 15px;"><a href="https://naver.me/5Rh0OxaM" target="_blank" style="text-decoration: none;"><div style="background-color: #03C75A; color: white; padding: 12px 20px; border-radius: 5px; font-weight: bold; display: inline-block;">N 네이버 지도로 보기 / 길찾기</div></a></div>', unsafe_allow_html=True)

st.divider()

# 7. 축의금 및 복사 (HTML/JS 결합형 최종)
st.markdown('<p style="font-size: 20px; text-align: center;">마음 전하실 곳</p>', unsafe_allow_html=True)

def account_row(title, account_number):
    st.write(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 15px; border-bottom: 1px solid #eee; background: white; border-radius: 12px; margin-bottom: 12px;">
            <div style="text-align: left;">
                <span style="font-size: 13px; color: #888;">{title}</span><br>
                <span style="font-size: 16px; font-weight: bold; color: #333;">{account_number}</span>
            </div>
            <button class="copy-btn" onclick="const el = document.createElement('textarea'); el.value = '{account_number}'; document.body.appendChild(el); el.select(); document.execCommand('copy'); document.body.removeChild(el); alert('복사되었습니다: {account_number}');">복사</button>
        </div>
    """, unsafe_allow_html=True)

with st.expander("신랑 측 계좌번호"):
    account_row("국민은행 (신랑 김준태)", "123-45678-90")
with st.expander("신부 측 계좌번호"):
    account_row("신한은행 (신부 김경미)", "987-65432-10")
