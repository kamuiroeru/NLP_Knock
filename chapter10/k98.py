import pickle
from scipy.cluster.hierarchy import ward, dendrogram
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('white')
sns.set_context('talk', 2, {"lines.linewidth": 6})
plt.figure(figsize=(60, 20))

keys = pickle.load(open('countryNames.pkl', 'rb'))
vectors = pickle.load(open('countryVectors.pkl', 'rb'))

result = ward(vectors)
dendrogram(result, labels=keys, leaf_font_size=20)

plt.savefig('ward.pdf', bbox_inches="tight", pad_inches=0.1)
# plt.show()

# ['ivl', 'leaves', 'dcoord', 'icoord', 'color_list']
