import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('RUN3.csv')
tabela1 = df.set_index('f1')
tabela2 = df.set_index('f2')
f1=tabela1.index.values
f2=tabela2.index.values