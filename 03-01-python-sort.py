import pandas as pd

# data.csv の文字コード「UTF-8」、改行コード「LF」で開く
df = pd.read_csv("data.csv", encoding = "shift_jis", index_col = 0, header=0)

# 郵便番号でソート
df = df.sort_values(by = ["郵便番号"], ascending = True)
print (df)
