# -*- coding: utf-8 -*-
from Application.Movie_Website import movie

toy_story = movie.Movie('Toy Story',
                        '讲述了主角两个玩具牛仔警长胡迪和太空骑警巴斯光年的故事'.encode('gb2312'),
                        'https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=77119894c9fcc'
                        '3ceb4c0ce35aa7eb1b5/d62a6059252dd42a1835151d023b5bb5c9eab843.jpg',
                        'http://www.le.com/ptv/vplay/26893113.html?ch=baiduald_mfdy')

avatar = movie.Movie('avatar',
                     '该片主要讲述人类穿上阿凡达的躯壳，飞到遥远的星球潘多拉开采资源'.encode('gb2312'),
                     'https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=98f685814e086e066ea838493'
                     '2097b5a/eaf81a4c510fd9f9f7454cd9272dd42a2834a42b.jpg',
                     'http://www.iqiyi.com/v_19rrn8vkts.html?vfm=2008_aldbd&fc=828fb30b722f3164&fv=p_02_01')
movies = [toy_story,avatar]
#website_interface.open_movies_page(movies)
print(movie.Movie.VAILD_RATINGS)
print(movie.Movie.__doc__)