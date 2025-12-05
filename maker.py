import streamlit as st
import requests
import base64
from io import BytesIO

# ==========================================
# [설정] 여기에 아까 복사한 n8n Webhook URL을 붙여넣으세요! (기존 주소 그대로 쓰면 돼!)
N8N_WEBHOOK_URL = "https://sungmi.app.n8n.cloud/webhook/vintage-detail-maker"
# ==========================================

# 페이지 기본 설정
st.set_page_config(page_title="그린루프 빈티지 에디터", page_icon="♻️", layout="centered")

# 헤더 디자인
st.title("♻️ 그린루프 상세페이지 메이커")
st.markdown("---")
st.write("사진과 기초 정보만 입력하면, 판매를 부르는 상세페이지가 완성됩니다!")

# --- 입력 폼 ---
with st.form("product_form"):
    # 1. 이미지 업로드
    uploaded_file = st.file_uploader("📸 옷 사진을 올려주세요 (필수)", type=["jpg", "png", "jpeg"])
    
    # 미리보기 기능
    if uploaded_file is not None:
        st.image(uploaded_file, caption="업로드된 사진", use_column_width=True)

    st.markdown("### 📝 기초 정보 입력")
    
    # 레이아웃 2단 분리 (여기가 들여쓰기 중요한 부분!)
    col1, col2 = st.columns(2)
    
    with col1:
        # [수정됨] 브랜드가 없으면 자동으로 Vintage 처리
        brand_input = st.text_input("브랜드 (없으면 비워두세요)")
        if brand_input == "":
            brand = "Vintage"
        else:
            brand = brand_input

    with col2:
        # [수정됨] 사이즈 입력 안내 문구 변경
        size_info = st.text_input("사이즈 (실측 cm, S/M/L, 44/55 등)")
    
    notes = st.text_area("컨디션 및 특이사항 (예: 상태 A급, 소매에 작은 이염 있음)")

    # 제출 버튼
    submitted = st.form_submit_button("✨ AI 상세페이지 생성하기 (클릭)")


# --- 처리 로직 ---
if submitted:
    if uploaded_file is None:
        st.error("⚠️ 사진을 반드시 업로드해주세요!")
    elif not N8N_WEBHOOK_URL.startswith("http"):
        st.error("⚠️ 코드 상단에 n8n Webhook URL을 올바르게 입력해주세요!")
    else:
        with st.spinner("그린루프 AI가 옷을 분석하고 글을 쓰는 중입니다... (약 10~20초 소요)"):
            try:
                # 1. 이미지를 base64 텍스트로 변환 (n8n 전송용)
                bytes_data = uploaded_file.getvalue()
                base64_image = base64.b64encode(bytes_data).decode('utf-8')

                # 2. n8n으로 보낼 데이터 묶음 만들기
                payload = {
                    "image_base64": base64_image,
                    "brand": brand,
                    "size": size_info,
                    "notes": notes
                }

                # 3. n8n으로 데이터 전송 (POST 요청)
                response = requests.post(N8N_WEBHOOK_URL, json=payload)

                # 4. 결과 받기 및 표시
                if response.status_code == 200:
                    result_text = response.json().get("result", "생성된 결과가 없습니다.")
                    st.success("🎉 상세페이지 생성 완료!")
                    st.markdown("### 👇 아래 내용을 복사해서 사용하세요!")
                    # 텍스트 영역에 결과 표시 (복사하기 편함)
                    st.text_area("결과물", value=result_text, height=400)
                else:
                    st.error(f"오류가 발생했습니다. (상태 코드: {response.status_code})")
                    st.write(response.text)

            except Exception as e:
                st.error(f"에러 발생: {e}")

# 하단 푸터
st.markdown("---")
st.caption("ⓒ Greenloop Vintage AI Editor. Created for top sellers.")