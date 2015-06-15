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

import normalize

class prometheeII:
	def __init__(self,matrix):
		self.miN=float(min(matrix))
		self.maX=float(max(matrix))
		return 0
		
	def increase(self,criterion):
		"""normalize criterion withe gain/increase function"""
		miN=min(criterion)
		maX=max(criterion)
		normCritrion=[float((x-miN)/(maX-miN)) for x in criterion]
		return normCritrion
		
	def decrease(self,criterion):
		"""normalize criterion withe cost/decrease function"""
		miN=min(criterion)
		maX=max(criterion)
		normCritrion=[float((maX-x)/(maX-miN)) for x in criterion]
		return normCritrion
		

	def preferenceMatrix(self, matrix,criteria,weight):
		"""[3]Calcolus of preference finction Pj(i,i')"""
		preference=[]
		for i in range(len(criteria)):
			col=[row[i] for row in matrix]
			for ci in col:
				for cj in col:
					if ci>cj:
						value=ci-cj
					else:
						value=value
					row.append(value)
				preference.append(row)
					

	def preferenceAggregatedMatrix(self, matrix,weight):
		"""[3]Calcolus of preference finction Pj(i,i') 
		and [4]Calcolus of aggregation function of preference  (weighted)"""
		preference=[]
		for row1 in matrix:
			crow=[]
			for row2 in matrix:
				value=0
				for r1,r2,w in zip(row1,row2,weight):
					if r1>r2:
						value=value+((r1-r2)*w)
					else:
						value=value
				crow.append(value)
			preference.append(crow)
		return preference

	def poisitiveFlow(self,preference):
		positiveFlow=[sum(row) for row in preference]
		return positiveFlow
		
				
	def negativeFlow(self,preference):
		negativeFlow=[]
		for i in range(len(preference[0])):
			col=sum([row[i] for row in preference])
			negativeFlow.append(col)
		return negativeFlow
	
		
	def netFlow(self,positiveFlow,negativeFlow):
		netFlow=[(p-n) for p,n in zip(positiveFlow,negativeFlow)]
		return 0

		
		
	def run(self):
		"""process the matrix and get the ranking values for each alternative"""
		pass
	

def main():
	return 0

if __name__ == '__main__':
	main()
