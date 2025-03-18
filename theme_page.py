# theme_page.py
import streamlit as st

# 테마 선택 페이지
def theme_page():
    st.title("🔍 배드클루: 추리 게임")
    st.write("명탐정이 되어 사건을 해결하세요! 다양한 테마 중 하나를 선택해 추리를 시작해 보세요.")
    st.image("https://img.freepik.com/free-photo/truth-concept-composition-detective-desk_23-2149051321.jpg?t=st=1741827869~exp=1741831469~hmac=e68ee60fbe21a40ab38f5d24a54e53adf4b0f2d0454924a462aa997f959d3c4d&w=826")

    # 테마 선택
    theme = st.selectbox("🎭 테마 선택", ["테마 선택하기", "나이트 바론 살인 사건", "COMING SOON"], index=0)

    if theme == "나이트 바론 살인 사건":
        st.header("🕵️‍♂️ 나이트 바론 살인 사건")
        st.write("휴양지에서 열린 컴퓨터 콘테스트. 나이트 바론으로 변장한 누군가가 나타나고, 의문의 추락사가 발생한다.")
        st.image("https://image.tmdb.org/t/p/original/j2f0LOvPSh5ehJByNYOlJVSQhlO.jpg")
        
        if st.button("게임 시작하기"):
            st.session_state.page = "game"  # 페이지를 "game"으로 변경하여 게임 페이지로 전환
            st.session_state.theme = "나이트 바론 살인 사건"  # 테마 정보 저장
            st.session_state.stage = "intro"  # 게임 첫 번째 단계로 설정
            st.rerun()  # 새로고침하여 게임 페이지 로드

    elif theme == "COMING SOON":
        st.header("COMING SOON")
        st.write("두 개의 달이 하나가 되는 순간 찾아오겠습니다.")
        st.image("https://pbs.twimg.com/media/EcfML_FUMAERyu7?format=jpg&name=900x900")
