import streamlit as st
import random
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="瑪利諾外來語詞彙表 翻牌挑戰網站 v2",
    page_icon="🎴",
    layout="centered"
)

# --- Vocabulary Dataset ---
JAPAN_ENG_HAN = [
    # 台語羅馬字
    {"roman": "a-sa-lih", "kanji": "阿莎力 / 乾脆", "english": "generously / clean-cut, straight forward, wholeheartedly", "type": "台語羅馬字", "origin": "日語借詞 (Asari)"},
    {"roman": "a-su-phí-lín", "kanji": "阿斯匹林", "english": "aspirin", "type": "台語羅馬字", "origin": "英語借詞 (Aspirin)"},
    {"roman": "ak-sé-lé-tah", "kanji": "加速器", "english": "accelerator", "type": "台語羅馬字", "origin": "英語借詞 (Accelerator)"},
    {"roman": "I-tiân", "kanji": "伊甸，地堂，樂園", "english": "Eden", "type": "台語羅馬字", "origin": "英語/聖經借詞 (Eden)"},
    {"roman": "ín-tsih", "kanji": "英吋", "english": "inch, English inch", "type": "台語羅馬字", "origin": "英語借詞 (Inch)"},
    {"roman": "e-lé-bé-tà", "kanji": "電梯", "english": "elevator", "type": "台語羅馬字", "origin": "英語借詞 (Elevator)"},
    {"roman": "e-ná-mé-luh", "kanji": "釉，亮光漆", "english": "enamel", "type": "台語羅馬字", "origin": "英語借詞 (Enamel)"},
    {"roman": "óo-bà", "kanji": "大衣", "english": "overcoat, top coat", "type": "台語羅馬字", "origin": "英語借詞 (Overcoat)"},
    {"roman": "ai-noo-khooh", "kanji": "混種，混血兒", "english": "mixed blood, child of mixed ancestry", "type": "台語羅馬字", "origin": "日語/阿伊努語借詞"},
    {"roman": "ia̋n-jín", "kanji": "發動機", "english": "engine", "type": "台語羅馬字", "origin": "英語借詞 (Engine)"},
    {"roman": "io-koh", "kanji": "酸乳酪，優酪乳，養樂多", "english": "yogurt", "type": "台語羅馬字", "origin": "英語/日語借詞 (Yogurt)"},
    {"roman": "ió-lo-tsín-khih", "kanji": "碘酒", "english": "iodine", "type": "台語羅馬字", "origin": "德語/英語借詞 (Iodine)"},
    {"roman": "uá-suh-lôo", "kanji": "瓦斯爐", "english": "gas stove", "type": "台語羅馬字", "origin": "荷蘭語/英語借詞 (Gas)"},
    {"roman": "ui-sū-kī", "kanji": "威士忌酒", "english": "whisky", "type": "台語羅馬字", "origin": "英語借詞 (Whisky)"},
    {"roman": "uai-siá-tsuh", "kanji": "白櫬衫", "english": "white dress shirt", "type": "台語羅馬字", "origin": "英語借詞 (White shirt)"},
    {"roman": "pin-kó", "kanji": "賓果", "english": "bingo", "type": "台語羅馬字", "origin": "英語借詞 (Bingo)"},
    {"roman": "pe-gèn", "kanji": "醃肉，培根", "english": "bacon", "type": "台語羅馬字", "origin": "英語借詞 (Bacon)"},
    {"roman": "pó-lîng-kiû", "kanji": "保齡球", "english": "bowling", "type": "台語羅馬字", "origin": "英語借詞 (Bowling)"},
    {"roman": "phah-buh", "kanji": "酒店", "english": "pub, tavern", "type": "台語羅馬字", "origin": "英語借詞 (Pub)"},
    {"roman": "phi-sah", "kanji": "披薩，比薩", "english": "pizza", "type": "台語羅馬字", "origin": "義大利語借詞 (Pizza)"},
    {"roman": "phi-sú-tóng", "kanji": "活塞", "english": "piston", "type": "台語羅馬字", "origin": "法語/英語借詞 (Piston)"},
    {"roman": "phu-lo-phe-la", "kanji": "螺旋槳", "english": "screw propeller", "type": "台語羅馬字", "origin": "英語借詞 (Propeller)"},
    {"roman": "phuh-lá-guh", "kanji": "火星塞", "english": "spark plug", "type": "台語羅馬字", "origin": "英語借詞 (Plug)"},
    {"roman": "phòm-pù", "kanji": "抽水機，抽", "english": "water pump", "type": "台語羅馬字", "origin": "荷蘭語/英語借詞 (Pump)"},
    {"roman": "ba-tah", "kanji": "牛奶油", "english": "butter, tallow", "type": "台語羅馬字", "origin": "英語借詞 (Butter)"},
    {"roman": "bi-tá-mín", "kanji": "維他命，維生素", "english": "vitamin", "type": "台語羅馬字", "origin": "拉丁語/英語借詞 (Vitamin)"},
    {"roman": "ma-tsih", "kanji": "麻吉，好友", "english": "good friend, match", "type": "台語羅馬字", "origin": "英語借詞 (Match)"},
    {"roman": "má-sú-khuh", "kanji": "口罩", "english": "mask", "type": "台語羅馬字", "origin": "英語借詞 (Mask)"},
    {"roman": "máng-gà", "kanji": "漫畫", "english": "cartoon", "type": "台語羅馬字", "origin": "日語借詞 (Manga)"},
    {"roman": "mái-khù", "kanji": "擴聲機，麥克風", "english": "microphone", "type": "台語羅馬字", "origin": "英語借詞 (Mic)"},
    {"roman": "là-pah", "kanji": "喇叭", "english": "claxon", "type": "台語羅馬字", "origin": "荷蘭語/日語借詞 (Lappa)"},
    {"roman": "nâi-lóng", "kanji": "尼龍", "english": "nylon", "type": "台語羅馬字", "origin": "英語借詞 (Nylon)"},
    {"roman": "khi-moo-tsih", "kanji": "心情，情緒", "english": "mood, feelings", "type": "台語羅馬字", "origin": "日語借詞 (Kimochi)"},
    {"roman": "khu-lá-buh", "kanji": "俱樂部", "english": "club, bar", "type": "台語羅馬字", "origin": "英語借詞 (Club)"},
    {"roman": "khú/coo", "kanji": "酷", "english": "cool, good, great", "type": "台語羅馬字", "origin": "英語借詞 (Cool)"},
    {"roman": "khe-tsiap-puh", "kanji": "蕃茄醬", "english": "ketchup tomato", "type": "台語羅馬字", "origin": "閩南語原詞/英語回借 (Ketchup)"},
    {"roman": "tsio-ko-lei-to", "kanji": "巧克力，朱古力", "english": "chocolate", "type": "台語羅馬字", "origin": "西班牙語/英語借詞 (Chocolate)"},
    {"roman": "tshí-juh/tshí-suh", "kanji": "乳酪，起司", "english": "cheese", "type": "台語羅馬字", "origin": "英語借詞 (Cheese)"},
    {"roman": "sa-si-mih", "kanji": "生魚片", "english": "sashimi", "type": "台語羅馬字", "origin": "日語借詞 (Sashimi)"},
    {"roman": "suh-kuh-tà", "kanji": "速克達", "english": "scooter", "type": "台語羅馬字", "origin": "英語借詞 (Scooter)"},
    {"roman": "há-muh", "kanji": "火腿，燻腿", "english": "ham", "type": "台語羅馬字", "origin": "英語借詞 (Ham)"},
    {"roman": "hoo-theh-luh", "kanji": "旅館，大飯店", "english": "hotel", "type": "台語羅馬字", "origin": "法語/英語借詞 (Hotel)"},
    # 日語羅馬字
    {"roman": "guliselin", "kanji": "甘油", "english": "glycerine", "type": "日語羅馬字", "origin": "日語音譯 (Glycerine)"},
    {"roman": "pasento", "kanji": "百分比", "english": "percent", "type": "日語羅馬字", "origin": "日語音譯 (Pasento)"},
    {"roman": "biru", "kanji": "啤酒", "english": "beer", "type": "日語羅馬字", "origin": "日語音譯 (Biru)"},
    {"roman": "beluto", "kanji": "帶子，地帶", "english": "belt, band, sash, ribbon", "type": "日語羅馬字", "origin": "日語音譯 (Beluto)"},
    {"roman": "brei-ki", "kanji": "煞車，煞車器", "english": "brake", "type": "日語羅馬字", "origin": "日語音譯 (Brake)"},
    {"roman": "bro-ka", "kanji": "經紀人，掮客", "english": "broker, agent", "type": "日語羅馬字", "origin": "日語音譯 (Broker)"},
    {"roman": "maskou", "kanji": "口罩", "english": "gas mask", "type": "日語羅馬字", "origin": "日語音譯 (Gas mask)"},
    {"roman": "mahula", "kanji": "滅音器，消音器", "english": "muffler", "type": "日語羅馬字", "origin": "日語音譯 (Muffler)"},
    # 英語羅馬字
    {"roman": "BB call", "kanji": "呼叫器，傳呼機，BB call", "english": "beeper", "type": "英語羅馬字", "origin": "英語原文"},
    {"roman": "gasolin", "kanji": "汽油", "english": "gasoline", "type": "英語羅馬字", "origin": "英語原文"},
    {"roman": "model", "kanji": "模特兒", "english": "model", "type": "英語羅馬字", "origin": "英語原文"},
    {"roman": "mosaik", "kanji": "剪貼", "english": "mosaic, cut out and paste", "type": "英語羅馬字", "origin": "英語原文"},
    {"roman": "SARS", "kanji": "SARS，嚴重急性呼吸道感染症候群", "english": "SARS", "type": "英語羅馬字", "origin": "英語縮寫"},
    {"roman": "Seven-Eleven", "kanji": "7-11", "english": "Seven-Eleven", "type": "英語羅馬字", "origin": "英語專名"}
]

