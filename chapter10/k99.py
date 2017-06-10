import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
import numpy as np

sns.set_style('white')
sns.set_context('talk', 2, {"lines.linewidth": 6})

keys = pickle.load(open('countryNames.pkl', 'rb'))
vectors = pickle.load(open('countryVectors.pkl', 'rb'))

tsne = TSNE(n_components=2, random_state=0).fit_transform(np.array(vectors))

x, y = tsne.T
plt.scatter(x, y)

for lc, countryname in enumerate(keys):
    plt.annotate(countryname, xy=(x[lc], y[lc]), fontsize=10)

plt.savefig('tsne.pdf', bbox_inches="tight", pad_inches=0.1)
plt.show()
