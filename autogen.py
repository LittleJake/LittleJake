# -*- coding: UTF-8 -*-
import requests
import time
from random import shuffle

URL = 'https://cdn.jsdelivr.net/gh/LittleJake/blog-static-files@imgs/imgs/'
IMGS = ['20201026111223.png', '20201026130220.png', '20201026130227.png', '20201026130145.png',
        '20201026130233.png', '20201026130159.png', '20201026130212.png']

def get_hitokoto():
    q = requests.get("https://international.v1.hitokoto.cn/?c=a")
    return q.json()


def generate_readme(hitokoto):
    if 6 <= int(time.strftime("%H")) < 12:
        welcome = 'Good morning work time'
    elif 12 <= int(time.strftime("%H")) < 18:
        welcome = 'Good afternoon work time'
    else:
        welcome = 'Good evening work time'

    with open('README.md', 'w', encoding='utf-8') as fp:
        fp.write("{}!\n\nToday is {}.\n\n".format(welcome, time.strftime("%m/%d/%Y")))
        fp.write("### Hitokoto\n\n> {}\n> \n> ——{}\n\n".format(hitokoto['hitokoto'],hitokoto['from']))
        shuffle(IMGS)
        fp.write("![{}]({}{})\n\n".format(welcome, URL, IMGS.pop()))
        fp.write("Autogen by LittleJake.")

    return


generate_readme(get_hitokoto())

