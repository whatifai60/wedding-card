import streamlit as st
import os
import folium
import base64
from streamlit_folium import st_folium

# 1. 페이지 설정
st.set_page_config(page_title="김준태 · 김경미 결혼식", page_icon="💍", layout="centered")

# 2. 이미지 Base64 변환 함수
def get_image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 3. CSS 설정 (상단 노출되던 코드들을 style 태그 안으로 정리)
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@400;700;800&display=swap" rel="stylesheet">
    <style>
    /* 전체 폰트 및 중앙 정렬 */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Nanum Myeongjo', serif !important;
        text-align: center !important;
    }
    
    .stApp { background-color: #F9F8F6; }

    /* 모든 마크다운 요소 강제 중앙 정렬 */
    div.stMarkdown, div.stMarkdown p, div.stText {
        text-align: center !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
    }
    
    /* 메인 이름 크기 조절 */
    .main-names {
        display: block;
        text-align: center;
        width: 100%;
        margin: 10px 0 25px 0;
        font-weight: 700;
        color: #333333;
        font-size: 26px; 
        letter-spacing: 1px;
    }

    /* 터치 회색 잔상 제거 */
    * { -webkit-tap-highlight-color: transparent !important; outline: none !important; }

    .eng-title {
        font-family: 'Times New Roman', serif;
        font-style: italic; font-size: 24px;
        color: #B2A59B; margin-top: 30px; margin-bottom: 5px;
        text-align: center;
        width: 100%;
    }

    /* 지도 태그 스타일 */
    .map-tag {
        background-color: #333333 !important; color: white !important;
        text-align: center !important; line-height: 34px !important;
        font-size: 14px !important; font-weight: bold !important;
        border-radius: 18px !important; border: 2px solid white !important;
        width: 120px !important; white-space: nowrap !important;
        display: block !important;
    }
    
    .leaflet-marker-icon, .leaflet-marker-shadow { display: none !important; }
    
    /* 구분선 중앙 정렬 */
    hr { margin-left: auto !important; margin-right: auto !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. 메인 이미지
if os.path.exists("main.jpg"):
    main_b64 = get_image_base64("main.jpg")
    st.markdown(f'<div style="text-align:center;"><img src="data:image/jpeg;base64,{main_b64}" style="width:100%; height:auto;"></div>', unsafe_allow_html=True)

st.markdown(f"""
    <p class="eng-title">THE WEDDING OF</p>
    <div class="main-names">김준태 &nbsp; · &nbsp; 김경미</div>
    <div style="color: #333333; font-size: 16px; line-height: 1.6; font-weight: 500;">
        2026.05.10 SUN PM 1:20<br>
        웨딩시티 4층
    </div>
    """, unsafe_allow_html=True)

st.divider()

# 3. 인사말
st.markdown('<p class="eng-title">Our Wedding</p>', unsafe_allow_html=True)
st.markdown("""
    <div style="font-size: 15px; line-height: 2.2; color: #444; text-align: center;">
        오랜 시간 소중한 이야기를 쌓아온<br>
        우리 두 사람, 결혼합니다.<br><br>
        변함없이 서로를 아끼며 살겠습니다.<br>
        서로를 향한 사랑과 믿음으로<br>
        하나가 되는 자리에 함께해 주세요.
    </div>
    """, unsafe_allow_html=True)

st.divider()

# 4. 연락처
st.markdown("""
    <div style="display: flex; justify-content: space-around; align-items: center; width: 100%; margin: 20px 0; font-family: 'Nanum Myeongjo', serif;">
        <div style="text-align: center; flex: 1;">
            <p style="font-weight: bold; font-size: 17px; margin-bottom: 5px;">신랑</p>
            <p style="font-size: 16px; margin-bottom: 10px;">김준태</p>
            <p style="font-size: 13px; color: #777; line-height: 1.5;">부 김종우<br>모 김미나</p>
        </div>
        <div style="text-align: center; flex: 1;">
            <p style="font-weight: bold; font-size: 17px; margin-bottom: 5px;">신부</p>
            <p style="font-size: 16px; margin-bottom: 10px;">김경미</p>
            <p style="font-size: 13px; color: #777; line-height: 1.5;">부 김봉욱<br>모 남회숙</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# 5. 갤러리 (자동 무한 루프 슬라이더)
st.markdown('<p class="eng-title">Gallery</p>', unsafe_allow_html=True)
existing_photos = [f"photo ({i}).jpg" for i in range(1, 31) if os.path.exists(f"photo ({i}).jpg")]

if existing_photos:
    slides_html = ""
    for photo in existing_photos:
        b64 = get_image_base64(photo)
        slides_html += f'<div class="swiper-slide"><img src="data:image/jpeg;base64,{b64}" style="width:100%; border-radius:10px;"></div>'
    
    slider_content = f"""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
    <style>
        .swiper {{ width: 100%; padding-bottom: 30px; }}
        .swiper-slide {{ display: flex; justify-content: center; align-items: center; width: 85%; }}
        .swiper-pagination-bullet-active {{ background: #B2A59B !important; }}
    </style>
    <div class="swiper mySwiper">
        <div class="swiper-wrapper">
            {slides_html}
        </div>
        <div class="swiper-pagination"></div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
    <script>
        var swiper = new Swiper(".mySwiper", {{
            loop: true,
            centeredSlides: true,
            slidesPerView: "auto",
            spaceBetween: 20,
            autoplay: {{
                delay: 1500,
                disableOnInteraction: false,
            }},
            speed: 1000,
            pagination: {{
                el: ".swiper-pagination",
                clickable: true,
            }},
        }});
    </script>
    """
    st.components.v1.html(slider_content, height=500)

st.divider()

# 6. 장소 및 지도 (중앙 정렬 강화)
st.markdown('<p class="eng-title">Location</p>', unsafe_allow_html=True)
st.markdown("""
    <div style="text-align: center; width: 100%; margin-bottom: 15px;">
        <p style="font-size: 17px; font-weight: bold; color: #333333; margin-bottom: 5px;">웨딩시티 4층</p>
        <p style="color: #666; font-size: 14px;">서울 구로구 구로동 3-25 (신도림 테크노마트)</p>
    </div>
    """, unsafe_allow_html=True)

m = folium.Map(location=[37.5070431, 126.8902185], zoom_start=17)
folium.Marker(
    [37.5070431, 126.8902185], 
    icon=folium.DivIcon(icon_size=(120,36), icon_anchor=(60,18), html='<div class="map-tag">웨딩시티 4층</div>')
).add_to(m)
st_folium(m, width="100%", height=350, returned_objects=[])

st.markdown('<div style="text-align: center; margin-top: 15px;"><a href="https://naver.me/5Rh0OxaM" target="_blank" style="text-decoration: none;"><div style="background-color: #03C75A; color: white; padding: 12px 20px; border-radius: 5px; font-weight: bold; display: inline-block; font-size: 14px;">네이버 지도로 보기</div></a></div>', unsafe_allow_html=True)

st.divider()

# 7. 축의금 복사
st.markdown('<p style="font-size: 18px; text-align: center; margin-bottom: 20px;">마음 전하실 곳</p>', unsafe_allow_html=True)

def account_row(title, account_number):
    acc_html = f"""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 15px; border-bottom: 1px solid #eee; background: white; border-radius: 12px; margin-bottom: 12px; font-family: 'Nanum Myeongjo', serif;">
        <div style="text-align: left;">
            <div style="font-size: 12px; color: #888; margin-bottom: 4px;">{title}</div>
            <div style="font-size: 15px; font-weight: bold; color: #333;">{account_number}</div>
        </div>
        <button onclick="copyAcc('{account_number}', this)" style="background-color: #333; color: white; border: none; padding: 7px 14px; border-radius: 20px; font-size: 12px; font-weight: bold; cursor: pointer; transition: 0.2s;">복사</button>
    </div>
    <script>
        function copyAcc(val, btn) {{
            const t = document.createElement('textarea');
            t.value = val;
            document.body.appendChild(t);
            t.select();
            document.execCommand('copy');
            document.body.removeChild(t);
            const ori = btn.innerText;
            btn.innerText = '완료';
            btn.style.backgroundColor = '#03C75A';
            setTimeout(() => {{ btn.innerText = ori; btn.style.backgroundColor = '#333'; }}, 1000);
        }}
    </script>
    """
    st.components.v1.html(acc_html, height=80)

with st.expander("신랑 측 계좌번호"):
    account_row("국민은행 (신랑 김준태)", "123-45678-90")
with st.expander("신부 측 계좌번호"):
    account_row("신한은행 (신부 김경미)", "987-65432-10")
