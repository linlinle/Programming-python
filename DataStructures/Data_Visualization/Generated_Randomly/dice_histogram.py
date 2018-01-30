# -*- coding: utf-8 -*-
'''一个6面，一个10面骰子'''
import pygal

from DataStructures.Data_Visualization.Generated_Randomly.dice import Dice

die1 = Dice()
die2 = Dice(10)
results = []
for roll_num in range(5000):
    result = die1.roll()+die2.roll()
    results.append(result)
# 分析结果
frequencies = []
max_result = die1.num_sides+die2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = 'Results of rolling one D6 1000 times.'
hist.x_labels =  ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
'13', '14', '15', '16']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6+D10',frequencies)
hist.render_to_file('dice_histogram.svg')