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

class weightedsum:
	def __init__(self):
		pass
		
	def elaborate(self,matrix,preference,criteria):
		"""normalize matrix based on preference of criteria """
		stdMatrix=[]
		for c,p in zip(criteria,preference):
			if p=='g':
				col=normalize.increas(matrix[c])
			elif p=='c':
				col=normalize.decrease(matrix[c])
			elif p=='p':
				col=normalize.regression(matrix[c],Xvalues, Yvalues, polyFittValue)
			else:
				col=None
			stdMatrix.append(col)
		return stdMatrix.transpose()
		
		
	def run(self,stdMatrix,weight):
		"""process the matrix and get the ranking values for each alternative"""
		weigtedMatrix=[[r*w for r,w in zip(row,weigth)] for row in strdMatrix]
		rank=[sum(row) for row in weigtedMatrix]
		return rank
	

def main():
	return 0

if __name__ == '__main__':
	main()
