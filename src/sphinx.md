# Sphinx でドキュメントを作成する

```{contents}
:local:
:depth: 2
```

:::{admonition} **関連トピック**

- test
- test2
  :::

## Sphinx とは？

- Python のドキュメント作成ライブラリで，HTML や PDF などの形式でドキュメントを作成できる．
- デフォルトでは reStructuredText という形式のドキュメントを作成するが，拡張機能を使用することで，
  Markdown 形式のファイルでドキュメントを作成できる．

```{mermaid}
flowchart LR

markdown[Markdown]
rst[reStructuredText]
sphinx[Sphinx]

html[HTML]
pdf[PDF]

rst --> sphinx
markdown --> sphinx

sphinx -->|make html| html
sphinx -->|make latexpdf| pdf
```

## セットアップ

### プロジェクトフォルダの作成

任意の場所にフォルダを作成する．

### Python 仮想環境の作成

ターミナルなどで次のコマンドを実行して Sphinx ドキュメント作成用の Python 仮想環境を作成する．

```sh
python -m venv .venv
```

### 仮想環境の有効化

作成した Python 仮想環境を有効化するため，プロジェクトフォルダ内で次のコマンドを実行する．

:::::{tab-set}

::::{tab-item} Windows

```ps1
.\.venv\Scripts\Acticate.ps1
```

::::

:::{tab-item} MacOS or Linux

```sh
./.venv/bin/activate
```

:::::

### ライブラリのインストール

次のコマンドを実行して Sphinx ドキュメントの作成に必要なライブラリをインストールする．

```sh
pip install Sphinx sphinx myst-parser sphinxcontrib-marmaid sphinx-copybutton sphinx-design
```

:::{note}

| ライブラリ            | 機能概要                                   |
| --------------------- | ------------------------------------------ |
| Sphinx                | Sphinx 本体のライブラリ                    |
| myst-parser           | Markdown を使用できるようにする            |
| sphinxcontrib-mermaid | Mermaid.js を使用できるようにする          |
| sphinx-copybutton     | コードブロックなどにコピーボタンを追加する |
| sphinx-design         | タブブロックなどを作成できるようにする     |

:::

## ドキュメントの作成手順

### プロジェクトの初期化

プロジェクトフォルダ直下で`sphinx-quickstart`コマンドを実行する．
`sphinx-quickstart`コマンドは引数としてフォルダ名を指定できる．
引数無しの場合はカレントフォルダに，引数をつけた場合は指定したフォルダに
初期ファイルを生成する．
実行後に対話的に初期化が開始されるがプロジェクト名と製作者を除いてデフォルト値でよい (あとで設定ファイルを編集して変更できる)．

```text
You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]:

The project name will occur in several places in the built documentation.
> Project name: Your project name
> Author name(s): Your name
> Project release []:

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Project language [en]:
```

コマンドの実行後に以下のようなファイル・フォルダが生成される．

```diff
YOUR_PROJECT
+ |- _build
+ |- _static
+ |- _templates
+ |- Makefile
+ |- conf.py
+ |- index.rst
+ `- make.bat
```

### 設定ファイルの編集

初期化によって生成された`conf.py`をテキストエディタで開いて，設定を書き換える．
まずはじめに myst-parser をはじめとする拡張機能を有効化するために`extensions`を次の通りに書き換える．

```{code-block} diff
---
caption: conf.py
---

- extensions = []
+ extensions = [
+     "myst_parser",
+     "sphinx.ext.napoleon",
+     "sphinx.ext.imgmath",
+     "sphinx.ext.ifconfig",
+     "sphinx.ext.imgconverter",
+     "sphinxcontrib.mermaid",
+     "sphinx_copybutton",
+     "sphinx_design",
+ ]

```

次に myst-parser の拡張機能オプション`myst_enable_extensions`を追加する．

```{code-block} diff
---
caption: conf.py
---
+ myst_enable_extensions = [
+     "amsmath",
+     "colon_fence",
+     "deflist",
+     "dollarmath",
+     "fieldlist",
+     "html_admonition",
+     "html_image",
+     "linkify",
+     "replacements",
+     "smartquotes",
+     "strikethrough",
+     "substitution",
+     "tasklist",
+ ]
```

### Makefile の編集

ここでは`sphinx-autobuild`による自動ビルドプログラムの呼び出しを簡便化するために Makefile を修正する．

::::{tab-set}

:::{tab-item} Windows

Windows システムで`make`がインストールされていない環境では，
Sphinx ドキュメントのビルドにはプロジェクト初期化時に作成された
`make.bat`を使用する．そのため`sphinx-autobuild`に関する設定も
`make.bat`に以下のように追加する．

```{code-block} diff
---
caption: make.bat
---
  %SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
  goto end

