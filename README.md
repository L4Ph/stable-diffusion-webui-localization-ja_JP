# SD web UI 日本語化プロジェクト

## これはなに
日本語訳用の言語ファイルです。 [AUTOMATIC1111版Stable Diffusion web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)で使用します。


## 翻訳がおかしい/翻訳を手伝う📘
### [Crowdin](https://crowdin.com/project/stable-diffusion-webui-localization-ja_JP/invite?h=cb87e52376d1e1f2ba920b1a8bcccebe1650449)から翻訳ができます!  
Crowdinの使い方に関して、[sp8999](https://twitter.com/sp8999)さんがまとめてくださいました!  
[コチラの記事](https://sp8999.com/stable-diffusion/2023/03/20/870/)からどうぞ!

翻訳のソースは[stable-diffusion-webui-localization-source](https://github.com/harukaxxxx/stable-diffusion-webui-localization-source)からお借りしています  

また、ご自身で翻訳を始めたいという方へ向けて[テンプレート](https://github.com/Katsuyuki-Karasawa/stable-diffusion-webui-localization-template)を公開しています!

## 2ヶ国語同時表示対応について
以下のように2ヶ国語同時表示を可能にする[Bilingual Localization](https://github.com/journey-ad/sd-webui-bilingual-localization)拡張機能との併用を推奨します。    
**バイリンガル対応の拡張機能を標準で組み込んでおり、有効化すればすぐに使えます!** ([9d2551d](https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/9d2551d593a683d3bd3344cf708df85648210e1c)以降)  
詳しくは[Bilingual-Localizationの利用方法](#Bilingual-Localizationの利用方法)をご覧ください  
![Snipaste_2023-02-28_00-23-45](https://user-images.githubusercontent.com/16256221/221622328-a4e46b1c-f202-4a41-9a56-3df96c823f42.png)
### バイリンガル拡張機能が動作しない!
webuiの[9d2551d](https://github.com/AUTOMATIC1111/stable-diffusion-webui/commit/9d2551d593a683d3bd3344cf708df85648210e1c)のコミットから`git submodule`がサポートされました。  
これにより、古いバージョンでのバイリンガル拡張機能の組み込みは機能しません。  
継続してご利用されたい方は、webui側のアップデートを行う、もしくはご自身で[Bilingual Localization](https://github.com/journey-ad/sd-webui-bilingual-localization)のインストールを行ってください。

# Getting Started
## インストール
1. <kbd>Extensions</kbd>タブをクリックし、<kbd>Available</kbd>をクリックします。
2. `Extension index URL`が以下のURLであることを確認したら<kbd>Load From:</kbd>をクリックします。
![](./images/official-extensions-list1.avif)
```
https://raw.githubusercontent.com/AUTOMATIC1111/stable-diffusion-webui-extensions/master/index.json
```
or
```
https://raw.githubusercontent.com/Katsuyuki-Karasawa/sd.webui-Extension-ja_JP/main/index.json
```

3. 読込まれたことが確認できたら、`Hide extensions with tags`を<kbd>localization</kbd>**以外**にチェックマークを付けます。(<kbd>localization</kbd>にはつけません)
4. 各言語が出てきますので、`ja_JP Localization`の項目の<kbd>Install</kbd>をクリックします。
![](./images/official-extensions-list2.avif)
5. `Installed into...`と表示されたら、[利用方法](#利用方法)へ移動してください。

<details>
<summary>その他のインストール方法</summary>

## 拡張機能のリポジトリのURLからインストール
1. <kbd>Extensions</kbd>タブをクリックし、`URL for extension's git repository`のテキストボックスに以下のURLをペーストします。
```
https://github.com/Katsuyuki-Karasawa/stable-diffusion-webui-localization-ja_JP
```
2. <kbd>Install</kbd>をクリックします。
3. `Installed into...`と表示されたら、[利用方法](#利用方法)へ移動してください。
![](./images/install-from-url.avif)


## 手動でインストール
1. [zipファイル](https://github.com/Katsuyuki-Karasawa/stable-diffusion-webui-localization-ja_JP/archive/refs/heads/main.zip)をダウンロードします。
2. ダウンロードしたzipを`stable-diffusion-webui`以下の`extensions`に移動させます。
![](./images/local-install-dir.avif)
3. zipファイルを右クリックして、**すべて展開**します。
4. 展開されたことが確認できたら、[利用方法](#利用方法)へ移動してください。

## 日本語化ファイルを直接読み込む(非推奨)
**この手順はWeb UIからのアップデートができません。**  
**また、この手順はアップデートにて廃止される可能性があるためご注意ください。**  
1. [jsonファイル](https://raw.githubusercontent.com/Katsuyuki-Karasawa/stable-diffusion-webui-localization-ja_JP/main/localizations/ja_JP.json)にアクセスする。
2. 右クリックから`名前を付けて保存...`、もしくは`Ctrl+S`で保存します。  
![](./images/save-json.avif)
3. 保存先は`stable-diffusion-webui`以下の`localizations`です。  
![](./images/local-json-dir.avif)
4. 保存されたことを確認したら、[利用方法](#利用方法)へ移動してください。  
</details>

## 利用方法
### 日本語化ファイルを読み込む
1. <kbd>Settings</kbd>タブへ移動します。
2. <kbd>Settings</kbd>タブから`Localization (requires restart)`の項目を探します。
![](./images/localozation-section.avif)
3. ドロップダウンリストから`ja-JP`を選択します。(もし、出てこない場合は右側の🔄から再読込してください。)

### Bilingual-Localizationの利用方法
- <kbd>Settings</kbd> - <kbd>Bilingual Localization</kbd>パネルから、`ja_JP`を選択
![Snipaste_2023-02-28_00-04-21](https://user-images.githubusercontent.com/16256221/221625729-73519629-8c1f-4eb5-99db-a1d3f4b58a87.png)

> **⚠️注意⚠️**  
<kbd>Settings</kbd> - <kbd>User interface</kbd> - <kbd>Localization</kbd>が`None`に設定されていることを確認してください。

### 設定を適用する
1. ページ上部のオレンジ色のボタン(<kbd>Apply settings</kbd>)をクリックして設定を保存します。
![](https://user-images.githubusercontent.com/60730393/202901412-26765c04-e69c-4beb-a56b-9e310ed273ca.png)
2. ページ下部のオレンジ色のボタン(<kbd>Restart Gradio and Refresh components</kbd>)をクリックして、web UIを再起動します。
![](https://user-images.githubusercontent.com/60730393/202901401-de7d34e9-67c6-4f39-8f5f-b0c0c7a58b54.png)

## ディレクトリ構造 
```
📦 main branch
├─ .github
│  └─ workflows
│     ├─ Merge.yaml
│     ├─ translation_progress.yaml
│     └─ update-source.yaml
├─ .gitignore
├─ LICENSE
├─ README.md
├─ crowdin.yml
├─ images
├─ javascript
│  └─ bilingual_localization.js
├─ localizations
│  └─ ja_JP.json - 実際にWebUIで使用する言語ファイル
├─ scripts
│  └─ bilingual_localization_helper.py
├─ template
│  ├─ ja_JP - 翻訳の後のソースになる部分 マージすると/localizaions/ja_JP.jsonになる
│  │  ├─ ExtensionList.json
│  │  ├─ StableDiffusion.json
│  │  └─ extensions
│  │     └─ extension.json
│  └─ source - 翻訳前のソースとなる部分
│     ├─ ExtensionList.json
│     ├─ StableDiffusion.json
│     └─ extensions
│        └─ extension.json
└─ tools - いろいろなツール群
```
 - `/localizations/ja_JP.json`  
 実際にWebUIで使用される言語ファイル
 `Merge.yaml`を手動実行し、マージする  

 - `/template/source/`以下
 `update_source.yaml`で[翻訳ソース](https://github.com/harukaxxxx/stable-diffusion-webui-localization-source)から取得してきたファイル  
 こちらには基本変更を加えません  

 - `/template/ja_JP/`  
 Crowdinなどで翻訳後に出力されるファイル  
 **もし直接翻訳のPRを出す場合はこちらになります**

## Special Thanks!✨
<a href=https://github.com/yuuki76/webui-localization-ja_JP><img src="https://github.com/yuuki76.png" alt="yuuki76" style="display: inline-block; width: 100px; height: 100px;">
<a href=https://github.com/harukaxxxx/stable-diffusion-webui-localization-source><img src="https://github.com/harukaxxxx.png" alt="harukaxxxx" style="display: inline-block; width: 100px; height: 100px;">
<a href=https://github.com/journey-ad/sd-webui-bilingual-localization><img src="https://github.com/journey-ad.png" alt="journey-ad" style="display: inline-block; width: 100px; height: 100px;">
<a href=https://sp8999.com/stable-diffusion/2023/03/20/870/><img src="https://pbs.twimg.com/profile_images/1611351286477377538/86YeQooS.jpg" alt="sp8999" style="display: inline-block; width: 100px; height: 100px;">
