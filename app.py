import streamlit as st
import pandas as pd
from datetime import datetime
from engine import calculate

st.title("智慧數字人生")

name = st.text_input("姓名")

col1, col2, col3 = st.columns(3)

with col1:
    year = st.text_input("年", max_chars=4)

with col2:
    month = st.number_input(
        "月",
        min_value=1,
        max_value=12,
        step=1
    )

with col3:
    day = st.number_input(
        "日",
        min_value=1,
        max_value=31,
        step=1
    )

# 自動補零
month = str(int(month)).zfill(2)
day = str(int(day)).zfill(2)

birthday = f"{year}/{month}/{day}"

valid_date = True

try:
    datetime.strptime(birthday, "%Y/%m/%d")

except:
    valid_date = False

if year:

    if valid_date:

        result = calculate(birthday)

    else:

        st.error("日期不存在")

    st.header(f"{name}－{result['幾號人']}號人")

    

    html = f"""
    <table style="width:100%; font-size:14px;">
    <tr>
    <td>1. 父基因：{result['父基因']}</td>
    <td>8. 事業過程2：{result['事業過程2']}</td>
    </tr>

    <tr>
    <td>2. 母基因：{result['母基因']}</td>
    <td>9. 當下朋友：{result['當下朋友']}</td>
    </tr>

    <tr>
    <td>3. 主性格：{result['主性格']}</td>
    <td>10. 婚姻過程1：{result['婚姻過程1']}</td>
    </tr>

    <tr>
    <td>4. 過程1：{result['過程1']}</td>
    <td>11. 婚姻過程2：{result['婚姻過程2']}</td>
    </tr>

    <tr>
    <td>5. 過程2：{result['過程2']}</td>
    <td>12. 未來財富：{result['未來財富/健康/子媳']}</td>
    </tr>

    <tr>
    <td>6. 子女下屬：{result['子女下屬']}</td>
    <td>13. 隱藏號：{result['隱藏號']}</td>
    </tr>

    <tr>
    <td>7. 事業過程1：{result['事業過程1']}</td>
    <td></td>
    </tr>

    </table>
    """

    st.markdown(html, unsafe_allow_html=True)

    st.subheader("缺失數字")

    missing = result["缺失數字"]

    st.write("缺少：", "、".join(str(x) for x in missing))

    st.subheader("自身五行")

    five_elements = result["自身五行"]

    table_data = {
        "自己": [
            five_elements["自己"].split("：")[0],
            five_elements["自己"].split("：")[1]
        ],
        "子女錢財": [
            five_elements["子女錢財"].split("：")[0],
            five_elements["子女錢財"].split("：")[1]
        ],
        "事業伴侶": [
            five_elements["事業伴侶"].split("：")[0],
            five_elements["事業伴侶"].split("：")[1]
        ],
        "官鬼疾病": [
            five_elements["官鬼疾病"].split("：")[0],
            five_elements["官鬼疾病"].split("：")[1]
        ],
        "父母貴人": [
            five_elements["父母貴人"].split("：")[0],
            five_elements["父母貴人"].split("：")[1]
        ],
    }

    df = pd.DataFrame(table_data)

    st.dataframe(df, hide_index=True)