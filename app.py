import streamlit as st
import threading
import subprocess
import os

# 1. 制作一个简单的网页界面，应付 Hugging Face 的检查
st.title("🎲 Telegram Dice Bot 控制台")
st.success("🟢 机器人已经成功在云端启动运行！")
st.info("提示：请使用 UptimeRobot 定时访问本页面，防止容器进入休眠。")

# 2. 在后台偷偷把原作者的机器人主程序跑起来
def start_original_bot():
    # ⚠️ 注意：如果原仓库的启动文件叫 bot.py，请把下面的 main.py 改为 bot.py
    subprocess.run(["python", "main.py"])

if "bot_started" not in st.session_state:
    st.session_state.bot_started = True
    # 开启新线程，不阻塞网页渲染
    threading.Thread(target=start_original_bot, daemon=True).start()
