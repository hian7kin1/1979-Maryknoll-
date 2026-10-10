import streamlit as st
import random
import textwrap
import re

def clean_html(html_str):
    return re.sub(r'\s+', ' ', html_str).strip()


# --- Page Configuration ---
st.set_page_config(
    page_title="瑪利諾外來語詞彙表 翻牌挑戰網站",
    page_icon="🎴",
    layout="centered"
)

# --- Vocabulary Dataset strictly from 1979⁺ Maryknoll (phonetic)(整理)(序號).docx ---
JAPAN_ENG_HAN = [
    # 日英漢區 - 台語羅馬字
    {"roman": "a-sa-lih", "kanji": "阿莎力", "english": "generously", "type": "台語羅馬字"},
    {"roman": "a-sa-lih", "kanji": "乾脆", "english": "clean-cut, straight forward, wholly, solely, entirely, exclusively, devotedly, wholeheartedly", "type": "台語羅馬字"},
    {"roman": "a-su-phí-lín", "kanji": "阿斯匹林", "english": "aspirin", "type": "台語羅馬字"},
    {"roman": "ak-sé-lé-tah", "kanji": "加速器", "english": "accelerator", "type": "台語羅馬字"},
    {"roman": "I-tiân", "kanji": "伊甸，地堂，樂園", "english": "Eden", "type": "台語羅馬字"},
    {"roman": "ín-tsih", "kanji": "英吋", "english": "inch, English inch", "type": "台語羅馬字"},
    {"roman": "e-lé-bé-tà", "kanji": "電梯", "english": "elevator", "type": "台語羅馬字"},
    {"roman": "e-ná-mé-luh", "kanji": "釉，亮光漆", "english": "enamel", "type": "台語羅馬字"},
    {"roman": "óo-bà", "kanji": "大衣", "english": "overcoat, top coat", "type": "台語羅馬字"},
    {"roman": "ai-noo-khooh", "kanji": "混種，混血兒", "english": "mixed blood, child of an inter-racial marriage, half-breed, child of mixed ancestry", "type": "台語羅馬字"},
    {"roman": "ia̋n-jín", "kanji": "發動機", "english": "engine", "type": "台語羅馬字"},
    {"roman": "io-koh", "kanji": "酸乳酪，優酪乳，養樂多", "english": "yogurt", "type": "台語羅馬字"},
    {"roman": "ió-lo-tsín-khih", "kanji": "碘酒", "english": "iodine", "type": "台語羅馬字"},
    {"roman": "uá-suh-lôo", "kanji": "瓦斯爐", "english": "gas stove", "type": "台語羅馬字"},
    {"roman": "ui-sū-kī", "kanji": "威士忌酒", "english": "whisky", "type": "台語羅馬字"},
    {"roman": "uai-siá-tsuh", "kanji": "白櫬衫", "english": "white dress shirt", "type": "台語羅馬字"},
    {"roman": "pin-kó", "kanji": "賓果", "english": "bingo", "type": "台語羅馬字"},
    {"roman": "pe-gèn", "kanji": "醃肉，培根", "english": "bacon", "type": "台語羅馬字"},
    {"roman": "pó-lîng-kiû", "kanji": "保齡球", "english": "bowling", "type": "台語羅馬字"},
    {"roman": "phah-buh", "kanji": "酒店", "english": "pub, tavern", "type": "台語羅馬字"},
    {"roman": "phi-sah", "kanji": "披薩，比薩", "english": "pizza", "type": "台語羅馬字"},
    {"roman": "phi-sú-tóng", "kanji": "活塞", "english": "piston", "type": "台語羅馬字"},
    {"roman": "phi-sú-tóng-lín-gù", "kanji": "活塞環", "english": "piston ring", "type": "台語羅馬字"},
    {"roman": "phu-lo-phe-la", "kanji": "螺旋槳", "english": "screw propeller, propeller, screw", "type": "台語羅馬字"},
    {"roman": "phuh-lá-guh", "kanji": "火星塞", "english": "spark plug", "type": "台語羅馬字"},
    {"roman": "phuh-lóo-pheh-lá", "kanji": "推進機，螺旋槳", "english": "propeller of a ship, plane", "type": "台語羅馬字"},
    {"roman": "phòm-pù", "kanji": "抽水機，抽", "english": "pump, water pump", "type": "台語羅馬字"},
    {"roman": "phái", "kanji": "派，果子餅", "english": "pie", "type": "台語羅馬字"},
    {"roman": "ba-tah", "kanji": "牛奶油", "english": "butter, tallow, butter oil", "type": "台語羅馬字"},
    {"roman": "bi-tá-mín", "kanji": "維他命，維生素", "english": "vitamin", "type": "台語羅馬字"},
    {"roman": "Bīng-bé/Bīng-mái", "kanji": "孟買", "english": "Bombay", "type": "台語羅馬字"},
    {"roman": "bê-á-lín-gù", "kanji": "軸承", "english": "bearing, bearings of a machine", "type": "台語羅馬字"},
    {"roman": "bóo-lú-tooh", "kanji": "門閂，螺絲釘，閂", "english": "bolt", "type": "台語羅馬字"},
    {"roman": "bóo-lú-tooh", "kanji": "電壓的單位伏特", "english": "volt", "type": "台語羅馬字"},
    {"roman": "Bián-juh", "kanji": "賓士", "english": "Mercedes-Benz", "type": "台語羅馬字"},
    {"roman": "ma-tòo", "kanji": "模特兒", "english": "fashion model", "type": "台語羅馬字"},
    {"roman": "ma-tsih", "kanji": "麻吉，好友", "english": "good friend, match", "type": "台語羅馬字"},
    {"roman": "má-sú-khuh", "kanji": "口罩", "english": "mask", "type": "台語羅馬字"},
    {"roman": "mā-sa-tsih", "kanji": "馬殺雞，按摩", "english": "massage", "type": "台語羅馬字"},
    {"roman": "máng-gà", "kanji": "漫畫", "english": "cartoon", "type": "台語羅馬字"},
    {"roman": "máng-gah", "kanji": "卡通", "english": "comic strip, cartoons, the funnies, comic books", "type": "台語羅馬字"},
    {"roman": "môo-te-luh", "kanji": "模特兒", "english": "fashion model", "type": "台語羅馬字"},
    {"roman": "moo-tián", "kanji": "數據機", "english": "modem", "type": "台語羅馬字"},
    {"roman": "moo-lé-luh", "kanji": "模特兒", "english": "model, person who wears fashions to display for buyers", "type": "台語羅馬字"},
    {"roman": "mái-khù", "kanji": "擴聲機，麥克風", "english": "microphone", "type": "台語羅馬字"},
    {"roman": "thiàu thah-puh", "kanji": "跳踢躂舞", "english": "tap dance", "type": "台語羅馬字"},
    {"roman": "la-lí-ah", "kanji": "大理花，大麗花", "english": "dahlia", "type": "台語羅馬字"},
    {"roman": "là-pah", "kanji": "喇叭", "english": "claxon", "type": "台語羅馬字"},
    {"roman": "lí-lí-thi", "kanji": "一種殺蟲劑", "english": "DDT", "type": "台語羅馬字"},
    {"roman": "lú-puh", "kanji": "樂譜", "english": "loop, contraceptive device, an IUD", "type": "台語羅馬字"},
    {"roman": "loonat", "kanji": "油煎圈餅", "english": "doughnut", "type": "台語羅馬字"},
    {"roman": "lo̍k-phóo", "kanji": "樂譜", "english": "loop, contraceptive device, an IUD", "type": "台語羅馬字"},
    {"roman": "lián-tsì", "kanji": "螺旋鉗", "english": "wrench, spanner", "type": "台語羅馬字"},
    {"roman": "nî-kóo-ting", "kanji": "尼古丁，煙油", "english": "nicotine", "type": "台語羅馬字"},
    {"roman": "ne-óng", "kanji": "霓虹燈", "english": "neon", "type": "台語羅馬字"},
    {"roman": "ne-óng-ting", "kanji": "霓虹燈", "english": "neon light", "type": "台語羅馬字"},
    {"roman": "ne-khu-tái", "kanji": "領帶", "english": "necktie", "type": "台語羅馬字"},
    {"roman": "nőo-khó", "kanji": "反效果，汽油過多", "english": "backfire", "type": "台語羅馬字"},
    {"roman": "nâi-lóng", "kanji": "尼龍", "english": "nylon", "type": "台語羅馬字"},
    {"roman": "ka-lûn", "kanji": "加侖", "english": "gallon", "type": "台語羅馬字"},
    {"roman": "kik bí-lù", "kanji": "釀啤酒", "english": "brew beer", "type": "台語羅馬字"},
    {"roman": "ko-lô-hóng", "kanji": "哥羅仿，一種麻醉藥", "english": "chloroform", "type": "台語羅馬字"},
    {"roman": "kha-phuh-sé-lù", "kanji": "膠囊，膠囊劑", "english": "capsule for medicine", "type": "台語羅馬字"},
    {"roman": "kha-tián", "kanji": "窗簾", "english": "curtain", "type": "台語羅馬字"},
    {"roman": "kha-lu-siú-muh", "kanji": "鈣質", "english": "calcium", "type": "台語羅馬字"},
    {"roman": "kha-lóo-lí", "kanji": "熱量，卡路里", "english": "calorie", "type": "台語羅馬字"},
    {"roman": "kha-ná-lí-á", "kanji": "金絲雀", "english": "canary", "type": "台語羅馬字"},
    {"roman": "kha̋n-páng", "kanji": "看板", "english": "signboard of a store or any other business concern", "type": "台語羅馬字"},
    {"roman": "khap-pih/khop-pih", "kanji": "拷貝", "english": "copy a film print", "type": "台語羅馬字"},
    {"roman": "khah-pin-tshìng", "kanji": "卡賓槍", "english": "carbine, rifle", "type": "台語羅馬字"},
    {"roman": "khi-moo-tsih", "kanji": "心情，情緒，樣子，態度", "english": "mood, feelings, mind, emotional state, affection, state of mind", "type": "台語羅馬字"},
    {"roman": "khi-nih-neh", "kanji": "奎寧", "english": "quinine", "type": "台語羅馬字"},
    {"roman": "khí-moo", "kanji": "心情，氣氛", "english": "frame, state of mind, mood", "type": "台語羅馬字"},
    {"roman": "khu-lá-buh", "kanji": "俱樂部", "english": "club, bar, entertainment place", "type": "台語羅馬字"},
    {"roman": "khu-lak-sióng", "kanji": "喇叭", "english": "claxon", "type": "台語羅馬字"},
    {"roman": "khú/coo", "kanji": "酷", "english": "cool, good, great", "type": "台語羅馬字"},
    {"roman": "khe-tsiap-puh", "kanji": "蕃茄醬", "english": "ketchup tomáto", "type": "台語羅馬字"},
    {"roman": "khé-lih", "kanji": "雜役，球童", "english": "caddie", "type": "台語羅馬字"},
    {"roman": "khé-suh", "kanji": "病例", "english": "case, medicine case", "type": "台語羅馬字"},
    {"roman": "khoo-í-luh", "kanji": "盤繞，一捲，線圈", "english": "coil", "type": "台語羅馬字"},
    {"roman": "khoo-ín", "kanji": "叩應", "english": "call in to participate in a TV program", "type": "台語羅馬字"},
    {"roman": "khoo-ín ê lâng", "kanji": "叩應的人", "english": "caller, one who calls in to participate in a TV program", "type": "台語羅馬字"},
    {"roman": "khoo-leh-lah", "kanji": "霍亂", "english": "cholera", "type": "台語羅馬字"},
    {"roman": "khóo-khah-ín", "kanji": "可可因", "english": "cocaine", "type": "台語羅馬字"},
    {"roman": "khó-toh", "kanji": "大衣", "english": "coat", "type": "台語羅馬字"},
    {"roman": "khó-khó-ah", "kanji": "可可亞", "english": "cocoa", "type": "台語羅馬字"},
    {"roman": "khong-mi-sióng", "kanji": "傭金", "english": "commission, percentage of the profit", "type": "台語羅馬字"},
    {"roman": "gah-suh-lôo", "kanji": "瓦斯爐", "english": "gas stove", "type": "台語羅馬字"},
    {"roman": "guh-lí-suh", "kanji": "黃油", "english": "grease", "type": "台語羅馬字"},
    {"roman": "goo-lu-huh kiû-tiûnn ê kiû-tông", "kanji": "雜役，球童", "english": "caddie", "type": "台語羅馬字"},
    {"roman": "tsó-sió", "kanji": "作秀，舞臺演唱等表演", "english": "show, stage concerts, political show off, limelight", "type": "台語羅馬字"},
    {"roman": "tsio-ko-lei-to", "kanji": "巧克力，朱古力", "english": "chocolate", "type": "台語羅馬字"},
    {"roman": "tshí-juh/tshí-suh", "kanji": "乳酪，起司", "english": "cheese", "type": "台語羅馬字"},
    {"roman": "sa-si-mih", "kanji": "生魚片", "english": "sashimi", "type": "台語羅馬字"},
    {"roman": "sa-sí-mih", "kanji": "生魚片", "english": "raw fish", "type": "台語羅馬字"},
    {"roman": "sá-suh", "kanji": "SARS，嚴重急性呼吸道感染症候群", "english": "SARS, Severe Acute Respiratory Syndrome", "type": "台語羅馬字"},
    {"roman": "sat-khik-su-hong", "kanji": "薩克斯風", "english": "saxophone", "type": "台語羅馬字"},
    {"roman": "si-lín-tah", "kanji": "汽缸", "english": "cylinders in automobiles, motorcycles", "type": "台語羅馬字"},
    {"roman": "su-pái", "kanji": "間諜", "english": "spy", "type": "台語羅馬字"},
    {"roman": "su-pú-lín-guh", "kanji": "彈簧", "english": "springs in a easy chair or sofa, bed springs", "type": "台語羅馬字"},
    {"roman": "suh-phí-khà", "kanji": "擴音器", "english": "loud speaker", "type": "台語羅馬字"},
    {"roman": "suh-kuh-tà", "kanji": "速克達", "english": "scooter", "type": "台語羅馬字"},
    {"roman": "Sóo-nih", "kanji": "新力", "english": "Sony", "type": "台語羅馬字"},
    {"roman": "sòo-tà", "kanji": "蘇打", "english": "soda", "type": "台語羅馬字"},
    {"roman": "sió", "kanji": "秀，表演", "english": "show, performance", "type": "台語羅馬字"},
    {"roman": "siok-khuh", "kanji": "休克", "english": "shock, stun", "type": "台語羅馬字"},
    {"roman": "sioh-toh", "kanji": "短路，神經不正常", "english": "shortcut, crazy", "type": "台語羅馬字"},
    {"roman": "jé-lih", "kanji": "果子醬，果子膏", "english": "jelly", "type": "台語羅馬字"},
    {"roman": "jiá-muh", "kanji": "果醬", "english": "jam, marmalade", "type": "台語羅馬字"},
    {"roman": "jián-bah", "kanji": "外衣，夾克", "english": "jacket", "type": "台語羅馬字"},
    {"roman": "há-muh", "kanji": "火腿，燻腿", "english": "ham", "type": "台語羅馬字"},
    {"roman": "hā-ma-kih", "kanji": "雪茄", "english": "cigar", "type": "台語羅馬字"},
    {"roman": "hah-móo-ní-khah", "kanji": "口琴", "english": "harmonica", "type": "台語羅馬字"},
    {"roman": "hi-sí-te-lí", "kanji": "神經錯亂，歇斯底里", "english": "hysteria", "type": "台語羅馬字"},
    {"roman": "Hí-lóo-sih-mah", "kanji": "廣島", "english": "Hiroshima", "type": "台語羅馬字"},
    {"roman": "he-lu-meh-toh", "kanji": "鋼盔，頭盔", "english": "helmet", "type": "台語羅馬字"},
    {"roman": "hoo-theh-luh", "kanji": "旅館，大飯店，旅社", "english": "hotel", "type": "台語羅馬字"},
    {"roman": "hoo-lú-bóng", "kanji": "賀爾蒙", "english": "hormones", "type": "台語羅馬字"},
    {"roman": "hông-tsí lâng khop-pih", "kanji": "防拷貝保護", "english": "copy protection", "type": "台語羅馬字"},
    {"roman": "hiuh-juh", "kanji": "保險絲，熔", "english": "fuse, melting fuse", "type": "台語羅馬字"},

    # 日英漢區 - 日語羅馬字
    {"roman": "guliselin", "kanji": "甘油", "english": "glycerine", "type": "日語羅馬字"},
    {"roman": "pasento", "kanji": "百分比", "english": "percent", "type": "日語羅馬字"},
    {"roman": "biru", "kanji": "啤酒", "english": "beer", "type": "日語羅馬字"},
    {"roman": "beluto", "kanji": "帶子，地帶", "english": "belt, band, sash, girdle, tape, ribbon", "type": "日語羅馬字"},
    {"roman": "brei-ki", "kanji": "煞車，煞車器", "english": "brake", "type": "日語羅馬字"},
    {"roman": "bro-ka", "kanji": "經紀人，掮客", "english": "broker, agent", "type": "日語羅馬字"},
    {"roman": "maskou", "kanji": "口罩", "english": "gas mask", "type": "日語羅馬字"},
    {"roman": "mahula", "kanji": "滅音器，排氣管，消音器", "english": "muffler", "type": "日語羅馬字"},

    # 日英漢區 - 英語羅馬字
    {"roman": "BB call", "kanji": "呼叫器，傳呼機，BB call", "english": "beeper", "type": "英語羅馬字"},
    {"roman": "gasolin", "kanji": "汽油", "english": "gasoline", "type": "英語羅馬字"},
    {"roman": "model", "kanji": "模特兒", "english": "model, person who wears fashions to display for buyers", "type": "英語羅馬字"},
    {"roman": "mosaik", "kanji": "剪貼", "english": "mosaic, cut out and paste together", "type": "英語羅馬字"},
    {"roman": "SARS", "kanji": "SARS，嚴重急性呼吸道感染症候群", "english": "SARS, Severe Acute Respiratory Syndrome", "type": "英語羅馬字"},
    {"roman": "seven/Seven-Eleven", "kanji": "7-11", "english": "Seven-Eleven", "type": "英語羅馬字"}
]

