# coding:utf-8

#英文(画像データ)を日本語へdeeplで変換するファイル

import deepl
from PIL import Image
import pyocr

#画像ファイルを探す時にカレントパスを取得するために必要
import os
# GUI
from tkinter import filedialog

API_KEY = 'xxxx-yyyy-zzzz' # 自身の deepl API キーを指定(deeplへの会員登録が必要です)

#text = 'Riemann Zeta function is a very important function in number theory.'
source_lang = 'EN'
target_lang = 'JA'





cwd = os.getcwd()#カレントディレクトリを取得



typ = [('画像ファイル','*.png'),('画像ファイル','*.jpeg'),('画像ファイル','*.jpg')]#画像アップロード
dir = cwd
fle = filedialog.askopenfilename(filetypes = typ, initialdir = dir)

# print(fle)ファイル名取得



# OCRエンジンを取得
engines = pyocr.get_available_tools()
engine = engines[0]

# 画像の文字を読み込む
text = engine.image_to_string(Image.open(fle), lang="eng")
#print(text) # 画像から英文を読み込みテキストデータにする


# イニシャライズ
translator = deepl.Translator(API_KEY)

# 翻訳を実行
result = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)

# print すると翻訳後の日本語の文章が出力される
print(result)

#翻訳後の日本語の文章がテキストファイルとして出力される

filename=os.path.basename(fle).split('.', 1)[0]#ファイル名
f = open(filename+'_ja.txt', 'w')
f.write(str(result))
f.close()


print("英語から日本語への翻訳が無事完了しました")

#windowsだと文字化けがあるかもしれません

# 参考文献


# deepl api
# https://qiita.com/Negelon/items/ad0e47d15372e0d82ca9

#画像から文字（今回は英文）の取得
#https://qiita.com/eiji-noguchi/items/c19c1e125eaa87c3616b

# GUI
# https://pg-chain.com/python-filedialog

#ファイル名,パスの取得など
# https://note.nkmk.me/python-os-basename-dirname-split-splitext/
# https://python.keicode.com/lang/path-get-current-directory.php
