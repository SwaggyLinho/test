#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  die_visual.py
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
import pygal
from die import Die
die_1 = Die()
die_2 = Die(10)
results =[]
for roll_num in range(50000):
	result = die_1.roll() + die_2.roll()
	results.append(result)
	
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
	
#print(results)
#print(frequencies)
hist = pygal.Bar()
hist.title = "投1000次骰子的结果"
hist.x_labels = []
#for x in range(2,17):
	#hist.x_labels.append(str(x))
hist.x_labels = [str(x) for x in range(2,max_result+1)]
hist.x_title = "结果"
hist.y_title = "次数"
hist.add('',frequencies)
hist.render_to_file('die_visual_10.svg')
