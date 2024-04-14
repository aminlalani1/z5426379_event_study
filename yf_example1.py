import yfinance
tic = "QAN.AX"
start = '2020-01-01'
end = None
df = yfinance.download(tic, start, end, ignore_tz=True)
print(df)
df.to_csv('qan_stk_prc.csv')