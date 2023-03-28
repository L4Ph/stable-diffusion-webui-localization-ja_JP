# SD web UI 日本語化プロジェクト

## これはなに
日本語訳用の言語ファイルです。 [AUTOMATIC1111版Stable Diffusion web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)で使用します。

## 2ヶ国語同時表示対応について
以下のように2ヶ国語同時表示を可能にする[Bilingual Localization](https://github.com/journey-ad/sd-webui-bilingual-localization/blob/main/README_JA.md)拡張機能との併用を推奨します。    
**バイリンガル対応の拡張機能を標準で組み込んでおり、有効化すればすぐに使えます!**  
詳しくは[Bilingual-Localizationの利用方法](#Bilingual-Localizationの利用方法)をご覧ください
![Snipaste_2023-02-28_00-23-45](https://user-images.githubusercontent.com/16256221/221622328-a4e46b1c-f202-4a41-9a56-3df96c823f42.png)

## 翻訳がおかしい/翻訳を手伝う📘
### [Crowdin](https://crowdin.com/project/stable-diffusion-webui-localization-ja_JP/invite?h=cb87e52376d1e1f2ba920b1a8bcccebe1650449)から翻訳ができます!  
Crowdinの使い方に関して、[sp8999](https://twitter.com/sp8999)さんがまとめてくださいました!  
[コチラの記事](https://sp8999.com/stable-diffusion/2023/03/20/870/)からどうぞ!

翻訳のソースは[stable-diffusion-webui-localization-source](https://github.com/harukaxxxx/stable-diffusion-webui-localization-source)からお借りしています  

また、ご自身で翻訳を始めたいという方へ向けて[テンプレート](https://github.com/Katsuyuki-Karasawa/stable-diffusion-webui-localization-template)を公開しています!

# Getting Started
## インストール
1. <kbd>Extensions</kbd>タブをクリックし、<kbd>Available</kbd>をクリックします。
2. `Extension index URL`が以下のURLであることを確認したら<kbd>Load From:</kbd>をクリックします。
![](./images/official-extensions-list1.png)
```
https://raw.githubusercontent.com/wiki/AUTOMATIC1111/stable-diffusion-webui/Extensions-index.md
```
or
```
https://raw.githubusercontent.com/Katsuyuki-Karasawa/sd.webui-Extension-ja_JP/main/index.json
```

3. 読込まれたことが確認できたら、`Hide extensions with tags`を<kbd>localization</kbd>**以外**にチェックマークを付けます。(<kbd>localization</kbd>にはつけません)
4. 各言語が出てきますので、`ja_JP Localization`の項目の<kbd>Install</kbd>をクリックします。
![](./images/official-extensions-list2.png)
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
![](./images/install-from-url.png)


## 手動でインストール
1. [zipファイル](https://github.com/Katsuyuki-Karasawa/stable-diffusion-webui-localization-ja_JP/archive/refs/heads/main.zip)をダウンロードします。
2. ダウンロードしたzipを`stable-diffusion-webui`以下の`extensions`に移動させます。
![](./images/local-install-dir.png)
3. zipファイルを右クリックして、**すべて展開**します。
4. 展開されたことが確認できたら、[利用方法](#利用方法)へ移動してください。

## 日本語化ファイルを直接読み込む(非推奨)
**この手順はWeb UIからのアップデートができません。**  
**また、この手順はアップデートにて廃止される可能性があるためご注意ください。**  
1. [jsonファイル](https://raw.githubusercontent.com/Katsuyuki-Karasawa/stable-diffusion-webui-localization-ja_JP/main/localizations/ja_JP.json)にアクセスする。
2. 右クリックから`名前を付けて保存...`、もしくは`Ctrl+S`で保存します。  
![](./images/save-json.png)
3. 保存先は`stable-diffusion-webui`以下の`localizations`です。  
![](./images/local-json-dir.png)
4. 保存されたことを確認したら、[利用方法](#利用方法)へ移動してください。  
</details>

## 利用方法
### 日本語化ファイルを読み込む
1. <kbd>Settings</kbd>タブへ移動します。
2. <kbd>Settings</kbd>タブから`Localization (requires restart)`の項目を探します。
![](./images/localozation-section.png)
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
 - `/localizations/ja_JP.json` - 実際にWebUIで使用される言語ファイル `Merge.yaml`を手動実行し、マージする  
 - `/template/source/`以下 - `update_source.yaml`で[翻訳ソース](https://github.com/harukaxxxx/stable-diffusion-webui-localization-source)から取得してきたファイル こちらには基本変更を加えません  
 - `/template/ja_JP/`以下 - Crowdinなどで翻訳後に出力されるファイル **もし直接翻訳のPRを出す場合はこちらになります**

## ローカライズの進捗

<details>
<summary>WebUI</summary>

- [x] ![ExtensionList translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [ExtensionList](https://raw.githubusercontent.com/wiki/AUTOMATIC1111/stable-diffusion-webui/Extensions-index.md)
- [x] ![StableDiffusion translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [StableDiffusion](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
</details>

<details>
<summary>拡張機能</summary>

- [x] ![DreamArtist-sd-webui-extension translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [DreamArtist-sd-webui-extension](https://github.com/7eu7d7/DreamArtist-sd-webui-extension)
- [x] ![Hypernetwork-Monkeypatch-Extension translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Hypernetwork-Monkeypatch-Extension](https://github.com/aria1th/Hypernetwork-MonkeyPatch-Extension)
- [x] ![SD-latent-mirroring translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [SD-latent-mirroring](https://github.com/dfaker/SD-latent-mirroring)
- [x] ![a1111-sd-webui-haku-img translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [a1111-sd-webui-haku-img](https://github.com/KohakuBlueleaf/a1111-sd-webui-haku-img)
- [x] ![a1111-sd-webui-tagcomplete translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [a1111-sd-webui-tagcomplete](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete)
- [x] ![a1111-stable-diffusion-webui-vram-estimator translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [a1111-stable-diffusion-webui-vram-estimator](https://github.com/space-nuko/a1111-stable-diffusion-webui-vram-estimator)
- [x] ![auto-sd-paint-ext translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [auto-sd-paint-ext](https://github.com/Interpause/auto-sd-paint-ext)
- [x] ![deforum-for-automatic1111-webui translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [deforum-for-automatic1111-webui](https://github.com/deforum-art/deforum-for-automatic1111-webui)
- [x] ![novelai-2-local-prompt translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [novelai-2-local-prompt](https://github.com/animerl/novelai-2-local-prompt)
- [x] ![openOutpaint-webUI-extension translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [openOutpaint-webUI-extension](https://github.com/zero01101/openOutpaint-webUI-extension)
- [x] ![openpose-editor translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [openpose-editor](https://github.com/fkunn1326/openpose-editor)
- [x] ![posex translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [posex](https://github.com/hnmr293/posex)
- [x] ![sd-3dmodel-loader translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd-3dmodel-loader](https://github.com/jtydhr88/sd-3dmodel-loader)
- [ ] ![sd-dynamic-prompts translated 92%](https://geps.dev/progress/92?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd-dynamic-prompts]()
- [x] ![sd-model-preview-xd translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd-model-preview-xd](https://github.com/CurtisDS/sd-model-preview-xd)
- [x] ![sd-webui-additional-networks translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd-webui-additional-networks](https://github.com/kohya-ss/sd-webui-additional-networks)
- [x] ![sd-webui-bilingual-localization translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd-webui-bilingual-localization](https://github.com/journey-ad/sd-webui-bilingual-localization)
- [x] ![sd-webui-controlnet translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd-webui-controlnet](https://github.com/Mikubill/sd-webui-controlnet)
- [x] ![sd-webui-depth-lib translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd-webui-depth-lib](https://github.com/jexom/sd-webui-depth-lib)
- [x] ![sd-webui-llul translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd-webui-llul](https://github.com/hnmr293/sd-webui-llul)
- [x] ![sd-webui-tunnels translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd-webui-tunnels](https://github.com/Bing-su/sd-webui-tunnels)
- [ ] ![sd_dreambooth_extension translated 96%](https://geps.dev/progress/96?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd_dreambooth_extension]()
- [x] ![sd_smartprocess translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd_smartprocess](https://github.com/d8ahazard/sd_smartprocess)
- [x] ![seed_travel translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [seed_travel](https://github.com/yownas/seed_travel)
- [x] ![stable-diffusion-webui-aesthetic-gradients translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-aesthetic-gradients](https://github.com/AUTOMATIC1111/stable-diffusion-webui-aesthetic-gradients)
- [x] ![stable-diffusion-webui-aesthetic-image-scorer translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-aesthetic-image-scorer](https://github.com/tsngo/stable-diffusion-webui-aesthetic-image-scorer)
- [x] ![stable-diffusion-webui-artists-to-study translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-artists-to-study](https://github.com/camenduru/stable-diffusion-webui-artists-to-study)
- [x] ![stable-diffusion-webui-conditioning-highres-fix translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-conditioning-highres-fix](https://github.com/klimaleksus/stable-diffusion-webui-conditioning-highres-fix)
- [x] ![stable-diffusion-webui-daam translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-daam](https://github.com/toriato/stable-diffusion-webui-daam)
- [x] ![stable-diffusion-webui-dataset-tag-editor translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-dataset-tag-editor](https://github.com/toshiaki1729/stable-diffusion-webui-dataset-tag-editor)
- [x] ![stable-diffusion-webui-depthmap-script translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-depthmap-script](https://github.com/thygate/stable-diffusion-webui-depthmap-script)
- [x] ![stable-diffusion-webui-embedding-editor translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-embedding-editor]()
- [x] ![stable-diffusion-webui-images-browser translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-images-browser]()
- [x] ![stable-diffusion-webui-inspiration translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-inspiration](https://github.com/yfszzx/stable-diffusion-webui-inspiration)
- [x] ![stable-diffusion-webui-pixelization translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-pixelization](https://github.com/AUTOMATIC1111/stable-diffusion-webui-pixelization)
- [x] ![stable-diffusion-webui-randomize translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-randomize]()
- [x] ![stable-diffusion-webui-text2prompt translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-text2prompt](https://github.com/toshiaki1729/stable-diffusion-webui-text2prompt)
- [x] ![stable-diffusion-webui-tokenizer translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-tokenizer](https://github.com/AUTOMATIC1111/stable-diffusion-webui-tokenizer)
- [x] ![stable-diffusion-webui-two-shot translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-two-shot](https://github.com/opparco/stable-diffusion-webui-two-shot)
- [x] ![training-picker translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [training-picker](https://github.com/Maurdekye/training-picker)
- [x] ![ultimate-upscale-for-automatic1111 translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [ultimate-upscale-for-automatic1111](https://github.com/Coyote-A/ultimate-upscale-for-automatic1111)
- [x] ![unprompted translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [unprompted](https://github.com/ThereforeGames/unprompted)
- [x] ![multidiffusion-upscaler-for-automatic1111 translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [multidiffusion-upscaler-for-automatic1111](https://github.com/pkuliyi2015/multidiffusion-upscaler-for-automatic1111)
- [x] ![stable-diffusion-webui-rembg translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-rembg](https://github.com/AUTOMATIC1111/stable-diffusion-webui-rembg)
- [x] ![shift-attention translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [shift-attention](https://github.com/yownas/shift-attention)
- [x] ![sd-webui-aspect-ratio-helper translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd-webui-aspect-ratio-helper](https://github.com/thomasasfk/sd-webui-aspect-ratio-helper)
- [x] ![stable-diffusion-webui-state translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-state](https://github.com/ilian6806/stable-diffusion-webui-state)
- [x] ![stable-diffusion-webui-wd14-tagger translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-wd14-tagger]()
- [ ] ![sd-webui-cutoff translated 10%](https://geps.dev/progress/10?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd-webui-cutoff]()
- [x] ![stable-diffusion-webui-auto-translate-language translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-auto-translate-language]()
- [ ] ![stable-diffusion-webui-blip2-captioner translated 37%](https://geps.dev/progress/37?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-blip2-captioner]()
- [ ] ![stable-diffusion-webui-cafe-aesthetic translated 6%](https://geps.dev/progress/6?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-cafe-aesthetic]()
</details>

## Special Thanks!✨
<a href=https://github.com/yuuki76/webui-localization-ja_JP><img src="https://github.com/yuuki76.png" alt="yuuki76" style="display: inline-block; width: 100px; height: 100px;">
<a href=https://github.com/harukaxxxx/stable-diffusion-webui-localization-source><img src="https://github.com/harukaxxxx.png" alt="harukaxxxx" style="display: inline-block; width: 100px; height: 100px;">
<a href=https://github.com/journey-ad/sd-webui-bilingual-localization><img src="https://github.com/journey-ad.png" alt="journey-ad" style="display: inline-block; width: 100px; height: 100px;">
<a href=https://sp8999.com/stable-diffusion/2023/03/20/870/><img src="https://pbs.twimg.com/profile_images/1611351286477377538/86YeQooS.jpg" alt="sp8999" style="display: inline-block; width: 100px; height: 100px;">
