import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

# =========================
# 페이지 설정
# =========================
st.set_page_config(
    page_title="다기능 스마트 계산기",
    page_icon="🔢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CSS 스타일 (모던 배경 + 글라스모피즘)
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

:root{
  --bg-gradient-1: linear-gradient(120deg, #0f172a 0%, #081029 40%, #041226 100%);
  --bg-gradient-2: radial-gradient(60% 60% at 10% 20%, rgba(96,165,250,0.08), transparent 20%), radial-gradient(60% 60% at 90% 80%, rgba(124,58,237,0.06), transparent 18%);
  --card-bg: rgba(255,255,255,0.03);
  --card-border: rgba(255,255,255,0.06);
  --accent: #60a5fa;
}

/* 전체 배경 그라데이션 */
html, body, [data-testid="stAppViewContainer"] {
  height: 100%;
  background: var(--bg-gradient-1), var(--bg-gradient-2) !important;
  background-attachment: fixed;
  font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
}

/* 메인 컨텐츠 카드 (글라스모피즘) */
[data-testid="stMain"] {
  background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
  padding: 28px 32px 40px 32px;
  border-radius: 16px;
  box-shadow: 0 8px 40px rgba(2,6,23,0.6);
  border: 1px solid var(--card-border);
  backdrop-filter: blur(8px) saturate(120%);
}

/* 제목 색상 */
h1, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
  color: #e6eef8;
}

/* 사이드바 스타일 */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(12,18,36,0.95), rgba(2,6,23,0.92));
    border-right: 1px solid rgba(255,255,255,0.03);
    padding: 20px 18px 40px 18px;
}

/* 사이드바 글씨 */
section[data-testid="stSidebar"] * {
    color: #dbeafe !important;
    font-weight: 520;
}

/* 입력 박스, 숫자 입력, 텍스트 입력 스타일 */
.stTextInput>div>div>input, .stNumberInput>div>div>input, .stSelectbox>div>div>div>div>input {
    background: rgba(255,255,255,0.02) !important;
    color: #e6eef8 !important;
    border: 1px solid rgba(255,255,255,0.05) !important;
    border-radius: 10px !important;
}

/* Selectbox 내부 텍스트 */
.stSelectbox div[data-baseweb="select"] > div {
    background-color: transparent !important;
    color: #dbeafe !important;
}

/* Radio 버튼 */
div[role="radiogroup"] label {
    color: #dbeafe !important;
}

