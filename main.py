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
    layout="centered"
)

# =========================
# CSS 스타일
# =========================
st.markdown("""
<style>

/* 사이드바 */
section[data-testid="stSidebar"] {
    background-color: #1e293b;
}

/* 사이드바 글씨 */
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"] > div {
    background-color: white !important;
    color: black !important;
}

/* Radio 버튼 */
div[role="radiogroup"] label {
    color: white !important;
}

/* 버튼 */
.stButton button {
    width: 100%;
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    border: none;
}

.stButton button:hover {
    background-color: #1d4ed8;
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

            fig, ax = plt.subplots(figsize=(8, 5))
            ax.plot(x, y, color="blue", linewidth=2)

            ax.set_title(f"y = {expression}")
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.grid(True)

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
