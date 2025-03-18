import streamlit as st
import openai
from dotenv import load_dotenv
import os
import re
from fuzzywuzzy import fuzz

# 데이터 로드
load_dotenv()

# OpenAI API 키 설정 (환경 변수로 설정하는 것을 권장)
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_llm(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "당신은 명탐정 코난의 추리 보조 역할을 합니다."},
                  {"role": "user", "content": prompt}],
        max_tokens=100
    )
    return response.choices[0].message.content

# 게임 페이지
def game_page():
    # 테마가 "나이트 바론 살인 사건"일 경우에만 진행
    if 'theme' in st.session_state and st.session_state.theme == "나이트 바론 살인 사건":
        # 각 단계별로 함수를 호출
        if st.session_state.stage == "intro":
            intro_page()
        elif st.session_state.stage == "crime_scene":
            crime_scene_page()
        elif st.session_state.stage == "clue_collection":
            clue_collection_page()
        elif st.session_state.stage == "deduction":
            deduction_page()

def intro_page():
    st.subheader("🏨 휴양지에 도착한 가람")
    st.image("https://image.tmdb.org/t/p/original/kz0cvX01HYFmxmJwygPPfrY8jgL.jpg")

    # 가람의 대사를 말풍선 형태로 출력
    garam_dialogue = "드디어 휴양지에 도착했어! 그런데 뭔가 심상치 않은 기운이 느껴지는데..."
    st.markdown(f"""
    <div style="
        background: rgba(20, 120, 60, 0.4); 
        padding: 15px 20px;
        border-radius: 20px; 
        max-width: 100%; 
        margin-bottom: 15px; 
        color: #fff; 
        font-weight: bold; 
        display: inline-block; 
    ">
        👦🏻 <b>가람:</b> {garam_dialogue}
    </div>
    """, unsafe_allow_html=True)

    if st.button("사건 현장으로 이동하기"):
        st.session_state.stage = "crime_scene"
        st.rerun()  # 페이지 새로 고침

def crime_scene_page():
    st.subheader("💥 사건 발생!")
    st.image("https://mblogthumb-phinf.pstatic.net/MjAyMDAyMDZfODgg/MDAxNTgwOTQ5MzYwMzUz.bg19Q9yMh4lSFgLI974wDuX3R_9qlo4WcNG3zuKssVsg.gue6LADj-0bB0y5LGnmdAdM3ixNmXGiuV4-pxKh514kg.JPEG.mijung9750/1580949358992.jpg?type=w800")
    st.markdown("""
    <div style="
        background: rgba(60, 60, 160, 0.4);
        padding: 15px 20px;
        border-radius: 20px;
        max-width: 100%;
        margin-bottom: 15px;
        color: #fff;
        font-weight: bold;
        display: inline-block;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    ">
        휴양지에서 열린 컴퓨터 콘테스트 도중, 한 참가자가 나이트 바론으로 인해 추락사했다.
    </div>
    """, unsafe_allow_html=True)

    if st.button("단서 수집 시작"):
        st.session_state.stage = "clue_collection"
        st.rerun()  # 페이지 새로 고침

def clue_collection_page():
    st.subheader("🔎 단서 수집")
    st.write("사건 현장을 조사하고 증거를 모아 범인을 찾아내세요!")
    st.image("https://img.freepik.com/premium-psd/shinichi-kudo-from-detective-conan-wearing-brown-hat-black-glasses-stands-front-brown-building-with-blue-sky-background-he-holds-magnifying-glass_1054285-15392.jpg?w=826")

    clues = {
        "🛏️피해자의 방": "피해자의 방에서 이상한 흔적을 발견했다... 창문이 열린 채로 있었다.",
        "👤목격자 진술": "목격자: '검은 그림자가 피해자를 따라가는 것을 봤어요!'",
        "💻컴퓨터 로그": "컴퓨터에 '나이트 바론'이라는 프로그램이 실행된 흔적이 있다. 범인이 디지털 흔적을 남긴 것 같다.",
        "🔦의문의 그림자": "사건 직전, 복도를 서성이던 의문의 그림자가 목격되었다.",
        "👣미확인 발자국": "비가 오지 않았는데도 복도에 젖은 발자국이 남아 있었다."
    }

    # 카드로 단서 보여주기
    cols = st.columns(3)  # 3개의 카드로 나누기
    for i, (clue_name, clue_description) in enumerate(clues.items()):
        with cols[i % 3]:
            # 카드 형식으로 감추어진 단서를 추가
            with st.expander(clue_name):  # 클릭 시 펼쳐지는 카드
                st.markdown(f"<div style='background: rgba(80, 60, 30, 0.4); padding: 15px; margin-bottom: 15px; border-radius: 10px;'>{clue_description}</div>", unsafe_allow_html=True)

    if st.button("추리 시작하기"):
        st.session_state.stage = "deduction"
        st.rerun()  # 페이지 새로 고침