HUA_QU = [
    # 華區 - 台語羅馬字
    {"roman": "â-tsi", "kanji": "耳機，聽筒", "english": "headphone, earphone", "type": "台語羅馬字"},
    {"roman": "àn-môo", "kanji": "馬殺雞，按摩", "english": "massage", "type": "台語羅馬字"},
    {"roman": "î-tsia", "kanji": "瑜珈", "english": "yoga, mystic and ascetic practice in Hindu philosophy", "type": "台語羅馬字"},
    {"roman": "ín-tî", "kanji": "硬體", "english": "hardware, computer hardware", "type": "台語羅馬字"},
    {"roman": "ín-tê", "kanji": "硬碟", "english": "hard disk", "type": "台語羅馬字"},
    {"roman": "iâng-í-phián", "kanji": "洋芋片", "english": "potato chips", "type": "台語羅馬字"},
    {"roman": "io-ló-jû", "kanji": "酸乳酪，優酪乳，養樂多", "english": "yogurt", "type": "台語羅馬字"},
    {"roman": "iô-piau", "kanji": "游標", "english": "cursor", "type": "台語羅馬字"},
    {"roman": "Ue-â-kang", "kanji": "威而剛", "english": "Viagra", "type": "台語羅馬字"},
    {"roman": "ué-sing tâu-hâng", "kanji": "衛星導航", "english": "satellite navigation, global positioning system", "type": "台語羅馬字"},
    {"roman": "Pin-la-tan", "kanji": "賓拉登，賓拉丹", "english": "bin Laden", "type": "台語羅馬字"},
    {"roman": "pú-lóo-kô", "kanji": "個人網路日誌，部落格", "english": "blog", "type": "台語羅馬字"},
    {"roman": "pé-kôo", "kanji": "貝果", "english": "bagel", "type": "台語羅馬字"},
    {"roman": "pé-pau", "kanji": "背包", "english": "knapsack", "type": "台語羅馬字"},
    {"roman": "pâu-lí-lông", "kanji": "保麗龍", "english": "polylon", "type": "台語羅馬字"},
    {"roman": "pâu-sian-môo", "kanji": "保鮮膜", "english": "plastic wrap, preservative film or wrapping to keep food fresh", "type": "台語羅馬字"},
    {"roman": "pián-lí-sang-tián", "kanji": "便利商店", "english": "convenience store", "type": "台語羅馬字"},
    {"roman": "piau-tsho", "kanji": "飆車", "english": "drag racing, fast reckless car, bicycle or motorcycle race, go for a joyride", "type": "台語羅馬字"},
    {"roman": "phân-tiân", "kanji": "盤點，清點", "english": "make an inventory, check", "type": "台語羅馬字"},
    {"roman": "phi-thô-sú", "kanji": "披頭士", "english": "Beatles, Beatles", "type": "台語羅馬字"},
    {"roman": "phing-thû", "kanji": "拼圖", "english": "jigsaw puzzle", "type": "台語羅馬字"},
    {"roman": "phàu-phàu-thâng", "kanji": "口香糖，泡泡糖", "english": "chewing gum", "type": "台語羅馬字"},
    {"roman": "mî-nî", "kanji": "迷你，袖珍", "english": "mini, pocket-sized", "type": "台語羅馬字"},
    {"roman": "môo-nî", "kanji": "模擬", "english": "simulation", "type": "台語羅馬字"},
    {"roman": "môo-sú huang-khuái", "kanji": "魔術方塊", "english": "Rubik's Cube", "type": "台語羅馬字"},
    {"roman": "Mái-tang-lâu", "kanji": "麥當勞", "english": "MacDonald's", "type": "台語羅馬字"},
    {"roman": "mái-khó-hong", "kanji": "擴聲機，麥克風", "english": "microphone", "type": "台語羅馬字"},
    {"roman": "tá-lú-mé", "kanji": "萵苣，大陸妹", "english": "lettuce, mainland lettuce", "type": "台語羅馬字"},
    {"roman": "tân-kú-tshûn", "kanji": "膽固醇", "english": "cholesterol", "type": "台語羅馬字"},
    {"roman": "táng-tsi", "kanji": "當機", "english": "freeze", "type": "台語羅馬字"},
    {"roman": "ti-ná-iân", "kanji": "低鈉鹽", "english": "low-sodium salt", "type": "台語羅馬字"},
    {"roman": "tî-su-khô", "kanji": "狄斯可", "english": "disco", "type": "台語羅馬字"},
    {"roman": "to-iân pù pâu-hô tsû-huân-suan", "kanji": "多元不飽和脂肪酸", "english": "PUFA, polyunsaturated fatty acid", "type": "台語羅馬字"},
    {"roman": "tián-uân", "kanji": "電動玩具，電玩", "english": "electric toys, computerized toys", "type": "台語羅馬字"},
    {"roman": "Tng-kô-jó", "kanji": "登革熱", "english": "Dengue Fever", "type": "台語羅馬字"},
    {"roman": "liâng-mián", "kanji": "涼麵", "english": "cold noodles", "type": "台語羅馬字"},
    {"roman": "nái-mî", "kanji": "奈米", "english": "nanometer", "type": "台語羅馬字"},
    {"roman": "nâi-tsing", "kanji": "奶精", "english": "non-dairy creamer", "type": "台語羅馬字"},
    {"roman": "kô-tsâi-tué", "kanji": "狗仔隊", "english": "paparazzo", "type": "台語羅馬字"},
    {"roman": "kau-khong thân-thiáu", "kanji": "高空彈跳", "english": "bungee jump", "type": "台語羅馬字"},
    {"roman": "kuang-tê sau-lú-tsí", "kanji": "光碟燒錄器", "english": "CD writer", "type": "台語羅馬字"},
    {"roman": "kue-î", "kanji": "鮭魚", "english": "salmon", "type": "台語羅馬字"},
    {"roman": "khà-pin-tshiang", "kanji": "卡賓槍", "english": "carbine, rifle", "type": "台語羅馬字"},
    {"roman": "khà-thong", "kanji": "卡通", "english": "cartoon, comic strip, cartoons, the funnies, comic books", "type": "台語羅馬字"},
    {"roman": "khô-thî-í", "kanji": "口蹄疫", "english": "foot and mouth disease", "type": "台語羅馬字"},
    {"roman": "Khô-khô khô-ló", "kanji": "可口可樂", "english": "Coca Cola, Coke", "type": "台語羅馬字"},
    {"roman": "khô-siang-thâng", "kanji": "口香糖", "english": "chewing gum", "type": "台語羅馬字"},
    {"roman": "khâu-siang", "kanji": "爐，火爐，烤箱", "english": "oven, furnace, stove", "type": "台語羅馬字"},
    {"roman": "tsì-tsî", "kanji": "巨集", "english": "macro", "type": "台語羅馬字"},
    {"roman": "tsîn-sng-khú", "kanji": "緊身褲", "english": "drainpipe trousers", "type": "台語羅馬字"},
    {"roman": "tsu-io", "kanji": "有天才的，資優", "english": "gifted", "type": "台語羅馬字"},
    {"roman": "tsê-si-tú", "kanji": "解析度", "english": "resolution of a monitor, mirror or lense", "type": "台語羅馬字"},
    {"roman": "tsó-pí", "kanji": "作弊", "english": "cheat in an examination, cheat on test or exam, indulge in corrupt practices", "type": "台語羅馬字"},
    {"roman": "tsâi-phé", "kanji": "宅急配，宅配", "english": "home delivery of purchases", "type": "台語羅馬字"},
    {"roman": "Tsia-hue-mau", "kanji": "加菲貓", "english": "Garfield", "type": "台語羅馬字"},
    {"roman": "tsia̋-khó", "kanji": "外衣，夾克", "english": "jacket", "type": "台語羅馬字"},
    {"roman": "tshâng-píng-tû", "kanji": "腸炎，腸病毒", "english": "enterovirus, enteritis, intestinal virus", "type": "台語羅馬字"},
    {"roman": "tshî-í-kô", "kanji": "奇異果", "english": "kiwi fruit", "type": "台語羅馬字"},
    {"roman": "tshû-phián", "kanji": "磁片", "english": "diskette", "type": "台語羅馬字"},
    {"roman": "tshû-tsû-khâ", "kanji": "儲值卡", "english": "pre-paid phone card", "type": "台語羅馬字"},
    {"roman": "tshiú-ki-á ê tsing-phián", "kanji": "手機門號晶片卡", "english": "SIM card, subscriber identity module card", "type": "台語羅馬字"},
    {"roman": "jún-su", "kanji": "潤絲", "english": "hair care", "type": "台語羅馬字"},
    {"roman": "sa-hên-tá", "kanji": "殺很大", "english": "reduce price sharply", "type": "台語羅馬字"},
    {"roman": "san-iáu", "kanji": "紅薯，山藥", "english": "yam, Chinese yam", "type": "台語羅馬字"},
    {"roman": "san-ti tiān-iánn", "kanji": "立體電影，3D 電影", "english": "three dimensional film", "type": "台語羅馬字"},
    {"roman": "Sí-kû", "kanji": "矽谷", "english": "Silicon Valley", "type": "台語羅馬字"},
    {"roman": "sí-tsing-phián", "kanji": "矽晶片", "english": "silicon chip", "type": "台語羅馬字"},
    {"roman": "sôo-mâ", "kanji": "鎖碼裝置", "english": "V-chip", "type": "台語羅馬字"},
    {"roman": "só-în-phn̂g", "kanji": "攝影棚", "english": "studio, movie set", "type": "台語羅馬字"},
    {"roman": "siá-tsâi", "kanji": "下載", "english": "download", "type": "台語羅馬字"},
    {"roman": "sián-sáng", "kanji": "線上", "english": "online", "type": "台語羅馬字"},
    {"roman": "siang-tshâu", "kanji": "香草，香料", "english": "vanilla", "type": "台語羅馬字"},
    {"roman": "sua-khâ", "kanji": "刷卡", "english": "scan credit card", "type": "台語羅馬字"},
    {"roman": "suā-khâ", "kanji": "刷卡", "english": "use a credit card", "type": "台語羅馬字"},
    {"roman": "suê-sng-tê", "kanji": "隨身碟", "english": "flash drive", "type": "台語羅馬字"},
    {"roman": "suê-sng-thing", "kanji": "隨身聽", "english": "personal stereo, Walkman", "type": "台語羅馬字"},
    {"roman": "hu-tsiáu-khí", "kanji": "呼叫器，傳呼機，BB call", "english": "beeper, pager", "type": "台語羅馬字"},
    {"roman": "hù-huâ", "kanji": "護髮", "english": "hair care", "type": "台語羅馬字"},
    {"roman": "hô-niâu", "kanji": "候鳥", "english": "migratory birds", "type": "台語羅馬字"},
    {"roman": "hâi-thâi", "kanji": "海苔", "english": "coarser kind of seweed, seldom eaten", "type": "台語羅馬字"},
    {"roman": "Hâu-lâi-u", "kanji": "好萊塢", "english": "Hollywood", "type": "台語羅馬字"},
    {"roman": "huâ-sû", "kanji": "浮標移動器，滑鼠", "english": "mouse, electronic mouse", "type": "台語羅馬字"},
    {"roman": "huâng-sái-iô", "kanji": "防曬乳", "english": "sun block, sunburn protection", "type": "台語羅馬字"},
    {"roman": "huâng-sái-jû", "kanji": "防曬乳", "english": "sun block, sunburn protection", "type": "台語羅馬字"},

    # 華區 - 日語羅馬字
    {"roman": "jê-kô-û", "kanji": "捷格舞", "english": "jig, dance", "type": "日語羅馬字"},
    {"roman": "Yâ-hu", "kanji": "雅虎", "english": "Yahoo", "type": "日語羅馬字"},

    # 華區 - 漢語拼音羅馬字
    {"roman": "jiāo-dài", "kanji": "膠帶", "english": "Scotch tape, tape", "type": "漢語拼音羅馬字"},
    {"roman": "jia-you", "kanji": "加油", "english": "exhortation, Step on the gas, Let's go, very often pronounced in Mandarin", "type": "漢語拼音羅馬字"},
    {"roman": "tiào tī-tā-wû", "kanji": "跳踢躂舞", "english": "tap dance", "type": "漢語拼音羅馬字"},
    {"roman": "wâng-kóo", "kanji": "線上購物，網路購物", "english": "online shopping", "type": "漢語拼音羅馬字"},
    {"roman": "yáo kòng", "kanji": "遙控", "english": "remote control", "type": "漢語拼音羅馬字"},

    # 華區 - 英語羅馬字
    {"roman": "CD sau-lú-tsi", "kanji": "CD 燒錄機", "english": "CD recorder", "type": "英語羅馬字"},
    {"roman": "enter tsián", "kanji": "enter 鍵", "english": "enter key on a computer keyboard", "type": "英語羅馬字"},
    {"roman": "SIM khà", "kanji": "SIM卡", "english": "SIM card, subscriber identity module card", "type": "英語羅馬字"},
    {"roman": "x-kuang", "kanji": "X光相片", "english": "x-ray photograph", "type": "英語羅馬字"}
]

