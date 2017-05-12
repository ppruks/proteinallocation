from matplotlib import pyplot as plt
from matplotlib_venn import venn2

class GOGroups():
	'''
		This class generates a GO (Gene Ontology) group - a set of proteins.
	'''
	def __init__(self, filename, name):
		self.filename = filename
		with open (filename, 'rt') as f:
			self.proteins = set(f.read().split())
			self.name = name

	def getProteins(self):
		'''
			returns a set containing the proteins in the GO group 
		'''
		return self.proteins

	def getName(self):
		'''
			return the name of the GO group
		'''
		return self.name
	
	def sum(self, other):
		'''
			sums two GO groups like two sets 
		'''
		self.proteins = self.proteins | other.getProteins()

	def keepIntersection(self, other):
		'''
			turns the GO group into intersection of two GO groups
		'''
		self.proteins = self.proteins & other.getProteins() 

	def keepSelf(self, other):
		'''
			keeps proteins exclusively in self 
		'''
		self.proteins = self.proteins - other.getProteins()

	def keepOther(self, other):		
		'''
			keeps proteins exclusively in other 
		'''
		self.proteins = other.getProteins() - self.proteins

	def plotVenn(self, other):
		venn2(subsets = (self.proteins, other.getProteins()), set_labels = (self.name, other.getName()))
		plt.show()
	