/* 버튼 스타일 */
.stButton button {
    width: 100%;
    background: linear-gradient(90deg, #2563eb 0%, #7c3aed 100%);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 10px 14px;
    font-weight: 600;
    box-shadow: 0 6px 18px rgba(99,102,241,0.18);
}

.stButton button:hover {
    filter: brightness(1.04);
}

/* 경고 / 성공 메시지 색상 개선 */
.stAlert>div[role="status"] {
    border-radius: 10px;
}

/* Matplotlib 플롯 스타일 */
[data-testid="stImage"] img {
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(2,6,23,0.6);
}

/* footer / caption 색상 */
footer, .stCaption {
  color: rgba(220,230,255,0.6) !important;
}

/* 반응형 패딩 */
@media (max-width: 768px) {
  [data-testid="stMain"] { padding: 16px; }
  section[data-testid="stSidebar"] { padding: 12px; }
}

</style>
""", unsafe_allow_html=True)

# =========================
# 제목
# =========================
st.title("🔢 다기능 스마트 계산기")
st.write("사칙연산, 로그연산, 함수 그래프를 지원하는 계산기입니다.")

# =========================
# 기능 선택
# =========================
operation = st.sidebar.selectbox(
    "원하는 기능을 선택하세요",
    [
        "더하기 (+)",
        "빼기 (-)",
        "곱하기 (*)",
        "나누기 (/)",
        "모듈러 (%, 나머지)",
        "지수 (^)",
        "로그 (log)",
        "함수 그래프"
    ]
)

st.subheader(f"현재 선택된 기능: {operation}")

# ==================================================
# 함수 그래프
# ==================================================
if operation == "함수 그래프":

    st.write("### 함수 그래프 그리기")

    st.info("""
    사용 예시

    x**2
    sin(x)
    cos(x)
    exp(x)
    log(x)
    sqrt(x)
    """)

    expression = st.text_input(
        "함수를 입력하세요",
        value="x**2"
    )

    x_min = st.number_input(
        "x 최소값",
        value=-10.0
    )

    x_max = st.number_input(
        "x 최대값",
        value=10.0
    )

    if st.button("그래프 그리기"):

        try:
            x = np.linspace(x_min, x_max, 1000)

            allowed = {
                "x": x,
                "sin": np.sin,
                "cos": np.cos,
                "tan": np.tan,
                "sqrt": np.sqrt,
                "log": np.log,
                "exp": np.exp,
                "pi": np.pi,
                "e": np.e,
                "abs": np.abs
            }

            y = eval(expression, {"__builtins__": {}}, allowed)

            fig, ax = plt.subplots(figsize=(8, 5), facecolor='none')
            ax.plot(x, y, color="#60a5fa", linewidth=2)

            ax.set_facecolor('none')
            ax.set_title(f"y = {expression}", color='#e6eef8')
            ax.set_xlabel("x", color='#dbeafe')
            ax.set_ylabel("y", color='#dbeafe')
            ax.tick_params(colors='#cfe8ff')
            ax.grid(True, color='white', alpha=0.06)

            for spine in ax.spines.values():
                spine.set_color((1, 1, 1, 0.08))

            st.pyplot(fig)

        except Exception as e:
            st.error(f"함수를 계산할 수 없습니다.\n오류: {e}")

# ==================================================
# 로그 계산
# ==================================================
elif operation == "로그 (log)":

    num = st.number_input(
        "진수(Value)를 입력하세요 (0보다 커야 함)",
        value=1.0
    )

    base_choice = st.radio(
        "로그 밑(Base)",
        [
            "상용로그 (밑 10)",
            "자연로그 (밑 e)",
            "직접 입력"
        ]
    )

    if base_choice == "상용로그 (밑 10)":
        base = 10.0

    elif base_choice == "자연로그 (밑 e)":
        base = math.e

    else:
        base = st.number_input(
            "밑(Base)을 입력하세요",
            value=2.0
        )

    if st.button("계산하기"):

        if num <= 0 or base <= 0 or base == 1:
            st.error("❌ 로그의 정의역 조건을 만족하지 않습니다.")

        else:

            if base_choice == "자연로그 (밑 e)":

                result = math.log(num)

                st.success(
                    f"ln({num}) = {result:.6f}"
                )

            else:

                result = math.log(num, base)

                st.success(
                    f"log₍{base}₎({num}) = {result:.6f}"
                )

# ==================================================
# 일반 계산기
# ==================================================
else:

    num1 = st.number_input(
        "첫 번째 숫자",
        value=0.0
    )

    num2 = st.number_input(
        "두 번째 숫자",
        value=0.0
    )

    if st.button("계산하기"):

        if operation == "더하기 (+)":

            result = num1 + num2
            st.success(f"{num1} + {num2} = {result}")

        elif operation == "빼기 (-)":

            result = num1 - num2
            st.success(f"{num1} - {num2} = {result}")

        elif operation == "곱하기 (*)":

            result = num1 * num2
            st.success(f"{num1} × {num2} = {result}")

        elif operation == "나누기 (/)":

            if num2 == 0:
                st.error("❌ 0으로 나눌 수 없습니다.")
            else:
                result = num1 / num2
                st.success(f"{num1} ÷ {num2} = {result}")

        elif operation == "모듈러 (%, 나머지)":

            if num2 == 0:
                st.error("❌ 0으로 나눈 나머지는 계산할 수 없습니다.")
            else:
                result = num1 % num2
                st.success(
                    f"{num1} % {num2} = {result}"
                )

        elif operation == "지수 (^)":

            try:
                result = math.pow(num1, num2)

                st.success(
                    f"{num1}^{num2} = {result}"
                )

            except OverflowError:

                st.error(
                    "❌ 숫자가 너무 커서 계산할 수 없습니다."
                )

# =========================
# 하단 정보
# =========================
st.markdown("---")
st.caption("Smart Calculator v2.0 | Streamlit")
