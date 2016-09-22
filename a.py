#Algorithm parameters:
import math
import random
v = input()
d = input()
N = 6040
I = 3952
#data in mu
epsilonN = pow((pow(2,(5*d+18))/float(v))*630*(2*d+11)*pow((d+2),4)*(1/float(N)),(1/float(d+5)))
print epsilonN
C = v/float(20*148)
print C
def epsTow(tow):
	EpsilonTow = max(1/(pow(2,tow)),epsilonN)
	EpsilonTow = EpsilonTow*C
	return EpsilonTow
def mTow(tow):
	MTow = (pow(2,max(3.5*d,8))/float(v))*((3*d+1)/(pow(epsTow(tow),d+2)))*math.log((2/epsTow(tow))) 
	return MTow
def dTow(tow):
	DTow = (v/2.0)*(mTow(tow))

def randomM(M):
	M_random_items = []
	for i in range(M):
		m = np.random.random_integers(1,3952,1)
		M_random_items.append(m)
	return M_random_items

def ItemItemCF(N):
	

def GetNet(epsilon,delta):
	C = []
	COUNT = 0
	MAX_SIZE = pow(4/float(epsilon),d)
	MAX_WAIT = pow(5/float(epsilon),d)*math.log(2*MAX_SIZE/delta)
	delta_dash = delta/(4*MAX_WAIT*pow(MAX_SIZE,2))
	while COUNT<= MAX_WAIT and len(C)<MAX_SIZE:
		for i in mu:
			for j in C:
				if Similar(i,j,epsilon,delta_dash):
					COUNT = COUNT + 1
				else:
					C.append(i)
	return C


def MakePartitions(M,epsilon,delta):
	C = GetNet(epsilon/2.0,delta/2.0)
	M = randomM()
	P_i = []
	for i in range(len(C)):
		P_i.append([])
	for j in M:
		S_j = []
		for i in C:
			if Similar(i,j,0.6*epsilon,(delta/(4*len(M)*len(C))):
				S_j.append(i)
		if len(S_j)>0:
			for i in S_j:
				P_i[i-1].append(j)









