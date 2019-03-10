#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mpl_squares.py
#  
#  Copyright 2018 Administrator <Administrator@USER-20160131CH>
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
import matplotlib.pyplot as plt
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth=0.5)
#plt.plot(squares)
#plt.plot(squares,linewidth=5)
#设置图表标题
plt.title("squares Numbers" ,fontsize=24)
plt.xlabel("Value" , fontsize=14)
plt.ylabel("square of value" , fontsize=14)
#设置刻度
plt.tick_params(axis='both', labelsize=14)
plt.show()