HUA_QU = [
    # 台語羅馬字
    {"roman": "â-tsi", "kanji": "耳機，聽筒", "english": "headphone, earphone", "type": "台語羅馬字", "origin": "華語借詞音譯"},
    {"roman": "àn-môo", "kanji": "馬殺雞，按摩", "english": "massage", "type": "台語羅馬字", "origin": "華語借詞音譯"},
    {"roman": "î-tsia", "kanji": "瑜珈", "english": "yoga", "type": "台語羅馬字", "origin": "華語借詞音譯"},
    {"roman": "ín-tsia", "kanji": "硬體", "english": "hardware", "type": "台語羅馬字", "origin": "華語意譯音變"},
    {"roman": "ín-tê", "kanji": "硬碟", "english": "hard disk", "type": "台語羅馬字", "origin": "華語借詞音譯"},
    {"roman": "iâng-í-phián", "kanji": "洋芋片", "english": "potato chips", "type": "台語羅馬字", "origin": "華語借詞音譯"},
    {"roman": "Ue-â-kang", "kanji": "威而剛", "english": "Viagra", "type": "台語羅馬字", "origin": "華語譯名借音"},
    {"roman": "pú-lóo-kô", "kanji": "個人網路日誌，部落格", "english": "blog", "type": "台語羅馬字", "origin": "華語音譯 (Blog)"},
    {"roman": "pé-kôo", "kanji": "貝果", "english": "bagel", "type": "台語羅馬字", "origin": "華語音譯 (Bagel)"},
    {"roman": "pâu-lí-lông", "kanji": "保麗龍", "english": "polylon", "type": "台語羅馬字", "origin": "華語音譯 (Polylon)"},
    {"roman": "mî-nî", "kanji": "迷你，袖珍", "english": "mini, pocket-sized", "type": "台語羅馬字", "origin": "華語音譯 (Mini)"},
    {"roman": "môo-sú huang-khuái", "kanji": "魔術方塊", "english": "Rubik's Cube", "type": "台語羅馬字", "origin": "華語借詞音譯"},
    {"roman": "Mái-tang-lâu", "kanji": "麥當勞", "english": "MacDonald's", "type": "台語羅馬字", "origin": "華語譯名借音"},
    {"roman": "táng-tsi", "kanji": "當機", "english": "freeze", "type": "台語羅馬字", "origin": "華語借詞音譯"},
    {"roman": "liâng-mián", "kanji": "涼麵", "english": "cold noodles", "type": "台語羅馬字", "origin": "華語借詞音譯"},
    {"roman": "nái-mî", "kanji": "奈米", "english": "nanometer", "type": "台語羅馬字", "origin": "華語音譯 (Nano)"},
    {"roman": "kô-tsâi-tué", "kanji": "狗仔隊", "english": "paparazzo", "type": "台語羅馬字", "origin": "華語/粵語借詞"},
    {"roman": "tshî-í-kô", "kanji": "奇異果", "english": "kiwi fruit", "type": "台語羅馬字", "origin": "華語音譯 (Kiwi)"},
    {"roman": "tshiú-ki-á ê tsing-phián", "kanji": "手機門號晶片卡", "english": "SIM card", "type": "台語羅馬字", "origin": "華語意譯借音"},
    {"roman": "sa-hên-tá", "kanji": "殺很大", "english": "reduce price sharply", "type": "台語羅馬字", "origin": "流行華語借詞"},
    {"roman": "Sí-kû", "kanji": "矽谷", "english": "Silicon Valley", "type": "台語羅馬字", "origin": "華語音譯"},
    {"roman": "siá-tsâi", "kanji": "下載", "english": "download", "type": "台語羅馬字", "origin": "華語借詞音譯"},
    {"roman": "sián-sáng", "kanji": "線上", "english": "online", "type": "台語羅馬字", "origin": "華語借詞音譯"},
    {"roman": "sua-khâ", "kanji": "刷卡", "english": "scan credit card", "type": "台語羅馬字", "origin": "華語借詞音譯"},
    # 日語羅馬字
    {"roman": "karaoke", "kanji": "卡拉OK", "english": "Karaoke", "type": "日語羅馬字", "origin": "日語原文"},
    {"roman": "otaku", "kanji": "御宅族", "english": "Otaku, nerd", "type": "日語羅馬字", "origin": "日語原文"},
    # 漢語拼音羅馬字
    {"roman": "taikonaut", "kanji": "太空人", "english": "Chinese astronaut", "type": "漢語拼音羅馬字", "origin": "漢語拼音借詞"},
    {"roman": "guanxi", "kanji": "關係", "english": "social network, connections", "type": "漢語拼音羅馬字", "origin": "漢語拼音借詞"},
    {"roman": "fengshui", "kanji": "風水", "english": "Feng Shui", "type": "漢語拼音羅馬字", "origin": "漢語拼音借詞"},
    {"roman": "tofu", "kanji": "豆腐", "english": "tofu, bean curd", "type": "漢語拼音羅馬字", "origin": "漢語拼音/日語音譯"},
    # 英語羅馬字
    {"roman": "App", "kanji": "應用程式，App", "english": "Application", "type": "英語羅馬字", "origin": "英語縮寫"},
    {"roman": "WiFi", "kanji": "無線網路", "english": "Wi-Fi", "type": "英語羅馬字", "origin": "英語縮寫"},
    {"roman": "USB", "kanji": "隨身碟，USB", "english": "USB drive", "type": "英語羅馬字", "origin": "英語縮寫"},
    {"roman": "Podcast", "kanji": "播客，網路廣播", "english": "Podcast", "type": "英語羅馬字", "origin": "英語原文"}
]

