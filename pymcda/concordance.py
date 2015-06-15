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

class concordance:
	def __init__(self):
		pass
		
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
		
		
	
	def concordanceMatrix(self, matrix,weight):
		concordance=[]
		for row1 in matrix:
			crow=[]
			for row2 in matrix:
				value=0
				for r1,r2,w in zip(row1,row2,weight):
					if r1>r2:
						value=value+w
				crow.append(value)
			concordance.append(crow)
		return concordance

	def discordanceMatrix(self, matrix):
		discordance=[]
		for row1 in matrix:
			drow=[]
			value=0
			for row2 in matrix:
				for r1,r2 in zip(row1,row2):
					if (r1-r2)>value:
						value=(r1-r2)
					else:
						value=value
				drow.append(value)
			discordance.append(drow)
		return discordance
		
	
	def concordanceIndex(self,concordance):
		concIndx=[]
		concordance=np.array(concordance, dtype = 'float32')
		for i in range(len(concordance)):
			row=concordance[i]
			col=concordance[:,i]
			value=sum(row)-sum(col)
			concIndx.append(value)
		return concIndx
		
	def discordanceIndex(self,discordance):
		discIndx=[]
		discordance=np.array(discordance, dtype = 'float32')
		for i in range(len(discordance[0])):
			row=discordance[i]
			col=discordance[:,i]
			value=sum(row)-sum(col)
			discIndx.append(value)
		return discIndx


def main():
	print "concordance mcda model"
	return 0

if __name__ == '__main__':
	main()
