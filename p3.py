import pandas as pd
import scipy.stats as st
import numpy as np

BT = pd.read_csv("data\coin_Bitcoin.csv")
ETH = pd.read_csv("data\coin_Ethereum.csv")
dfbBT = list(BT.Low)
dfhBT = list(BT.High)

altoBT = list(dfhBT)
bajoBT = list(dfbBT)


promedioBT = []
for x in range(len(dfhBT)):
    promedioBT.append(round(((altoBT[x]+bajoBT[x])/2),4))

BT["Price"] = promedioBT
BTp = BT.Price

dfb = list(ETH.Low)
dfh = list(ETH.High)

alto = list(dfh)
bajo = list(dfb)


promedio = []
for x in range(len(dfh)):
    promedio.append(round(((alto[x]+bajo[x])/2),4))

ETH["Price"] = promedio
ETHp = ETH.Price

BTlist = list(BTp)
BTlist.sort()
ETHlist = list(ETHp)
ETHlist.sort()

BTC = st.t.interval (alpha = 0.95, df = len (BTlist) -1, loc = np.mean (BTlist), scale = st.sem (BTlist))
ETHi = st.t.interval (alpha = 0.95, df = len (ETHlist) -1, loc = np.mean (ETHlist), scale = st.sem (ETHlist))
print(f'Intervalo de confianza de bitcoin: {BTC}')
print(f'Intervalo de confianza de etherium: {ETHi}')