# -*- coding: UTF-8 -*-
import requests
import time
from random import choice

URL = 'https://cdn.jsdelivr.net/gh/LittleJake/blog-static-files@imgs/imgs/'
IMGS = ['20201026111223.png', '20201026130220.png', '20201026130227.png', '20201026130145.png',
        '20201026130233.png', '20201026130159.png', '20201026130212.png']

def get_hitokoto():
    q = requests.get("https://cdn.jsdelivr.net/gh/hitokoto-osc/sentences-bundle@1.0.89/sentences/a.json")
    return choice(q.json())


def generate_readme(hitokoto):
    if 6 <= int(time.strftime("%H")) < 12:
        welcome = 'Good morning work time'
    elif 12 <= int(time.strftime("%H")) < 18:
        welcome = 'Good afternoon work time'
    else:
        welcome = 'Good evening work time'

    with open('README.md', 'w', encoding='utf-8') as fp:
        fp.write("<img alt='{}' src='{}{}' align='right' style='max-width:100%;'>\n\n".format(welcome, URL, choice(IMGS)))
        fp.write("{}!\n\nToday is {}.\n\n".format(welcome, time.strftime("%m/%d/%Y")))
        fp.write("### Hitokoto\n\n> {}\n> \n> ——{}\n\n".format(hitokoto['hitokoto'],hitokoto['from']))
        fp.write("![Jake Liu's GitHub stats](https://github-readme-stats.vercel.app/api?username=LittleJake&show_icons=true)\n\n")
        fp.write("Autogen by LittleJake at {}".format(time.strftime("%H:%M:%S")))
    return


generate_readme(get_hitokoto())

