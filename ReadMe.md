# このソフトウェアについて

Pythonで国際化してみた。

`Hello World!!`を`こんにちは世界！`へ置き換えた。

# 参考

* http://d.hatena.ne.jp/fgshun/20100319/1269004530

# 実行

```sh
$ python main.py
こんにちは世界！
```

# 手順

1. コードを書く
1. 以下のファイルを入手する
    * [pygettext.py](https://github.com/python/cpython/blob/6f0eb93183519024cb360162bdd81b9faec97ba6/Tools/i18n/pygettext.py)
    * [msgfmt.py](https://github.com/python/cpython/blob/6f0eb93183519024cb360162bdd81b9faec97ba6/Tools/i18n/msgfmt.py)
1. `$ python pygettext.py main.py`で`messages.pot`ファイルが出力される
1. `messages.pot`ファイルをコピーして`hello.po`にリネームする
1. `hello.po`の項目を任意に埋める（`msgstr ""`を`msgstr "こんにちは世界！"`とする等）
1. `$ python msgfmt.py hello.po`で`hello.mo`ファイルが出力される
1. `./ja/LC_MESSAGES/hello.mo`に配置する
1. `$ python main.py`を実行して`Hello World !!`でなく`こんにちは世界！`と表示されたら成功

main.py
```python
import gettext
import os
_ = gettext.translation(
        domain='hello',
        localedir=os.path.join(os.path.dirname(__file__)),
        fallback=True).gettext

print(_('Hello World !!'))
```
```sh
$ python main.py
こんにちは世界！
```

* domain: `hello.mo`ファイルと同じ名前にする(拡張子をとる)
* localedir: `(ここで指定したディレクトリ)/ja/LC_MESSAGES/hello.mo`
* fallback: moファイルが見つからない場合そのまま実行する
* `_(...)`で囲った文字列が翻訳対象となる

poファイルのヘッダ部分は[こちら](http://www.gnu.org/software/gettext/manual/gettext.html#Header-Entry)を参照。

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [pyenv](https://github.com/pylangstudy/201705/blob/master/27/Python%E5%AD%A6%E7%BF%92%E7%92%B0%E5%A2%83%E3%82%92%E7%94%A8%E6%84%8F%E3%81%99%E3%82%8B.md) 1.0.10
    * Python 3.6.1
* [pygettext.py](https://github.com/python/cpython/blob/6f0eb93183519024cb360162bdd81b9faec97ba6/Tools/i18n/pygettext.py)
* [msgfmt.py](https://github.com/python/cpython/blob/6f0eb93183519024cb360162bdd81b9faec97ba6/Tools/i18n/msgfmt.py)

# ライセンス

* https://sites.google.com/site/michinobumaeda/programming/pythonconst

Library|License|Copyright
-------|-------|---------
http://code.activestate.com/recipes/65207/|[PSF](https://ja.osdn.net/projects/opensource/wiki/licenses%2FPython_Software_Foundation_License)|Copyright (c) 2001 Python Software Foundation; All Rights Reserved
