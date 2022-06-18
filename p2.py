import pandas as pd
import scipy.stats as st
import numpy as np

df = pd.read_csv("data\coin_Bitcoin.csv")
dfb = list(df.Low)
dfh = list(df.High)

alto = list(dfh)
bajo = list(dfb)


promedio = []
for x in range(len(dfh)):
    promedio.append(round(((alto[x]+bajo[x])/2),4))

df["Price"] = promedio
dfp = df.Price

bajo100 = list(dfp.sample(100))
bajo100.sort()

confianza90 = st.t.interval (alpha = 0.90, df = len (bajo100) -1, loc = np.mean (bajo100), scale = st.sem (bajo100))
confianza95 = st.t.interval (alpha = 0.95, df = len (bajo100) -1, loc = np.mean (bajo100), scale = st.sem (bajo100))
confianza100 = st.t.interval (alpha = 0.100, df = len (bajo100) -1, loc = np.mean (bajo100), scale = st.sem (bajo100))

print(f'El intervalo de confianza con confianza 90 fue de: {confianza90}')
print(f'El intervalo de confianza con confianza 90 fue de: {confianza95}')
print(f'El intervalo de confianza con confianza 90 fue de: {confianza100}')