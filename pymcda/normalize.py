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


class normalize:
	def __init__(self,criterion):
		self.miN=[min(r) for r in matrix] #min values vector
		self.maX=[max(r) for r in matrix] ##man values vector
		
	def increase(self,criterion):
		"""normalize all values in a list with linear increas/gain function"""
		miN=min(criterion)
		maX=max(criterion)
		normCritrion=[float((x-miN)/(maX-miN)) for x in criterion]
		return normCritrion
		
	def decrease(self,criterion):
		"""normalize all values in a list with linear decreas/cost function"""
		miN=min(criterion)
		maX=max(criterion)
		normCritrion=[float((maX-x)/(maX-miN)) for x in criterion]
		return normCritrion
		
	def regression(self,criterion,Xvalues, Yvalues, polyFittValue):
		fit=np.polyfit(Xvalues, Yvalues, polyFittValue)
		valuer = np.poly1d(fit)
		normCritrion=[valuer(x) for x in criterion]
		return normCritrion
		
