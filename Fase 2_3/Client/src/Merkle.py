import hashlib
import os

class Node:
	def __init__(self, _data):
		self.data = _data

class HashNode:
	def __init__(self, _hash):
		self.hash = _hash
		self.left = None
		self.right = None

class Merkle:
	def __init__(self):
		self.tophash = None
		self.dataBlock = []
		self.dot = ""
		self.index = 0

	def add(self, value):
		self.dataBlock.append(Node(value))

	def createTree(self,exp):
		self.tophash = HashNode('0')
		self._createTree(self.tophash, exp)
	
	def _createTree(self, tmp, exp):
		if (exp > 0):
			tmp.left = HashNode('0')
			tmp.right = HashNode('0')
			self._createTree(tmp.left, exp-1)
			self._createTree(tmp.right, exp-1)
	
	def genHash(self, tmp, n):#Metodo postOrder
		if(tmp != None):
			self.genHash(tmp.left, n)
			self.genHash(tmp.right, n)

			if(tmp.left == None and tmp.right == None):
				self.index -=1
				# range = n-self.index
				tmp.left = self.dataBlock[n-self.index-1]
				# print(tmp.left.data)
				id = hashlib.sha256(str(tmp.left.data).encode('utf-8')).hexdigest()
				tmp.hash = id
			else:
				id = hashlib.sha256(str(tmp.left.hash + tmp.right.hash).encode('utf-8')).hexdigest()
				tmp.hash = id

	def preOrder(self,tmp):
		if(tmp != None):
			if(isinstance(tmp, Node)):
				print('DB:',tmp.data)
				return
				# self.preOrder(tmp)
			else:
				# print(tmp.hash)
				print(tmp.hash)
			self.preOrder(tmp.left)
			self.preOrder(tmp.right)


	def auth(self):
		exp = 1
		while(pow(2,exp) < len(self.dataBlock)):
			exp +=1 
		i = len(self.dataBlock)
		for i in range(pow(2,exp)-len(self.dataBlock)):
			print('iterator es: '+str(i))
			self.dataBlock.append(Node(-10))
		self.index = pow(2,exp)
		self.createTree(exp)
		self.genHash(self.tophash, self.index)
		self.preOrder(self.tophash)

	def show(self):
		print('\n---SHOWING TREE NODES---')
		for i in self.dataBlock:
			print(i.data)

	def dotgen(self, tmp):
		if (tmp != None):
			if (tmp.left != None):
				if (isinstance(tmp.left, Node)):
						self.dot+='\n"'+str(tmp.left.data)+'" [color=gray]"'+str(tmp.left.data)+'" -> "'+str(tmp.hash)+'";\n'
						return
			if (isinstance(tmp.left, HashNode)):
				if(tmp.left != None): self.dot+='"'+str(tmp.left.hash)+'" -> "'+str(tmp.hash)+'";'
				if(tmp.right != None): self.dot+='"'+str(tmp.right.hash)+'" -> "'+str(tmp.hash)+'";'
				# return
			self.dotgen(tmp.left)
			self.dotgen(tmp.right)
			#--- se genera DOT y se procede a ecjetuar el comando
			
# if __name__ == "__main__":
# 	print('MERKLE TREE')
# 	m = Merkle()
# 	m.add('7 BarcoPeral 13/11/2022')
# 	m.add('8 NEgro 25/11/2022')	
# 	m.add('9 Amarillo tier2 2/11/2022')
# 	m.auth()
# 	m.show()
# 	print(m.tophash.hash)
# 	m.dot = 'digraph G {rankdir=BT;node [shape=box]'
# 	m.dotgen(m.tophash)
# 	m.dot+='}'
# 	dot = "/home/ijosuer/Escritorio/EDD_2S_BatallaNaval_202000895/archivos/{}_dot.txt".format('merkle')
# 	with open(dot, 'w') as grafo:
# 			grafo.write(m.dot)
# 	result = "./{}.png".format('merkle')
# 	os.system("dot -Tpng " + dot + " -o " + result)



	# print('Aplicar hash')
	# id = 'BarcoLeyenda1'+'1:34'+'26/10/2022'
	# id = '7'
	# hashid = hashlib.sha256('7'.encode('utf-8')).hexdigest()
	# print(id)
	# print(hashid)