import streamlit as st
import random


QUESTION_BANK = [
    {"category":"發射流程","question":"以下敘述之火箭正式上架前的程序哪項正確?","options":{"A":"不須額外的程序","B":"可試上發射架","C":"需審查委員確認","D":"B、C都正確"},"answer":"D"},
    {"category":"發射流程","question":"火箭上架準備超過多久時間便會要求重新排隊進行發射準備?","options":{"A":"30 分鐘","B":"60 分鐘","C":"50 分鐘","D":"75 分鐘"},"answer":"C"},
    {"category":"發射流程","question":"火箭於發射架上電後能否再下電?","options":{"A":"任何時候都可以","B":"不可以，經審查委員確認完即不可下電","C":"不可以，經隊內航電人員確認完即不可下電","D":"可以，但須審查員的許可"},"answer":"B"},
    {"category":"發射流程","question":"審查人員發射許可檢查項目包含哪些?","options":{"A":"Rail button位於質心兩側","B":"火箭外型無異狀突起物","C":"所有零件已鎖緊固定","D":"以上皆是"},"answer":"D"},
    {"category":"發射流程","question":"火箭發射後，回收的時間區間為多久?","options":{"A":"1 小時","B":"2 小時","C":"30 分鐘","D":"1.5 小時"},"answer":"A"},
    {"category":"發射流程","question":"以下關於發射流程的敘述何者正確?","options":{"A":"火箭上架準備完成後需全員撤離","B":"在任何情況下皆可發射","C":"火箭需能在軌道上滑動無阻礙","D":"A、C正確"},"answer":"D"},
    {"category":"發射流程","question":"固態火箭發動機何時組裝完成?","options":{"A":"發射許可審查時間","B":"火箭上架準備時間","C":"火箭發射準備時間","D":"團隊技術交流時間"},"answer":"B"},
    {"category":"發射流程","question":"固態火箭發動機點火線路由誰安裝","options":{"A":"審查委員","B":"競賽現場工作人員","C":"參賽隊員","D":"團隊指導員"},"answer":"B"},
    {"category":"發射流程","question":"若固態火箭發動機點火啟動失敗（未燃燒）該如何處理","options":{"A":"由競賽現場工作人員確認安全","B":"重新安裝點火線路並發射","C":"取消並重新排隊","D":"A、C正確"},"answer":"D"},
    {"category":"發射流程","question":"火箭落海後由誰打撈回收","options":{"A":"審查委員","B":"競賽現場工作人員","C":"參賽隊員","D":"團隊指導員"},"answer":"B"},
    {"category":"發射流程","question":"火箭落海打撈後於哪邊上岸","options":{"A":"旭海漁港","B":"科研火箭發射場","C":"沙灘","D":"觀看區"},"answer":"A"},
    {"category":"發射流程","question":"參賽隊員撤離後何者錯誤","options":{"A":"於安全區觀看","B":"注意發射動態","C":"進行發射程序","D":"拍攝"},"answer":"C"},

    {"category":"火箭系統","question":"為什麼製作火箭通常會建議開一個小洞在分節段?","options":{"A":"降落傘","B":"紀錄氣壓","C":"釋放內壓避免過早脫節","D":"組裝記號"},"answer":"C"},
    {"category":"火箭系統","question":"使用壓力計時為何需在航電段開孔?","options":{"A":"減少瞬間影響","B":"紀錄氣壓","C":"釋放內壓","D":"電池記號"},"answer":"B"},
    {"category":"火箭系統","question":"公版固態火箭發動機最大推力為多少公斤重?","options":{"A":"200","B":"100","C":"1000","D":"400"},"answer":"A"},
    {"category":"火箭系統","question":"火箭動態穩定性至少需大於多少?","options":{"A":"2","B":"1","C":"1.5","D":"3"},"answer":"C"},
    {"category":"火箭系統","question":"無導控火箭設計時氣壓中心需位於質心哪?","options":{"A":"後方","B":"前方","C":"重合","D":"無關"},"answer":"A"},
    {"category":"火箭系統","question":"如何讓不穩定火箭變穩定?","options":{"A":"鼻錐增重","B":"鼻錐減重","C":"尾翼前移","D":"縮短箭長"},"answer":"A"},
    {"category":"火箭系統","question":"火箭在加速時會趨向?","options":{"A":"逐漸穩定","B":"逐漸不穩","C":"不影響","D":"變不穩"},"answer":"A"},
    {"category":"火箭系統","question":"尾翼通常建議如何固定?","options":{"A":"黏貼外殼","B":"釘子","C":"穿殼固定","D":"皆可"},"answer":"C"},
    {"category":"火箭系統","question":"離架穩定性需小於多少?","options":{"A":"6","B":"4","C":"2","D":"1.5"},"answer":"B"},
    {"category":"火箭系統","question":"軌道滑塊正確敘述?","options":{"A":"質心前後各一","B":"可3D列印","C":"不須考慮航電","D":"可用膠固定"},"answer":"A"},
    {"category":"火箭系統","question":"火箭主結構需承受什麼?","options":{"A":"無須考慮","B":"僅地面","C":"飛行應力","D":"搬運"},"answer":"C"},
    {"category":"火箭系統","question":"氣壓中心可如何得出?","options":{"A":"理論","B":"模擬軟體","C":"秤台","D":"A、B"},"answer":"D"},
    {"category":"火箭系統","question":"火箭系統三大類?","options":{"A":"結構、航電、推進","B":"航電、鼻錐、推進","C":"結構、天線、噴嘴","D":"結構、鼻錐、噴嘴"},"answer":"A"},
    {"category":"火箭系統","question":"飛行模擬目的?","options":{"A":"軌跡設計","B":"受力估算","C":"飛後分析","D":"以上皆是"},"answer":"D"},
    {"category":"火箭系統","question":"任務規劃正確順序?","options":{"A":"發射→開傘→慣性","B":"慣性→結束→落地","C":"慣性→開傘→落地","D":"發射→開傘→結束"},"answer":"C"},
    {"category":"火箭系統","question":"尾翼顫振速度至少高於最大速度多少?","options":{"A":"10%","B":"25%","C":"50%","D":"100%"},"answer":"C"},
    {"category":"火箭系統","question":"一定要做的航電測試?","options":{"A":"衝擊振動","B":"溫循","C":"真空","D":"噪音"},"answer":"A"},
    {"category":"火箭系統","question":"海面回收終端速度建議低於?","options":{"A":"10","B":"11","C":"12","D":"13"},"answer":"C"},
    {"category":"火箭系統","question":"航電電池需供電至少多久?","options":{"A":"0.5","B":"1","C":"1.5","D":"2"},"answer":"C"},
    {"category":"火箭系統","question":"何者非允許儲能裝置?","options":{"A":"高壓氣瓶","B":"黑色火藥","C":"煙霧棒","D":"彈簧"},"answer":"B"},
    {"category":"火箭系統","question":"3K組火箭總重不得超過?","options":{"A":"20","B":"25","C":"28.5","D":"30.5"},"answer":"C"},
    {"category":"火箭系統","question":"禁用材料為?","options":{"A":"玻璃纖維","B":"PVC","C":"鋁","D":"鉛"},"answer":"D"},

    {"category":"發射安全","question":"禁止行為?","options":{"A":"飲酒","B":"影響判斷藥物","C":"手機通話","D":"A、B"},"answer":"D"},
    {"category":"發射安全","question":"建議攜帶裝備?","options":{"A":"滅火器","B":"急救箱","C":"兩者","D":"兩者加聯絡"},"answer":"D"},
    {"category":"發射安全","question":"射場環境確認包含?","options":{"A":"地震","B":"風速","C":"濃霧","D":"以上皆是"},"answer":"D"},
    {"category":"發射安全","question":"人員距離至少?","options":{"A":"50","B":"80","C":"100","D":"150"},"answer":"C"},
    {"category":"發射安全","question":"最大允許風速?","options":{"A":"6","B":"7","C":"8","D":"15"},"answer":"A"},
    {"category":"發射安全","question":"發射架仰角上限?","options":{"A":"88","B":"86","C":"85","D":"83"},"answer":"C"},
    {"category":"發射安全","question":"點火後留在架上應?","options":{"A":"滅火","B":"等燃盡","C":"拉封鎖線","D":"以上皆非"},"answer":"B"},
    {"category":"發射安全","question":"整備期間何者錯誤?","options":{"A":"護目鏡","B":"防割手套","C":"安全帽","D":"招待訪客"},"answer":"D"},
    {"category":"發射安全","question":"不確定問題處理方式何者錯?","options":{"A":"自行處理","B":"問指導員","C":"問現場人員","D":"問審查"},"answer":"A"},
    {"category":"發射安全","question":"車輛停放規定何者正確?","options":{"A":"可停管制內","B":"點火後可移動","C":"須停管制外","D":"無規定"},"answer":"C"},

    {"category":"風險管理","question":"風險管理目的?","options":{"A":"發現風險","B":"降低風險","C":"形成經驗","D":"以上皆是"},"answer":"D"},
    {"category":"風險管理","question":"何者優先處理?","options":{"A":"嚴重9 發生3","B":"嚴重3 發生9","C":"嚴重3 難檢9","D":"嚴重3 發生3"},"answer":"A"},
    {"category":"風險管理","question":"DFMEA不包含?","options":{"A":"成本","B":"檢測性","C":"人身危險","D":"發生率"},"answer":"A"},
    {"category":"風險管理","question":"正確標準化觀念?","options":{"A":"訂容許誤差","B":"免校驗","C":"可直接改SOP","D":"以上皆是"},"answer":"A"},
    {"category":"風險管理","question":"FMEA適用範圍?","options":{"A":"新產品","B":"變更設計","C":"修改情境","D":"以上皆是"},"answer":"D"}
]


