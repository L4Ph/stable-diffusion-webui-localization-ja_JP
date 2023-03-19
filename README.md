# SD web UI 日本語化プロジェクト
[![Crowdin](https://badges.crowdin.net/stable-diffusion-webui-localization-ja_JP/localized.svg)](https://crowdin.com/project/stable-diffusion-webui-localization-ja_JP)

## これはなに
日本語訳用の言語ファイルです。 [AUTOMATIC1111版Stable Diffusion web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui)で使用します。

~~また、2カ国語の同時表示を可能にする[Bilingual Localization](https://github.com/journey-ad/sd-webui-bilingual-localization/blob/main/README_JA.md)拡張機能との併用を推奨します。  
この拡張機能を使えば、日本語環境での利用だけでなく、英語での情報収集も容易になります。~~  
**現在はこの拡張機能を標準で組み込んでいます**
[使い方はコチラ](https://github.com/journey-ad/sd-webui-bilingual-localization/blob/main/README_JA.md)


# Getting Started

### 1. 公式の拡張機能リストからインストール(最も推奨)
1. `Extensions`タブをクリックし、`Available`をクリックします。
2. `Extension index URL`が以下のURLであることを確認したら`Load From:`をクリックします。
![](./images/official-extensions-list1.png)
```
https://raw.githubusercontent.com/wiki/AUTOMATIC1111/stable-diffusion-webui/Extensions-index.md
```
3. 読込まれたことが確認できたら、`Hide extensions with tags`を`localization`**以外**にチェックマークを付けます。(`localization`にはつけません)
4. 各言語が出てきますので、`ja_JP Localization`の項目の`Install`をクリックします。
![](./images/official-extensions-list2.png)
5. `Installed into...`と表示されたら、[利用方法](#利用方法)へ移動してください。


### 2. 拡張機能のリポジトリのURLからインストール(推奨)
1. `Extensions`タブをクリックし、`URL for extension's git repository`のテキストボックスに以下のURLをペーストします。
```
https://github.com/Katsuyuki-Karasawa/stable-diffusion-webui-localization-ja_JP
```
2. `Install`をクリックします。
3. `Installed into...`と表示されたら、[利用方法](#利用方法)へ移動してください。
![](./images/install-from-url.png)


### 3. ローカルでインストール(推奨)
1. [zipファイル](https://github.com/Katsuyuki-Karasawa/stable-diffusion-webui-localization-ja_JP/archive/refs/heads/main.zip)をダウンロードします。
2. ダウンロードしたzipを`stable-diffusion-webui`以下の`extensions`に移動させます。
![](./images/local-install-dir.png)
3. zipファイルを右クリックして、**すべて展開**します。
4. 展開されたことが確認できたら、[利用方法](#利用方法)へ移動してください。

### 4. ローカルでインストール(非推奨)
**この手順はWeb UIからのアップデートができません。**  
**また、この手順はアップデートにて廃止される可能性があるためご注意ください。**
1. [jsonファイル](https://raw.githubusercontent.com/Katsuyuki-Karasawa/stable-diffusion-webui-localization-ja_JP/main/localizations/ja_JP.json)にアクセスする。
2. 右クリックから`名前を付けて保存...`、もしくは`Ctrl+S`で保存します。
![](./images/save-json.png)
3. 保存先は`stable-diffusion-webui`以下の`localizations`です。
![](./images/local-json-dir.png)
4. 保存されたことを確認したら、[利用方法](#利用方法)へ移動してください。


## 利用方法
### 日本語化ファイルを読み込む
1. `Settings`タブへ移動します。
2. `Settings`タブから`Localization (requires restart)`の項目を探します。
![](./images/localozation-section.png)
3. ドロップダウンリストから`ja-JP`を選択します。(もし、出てこない場合は右側の🔄から再読込してください。)

### 設定を適用する
1. ページ上部のオレンジ色のボタン(*Apply settings*)をクリックして設定を保存します。
![](https://user-images.githubusercontent.com/60730393/202901412-26765c04-e69c-4beb-a56b-9e310ed273ca.png)
2. ページ下部のオレンジ色のボタン(*Restart Gradio and Refresh components*)をクリックして、web UIを再起動します。
![](https://user-images.githubusercontent.com/60730393/202901401-de7d34e9-67c6-4f39-8f5f-b0c0c7a58b54.png)

## 翻訳がおかしい/翻訳を手伝う
### [Crowdin](https://crwd.in/stable-diffusion-webui-localization-ja_JP)から翻訳ができます!
気軽に[issue](https://github.com/Katsuyuki-Karasawa/stable-diffusion-webui-localization-ja_JP/issues)を投げましょう!  
分からないことがあれば[Disscussions](https://github.com/Katsuyuki-Karasawa/stable-diffusion-webui-localization-ja_JP/discussions)へどうぞ!  

# Thanks
- [stable-diffusion-webui-localization-source](https://github.com/harukaxxxx/stable-diffusion-webui-localization-source)
    - 翻訳のソース(Translate Sources)

- [sd-webui-bilingual-localization](https://github.com/journey-ad/sd-webui-bilingual-localization)
    - バイリンガル対応拡張機能(bilingual localization extensions)# i18n/l10n Progress

<details>
<summary>i18n/l10nの進捗(WebUI)</summary>

- [ ] ![ExtensionList translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [ExtensionList](https://raw.githubusercontent.com/wiki/AUTOMATIC1111/stable-diffusion-webui/Extensions-index.md)
- [ ] ![StableDiffusion translated 73%](https://geps.dev/progress/73?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [StableDiffusion](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
</details>

<details>
<summary>i18n/l10nの進捗(Extensions)</summary>

- [ ] ![Aesthetic Gradients translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Aesthetic Gradients](https://github.com/AUTOMATIC1111/stable-diffusion-webui-aesthetic-gradients)
- [ ] ![Aesthetic Image Scorer translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Aesthetic Image Scorer]()
- [ ] ![Artists To Study translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Artists To Study]()
- [ ] ![Auto TLS-HTTPS translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Auto TLS-HTTPS]()
- [ ] ![Bilingual Localization translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Bilingual Localization]()
- [ ] ![Booru tag autocompletion translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Booru tag autocompletion](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete)
- [ ] ![DAAM translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [DAAM]()
- [ ] ![Dataset Tag Editor translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Dataset Tag Editor](https://github.com/toshiaki1729/stable-diffusion-webui-dataset-tag-editor)
- [ ] ![Deforum translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Deforum]()
- [ ] ![Depth Maps translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Depth Maps]()
- [ ] ![Depth map library and poser translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Depth map library and poser]()
- [ ] ![Detection Detailer translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Detection Detailer]()
- [ ] ![DreamArtist translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [DreamArtist](https://github.com/7eu7d7/DreamArtist-sd-webui-extension)
- [ ] ![Dreambooth translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Dreambooth]()
- [ ] ![Dynamic Prompts translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Dynamic Prompts]()
- [ ] ![Embeddings editor translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Embeddings editor]()
- [ ] ![Hypernetwork-Monkeypatch-Extension translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Hypernetwork-Monkeypatch-Extension]()
- [ ] ![Image Browser translated 1%](https://geps.dev/progress/1?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Image Browser]()
- [ ] ![Inspiration translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Inspiration]()
- [ ] ![LLUL translated 10%](https://geps.dev/progress/10?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [LLUL](https://github.com/hnmr293/sd-webui-llul)
- [ ] ![Latent Couple translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Latent Couple](https://github.com/opparco/stable-diffusion-webui-two-shot)
- [ ] ![Latent Mirroring translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Latent Mirroring]()
- [ ] ![Model Previews translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Model Previews]()
- [ ] ![OpenPose Editor translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [OpenPose Editor]()
- [ ] ![Pixelization translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Pixelization]()
- [ ] ![Randomize translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Randomize]()
- [ ] ![Smart Process translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Smart Process]()
- [ ] ![Text2Prompt translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Text2Prompt]()
- [ ] ![Tokenizer translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Tokenizer]()
- [ ] ![Ultimate SD Upscale translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Ultimate SD Upscale](https://github.com/Coyote-A/ultimate-upscale-for-automatic1111)
- [ ] ![Unprompted translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Unprompted]()
- [ ] ![VRAM Estimator translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [VRAM Estimator](https://github.com/space-nuko/a1111-stable-diffusion-webui-vram-estimator)
- [ ] ![WD 1.4 Tagger translated 50%](https://geps.dev/progress/50?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [WD 1.4 Tagger]()
- [x] ![Wildcards translated 100%](https://geps.dev/progress/100?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [Wildcards]()
- [ ] ![auto-sd-paint-ext translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [auto-sd-paint-ext](https://github.com/Interpause/auto-sd-paint-ext)
- [ ] ![conditioning-highres-fix translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [conditioning-highres-fix]()
- [ ] ![haku-img translated 94%](https://geps.dev/progress/94?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [haku-img]()
- [ ] ![novelai-2-local-prompt translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [novelai-2-local-prompt](https://github.com/animerl/novelai-2-local-prompt)
- [ ] ![openOutpaint extension translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [openOutpaint extension]()
- [ ] ![posex translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [posex](https://github.com/hnmr293/posex)
- [ ] ![prompt travel translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [prompt travel]()
- [ ] ![sd-webui-controlnet translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd-webui-controlnet](https://github.com/Mikubill/sd-webui-controlnet)
- [ ] ![seed travel translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [seed travel]()
- [ ] ![shift-attention translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [shift-attention](https://github.com/yownas/shift-attention)
- [ ] ![training-picker translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [training-picker](https://github.com/Maurdekye/training-picker)
- [ ] ![DreamArtist-sd-webui-extension translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [DreamArtist-sd-webui-extension](https://github.com/7eu7d7/DreamArtist-sd-webui-extension)
- [ ] ![SD-latent-mirroring translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [SD-latent-mirroring](https://github.com/dfaker/SD-latent-mirroring)
- [ ] ![a1111-sd-webui-haku-img translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [a1111-sd-webui-haku-img](https://github.com/KohakuBlueleaf/a1111-sd-webui-haku-img)
- [ ] ![a1111-sd-webui-tagcomplete translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [a1111-sd-webui-tagcomplete](https://github.com/DominikDoom/a1111-sd-webui-tagcomplete)
- [ ] ![a1111-stable-diffusion-webui-vram-estimator translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [a1111-stable-diffusion-webui-vram-estimator](https://github.com/space-nuko/a1111-stable-diffusion-webui-vram-estimator)
- [ ] ![deforum-for-automatic1111-webui translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [deforum-for-automatic1111-webui](https://github.com/deforum-art/deforum-for-automatic1111-webui)
- [ ] ![openOutpaint-webUI-extension translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [openOutpaint-webUI-extension](https://github.com/zero01101/openOutpaint-webUI-extension)
- [ ] ![openpose-editor translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [openpose-editor](https://github.com/fkunn1326/openpose-editor)
- [ ] ![sd-3dmodel-loader translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd-3dmodel-loader](https://github.com/jtydhr88/sd-3dmodel-loader)
- [ ] ![sd-dynamic-prompts translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd-dynamic-prompts](https://github.com/adieyal/sd-dynamic-prompts)
- [ ] ![sd-model-preview-xd translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd-model-preview-xd](https://github.com/CurtisDS/sd-model-preview-xd)
- [ ] ![sd-webui-additional-networks translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd-webui-additional-networks](https://github.com/kohya-ss/sd-webui-additional-networks)
- [ ] ![sd-webui-bilingual-localization translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd-webui-bilingual-localization](https://github.com/journey-ad/sd-webui-bilingual-localization)
- [ ] ![sd-webui-depth-lib translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd-webui-depth-lib](https://github.com/jexom/sd-webui-depth-lib)
- [ ] ![sd-webui-llul translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd-webui-llul](https://github.com/hnmr293/sd-webui-llul)
- [ ] ![sd-webui-tunnels translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd-webui-tunnels](https://github.com/Bing-su/sd-webui-tunnels)
- [ ] ![sd_dreambooth_extension translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd_dreambooth_extension]()
- [ ] ![sd_smartprocess translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [sd_smartprocess](https://github.com/d8ahazard/sd_smartprocess)
- [ ] ![seed_travel translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [seed_travel](https://github.com/yownas/seed_travel)
- [ ] ![stable-diffusion-webui-aesthetic-gradients translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-aesthetic-gradients](https://github.com/AUTOMATIC1111/stable-diffusion-webui-aesthetic-gradients)
- [ ] ![stable-diffusion-webui-aesthetic-image-scorer translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-aesthetic-image-scorer](https://github.com/tsngo/stable-diffusion-webui-aesthetic-image-scorer)
- [ ] ![stable-diffusion-webui-artists-to-study translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-artists-to-study](https://github.com/camenduru/stable-diffusion-webui-artists-to-study)
- [ ] ![stable-diffusion-webui-conditioning-highres-fix translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-conditioning-highres-fix](https://github.com/klimaleksus/stable-diffusion-webui-conditioning-highres-fix)
- [ ] ![stable-diffusion-webui-daam translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-daam](https://github.com/toriato/stable-diffusion-webui-daam)
- [ ] ![stable-diffusion-webui-dataset-tag-editor translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-dataset-tag-editor](https://github.com/toshiaki1729/stable-diffusion-webui-dataset-tag-editor)
- [ ] ![stable-diffusion-webui-depthmap-script translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-depthmap-script](https://github.com/thygate/stable-diffusion-webui-depthmap-script)
- [ ] ![stable-diffusion-webui-embedding-editor translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-embedding-editor]()
- [ ] ![stable-diffusion-webui-images-browser translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-images-browser]()
- [ ] ![stable-diffusion-webui-inspiration translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-inspiration](https://github.com/yfszzx/stable-diffusion-webui-inspiration)
- [ ] ![stable-diffusion-webui-pixelization translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-pixelization](https://github.com/AUTOMATIC1111/stable-diffusion-webui-pixelization)
- [ ] ![stable-diffusion-webui-randomize translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-randomize]()
- [ ] ![stable-diffusion-webui-text2prompt translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-text2prompt](https://github.com/toshiaki1729/stable-diffusion-webui-text2prompt)
- [ ] ![stable-diffusion-webui-tokenizer translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-tokenizer](https://github.com/AUTOMATIC1111/stable-diffusion-webui-tokenizer)
- [ ] ![stable-diffusion-webui-two-shot translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [stable-diffusion-webui-two-shot](https://github.com/opparco/stable-diffusion-webui-two-shot)
- [ ] ![ultimate-upscale-for-automatic1111 translated 0%](https://geps.dev/progress/0?dangerColor=c9f2dc&warningColor=6cc570&successColor=00ff7f) [ultimate-upscale-for-automatic1111](https://github.com/Coyote-A/ultimate-upscale-for-automatic1111)
</details>

# Getting Started

### 1. 公式の拡張機能リストからインストール(最も推奨)
1. `Extensions`タブをクリックし、`Available`をクリックします。
2. `Extension index URL`が以下のURLであることを確認したら`Load From:`をクリックします。
![](./images/official-extensions-list1.png)
```
https://raw.githubusercontent.com/wiki/AUTOMATIC1111/stable-diffusion-webui/Extensions-index.md
```
3. 読込まれたことが確認できたら、`Hide extensions with tags`を`localization`**以外**にチェックマークを付けます。(`localization`にはつけません)
4. 各言語が出てきますので、`ja_JP Localization`の項目の`Install`をクリックします。
![](./images/official-extensions-list2.png)
5. `Installed into...`と表示されたら、[利用方法](#利用方法)へ移動してください。


### 2. 拡張機能のリポジトリのURLからインストール(推奨)
1. `Extensions`タブをクリックし、`URL for extension's git repository`のテキストボックスに以下のURLをペーストします。
```
https://github.com/Katsuyuki-Karasawa/stable-diffusion-webui-localization-ja_JP
```
2. `Install`をクリックします。
3. `Installed into...`と表示されたら、[利用方法](#利用方法)へ移動してください。
![](./images/install-from-url.png)


### 3. ローカルでインストール(推奨)
1. [zipファイル](https://github.com/Katsuyuki-Karasawa/stable-diffusion-webui-localization-ja_JP/archive/refs/heads/main.zip)をダウンロードします。
2. ダウンロードしたzipを`stable-diffusion-webui`以下の`extensions`に移動させます。
![](./images/local-install-dir.png)
3. zipファイルを右クリックして、**すべて展開**します。
4. 展開されたことが確認できたら、[利用方法](#利用方法)へ移動してください。

### 4. ローカルでインストール(非推奨)
**この手順はWeb UIからのアップデートができません。**  
**また、この手順はアップデートにて廃止される可能性があるためご注意ください。**
1. [jsonファイル](https://raw.githubusercontent.com/Katsuyuki-Karasawa/stable-diffusion-webui-localization-ja_JP/main/localizations/ja_JP.json)にアクセスする。
2. 右クリックから`名前を付けて保存...`、もしくは`Ctrl+S`で保存します。
![](./images/save-json.png)
3. 保存先は`stable-diffusion-webui`以下の`localizations`です。
![](./images/local-json-dir.png)
4. 保存されたことを確認したら、[利用方法](#利用方法)へ移動してください。


## 利用方法
### 日本語化ファイルを読み込む
1. `Settings`タブへ移動します。
2. `Settings`タブから`Localization (requires restart)`の項目を探します。
![](./images/localozation-section.png)
3. ドロップダウンリストから`ja-JP`を選択します。(もし、出てこない場合は右側の🔄から再読込してください。)

### 設定を適用する
1. ページ上部のオレンジ色のボタン(*Apply settings*)をクリックして設定を保存します。
![](https://user-images.githubusercontent.com/60730393/202901412-26765c04-e69c-4beb-a56b-9e310ed273ca.png)
2. ページ下部のオレンジ色のボタン(*Restart Gradio and Refresh components*)をクリックして、web UIを再起動します。
![](https://user-images.githubusercontent.com/60730393/202901401-de7d34e9-67c6-4f39-8f5f-b0c0c7a58b54.png)

## 翻訳がおかしい/翻訳を手伝う
### [Crowdin](https://crwd.in/stable-diffusion-webui-localization-ja_JP)から翻訳ができます!
気軽に[issue](https://github.com/Katsuyuki-Karasawa/stable-diffusion-webui-localization-ja_JP/issues)を投げましょう!  
分からないことがあれば[Disscussions](https://github.com/Katsuyuki-Karasawa/stable-diffusion-webui-localization-ja_JP/discussions)へどうぞ!  

# Thanks
- [stable-diffusion-webui-localization-source](https://github.com/harukaxxxx/stable-diffusion-webui-localization-source)
    - 翻訳のソース(Translate Sources)

- [sd-webui-bilingual-localization](https://github.com/journey-ad/sd-webui-bilingual-localization)
    - バイリンガル対応拡張機能(bilingual localization extensions)