# clues 정의
clues = {
        "🛏️피해자의 방": "피해자의 방에서 이상한 흔적을 발견했다... 창문이 열린 채로 있었다.",
        "👤목격자 진술": "목격자: '검은 그림자가 피해자를 따라가는 것을 봤어요!'",
        "💻컴퓨터 로그": "컴퓨터에 '나이트 바론'이라는 프로그램이 실행된 흔적이 있다. 범인이 디지털 흔적을 남긴 것 같다.",
        "🔦의문의 그림자": "사건 직전, 복도를 서성이던 의문의 그림자가 목격되었다.",
        "👣미확인 발자국": "비가 오지 않았는데도 복도에 젖은 발자국이 남아 있었다."
    }

# clue_phrases를 사용하여 유사도 체크
clue_phrases = list(clues.values())

# clue_keywords 정의 (각 단서의 주요 단어들)
clue_keywords = set()
for clue in clues.values():
    clue_keywords.update(re.findall(r'\b\w+\b', clue))

def check_similarity(user_input, clue_phrases, threshold=80):
    """
    유사도 비교하여 threshold 이상의 유사도를 가진 단서를 찾는 함수
    """
    similar_clues = []
    for clue in clue_phrases:
        similarity = fuzz.partial_ratio(user_input, clue)
        if similarity >= threshold:
            similar_clues.append(clue)
    return similar_clues

def deduction_page():
    st.subheader("🧠 추리 시간")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXp1Hv8x8MCzlAh3p_3Z1qEShmSeqhlFchtw&s")
    
    # 등장인물 배경 소개
    st.markdown("### 등장인물 배경")
    st.markdown("""
        **A: 프로그래머**  
        프로그래머는 최근 나이트 바론 프로그램을 개발하였으며, 대회에 참가한 다른 사람들에게 경쟁심을 느끼고 있었다. 그는 과거에도 디지털 기술을 이용한 범죄에 연루된 적이 있다.

        **B: 대회 주최자**  
        대회 주최자는 최근 몇몇 참가자들과 트러블을 겪었고, 큰 상금을 걸어두어 참가자들에게 큰 압박감을 주었다. 그는 모든 참가자의 움직임을 철저히 감시하고 있었다.

        **C: 참가자**  
        참가자는 몇 년간 컴퓨터 대회에 참가해온 경력이 있으며, 대회에서 항상 상위권을 차지해왔다. 그러나 최근 몇 가지 의심스러운 행동을 보였다.
    """)
    
    user_input = st.text_input("추리를 입력하세요 (단서 기반 가설 작성)")
    if st.button("LLM에게 추리 확인"):
        if user_input:
            # 사용자 입력에서 단어 추출
            user_input_words = re.findall(r'\b\w+\b', user_input)

            # 사용자가 입력한 단어 중 clue_keywords에 포함된 단어가 있는지 체크
            matching_keywords = set(user_input_words) & clue_keywords
            
            if matching_keywords:
                result = f"추론 결과: '{', '.join(matching_keywords)}'는 유력한 단서로 판단됩니다."
            else:
                result = f"추론 결과: 입력한 내용은 유력한 단서와 일치하지 않습니다. 다시 확인해 보세요."
            
            st.markdown(f"""
            <div style="background: rgba(200, 100, 50, 0.4); padding: 15px 20px; border-radius: 20px; max-width: 80%; margin-bottom: 15px; color: #fff; font-weight: bold; display: inline-block; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                {result}
            </div>
            """, unsafe_allow_html=True)

    suspect = st.selectbox("누가 범인일까요?", ["A: 프로그래머", "B: 대회 주최자", "C: 참가자"], index=0)
    
    # 오답 여부 플래그 초기화
    if "is_wrong" not in st.session_state:
        st.session_state.is_wrong = False

    # 범인 지목하기
    if st.button("범인 지목하기"):
        if suspect == "A: 프로그래머":
            st.success("🎉 정답! 프로그래머가 나이트 바론으로 변장해 범행을 저질렀습니다!")
            st.balloons()  # 풍선 애니메이션
            st.session_state.stage = "theme"  # 다음 단계로 이동
            st.session_state.is_wrong = False  # 정답 시 오답 상태 초기화
        else:
            # 오답 처리 (플래그 업데이트)
            st.session_state.is_wrong = True
    
    # 오답일 경우 메시지 유지
    if st.session_state.is_wrong:
        st.error("❌ 오답! 다시 사건을 조사해 보세요.")
            