RULES = {"發射流程":8,"火箭系統":20,"發射安全":8,"風險管理":4}


def generate_exam():
    exam=[]
    for c,n in RULES.items():
        pool=[q for q in QUESTION_BANK if q["category"]==c]
        exam+=random.sample(pool,n)
    random.shuffle(exam)
    return exam


st.title("火箭測驗系統")

if "exam" not in st.session_state:
    st.session_state.exam = generate_exam()
    st.session_state.answers = {}

exam = st.session_state.exam


for i, q in enumerate(exam, 1):
    st.subheader(f"{i}. {q['question']}")
    choice = st.radio(
        label="請選擇答案",
        options=list(q["options"].keys()),
        format_func=lambda x: f"{x}. {q['options'][x]}",
        key=f"q{i}"
    )
    st.session_state.answers[i] = choice


if st.button("📨 交卷"):
    correct = 0
    wrong = []

    for i, q in enumerate(exam, 1):
        if st.session_state.answers[i] == q["answer"]:
            correct += 1
        else:
            wrong.append((q, st.session_state.answers[i]))

    total = len(exam)
    st.success(f"答對 {correct} / {total} 題")
    st.write("結果：", "通過" if correct >= 35 else "未通過")

    if wrong:
        st.error("錯題回顧：")
        for q, a in wrong:
            st.write("題目：", q["question"])
            st.write(
                "你的答案：", f"{a}. {q['options'][a]}",
                "｜正確答案：", f"{q['answer']}. {q['options'][q['answer']]}"
            )
            st.write("---")
            
    st.markdown("---")

    with st.expander("📚 顯示題庫與答案"):
        for i, q in enumerate(QUESTION_BANK, 1):
            st.write(f"{i}. [{q['category']}] {q['question']}")
            
            for key, text in q["options"].items():
                if key == q["answer"]:
                    st.write(f"{key}. {text} ✅")  # 正確答案標記
                else:
                    st.write(f"{key}. {text}")
            
            st.write("")