# --- Custom CSS (dedented) ---
css_style = textwrap.dedent("""
<style>
.quiz-card {
    background-color: #f0f4f8;
    border-radius: 16px;
    padding: 28px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.08);
    text-align: center;
    margin-bottom: 20px;
    border: 2px solid #3182ce;
}
.roman-text {
    font-size: 2.2rem;
    font-weight: bold;
    color: #1a365d;
    margin-top: 10px;
    margin-bottom: 10px;
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
    margin-bottom: 12px;
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
    margin-top: 6px;
}
.english-text {
    font-size: 1.1rem;
    color: #4a5568;
    margin-top: 4px;
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
""")
st.markdown(clean_html(css_style), unsafe_allow_html=True)

# --- Title Header ---
st.title("🎴 瑪利諾外來語詞彙表 翻牌挑戰")
st.caption("1979⁺ Maryknoll (phonetic) 外來語辭典數位學習翻牌測驗")

# --- Region Selection Sidebar ---
st.sidebar.header("⚙️ 測驗設定與選單")
region = st.sidebar.radio("請選擇測驗區域：", ["日英漢區", "華區"])
game_mode = st.sidebar.selectbox("🎯 測驗模式：", ["🎴 經典翻牌挑戰", "猜猜羅馬字來源（加分關卡）", "⚡ 快速連續計分賽"])

