# Sphinxでドキュメントを作成する

## Sphinxとは？

- Pythonのドキュメント作成ライブラリで，HTMLやPDFなどの形式でドキュメントを作成できる．
- デフォルトではreStructuredTextという形式のドキュメントを作成するが，拡張機能を使用することで，
  Markdown形式のファイルでドキュメントを作成できる．

```{mermaid}
flowchart LR

markdown[Markdown]
rst[reStructuredText]
sphinx[Sphinx]

html[HTML]
pdf[PDF]

rst --> Sphinx
markdown --> Sphinx

sphinx --> html
sphinx --> pdf
```
