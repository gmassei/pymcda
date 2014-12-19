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
#  
import numpy as np

def inputFromTXT(path):
	"""load assesment matrix, with alternatives name in the col 1 and
	critera names in row 1"""
	matrix = np.genfromtxt(path, dtype=None, delimiter=';', names=True)
	return matrix

def listCriteria(matrix):
	"""return criteria names"""
	criteria=list(matrix.dtype.names)
	return criteria
	
def listAlternatives(matrix):
	"""return alternative names"""
	alternatives=[row[0] for row in matrix]
	return alternatives
	
def matrix2values(matrix):
	"""return tha values of assesment matrix"""
	values=[list(row)[1:] for row in matrix]
	return values
	