# --- Custom CSS ---
st.markdown("""
<style>
.quiz-card {
    background-color: #f0f4f8;
    border-radius: 16px;
    padding: 30px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.08);
    text-align: center;
    margin-bottom: 20px;
    border: 2px solid #3182ce;
}
.roman-text {
    font-size: 2.2rem;
    font-weight: bold;
    color: #1a365d;
    margin-bottom: 12px;
}
.o-alert {
    background-color: #fffaf0;
    border: 1px solid #feebc8;
    color: #c05621;
    padding: 8px 12px;
    border-radius: 8px;
    font-size: 0.95rem;
    font-weight: 600;
    display: inline-block;
    margin-bottom: 15px;
}
.answer-box {
    background-color: #ffffff;
    border-radius: 12px;
    padding: 20px;
    margin-top: 15px;
    border-left: 5px solid #3182ce;
    text-align: left;
}
.kanji-text {
    font-size: 1.6rem;
    font-weight: bold;
    color: #2b6cb0;
}
.english-text {
    font-size: 1.1rem;
    color: #4a5568;
}
.type-tag {
    display: inline-block;
    background-color: #e2e8f0;
    color: #2d3748;
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# --- Title Header ---
st.title("🎴 瑪利諾外來語詞彙表 翻牌挑戰 v2")
st.caption("瑪利諾英台辭典外來語研究與學習互動測驗平台")

# --- Region Selection Sidebar ---
st.sidebar.header("⚙️ 測驗設定與選單")
region = st.sidebar.radio("請選擇測驗區域：", ["日英漢區", "華區"])
game_mode = st.sidebar.selectbox("🎯 測驗模式：", ["🎴 經典翻牌挑戰", "猜猜羅馬字來源（加分關卡）", "⚡ 快速連續計分賽"])

# Select dataset
dataset = JAPAN_ENG_HAN if region == "日英漢區" else HUA_QU

# Initialize Session States
if "current_region" not in st.session_state or st.session_state.current_region != region:
    st.session_state.current_region = region
    st.session_state.shuffled_deck = list(dataset)
    random.shuffle(st.session_state.shuffled_deck)
    st.session_state.card_idx = 0
    st.session_state.flipped = False
    st.session_state.score = 0
    st.session_state.combo = 0
    st.session_state.guess_correct = None
    st.session_state.wrong_list = []

# --- Region Rules & Pronunciation Notice ---
with st.expander("📌 **測驗前重要提示與發音指南（點擊展開）**", expanded=True):
    if region == "日英漢區":
        st.info("💡 **【日英漢區】語種表示說明**：本區包含 **台語羅馬字**、**日語羅馬字**、**英語羅馬字** 共 3 種表示方式，測驗時順序隨機混合。")
    else:
        st.info("💡 **【華區】語種表示說明**：本區包含 **台語羅馬字**、**日語羅馬字**、**漢語拼音羅馬字**、**英語羅馬字** 共 4 種表示方式，測驗時順序隨機混合。")
    
    st.warning("""
    🗣️ **台語羅馬字發音提示**：
    與台語羅馬字如注音符號 **ㆦ** 的「`oo`」[ɔ] 不同。
    台語羅馬字的「`o`」，會有兩種發音：
    1. 如注音符號 **ㄛ** [o]
    2. 如注音符號 **ㄜ** [ə]
    
    👉 **挑戰技巧**：遇到含有字母「`o`」的詞彙時，可以試著以 **[o]** 與 **[ə]** 兩種發音都唸唸看，會更快聯想到正確答案喔！
    """)

# Ensure deck is not empty
if not st.session_state.shuffled_deck:
    st.success("🎉 恭喜！您已經完成本區的所有詞彙挑戰！")
    if st.button("🔄 重新抽牌挑戰"):
        st.session_state.shuffled_deck = list(dataset)
        random.shuffle(st.session_state.shuffled_deck)
        st.session_state.card_idx = 0
        st.session_state.score = 0
        st.session_state.combo = 0
        st.rerun()
else:
    current_card = st.session_state.shuffled_deck[st.session_state.card_idx % len(st.session_state.shuffled_deck)]
    roman = current_card["roman"]
    kanji = current_card["kanji"]
    english = current_card["english"]
    card_type = current_card["type"]
    origin = current_card.get("origin", "")

    # Progress bar
    total_cards = len(st.session_state.shuffled_deck)
    current_no = (st.session_state.card_idx % total_cards) + 1
    st.progress(current_no / total_cards)
    st.write(f"第 **{current_no}** / **{total_cards}** 題 | 當前累計得分：**{st.session_state.score}** | 連勝 Combo：**{st.session_state.combo}** 🔥")

    # Check if contains 'o'
    has_o = "o" in roman.lower() and "oo" not in roman.lower()

    # --- Mode 1: Classic Card Flip ---
    if game_mode == "🎴 經典翻牌挑戰":
        st.markdown(f"""
        <div class="quiz-card">
            <span class="type-tag">【{region}】挑戰題</span>
            {'<br><div class="o-alert">⚠️ 本詞含有字母 o：請試唸 [o] (ㄛ) 與 [ə] (ㄜ)</div>' if has_o else ''}
            <div class="roman-text">{roman}</div>
            <p style="color:#718096; font-size:0.9rem;">(猜猜看背後的漢字與英文解釋是什麼？)</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if not st.session_state.flipped:
                if st.button("🎴 翻牌查看答案", use_container_width=True):
                    st.session_state.flipped = True
                    st.rerun()
            else:
                st.markdown(f"""
                <div class="answer-box">
                    <span class="type-tag">{card_type}</span> <span style="color:#718096; font-size:0.85rem;">({origin})</span>
                    <div class="kanji-text">漢字：{kanji}</div>
                    <div class="english-text">英文解釋：{english}</div>
                </div>
                """, unsafe_allow_html=True)

                st.write("自我檢測結果：")
                btn_col1, btn_col2 = st.columns(2)
                with btn_col1:
                    if st.button("✅ 猜對了！", use_container_width=True):
                        st.session_state.score += 10
                        st.session_state.combo += 1
                        st.session_state.card_idx += 1
                        st.session_state.flipped = False
                        st.rerun()
                with btn_col2:
                    if st.button("❌ 還不熟", use_container_width=True):
                        st.session_state.combo = 0
                        st.session_state.wrong_list.append(current_card)
                        st.session_state.card_idx += 1
                        st.session_state.flipped = False
                        st.rerun()

    # --- Mode 2: Guess Source Language ---
    elif game_mode == "猜猜羅馬字來源（加分關卡）":
        st.markdown(f"""
        <div class="quiz-card">
            <span class="type-tag">【加分關卡】語種來源猜測</span>
            {'<br><div class="o-alert">⚠️ 本詞含有字母 o：請試唸 [o] (ㄛ) 與 [ə] (ㄜ)</div>' if has_o else ''}
            <div class="roman-text">{roman}</div>
            <p style="color:#718096;">這個羅馬字屬於哪一種語言的表示方式？</p>
        </div>
        """, unsafe_allow_html=True)

        options = ["台語羅馬字", "日語羅馬字", "英語羅馬字"]
        if region == "華區":
            options.append("漢語拼音羅馬字")

        user_choice = st.radio("選擇羅馬字類型：", options, horizontal=True)

        if not st.session_state.flipped:
            if st.button("🎯 確認答案並翻牌", use_container_width=True):
                st.session_state.flipped = True
                st.session_state.guess_correct = (user_choice == card_type)
                if st.session_state.guess_correct:
                    st.session_state.score += 15
                    st.session_state.combo += 1
                else:
                    st.session_state.combo = 0
                st.rerun()
        else:
            if st.session_state.guess_correct:
                st.success(f"🎉 猜對了！正確語種是【{card_type}】(+15分)")
            else:
                st.error(f"❌ 答錯囉！正確語種其實是【{card_type}】")

            st.markdown(f"""
            <div class="answer-box">
                <span class="type-tag">{card_type}</span> <span style="color:#718096; font-size:0.85rem;">({origin})</span>
                <div class="kanji-text">漢字：{kanji}</div>
                <div class="english-text">英文解釋：{english}</div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("下一題 ➡️", use_container_width=True):
                st.session_state.card_idx += 1
                st.session_state.flipped = False
                st.rerun()

    # --- Mode 3: Speed Run Challenge ---
    elif game_mode == "⚡ 快速連續計分賽":
        st.markdown(f"""
        <div class="quiz-card">
            <span class="type-tag">⚡ 快速連續挑戰賽</span>
            {'<br><div class="o-alert">⚠️ 本詞含有字母 o：請試唸 [o] (ㄛ) 與 [ə] (ㄜ)</div>' if has_o else ''}
            <div class="roman-text">{roman}</div>
        </div>
        """, unsafe_allow_html=True)

        if not st.session_state.flipped:
            if st.button("👀 顯示答案", use_container_width=True):
                st.session_state.flipped = True
                st.rerun()
        else:
            st.markdown(f"""
            <div class="answer-box">
                <div class="kanji-text">漢字：{kanji}</div>
                <div class="english-text">英文解釋：{english}</div>
                <span class="type-tag">{card_type}</span>
            </div>
            """, unsafe_allow_html=True)

            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("⚡ 快速紀錄：秒答極限 (+20分)", use_container_width=True):
                    st.session_state.score += 20
                    st.session_state.combo += 1
                    st.session_state.card_idx += 1
                    st.session_state.flipped = False
                    st.rerun()
            with col_b:
                if st.button("😅 思考較久 / 還不熟 (+5分)", use_container_width=True):
                    st.session_state.score += 5
                    st.session_state.card_idx += 1
                    st.session_state.flipped = False
                    st.rerun()

# --- Review & Summary Area ---
st.divider()
st.subheader("📚 錯題與尚不熟悉詞彙筆記本")
if st.session_state.wrong_list:
    st.caption(f"目前尚不熟悉的詞彙共 {len(st.session_state.wrong_list)} 個：")
    for idx, item in enumerate(st.session_state.wrong_list, 1):
        st.write(f"**{idx}. {item['roman']}** ➔ {item['kanji']} (*{item['english']}*) 【{item['type']}】")
else:
    st.info("太棒了！目前沒有標註不熟悉的詞彙。")
