import streamlit as st

# 頁面標題與風格
st.set_page_config(page_title="印刷書背計算工具", layout="centered")

st.title("📖 印刷書背計算工具")
st.write("直接輸入參數，快速計算建議書背寬度。")

# 直接在代碼中定義紙張條數資料 (資料來源於你的條數表 )
# 你可以隨時在這裡增減紙張種類
paper_options = {
    "道林紙 80g": 10.5,
    "道林紙 100g": 13.5,
    "模造紙 80g": 9.5,
    "模造紙 100g": 12.0,
    "特級道林 120g": 15.0,
    "銅版紙 100g": 8.5,
    "銅版紙 150g": 13.0,
    "自定義紙張": 0.0
}

# --- 介面佈局 ---
col1, col2 = st.columns(2)

with col1:
    selected_name = st.selectbox("選擇內頁紙張：", list(paper_options.keys()))
    
    # 如果選自定義，則讓使用者輸入，否則自動帶入數值
    if selected_name == "自定義紙張":
        thickness = st.number_input("輸入單張條數 (μm)：", value=10.0, step=0.1)
    else:
        thickness = paper_options[selected_name]
        st.info(f"當前條數：{thickness} μm")

    pages = st.number_input("總頁數 (P)：", min_value=2, value=200, step=2)

with col2:
    cover_thickness = st.number_input("封面厚度 (條數)：", value=25.0, step=1.0, help="一般 250 磅封面約 25-30 條")
    
    # 計算公式 
    # (頁數 / 2) * (單張條數 / 100) + (封面條數 / 100)
    spine_width = (pages / 2) * (thickness / 100) + (cover_thickness / 100)

# --- 顯示結果 ---
st.divider()
st.subheader("計算結果")
st.metric(label="建議書背寬度", value=f"{spine_width:.2f} mm")

# 專業提醒
st.caption(f"公式依據：({pages}P / 2) × {thickness/100:.3f}mm + {cover_thickness/100:.2f}mm (封面)")
st.warning("💡 提示：此為理論值，實際製作時建議與印刷廠確認，或預留 0.1mm 的放數空間。")
