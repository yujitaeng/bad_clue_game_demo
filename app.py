import streamlit as st

# 세션 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = "theme"  # 처음엔 테마 선택 페이지로 시작
if "stage" not in st.session_state:
    st.session_state.stage = "intro"  # 게임 시작 시 초기 단계 설정

# 페이지 전환
if st.session_state.page == "theme":
    import theme_page  # 테마 선택 페이지
    theme_page.theme_page()  # theme_page() 함수 호출

elif st.session_state.page == "game":
    import game_page  # 게임 진행 페이지
    game_page.game_page()  # game_page() 함수 호출
