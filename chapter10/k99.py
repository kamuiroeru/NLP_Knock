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
plt.scatter(x, y, s=0)

ddg = pickle.load(open('./ddg.pkl', 'rb'))
countrynameToColor = {k: color for k, color in zip(ddg['ivl'], ddg['color_list'] + [ddg['color_list'][-1]])}
for lc, countryname in enumerate(keys):
    plt.annotate(countryname, xy=(x[lc], y[lc]), fontsize=10, color=countrynameToColor[countryname])

plt.savefig('tsne.pdf', bbox_inches="tight", pad_inches=0.1)
plt.show()
