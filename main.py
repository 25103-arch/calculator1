import streamlit as st
import math

# 웹앱 제목 설정
st.title("🔢 다기능 스마트 계산기")
st.write("사칙연산부터 로그연산까지 가능한 웹 계산기입니다.")

# 사이드바에서 연산 종류 선택
operation = st.sidebar.selectbox(
    "원하는 연산을 선택하세요",
    ["더하기 (+)", "빼기 (-)", "곱하기 (*)", "나누기 (/)", "모듈러 (%, 나머지)", "지수 (^)", "로그 (log)"]
)

st.write(f"### 현재 선택된 연산: {operation}")

# 로그 연산과 일반 연산은 입력 화면을 다르게 구성하는 것이 좋습니다.
if operation == "로그 (log)":
    # 로그 연산 입력
    num = st.number_input("진수(Value)를 입력하세요 (0보다 커야 합니다)", value=1.0, step=1.0)
    base_choice = st.radio("로그의 밑(Base)을 선택하세요", ["상용로그 (밑 10)", "자연로그 (밑 e)", "직접 입력"])
    
    if base_choice == "상용로그 (밑 10)":
        base = 10.0
    elif base_choice == "자연로그 (밑 e)":
        base = math.e
    else:
        base = st.number_input("밑(Base)을 직접 입력하세요 (0보다 크고 1이 아니어야 합니다)", value=2.0, step=1.0)

    # 계산 버튼
    if st.button("계산하기"):
        if num <= 0 or base <= 0 or base == 1:
            st.error("❌ 로그의 정의 조건에 맞지 않습니다. 입력값을 확인해 주세요.")
        else:
            if base_choice == "자연로그 (밑 e)":
                result = math.log(num)
                st.success(ln"Result: ln({num}) = {result:.4f}")
            else:
                result = math.log(num, base)
                st.success(f"Result: log_{base}({num}) = {result:.4f}")

else:
    # 일반 연산 입력 (숫자 2개 필요)
    num1 = st.number_input("첫 번째 숫자를 입력하세요", value=0.0, step=1.0)
    num2 = st.number_input("두 번째 숫자를 입력하세요", value=0.0, step=1.0)
    
    # 계산 버튼
    if st.button("계산하기"):
        if operation == "더하기 (+)":
            result = num1 + num2
            st.success(f" 결과: {num1} + {num2} = {result}")
            
        elif operation == "빼기 (-)":
            result = num1 - num2
            st.success(f" 결과: {num1} - {num2} = {result}")
            
        elif operation == "곱하기 (*)":
            result = num1 * num2
            st.success(f" 결과: {num1} × {num2} = {result}")
            
        elif operation == "나누기 (/)":
            if num2 == 0:
                st.error("❌ 0으로 나눌 수 없습니다.")
            else:
                result = num1 / num2
                st.success(f" 결과: {num1} ÷ {num2} = {result}")
                
        elif operation == "모듈러 (%, 나머지)":
            if num2 == 0:
                st.error("❌ 0으로 나눈 나머지는 계산할 수 없습니다.")
            else:
                result = num1 % num2
                st.success(f" 결과: {num1}을(를) {num2}(으)로 나눈 나머지 = {result}")
                
        elif operation == "지수 (^)":
            try:
                result = math.pow(num1, num2)
                st.success(f" 결과: {num1}의 {num2}제곱 = {result}")
            except OverflowError:
                st.error("❌ 숫자가 너무 커서 계산할 수 없습니다.")
