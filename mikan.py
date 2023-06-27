import os
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

# 保存先のディレクトリ名
dir_name = 'C:\\Users\\prexs\\Desktop\\img_classfied\\とびら'
os.makedirs(dir_name, exist_ok=True)

# 検索結果のURL
url = 'https://www.photo-ac.com/main/search?q=%E3%81%A8%E3%81%B3%E3%82%89&pp=210&qid=&creator=&ngcreator=&nq=&srt=dlrank&orientation=all&sizesec=all&color=all&model_count=-1&age=all&mdlrlrsec=all&prprlrsec=all'

# ページを取得
response = requests.get(url)

# BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(response.text, 'html.parser')

# <figure>タグを取得
figure_tags = soup.find_all('figure', {'class': 'photo-img item'})

# 各<figure>タグに対して処理
for i, figure_tag in enumerate(figure_tags):
    # <img>タグを探す
    img_tag = figure_tag.find('img')
    # 画像URLを取得
    img_url = img_tag.get('src')

    # URLが存在する場合、画像をダウンロード
    if img_url is not None:
        print(f'Downloading image {i+1}...')
        urlretrieve(img_url, os.path.join(dir_name, f'image_{i+1}.jpg'))