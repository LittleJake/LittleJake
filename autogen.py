# -*- coding: UTF-8 -*-
import requests
import time
from random import choice

URL = 'https://cdn.jsdelivr.net/gh/LittleJake/blog-static-files@imgs/imgs/'
IMGS = ['20201026111223.png', '20201026130220.png', '20201026130227.png', '20201026130145.png',
        '20201026130233.png', '20201026130159.png', '20201026130212.png']

def get_hitokoto():
    q = requests.get("https://cdn.jsdelivr.net/gh/hitokoto-osc/sentences-bundle/sentences/a.json")
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
        fp.write("<details>\n\n")
        fp.write("<summary><h3>Stat</h3></summary>\n\n")
        fp.write("![Jake Liu's GitHub stats](https://github-readme-stats.vercel.app/api?username=LittleJake&show_icons=true)\n\n")
        fp.write("![Most Used Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=LittleJake&layout=compact)\n\n")
        fp.write("[![Jake Liu's wakatime stats](https://github-readme-stats.vercel.app/api/wakatime?username=LittleJake&layout=compact)](https://wakatime.com/@LittleJake)\n\n")
        fp.write("</details>\n\n")
        fp.write("<details>\n\n")
        fp.write("<summary><h3>Donate</h3></summary>\n\n")
        fp.write("<a href='https://www.buymeacoffee.com/littlejake'><img alt='buymeacoffee' src='https://cdn.jsdelivr.net/gh/simple-icons/simple-icons@develop/icons/buymeacoffee.svg' width='50'></a>\n\n")
        fp.write("<a href='https://afdian.net/@LittleJake'>Aifadian</a>\n\n")
        fp.write("</details>\n\n")
        fp.write("Autogen by LittleJake at {}".format(time.strftime("%H:%M:%S")))
    return


generate_readme(get_hitokoto())

