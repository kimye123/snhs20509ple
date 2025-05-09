import streamlit as st

st.title("k")
st.info(
    "안녕하세요 저는 포도입니다")
st.title(
    "과수원")
st.markdown("----")



st.image("https://blog.malcang.com/wp-content/uploads/2024/03/1-1.png")
st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExejRqcmU5cnB1cDMxMTh6aDV5NjNuNTJyaWhnYXVxdHE0N3dsbWF1OCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/d8D5RoR8adbJaFF3TV/giphy.gif")
st.code("""
import streamlit as st
st.title('Hello World')
""", language="python")
st.link_button("연결할 url을 이 다음 변수에 써주세요!", 'https://docs.streamlit.io/develop/quick-reference/cheat-sheet')
# st.columns(n): 화면을 n개의 수직 열로 나눕니다
col1, col2 = st.columns(2)  # 2개의 열 생성

with col1:
    st.write("왼쪽 열입니다.")  # 첫 번째 열에 내용 작성
with col2:
    st.write("오른쪽 열입니다.")  # 두 번째 열에 내용 작성
    # st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

with tab1:
    st.write("탭 1에 해당하는 내용입니다.")  # 첫 번째 탭에 표시할 내용
with tab2:
    st.write("탭 2에 해당하는 내용입니다.")  # 두 번째 탭에 표시할 내용
    # st.expander("제목"): 내용을 접었다 펼 수 있는 컨테이너입니다
with st.expander("ℹ️ 자세한 설명 보기"):
    st.write("여기에 상세 설명이나 보조 정보를 넣을 수 있습니다.")
    # st.sidebar: 사이드바 영역에 콘텐츠를 배치합니다
st.sidebar.title("📌 사이드바 메뉴")
option = st.sidebar.selectbox("옵션을 선택하세요", ["A", "B", "C"])
st.write("선택한 옵션:", option)
name=st.text_area("이름을 입력해주세요")
if name=="감자":
  st.success(name+"님 반갑습니다다")
else:
     st.error("아....")
st.error(name+"님 안녕하세요")
# 여러 옵션 중 하나 선택
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
st.write("선택한 성별:", gender)
# 카메라로 사진 촬영
image_data = st.camera_input("사진을 찍어보세요")
if image_data:
    st.image(image_data)
