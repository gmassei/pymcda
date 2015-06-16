#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  iomcda.py
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
# 
try: 
	import numpy as np
except ImportError:
	print "numpy missing!"
	

def inputFromTxt(path,idCol=0):
	"""Create records. Load assesment matrix, with alternatives name in 
	the col 1 and critera names in row 1"""
	SI = np.genfromtxt(path, dtype=None, delimiter=';', names=True)
	SI={'alternatives':[row[idCol] for row in SI],'criteria':list(SI.dtype.names),'preference':[],'matrix':[list(row)[1:] for row in SI]}
	return SI

def getMatrix(alternatives,critaria, matrix ):
	SI={'alternatives':alternatives,'critaria':critaria,'matrix':matrix}
	return matrix

def getCriteriaLabels(SI):
	"""return criteria names"""
	lblCriteria=matrix['critaria']
	return lblCriteria
	
def getAlternativesLabels(SI,idCol=0):
	"""return alternative names"""
	lblAlternatives=SI['alternatives']
	return lblAlternatives
	
def matrix2values(SI):
	"""return tha values of assesment matrix"""
	matrix=SI['matrix']
	return matrix
	
def extractColumn(SI,colId):
	"""extract a single column based it's index"""
	column=[row[colId] for row in SI['matrix']]
	return np.array(column)
	
