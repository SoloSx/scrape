import os
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

# 保存先のディレクトリ名
dir_name = 'C:\\Users\\'
os.makedirs(dir_name, exist_ok=True)

# 検索結果のURL
url = ''

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
