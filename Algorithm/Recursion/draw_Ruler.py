# -*- coding: utf-8 -*-
'''画尺子  O(2^N)
draw_interval(3)
    draw_interval(2)
        draw_interval(1)
            draw_interval(0)
            draw_line(1)                  -
            draw_interval(0)
        draw_line(2)                      - -
        draw_interval(1)
            draw_interval(0)
            draw_line(1)                  -
            draw_interval(0)
    draw_line(3)                          - - -
    draw_interval(2)
        draw_interval(1)
            draw_interval(0)
            draw_line(1)                 -
            draw_interval(0)
        draw_line(2)                     - -
        draw_interval(1)
            draw_interval(0)
            draw_line(1)                 -
            draw_interval(0)
draw_interval(3)

'''

def draw_line(tick_length,tick_label=''):
    '''根据长度tick_length画出刻度线'''
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    '''在上一个等级区间内，插入一个下一个等级刻度线'''
    if center_length >0:                #当长度下降到0时停止。
        draw_interval(center_length-1)  # recursively draw top ticks
        draw_line(center_length)        # draw center tick
        draw_interval(center_length-1)  # recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
    draw_line(major_length,'0')
    for j in range(1,num_inches+1):
        draw_interval(major_length-1)   #按等级绘制内刻度线
        draw_line(major_length,str(j)) #负责最外围刻度线以及号码；

if __name__ == '__main__':
    draw_ruler(4,3)