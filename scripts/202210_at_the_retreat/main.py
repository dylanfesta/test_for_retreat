
#%%
import PackageOne as one
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print(f' Constant inside package 1 : {one.c1}')

# %%

one.error_maybe()
# %%

N = 100
# numpy array of size N filled with 4s

v4 = np.full(N, 4) 

# numpy array of gaussian random variables of size N
vrand = np.random.randn(N)

# if value in vrand is smaller than 0, swap it with v4
vswap = np.where(vrand < 0, v4, vrand)

# plot vswap as a scatter
plt.scatter(range(N), vswap)

# %%

# function that creates a numpy array of size N filled
# with x values
def make_array(N,x):
  return np.full(N,x)

