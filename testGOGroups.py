from GOGroups import GOGroups
from matplotlib import pyplot as plt
from matplotlib_venn import venn2

def plotVenn(first, second):
	venn2(subsets = (first.getProteins(), other.getProteins()), set_labels = (first.getName(), other.getName()))
	plt.show()

filename1 = "gogroups/go006417.txt"
filename2 = "gogroups/go0006555.txt"
ribosome = GOGroups(filename1, "ribosome")
other = GOGroups(filename2, "other")
plotVenn(ribosome, other)
ribosome.unionWith(other)
plotVenn(ribosome,other)


