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

def intconfVar(lista, dt):
    gl = (len(lista)-1)
    print(gl)
    s = np.std(dt)
    Chili = round(st.chi2.ppf(0.975,gl),2)
    Chils = round(st.chi2.ppf(0.025,gl),2)
    print(F'Chili: {Chili}')
    v = s**2
    liminf = (gl*v)/Chili
    limisup = (gl*v)/Chils
    print("limisup")
    print(limisup)
    print("directo")
    print(((39*v)/Chils)**1/2)
    dif = limisup - liminf
    intervalo = (f'[{liminf} < x < {limisup}]')
    return (intervalo, dif, v)

print(intconfVar(list(BTp), BTp))

dfb = list(ETH.Low)
dfh = list(ETH.High)

alto = list(dfh)
bajo = list(dfb)


promedio = []
for x in range(len(dfh)):
    promedio.append(round(((alto[x]+bajo[x])/2),4))

ETH["Price"] = promedio
ETHp = ETH.Price

promedio = ETHp.sample(n=40)
print(intconfVar(list(promedio), promedio))
