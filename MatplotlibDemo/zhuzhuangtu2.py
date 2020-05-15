import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn

norm_reviews = pd.read_excel('testing.xlsx')
norm_reviews_cols =  norm_reviews.columns.tolist()
print(norm_reviews_cols)
fig,ax = plt.subplots()
ax.hist(norm_reviews['Value'],range=(4,5),bins = 20)
plt.show()