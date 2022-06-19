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

bajo25 = list(dfp.sample(25))
bajo25.sort()


bajo100 = list(dfp.sample(100))
bajo100.sort()
bajo1000 = list(dfp.sample(1000))
bajo1000.sort()

muestral25 = st.t.interval (alpha = 0.95, df = len (bajo25) -1, loc = np.mean (bajo25), scale = st.sem (bajo25))
muestral100 = st.norm.interval (alpha = 0.95, loc = np.mean (bajo100), scale = st.sem (bajo100))
muestral1000 = st.norm.interval (alpha = 0.95, loc = np.mean (bajo1000), scale = st.sem (bajo1000))

print(f'Intervalo de confianza de muestra 25: {muestral25}')
print(f'Intervalo de confianza de muestra 100: {muestral100}')
print(f'Intervalo de confianza de muestra 1000: {muestral1000}')

