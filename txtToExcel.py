import pandas as pd

turkce=pd.read_fwf("sozlukTurkce")
ingilizce=pd.read_fwf("sozlukIngilizce")

turki=pd.DataFrame(turkce)

ingilizi=pd.DataFrame(ingilizce)


df=pd.concat([ingilizi,turki],axis=1)
df.columns=["ingilizce","notNumber","turkce"]

DF=df.copy()
#test1=DF.to_excel("Sozluk.xlsx")

test2=pd.read_excel("Sozluk.xlsx")
test2.to_csv("sozluk.csv",encoding="utf-8")
print(df)