#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  weightedsum.py
#  
#  Copyright 2014 gianluca <g_massa@libero.it>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

class topsis:
	def __init__(self,matrix):
		self.rows=len(matrix)
		self.cols=len(matrix[0])
		self.idealPoints=[max(x) for x in zip(*matrix)]
		self.worstPoints=[min(x) for x in zip(*matrix)]
		pass
	
	def setPoints(self,idealPoints,worstPoints):
		self.idealPoints=idealPoints
		self.worstPoints=worstPoints
		
	def normMatrix(self,matrix):
		squareMatrix=[[y**2 for y in row] for row in matrix] #elevation square matrix
		vectorSumSquare=[sum(x) for x in zip(*squareMatrix)] #get vector of column sum og square matrix
		normMatrix=[[z/v for z,v in zip(row,vectorSumSquare)] for row in squareMatrix] #normalize Matrix: TOPSIS algorithm: STEP 1
		return normMatrix
		
	def weightMatrix(self,normMatrix,weight):
		normWeightMatrix=[[ z*w for z,x in zip(row,weight)] for row in normMatrix] #weight normalized matrix: TOPSIS algorithm: STEP 2
		return normWeightMatrix
		
	def idealPointDistance(self,normWeightMatrix,idealPoints): #distance  fro idealpoint: TOPSIS algorithm: STEP 4
		mat=[[(x-y)**2 for x,y in zip(row,idealpoints)]for row in normWeightMatrix]
		sumDifferenceVector=[sum(x) for x in zip(*mat)] 
		idealPointsDistance=[x**0.5 for x in sumDifferenceVector]
		return idealPointsDistance
		
	def negativePointDistance(self,normWeightMatrix,worstPoints): #distance  from idealpoint: TOPSIS algorithm: STEP 4
		mat=[[(x-y)**2 for x,y in zip(row,worstPoints)]for row in normWeightMatrix]
		sumDifferenceVector=[sum(x) for x in zip(*mat)] 
		negativePointDistance=[x**0.5 for x in sumDifferenceVector]
		return negativePointDistance
		
	def relativeCloseness(self,):  #relative closeness - TOPSIS algorithm STEP 5
		relativeCloseness=[(n/(n+p)) for n,p in zip(negativePointDistance,idealPointsDistance)]
		return relativeCloseness
		
	def runTOPSIS(self,stdMatrix,weight):
		"""process the matrix and get the ranking values for each alternative"""
		pass
	

if __name__ == '__main__':
	main()
