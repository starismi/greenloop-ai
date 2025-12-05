[app.py](https://github.com/user-attachments/files/23958359/app.py)
import streamlit as st

# ==========================================
# [설정 1] 이번 주 비밀번호 (매주 여기서 바꾸면 돼!)
SECRET_PW = "love1225"

# [설정 2] 상품 리스트 (여기에 15개 정보를 채워넣으면 돼!)
# 형식: {"name": "상품명", "img": "이미지파일이름.jpg", "desc": "설명", "link": "토스링크"},
products = [
    {
        "name": "[폴로] 케이블 니트 아이보리",
        "price": "45,000원",
        "img": "image_01.jpg",  # 깃허브에 올린 사진 파일 이름
        "desc": "상태 S급! 보자마자 소리 질렀던 그 니트예요. 핏이 진짜 예술...",
        "link": "https://toss.me/..." # 토스 구매 링크
    },
    {
        "name": "[버버리] 90s 트렌치 코트",
        "price": "120,000원",
        "img": "image_02.jpg",
        "desc": "단추 하나가 없어서 저렴하게 내놔요! 하지만 분위기 깡패...",
        "link": "https://toss.me/..."
    },
    {
        "name": "[나이키] 올드스쿨 바람막이",
        "price": "38,000원",
        "img": "image_03.jpg",
        "desc": "색감이 미쳤어요. 쿨톤 언니들 무조건 가져가세요!",
        "link": "https://toss.me/..."
    },
    # ... 이런 식으로 15개까지 계속 복사해서 추가하면 돼! ...
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
    
    st.stop() # 비밀번호 틀리면 여기서 멈춤 (아래 내용 안 보여줌)


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
            st.error(f"사진 파일({item['img']})을 못 찾았어요 ㅠㅠ")

    with col2:
        st.subheader(item["name"]) # 상품명
        st.write(f"**가격:** {item['price']}")
        st.info(item["desc"]) # 설명 (회색 박스 안에 예쁘게)
    
    # 🚨 여기에 경고 문구 추가!
    st.warning(f"💡 결제 시 배송 메모에 암호 **'{SECRET_PW}'**를 꼭 적어주세요! (미기재 시 취소)")
    
    st.link_button("👉 구매하러 가기", item["link"], type="primary")
        # 구매 버튼 (누르면 토스로 이동)
        st.link_button("👉 구매하러 가기 (선착순)", item["link"], type="primary")
    
    st.markdown("---") # 상품 사이 구분선

# 푸터
st.caption("ⓒ Greenloop VIP Secret Shop. Only for our best fans.")