+ :livehtml
+ sphinx-autobuild %SOURCEDIR% %BUILDDIR%\html
+ goto end
```

:::

:::{tab-item} Windows (with Make) or MacOS or Linux

`make`がインストールされた Windows または MacOS や Linux では
Sphinx ドキュメントのビルドに`Makefile`を使用する．
そのため`sphinx-autobuild`に関する設定を
`Makefile`に以下のように追加する．

```{code-block} diff
---
caption: Makefile
---


  .PHONY: help Makefile

+ livehtml:
+   sphinx-autobuild $(SOURCEDIR) $(BUILDDIR)/html
```

```{warning}
`sphinx-autobuild`の前の空白はタブ空白であることに注意．
```

:::

::::

### インデックスページの作成

プロジェクトの初期化時に`index.rst`ファイルが生成されているが，
これを削除して，代わりに以下の内容の`index.md`を作成する．

```{code-block} markdown

# Document Title

:::{toctree}
---
maxdepth: 2
caption: Contents
---
:::
```

ここで，`Document Title`は作成するドキュメントのトップページに表示されるタイトルであり，任意に設定できる．

`{toctree}`ブロックはファイルのリンク構成を記述するブロックである．
詳細については後の\*\*\*で説明する．

### ドキュメントページの追加

プロジェクトフォルダ内の任意の場所に Markdown ファイルを作成する．
ここでは`src/page1.md`を作成したものとして以降の説明を記載する．

次に`index.md`の`toctree`ブロックにドキュメントページファイルの
パスを`index.md`からの相対パスとして追加する．

```{code-block} diff
---
caption: index.md
---

  :::{toctree}
  ---
  maxdepth: 2
  caption: Contents
  ---
+
+ src/page1.md
  :::
```

これによって`index.md`の次のページとして`src/page1.md`が定義される．

toctree ブロックには複数のファイルを記述することが可能である．
例えば以下のように記述できる．

```{code-block} markdown

:::{toctree}
---
maxdepth: 2
caption: Contents
---

src/sample.md
src/sample2.md
src/sample3.md
:::
```

上記の例の場合だと，`index.md`→`src/page1.md`
→`src/page2.md`→`src/page3.md`の順番でページがリンクされる．

toctree は`index.md`以外のドキュメントページにも記述可能である．
例えば`page1.md`に以下のように記述した場合を考える．

```{code-block} markdown
# Page 1

:::{toctree}
---
maxdepth: 2
caption: Contents
---

src/subpage1-1.md
src/subpage1-2.md
:::
```

上記の例の場合だと，`index.md`→`src/page1.md`
→`src/subpage1-1.md`→`src/subpage1-2.md`
→`src/page2.md`→`src/page3.md`の順番でページがリンクされる．

このように Sphinx ドキュメントでは，各ドキュメントファイルの
リンク構造を toctree によって階層的に定義していく．

### HTMLドキュメントのビルド

各ドキュメントファイルの作成が終わったら，プロジェクトフォルダ直下で
次のコマンドを実行して，HTMLファイルをビルドする．

::::{tab-set}

:::{tab-item} Windows

```ps1
.\make.bat html
```

:::

:::{tab-item} Windows (with make) or MacOS or Linux

```ps1
make html
```

:::

::::

### HTMLドキュメントの自動ビルド

Sphinxドキュメントはドキュメントファイルを更新する度に
ビルドをし直す必要があるが，`sphinx-autobuild`によって
ドキュメントの更新を監視するサーバープログラムを起動して，
ビルド作業を自動化できる．

sphinx-autobuildのサーバープログラムは，以下のコマンドで起動する．

::::{tab-set}

:::{tab-item} Windows

```ps1
.\make.bat livehtml
```

:::

:::{tab-item} Windows (with make) or MacOS or Linux

```sh
make livehtml
```

::::

コマンドの実行後にサーバプログラムが起動して
次のようなメッセージが表示される．

```text
The HTML pages are in _build/html.
[sphinx-autobuild] Serving on http://127.0.0.1:8000
```

メッセージの通りサーバプログラムがローカルPCの8000番ポートを
使用して起動されているので，Webブラウザで`http://127.0.0.1:8000`
もしくは `localhost:8000`にアクセスする．
ページにアクセスするとレンダリングされたHTMLページが表示される．
以降ドキュメントファイルを更新する度に自動的にビルドおよび
再レンダリング処理が実行されてページが更新される．

サーバプログラムを停止させる場合は，コンソール画面で`Ctrl+c`キーを
押す，もしくはコンソール画面を閉じる．
