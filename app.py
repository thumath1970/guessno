import streamlit as st
import random

# 設定網頁標題
st.set_page_config(page_title="猜數字遊戲", page_icon="🎯")
st.title("🎯 猜數字小遊戲")

# 初始化 Session State（記錄遊戲狀態與目標數字）
if "target_number" not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.message = ""

st.write("我已經想好了一個 **1 到 100** 之間的數字，請猜猜看！")

# 重置遊戲函式
def reset_game():
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.session_state.message = ""

# 使用者輸入框
guess = st.number_input("請輸入你猜的數字：", min_value=1, max_value=100, step=1, value=50)

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("提交答案", disabled=st.session_state.game_over):
        st.session_state.attempts += 1
        
        # 使用 f-string (字串插值) 動態產生提示字串
        if guess < st.session_state.target_number:
            st.session_state.message = f"【第 {st.session_state.attempts} 次】你猜的是 {guess}，太小了！"
        elif guess > st.session_state.target_number:
            st.session_state.message = f"【第 {st.session_state.attempts} 次】你猜的是 {guess}，太大了！"
        else:
            st.session_state.message = f"🎉 恭喜答對！目標數字就是 {st.session_state.target_number}，你一共猜了 {st.session_state.attempts} 次！"
            st.session_state.game_over = True

with col2:
    if st.button("重新開始"):
        reset_game()
        st.rerun()

# 顯示提示訊息
if st.session_state.message:
    if st.session_state.game_over:
        st.success(st.session_state.message)
    else:
        st.warning(st.session_state.message)
