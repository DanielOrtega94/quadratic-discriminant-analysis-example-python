import csv
import random
import math
from matplotlib import pyplot as plt
import numpy as np
#https://onlinecourses.science.psu.edu/stat505/node/94
datos = [[1,2,0],[2,2,0],[2,3,0],[3,1,0],[3,2,0],[9,12,1],[8,8,1],[8,7,1],[8,9,1],[7,10,1]]
def grafica(datos):
	features = zip(*datos)
	x = features[0]
	y = features[1]
	N = len(x)
	colors = []
	for i in range(N):
		if datos[i][-1] == 0:
			colors.append(0.52160121)
		else:
			colors.append(0.75089678)
	area = np.pi*20  # 0 to 15 point radiuses
	plt.scatter(x, y, s=area, c=colors, alpha=0.5)
	plt.show()

def porClase(datos):
	datosClase = {}
	for i in range(len(datos)):
		vector = datos[i]
		if (vector[-1] not in datosClase):
			datosClase[vector[-1]] = []
		datosClase[vector[-1]].append(vector)
	return datosClase

def mean(feature):
	return sum(feature)/float(len(feature))

def elemento(Entrenamiento):
	elementos = [mean(atributo) for atributo in zip(*Entrenamiento)]
	del elementos[-1]
	return elementos
		
def main(test):
	DatosClase = porClase(datos)
	for classValue, features in DatosClase.iteritems():		
		testa = np.array(test)
		x = zip(*features)
		del x[-1]
		m = np.array(elemento(features))
		mT = np.array(m)[np.newaxis].T
		testT = np.array(test)[np.newaxis].T
		print x
		cov =  np.ma.cov(x, y=None, rowvar=True, bias=False, allow_masked=True, ddof=None)
		print cov
		covinv =  np.linalg.inv(cov)
		eBeta = np.dot(m,covinv)
		en = np.dot(eBeta,mT)
		N = 1/float(len(features))
		Ln = np.log(N)
		a = -0.5*np.dot(test,covinv)
		b = np.dot(a,testa)
		dx = b +  np.dot(eBeta,testT) -0.5*en-0.5*np.log(en)
		dx[0] = dx[0] + Ln
		print dx
test =[9,12]
main(test)	
