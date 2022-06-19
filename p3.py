import pandas as pd
import scipy.stats as st
import numpy as np

BT = pd.read_csv("data\coin_Bitcoin.csv")
ETH = pd.read_csv("data\coin_Ethereum.csv")
COIN = pd.read_csv("data\coin_USDCoin.csv")
DOGE = pd.read_csv("data\coin_Dogecoin.csv")


muestra = ETH.sample(n=501)
muestraindex = muestra["High"].keys()
prices=[]
for i in muestraindex:
    prices.append((muestra["High"][i]+muestra["Low"][i])/2)
s = np.std(prices)

muestra = BT.sample(n=501)
muestraindex = muestra["High"].keys()
prices=[]
for i in muestraindex:
    prices.append((muestra["High"][i]+muestra["Low"][i])/2)
sB = np.std(prices)

muestra = COIN.sample(n=501)
muestraindex = muestra["High"].keys()
prices=[]
for i in muestraindex:
    prices.append((muestra["High"][i]+muestra["Low"][i])/2)
sC = np.std(prices)

muestra = DOGE.sample(n=501)
muestraindex = muestra["High"].keys()
prices=[]
for i in muestraindex:
    prices.append((muestra["High"][i]+muestra["Low"][i])/2)
sD = np.std(prices)

iE = [((500*(s**2))/563.8514)**(1/2), ((500*(s**2))/439.9360)**(1/2)]
iB = [((500*(sB**2))/563.8514)**(1/2), ((500*(sB**2))/439.9360)**(1/2)]
iC = [((500*(sC**2))/563.8514)**(1/2), ((500*(sC**2))/439.9360)**(1/2)]
iD = [((500*(sD**2))/563.8514)**(1/2), ((500*(sD**2))/439.9360)**(1/2)]

print("Etherium (n=501, confianza = 95%):")
print(iE)
print("Bitcoin (n=501, confianza = 95%):")
print(iB)
print("USDCoin (n=501, confianza = 95%):")
print(iC)
print("DogeCoin (n=501, confianza = 95%):")
print(iD)
