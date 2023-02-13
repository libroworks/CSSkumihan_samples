from pathlib import Path
output = '''---
link:
  - rel: 'stylesheet'
    href: 'css/colorchart.css'

---

'''

color = '0123456789ABCDEF'
for g1 in color:
    if (int(f'{g1}', base=16) <= 4):
        output += f'<div class="color-box" style="color:#fff; background:#{g1}{g1}{g1};">#{g1}{g1}{g1}</div>\n'
    else:
        output += f'<div class="color-box" style="background:#{g1}{g1}{g1};">#{g1}{g1}{g1}</div>\n'


for c1 in color:
    for c2 in color:
        for c3 in color:
            if (int(f'{c1}', base=16) <= 5 and int(f'{c2}', base=16) <= 5 and int(f'{c3}', base=16) <= 15):
                output += f'<div class="color-box" style="color:#fff; background:#{c1}{c2}{c3};">#{c1}{c2}{c3}</div>'
            else:
                output += f'<div class="color-box" style="background:#{c1}{c2}{c3};">#{c1}{c2}{c3}</div>'
            output += '\n'
        output += '\n'

targetpath = Path('sample_colorchart.md')
targetpath.write_text(output)