st.sidebar.divider()
with st.sidebar.expander("ℹ️ 題目資料來源聲明", expanded=False):
    st.markdown("""
本測驗資料經由 [ChhoeTaigi 找台語](https://chhoe.taigi.info/) 建立的搜尋引擎與資料庫。搜尋出所有在《1979⁺ Maryknoll英台辭典》中，包含 `(phonetic)` 條目的所有 213 條詞條，並經整理為此測驗的 229 條題目。分類為日英漢區 134 條，華區 95 條。

華區的 95 條是最驚喜的，居然 1979⁺ Maryknoll英台辭典收錄了民間習慣稱呼做「台灣國語」的發音條目。請大家一定要嘗試看看。這也是決定要做成小遊戲，讓大家都能看見的其中一個原因。

本 APP，題目資料庫由 Kin 蒐集整理，經由 NotebookLM 協助編寫程式碼。後續維護工作亦交由 Kin 維護。

有任何建議可以留言在「[Google表單](https://docs.google.com/forms/d/e/1FAIpQLSfFQm8c4y4Z8Gt2rbWaUZNj5zy_su3wHogASGcsfy8tILYd9g/viewform?usp=publish-editor)」。
""")

with st.sidebar.expander("💬 留言與建議", expanded=False):
    st.markdown("歡迎點擊下方按鈕前往 Google 表單給予建議與回饋：")
    st.link_button("📝 開啟 Google 表單留言", "https://docs.google.com/forms/d/e/1FAIpQLSfFQm8c4y4Z8Gt2rbWaUZNj5zy_su3wHogASGcsfy8tILYd9g/viewform?usp=publish-editor", use_container_width=True)
    st.caption("點擊上方按鈕開啟線上表單即可直接提交您的反饋，訊息會自動彙整給 Kin 喔！")

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

    # Progress bar
    total_cards = len(st.session_state.shuffled_deck)
    current_no = (st.session_state.card_idx % total_cards) + 1
    st.progress(current_no / total_cards)
    st.write(f"第 **{current_no}** / **{total_cards}** 題 | 當前累計得分：**{st.session_state.score}** | 連勝 Combo：**{st.session_state.combo}** 🔥")

    # Check if contains 'o'
    has_o = "o" in roman.lower() and "oo" not in roman.lower()

    # --- Mode 1: Classic Card Flip ---
    if game_mode == "🎴 經典翻牌挑戰":
        o_badge = '<br><div class="o-alert">⚠️ 本詞含有字母 o：請試唸 [o] (ㄛ) 與 [ə] (ㄜ)</div>' if has_o else ''
        card_html = textwrap.dedent(f"""
        <div class="quiz-card">
            <span class="type-tag">【{region}】挑戰題</span>
            {o_badge}
            <div class="roman-text">{roman}</div>
            <p style="color:#718096; font-size:0.9rem;">(猜猜看背後的漢字與英文解釋是什麼？)</p>
        </div>
        """)
        st.markdown(clean_html(card_html), unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if not st.session_state.flipped:
                if st.button("🎴 翻牌查看答案", use_container_width=True):
                    st.session_state.flipped = True
                    st.rerun()
            else:
                answer_html = textwrap.dedent(f"""
                <div class="answer-box">
                    <span class="type-tag">{card_type}</span>
                    <div class="kanji-text">漢字：{kanji}</div>
                    <div class="english-text">英文解釋：{english}</div>
                </div>
                """)
                st.markdown(clean_html(answer_html), unsafe_allow_html=True)

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
        o_badge = '<br><div class="o-alert">⚠️ 本詞含有字母 o：請試唸 [o] (ㄛ) 與 [ə] (ㄜ)</div>' if has_o else ''
        card_html = textwrap.dedent(f"""
        <div class="quiz-card">
            <span class="type-tag">【加分關卡】語種來源猜測</span>
            {o_badge}
            <div class="roman-text">{roman}</div>
            <p style="color:#718096;">這個羅馬字屬於哪一種語言的表示方式？</p>
        </div>
        """)
        st.markdown(clean_html(card_html), unsafe_allow_html=True)

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

            answer_html = textwrap.dedent(f"""
            <div class="answer-box">
                <span class="type-tag">{card_type}</span>
                <div class="kanji-text">漢字：{kanji}</div>
                <div class="english-text">英文解釋：{english}</div>
            </div>
            """)
            st.markdown(clean_html(answer_html), unsafe_allow_html=True)

            if st.button("下一題 ➡️", use_container_width=True):
                st.session_state.card_idx += 1
                st.session_state.flipped = False
                st.rerun()

    # --- Mode 3: Speed Run Challenge ---
    elif game_mode == "⚡ 快速連續計分賽":
        o_badge = '<br><div class="o-alert">⚠️ 本詞含有字母 o：請試唸 [o] (ㄛ) 與 [ə] (ㄜ)</div>' if has_o else ''
        card_html = textwrap.dedent(f"""
        <div class="quiz-card">
            <span class="type-tag">⚡ 快速連續挑戰賽</span>
            {o_badge}
            <div class="roman-text">{roman}</div>
        </div>
        """)
        st.markdown(clean_html(card_html), unsafe_allow_html=True)

        if not st.session_state.flipped:
            if st.button("👀 顯示答案", use_container_width=True):
                st.session_state.flipped = True
                st.rerun()
        else:
            answer_html = textwrap.dedent(f"""
            <div class="answer-box">
                <div class="kanji-text">漢字：{kanji}</div>
                <div class="english-text">英文解釋：{english}</div>
                <span class="type-tag">{card_type}</span>
            </div>
            """)
            st.markdown(clean_html(answer_html), unsafe_allow_html=True)

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
