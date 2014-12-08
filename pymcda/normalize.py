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
		self.miN=min(criterion)
		self.maX=max(criterion)
		return miN,maX
		
	def increas(self,criterion):
		normCritrion=[((x-self.miN)/(self.maX-self.miN)) for x in criterion]
		return normCritrion
		
	def decrease(self,criterion):
		normCritrion=[((self.maX-x)/(self.maX-self.miN)) for x in criterion]
		return normCritrion
		
	def regression(self,criterion,Xvalues, Yvalues, polyFittValue):
		fit=np.polyfit(Xvalues, Yvalues, polyFittValue)
		valuer = np.poly1d(fit)
		normCritrion=[valuer(x) for x in criterion]
		return normCritrion
		


if __name__ == '__main__':
	main()
