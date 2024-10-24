import streamlit as st
import random
timetable = [
    "18:20 豊後竹田行",
    "18:44 中判田行",
    "19:05 豊後竹田行",
    "19:26 三重町行",
    "19:49 豊後竹田行",
    "20:10 中判田行",
    "20:35 豊後竹田行",
    "21:09 犬飼行",
    "21:33 豊後竹田行",
    "22:13 豊後竹田行",
    "22:50 豊後竹田行",
    "23:30 三重町行"
]

# アプリケーションのタイトル
st.title("ランダム時刻抽出アプリ")

# 説明文
st.write("このアプリは、提供された時刻表からランダムに時刻を抽出します。")

# ボタンを作成
if st.button("ランダムな時刻を抽出"):
    # ランダムに時刻を選択
    random_time = random.choice(timetable)
    
    # 結果を表示
    st.success(f"抽出された時刻: {random_time}")

# 全ての時刻を表示
st.subheader("時刻表")
for time in timetable:
    st.write(time)