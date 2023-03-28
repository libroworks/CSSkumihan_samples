from pathlib import Path
from bs4 import BeautifulSoup

result = '<nav id="toc" role="doc-toc">'

# カレントフォルダ内の「chapで始まり.htmlで終わる」ファイルを列挙
current = Path()
for target in current.glob('chap*.html'):
    # print(target)
    soup = BeautifulSoup(
        target.read_text(encoding="utf-8"), 'html.parser')
    targetpath = str(target).replace('\\', '/')
    # h1～h3要素を取得
    elems = soup.find_all(['h1', 'h2', 'h3'])
    for elem in elems:
        id = elem['id']
        if elem.name == 'h1':
            result += f'- <a class="toc-chapter" href="{targetpath}#{id}">'
            result += elem.get_text().strip() + '</a>\n'
        if elem.name == 'h2':
            result += (' ' * 2)
            result += f'- <a class="toc-section" href="{targetpath}#{id}">'
            result += elem.get_text().strip() + '</a>\n'
        if elem.name == 'h3':
            result += (' ' * 4)
            result += f'- <a class="toc-subsection" href="{targetpath}#{id}">'
            result += elem.get_text().strip() + '</a>\n'

# 書き出し
print(result)
outpath = Path('tocoutput.md')
outpath.write_text(result, encoding='utf-8')
