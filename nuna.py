import streamlit as st
import os
import folium
import base64
from streamlit_folium import st_folium

# --- 미리보기(OG Tag) 설정 ---
st.markdown(f"""
    <head>
        <meta property="og:title" content="준태 & 경미 결혼합니다" />
        <meta property="og:description" content="2026년 5월 10일 오후 1시 20분, 웨딩시티 8층" />
    </head>
    """, unsafe_allow_html=True)

# 1. 페이지 설정
st.set_page_config(page_title="준태 경미 결혼합니다", page_icon="", layout="centered")

def get_image_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# CSS 설정 (배경색 ffffff 적용 및 스타일 정리)
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@400;700;800&display=swap" rel="stylesheet">
    <style>
    /* [수정] 배경색을 완전한 흰색으로 변경 */
    .stApp { background-color: #ffffff; }
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Nanum Myeongjo', serif !important;
        text-align: center !important;
        background-color: #ffffff !important;
    }
    
    div.stMarkdown, p, div {
        text-align: center !important;
    }
    
    .eng-title {
        font-family: 'Times New Roman', serif !important;
        font-style: italic !important; 
        font-size: 24px !important;
        color: #B2A59B !important; 
        margin: 30px 0 10px 0 !important;
        display: block !important;
    }
    
    .main-names {
        font-family: 'Nanum Myeongjo', serif !important;
        font-weight: 700 !important;
        color: #333333 !important;
        font-size: 26px !important; 
        letter-spacing: 1px !important;
        margin: 10px 0 25px 0 !important;
        text-align: center !important;
    }
    
    .contact-container {
        display: flex !important;
        flex-direction: row !important;
        justify-content: center !important;
        align-items: flex-start !important;
        width: 100% !important;
        margin: 20px 0 !important;
    }
    
    .contact-box {
        flex: 1 !important;
        text-align: center !important;
    }
    
    * { 
        -webkit-tap-highlight-color: transparent !important; 
        outline: none !important; 
    }
    
    .map-tag {
        background-color: #333333 !important; 
        color: white !important;
        text-align: center !important; 
        line-height: 34px !important;
        font-size: 14px !important; 
        font-weight: bold !important;
        border-radius: 18px !important; 
        border: 2px solid white !important;
        width: 120px !important; 
        white-space: nowrap !important;
        display: block !important;
    }
    
    .leaflet-marker-icon, .leaflet-marker-shadow { display: none !important; }
    
    /* 구분선 색상 살짝 조정 (흰 배경에 맞게) */
    hr { 
        margin: 40px 0 !important; 
        border-top: 1px solid #eeeeee !important;
    }

    /* 계좌번호 레이아웃 배경색 조정 */
    .acc-row-container {
        background: #fdfdfd !important; /* 미세한 회색으로 가독성 확보 */
        border: 1px solid #f0f0f0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 메인 콘텐츠 시작 ---

# "THE WEDDING OF"를 사진 위로 배치
st.markdown('<p class="eng-title">THE WEDDING OF</p>', unsafe_allow_html=True)

if os.path.exists("main.jpg"):
    main_b64 = get_image_base64("main.jpg")
    st.markdown(f'<div style="text-align:center;"><img src="data:image/jpeg;base64,{main_b64}" style="width:100%; height:auto;"></div>', unsafe_allow_html=True)

# 메인 정보
st.markdown(f"""
    <div class="main-names">김준태 &nbsp; · &nbsp; 김경미</div>
    <div style="color: #333333; font-size: 16px; line-height: 1.6; font-weight: 500;">
        2026.05.10 SUN PM 1:20<br>
        웨딩시티 8층
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.markdown('<p class="eng-title">Our Wedding</p>', unsafe_allow_html=True)
st.markdown("""
    <div style="font-size: 15px; line-height: 2.2; color: #444;">
        오랜 시간 소중한 이야기를 쌓아온<br>
        우리 두 사람, 결혼합니다.<br><br>
        변함없이 서로를 아끼며 살겠습니다.<br>
        서로를 향한 사랑과 믿음으로<br>
        하나가 되는 자리에 함께해 주세요.
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.markdown("""
    <div class="contact-container">
        <div class="contact-box">
            <p style="font-weight: bold; font-size: 17px; margin-bottom: 5px;">신랑</p>
            <p style="font-size: 16px; margin-bottom: 10px;">김준태</p>
            <p style="font-size: 13px; color: #777; line-height: 1.5;">부 김종우<br>모 김미나</p>
        </div>
        <div class="contact-box">
            <p style="font-weight: bold; font-size: 17px; margin-bottom: 5px;">신부</p>
            <p style="font-size: 16px; margin-bottom: 10px;">김경미</p>
            <p style="font-size: 13px; color: #777; line-height: 1.5;">부 김봉욱<br>모 남희숙</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

st.markdown('<p class="eng-title">Gallery</p>', unsafe_allow_html=True)
existing_photos = [f"photo ({i}).jpg" for i in range(1, 31) if os.path.exists(f"photo ({i}).jpg")]

if existing_photos:
    slides_html = ""
    for photo in existing_photos:
        b64 = get_image_base64(photo)
        slides_html += f'<div class="swiper-slide"><img src="data:image/jpeg;base64,{b64}" style="max-width:100%; max-height:100%; object-fit:contain; border-radius:10px;"></div>'
    
    slider_content = f"""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
    <style>
        .swiper {{ width: 100%; height: 450px; padding-bottom: 30px; }}
        .swiper-slide {{ display: flex; justify-content: center; align-items: center; }}
        .swiper-pagination-bullet-active {{ background: #B2A59B !important; }}
    </style>
    <div class="swiper mySwiper">
        <div class="swiper-wrapper">{slides_html}</div>
        <div class="swiper-pagination"></div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
    <script>
        var swiper = new Swiper(".mySwiper", {{
            loop: true, centeredSlides: true,
            autoplay: {{ delay: 1500, disableOnInteraction: false }},
            speed: 1000,
            pagination: {{ el: ".swiper-pagination", clickable: true }},
        }});
    </script>
    """
    st.components.v1.html(slider_content, height=480)

st.divider()

st.markdown('<p class="eng-title">Location</p>', unsafe_allow_html=True)
st.markdown("""
    <div style="margin-bottom: 15px; text-align: center;">
        <p style="font-size: 17px; font-weight: bold; color: #333333; margin-bottom: 5px;">웨딩시티 8층</p>
        <p style="color: #666; font-size: 14px;">서울 구로구 구로동 3-25 (신도림 테크노마트)</p>
    </div>
    """, unsafe_allow_html=True)

m = folium.Map(location=[37.5070431, 126.8902185], zoom_start=17)
folium.Marker(
    [37.5070431, 126.8902185], 
    icon=folium.DivIcon(icon_size=(120,36), icon_anchor=(60,18), html='<div class="map-tag">웨딩시티 8층</div>')
).add_to(m)
st_folium(m, width="100%", height=350, returned_objects=[])

st.markdown('<div style="text-align: center; margin-top: 15px;"><a href="https://naver.me/5Rh0OxaM" target="_blank" style="text-decoration: none;"><div style="background-color: #03C75A; color: white; padding: 12px 20px; border-radius: 5px; font-weight: bold; display: inline-block; font-size: 14px;">네이버 지도로 보기</div></a></div>', unsafe_allow_html=True)

st.divider()

st.markdown('<p style="font-size: 16px; text-align: center; margin-bottom: 20px; color: #444;">축복의 의미로 축의금을 전달해보세요</p>', unsafe_allow_html=True)

def account_row(title, account_number):
    acc_html = f"""
    <div class="acc-row-container" style="display: flex; justify-content: space-between; align-items: center; padding: 15px; border-bottom: 1px solid #eee; background: white; border-radius: 12px; margin-bottom: 12px; font-family: 'Nanum Myeongjo', serif;">
        <div style="text-align: left;">
            <div style="font-size: 12px; color: #888; margin-bottom: 4px;">{title}</div>
            <div style="font-size: 15px; font-weight: bold; color: #333;">{account_number}</div>
        </div>
        <button onclick="copyAcc('{account_number}', this)" style="background-color: #333; color: white; border: none; padding: 8px 15px; border-radius: 20px; font-size: 13px; font-weight: bold; cursor: pointer;">복사</button>
    </div>
    <script>
        function copyAcc(val, btn) {{
            const t = document.createElement('textarea');
            t.value = val; document.body.appendChild(t);
            t.select(); document.execCommand('copy'); document.body.removeChild(t);
            const ori = btn.innerText; btn.innerText = '완료'; btn.style.backgroundColor = '#03C75A';
            setTimeout(() => {{ btn.innerText = ori; btn.style.backgroundColor = '#333'; }}, 1000);
        }}
    </script>
    """
    st.components.v1.html(acc_html, height=80)

with st.expander("신랑 측 계좌번호"):
    account_row("국민은행 (신랑 김준태)", "123-45678-90")
with st.expander("신부 측 계좌번호"):
    account_row("신한은행 (신부 김경미)", "987-65432-10")
