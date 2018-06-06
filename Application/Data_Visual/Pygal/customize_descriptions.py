# -*- coding: utf-8 -*-
'''添加自定义工具提示：  在Pygal中，将鼠标指向条形将显示它表示的信息，称为工具提示
'''

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [{'value': 16101, 'label': 'Description of httpie.'},
              {'value': 15028, 'label': 'Description of django.'},
              {'value': 14798, 'label': 'Description of flask.'},
              ]

chart.add('',plot_dicts)
chart.render_to_file('bar_descriptions.svg')