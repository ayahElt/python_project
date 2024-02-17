# -*- coding: utf-8 -*-
"""optimizer module

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zh0kwGDtGzc84rhzWb1UwUj0X2A84pMr

# **OPTIMIZER MODULE**
"""

import numpy as np
from scipy.optimize import minimize

class Portfolio_optimizer:

  def __init__(self,data):
    self.log_return=np.log(data/data.shift(1))

  def expected_return (self):
    return self.log_return.sum().apply(lambda x : x*256/len(self.log_return)).to_numpy()

  def covariance (self):
    return self.log_return.cov().apply(lambda x: x *256).to_numpy()

  def optimal_weights (self):

    def excess_return(X):
    #excess return should be maximised to get the tangent portfolio. The risk free rate is set to 1%.
    #we define it as the opposite of what should be minimized, since the algorithm only minimizes
      return -1*(self.expected_return()@X.T-1/100)/(X@self.covariance()@X.T)

    #weights sum at 1
    def equal_constraint(X):
      return sum(X)-1

    X_nitial=1/35*np.ones(35)

    results=minimize(excess_return,X_nitial,method='trust-constr',constraints=[{'type': 'eq', 'fun': equal_constraint}]).x

    #we do not apply inequality constraints (eg. no short sell), as the results seem to be reasonable. Moreover, we would not get the "true" optimal portfolio as we stack constraints.

    return pd.DataFrame(results,columns=["Weights"],index=[
    "AC.PA", "AI.PA", "AIR.PA", "ALO.PA", "ATO.PA", "CS.PA", "BNP.PA",
    "EN.PA", "CAP.PA", "CA.PA", "ACA.PA", "BN.PA", "DSY.PA", "ENGI.PA", "EL.PA",
    "RMS.PA", "KER.PA", "OR.PA", "LR.PA", "MC.PA", "ML.PA", "ORA.PA", "RI.PA",
    "PUB.PA", "RNO.PA", "SAF.PA", "SGO.PA", "SAN.PA", "SU.PA", "GLE.PA",
    "TEP.PA", "HO.PA", "TTE.PA", "VIE.PA", "VIV.PA"]), pd.DataFrame([self.expected_return()@results.T,results@self.covariance()@results.T],index=["return expectation", "squared volatily"],columns=["characteristics"])

csv_handler = CSV_handler()

# Read stock data from CSV
df1 = csv_handler.read_stock_data_from_csv("/content/cac40_stock_data.csv",[
    "AC.PA", "AI.PA", "AIR.PA", "ALO.PA", "ATO.PA", "CS.PA", "BNP.PA",
    "EN.PA", "CAP.PA", "CA.PA", "ACA.PA", "BN.PA", "DSY.PA", "ENGI.PA", "EL.PA",
    "RMS.PA", "KER.PA", "OR.PA", "LR.PA", "MC.PA", "ML.PA", "ORA.PA", "RI.PA",
    "PUB.PA", "RNO.PA", "SAF.PA", "SGO.PA", "SAN.PA", "SU.PA", "GLE.PA",
    "TEP.PA", "HO.PA", "TTE.PA", "VIE.PA", "VIV.PA"],'2010-01-01','2014-12-31')

#pas de trous avec cette liste

testeur=Portfolio_optimizer(df1)
poids,profil_de_risque =testeur.optimal_weights()

poids.sum()

profil_de_risque

poids["Weights"]

def excess_return(X):
    #we define it as the opposite of what should be minimized, since the algorithm only minimizes
      return -1*(testeur.expected_return()@X.T-1/100)/(X@testeur.covariance()@X.T)

X_nitial=1/35*np.ones(35)

def perfo(X):
  return testeur.expected_return()@X.T,X@testeur.covariance()@X.T

-excess_return(X_nitial)

-excess_return(poids.to_numpy().T)

perfo(poids.to_numpy().T)

A=np.array([-0.05,0.22,0.06,-0.11,0,-0.5,0.1,0.1,0.1,0,0,0.3,0,0.2,0,0,0,0,0,0,0,0,0.7,0,0,0,0,0,0,0,0,0,0,-0.1199999999999999,0])

len(A)

-excess_return(poids.to_numpy().T+A)

perfo(poids.to_numpy().T+A)