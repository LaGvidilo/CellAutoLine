#coding: utf-8
import string, random, itertools
from PIL import Image, ImageDraw, ImageFont
class MetaCell(object):
	"""docstring for MetaCell"""
	def __init__(self, randomstate=0, sizeconf=15, configuration=""):
		super(MetaCell, self).__init__()
		if randomstate > 0:
			random.seed(randomstate)
			self.config = ''.join("0" for x in range(sizeconf-1))
			#s[:4] + '-' + s[4:]
			posrnd = random.randint(1,sizeconf-1)
			self.config = self.config[:posrnd] + "1" + self.config[posrnd:]
		else:
			self.config = configuration
		self.sizeconf = sizeconf
		self.matrix = []
		self.rules = {}
		self.name = str(randomstate)#''.join(random.choice("ABCDEF0123456789-,") for x in range(3))

	def genAllRules(self,n=3):
		mdl = [''.join(x) for x in itertools.product('01', repeat=n)]
		for i in mdl:
			self.rules[i] = str(random.randint(0,1))
		self.szn = n

	def setRules(self,rules=[]):
		self.rules = rules

	def live(self,generations=100):
		image = Image.new("RGB", (self.sizeconf, generations))
		ff = open("RS/sound"+self.name+".RS",'w+b')
		res = ""
		for g in range(0,generations):
			nextline = ""
			j=0
			for i in self.config:
				gogo = []
				#a,xNeg1,x0,xPos1,b = self.config[(j-2)%self.sizeconf],self.config[(j-1)%self.sizeconf],i,self.config[(j+1)%self.sizeconf],self.config[(j+2)%self.sizeconf]
				for d in range(-self.szn/2,self.szn/2):
					gogo.append(self.config[(j-d)%self.sizeconf])
				caze = "".join(gogo)#"".join([a,xNeg1,x0,xPos1,b])
				#print "CASE: ", caze

				nextline = nextline + self.rules[caze]
				if self.rules[caze]=="1":
					image.putpixel((j, g), (0,255,0))
					ff.write(str(j)+","+str(g)+"\n")
				j+=1
			res = res + nextline + "\n"
			self.config = nextline
		image.save("img_5/life_"+self.name+".png", "PNG")
		ff.close()
		return res

for i in range(128):
	cell = MetaCell(i,1000)
	cell.genAllRules(4)
	RESULT = cell.live(512)


