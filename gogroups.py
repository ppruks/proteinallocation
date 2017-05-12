class GOGroups():
	'''
		A GO Group is a set of proteins.
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
	
	def unionWith(self, other):
		'''
			sums two GO groups like two sets 
		'''
		self.proteins = self.proteins | other.getProteins()

	def intersectWith(self, other):
		'''
			turns the GO group into intersection of two GO groups
		'''
		self.proteins = self.proteins & other.getProteins() 

	def subtract(self, other):
		'''
			keeps only the proteins in self 
		'''
		self.proteins = self.proteins - other.getProteins()

	def subtractedFrom(self, other):		
		'''
			keeps only the proteins in other
		'''
		self.proteins = other.getProteins() - self.proteins

	


