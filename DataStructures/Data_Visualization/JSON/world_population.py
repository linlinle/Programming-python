# -*- coding: utf-8 -*-
import json

from pygal.style import RotateStyle, LightColorizedStyle
from pygal_maps_world.maps import World

from DataStructures.Data_Visualization.JSON.country_codes import get_country_code

# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)     # 一个列表

# 创建一个包含人口数量的字典
cc_populations = {}
for pop_dict in pop_data:   # 遍历每个字典
    if pop_dict['Year'] =='2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))  #float将字符串转换为小数
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# 根据人口数量将所有的国家分成三组
cc_pops1,cc_pops2,cc_pops3 = {},{},{}
for cc,pop in cc_populations.items():
    if pop < 10000000:
        cc_pops1[cc] = pop
    elif pop < 1000000000:
        cc_pops2[cc] = pop
    else:
        cc_pops3[cc] = pop


wm_style = RotateStyle('#336699',base_style=LightColorizedStyle)
wm = World(style = wm_style)
wm.title='World Population in 2010, by Country'
wm.add('0-10m', cc_pops1)
wm.add('10m-1bn', cc_pops2)
wm.add('>1bn', cc_pops3)

wm.render_to_file('world_population.svg')
