import streamlit as st

# ==========================================
# [설정 1] 이번 주 비밀번호 (매주 여기서 바꾸면 돼!)
SECRET_PW = "love1225"

# [설정 2] 상품 리스트 (여기에 15개 정보를 채워넣으면 돼!)
products = [
    {
        "name": "[폴로] 케이블 니트 아이보리",
        "price": "45,000원",
        "img": "image_01.jpg", 
        "desc": "상태 S급! 보자마자 소리 질렀던 그 니트예요. 핏이 진짜 예술...",
        "link": "https://s.tosspayments.com/BmcraUdk2ry" 
    },
    {
        "name": "[버버리] 90s 트렌치 코트",
        "price": "120,000원",
        "img": "image_02.jpg",
        "desc": "단추 하나가 없어서 저렴하게 내놔요! 하지만 분위기 깡패...",
        "link": "https://s.tosspayments.com/BmuRRI34miq"
    },
    {
        "name": "[나이키] 올드스쿨 바람막이",
        "price": "38,000원",
        "img": "image_03.jpg",
        "desc": "색감이 미쳤어요. 쿨톤 언니들 무조건 가져가세요!",
        "link": "https://s.tosspayments.com/BmuRRNMs78E"
    },
    # ... 필요한 만큼 복사해서 계속 추가 ...
]
# ==========================================

# 페이지 기본 설정
st.set_page_config(page_title="그린루프 VIP 쇼룸", page_icon="🔒")

# --- 1. 비밀번호 대문 (Gatekeeper) ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🔒 VIP 시크릿 쇼룸 입장")
    st.write("방송에서 공개된 비밀번호를 입력해주세요.")
    
    password = st.text_input("비밀번호", type="password")
    
    if st.button("입장하기"):
        if password == SECRET_PW:
            st.session_state.authenticated = True
            st.rerun() # 화면 새로고침 (문 열림!)
        else:
            st.error("비밀번호가 틀렸어요! 🙅‍♀️")
    
    st.stop() # 비밀번호 틀리면 여기서 멈춤


# --- 2. 상품 진열대 (Main Shop) ---
st.title("💎 그린루프 VIP Collection")
st.write(f"이번 주 **{len(products)}개**의 보물이 준비되어 있어요!")
st.markdown("---")

# 상품 리스트를 하나씩 꺼내서 화면에 그리기
for item in products:
    # 화면을 2칸으로 나눔 (왼쪽: 사진 / 오른쪽: 설명)
    col1, col2 = st.columns([1, 1.5]) 
    
    with col1:
        # 사진이 없으면 에러 나니까 try-except로 방어
        try:
            st.image(item["img"], use_column_width=True)
        except:
            st.warning(f"사진({item['img']}) 준비중")

    with col2:
        st.subheader(item["name"]) # 상품명
        st.write(f"**가격:** {item['price']}")
        st.info(item["desc"]) # 설명
        
        # 🚨 결제 경고 문구 추가
        st.caption(f"💡 결제 메모에 암호 **'{SECRET_PW}'** 필수 기재! (미기재 취소)")
        
        # 구매 버튼 (들여쓰기 주의!)
        st.link_button("👉 구매하러 가기 (선착순)", item["link"], type="primary")
    
    st.markdown("---") # 상품 사이 구분선

# 푸터
st.caption("ⓒ Greenloop VIP Secret Shop. Only for our best fans.")