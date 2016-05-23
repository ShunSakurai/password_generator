# password_generator
簡素なパスワード生成ツール

[英語のREADME](https://github.com/ShunSakurai/password_generator/blob/master/README.md)もあります。

![UI](https://raw.github.com/wiki/ShunSakurai/password_generator/password_ui.png)

## 説明
1クリックでクリップボードにパスワードをコピーできるような、**シンプルな**パスワード生成ツールを作りたいと思い、このツールを開発しました。
既存のプログラムやウェブサイトの多くは、パスワードをコピーするために(パスワードをドラッグして選択、右クリック、コピーの)3アクションが必要です。

このツールは、Pythonとtkinterを使用してコーディングし、[py2exe](http://www.py2exe.org/)を使用して.exe形式で配布、[py2app](https://pythonhosted.org/py2app/)を使用してMacの.app形式で配布するものです。

## インストール
現在、WindowsとMacに対応しています。プログラムファイルは[Releases(リリース)](https://github.com/ShunSakurai/password_generator/releases)で入手できます。iPhone版も、[Pythonista](http://omz-software.com/pythonista/)のコードとして入手できます。URLスキームのpythonista://password_iphone.pyを使用して実行したり、[Pythonista Shortcut](http://omz-software.com/pythonista/shortcut/)を使用してホーム画面に追加することができます。

Python環境をインストールしている場合、`python(3) password_generator.py`または`import password_generator`でソースコードをMacなど任意のOSで実行できます。

### Windows
インストーラーは現在開発中です。当面は、次の手順を実行してください。

- dist.zipをダウンロードし、解凍します
- フォルダー名を「Password」など、お好みの名前に変更します
- (任意)フォルダーをC:\Program Filesに移動します
- (任意).exeファイルへのショートカットを作成し、それをデスクトップ、ツール用フォルダー、C:\ProgramData\Microsoft\Windows\Start Menu\Programsなどに追加します(こうすると、Windowsスタートメニューからプログラムを実行できるようになります)

このプログラムが動作するには**フォルダーに含めたまま**にしておく必要があります。プログラム単体では動作しません。

### Mac
- Password.Generator.app.zipをダウンロードし、解凍します
- .appファイルを「アプリケーション」フォルダーに移動します。アプリが含まれていたフォルダーは削除してかまいません

アプリケーション単体で動作しない場合は、次を実行してください。

- .appファイルをお好みの場所に移動します。アプリが含まれていたフォルダーは削除してかまいません
- Password Generator.appを右クリックして、「パッケージの内容を表示」をクリックし、Password Generator.app/Contents/MacOS/Password Generatorのエイリアスを作成します
- エイリアスを「アプリケーション」フォルダーに移動します。

## 使用方法
プログラムを開くには、Password Generator.exeまたはPassword Generatorをダブルクリックします。

画面右側で選択肢の一つをクリックします。これで、クリップボードにコピーされます。
画面左側で、設定を変更します。記号、英字、数字の入切を切り替えることができます。生成されるパスワードの長さと選択肢の数は、1から20までの任意の数に設定できます。

![Selected](https://raw.github.com/wiki/ShunSakurai/password_generator/password_selected.png)

このツールは、パスワードを生成し、クリップボードにコピーする機能のみを提供します。
保存機能は用意されておらず、今後追加する予定もありません。

## 今後追加予定の機能
### 開発中の機能
- コードの[リーダブル](http://www.amazon.co.jp/dp/4873115655)化
- 設定を保存する機能
- インストーラーを用意
- アイコンを用意

### 棚上げ中の機能
- 使用する文字を編集する機能
- キーボードショートカットを追加(例: 1から10)

すぐに使用したい機能がある場合は[ご連絡ください](https://app.asana.com/-/share?s=132674863519248-e1JyDAuWLW0WnFErIjTrbz57EAmE077JUvQ45Y5pF43-29199191293549)。

## 履歴

文頭の「*」は、バグ修正を示します。
履歴の詳細は、[Releases(リリース)](https://github.com/ShunSakurai/password_generator/releases)でご覧ください。

### 最新版
- 連絡先情報を追加

### v1.2.0、2016年4月23日
- 更新時に乱数の種を初期化
- distフォルダーと.appファイルのサイズを縮小

### v1.1.3、2016年4月13日
- * パスワードが必要なときに必ずコピーされるようにインデントを修正

### v1.1.2、2016年4月8日
- Windows版でボタンの線幅を縮小
- * Windowsでボタンが再度有効にならない問題を解決

### v1.1.0、2016年3月31日
- バイナリファイルを配布
- README_jpn.mdを作成

### v1.0.0、2016年3月28日
- GitHubに追加
- README.mdを作成

## 貢献
これは個人的なプロジェクトにすぎませんが、どんな[ご意見](https://app.asana.com/-/share?s=132674863519248-e1JyDAuWLW0WnFErIjTrbz57EAmE077JUvQ45Y5pF43-29199191293549)や貢献でもいただけると幸いです。

## 使用権限
このツールは無料でお使いいただけます。

© 2016 Shun Sakurai

## 基本的な考え方
- 次の文字を含む文字列を用意します
- 次の文字列から、文字を無作為に選択します
- 「num」(選択肢の数)チェックボタンが選択されていて、さらに「length」(パスワードの長さ)が2以上の場合、パスワードには数字を少なくとも1文字含むようにします
- パスワードが文字列の長さより長い場合以外は、**パスワード中で同じ文字が重複して使用されることはありません**。安全性は劣るかもしれませんが、個人的にこちらのパスワードの見た目を気に入っています

> string = [chr(c) for c in range(33, 127)]
>
> 記号:
> 33 !, 34 ", 35 #, 36 $, 37 %, 38 &, 39 ', 40 (, 41 ), 42 *, 43 +, 44 ,, 45 -, 46 ., 47 /,
> 58 :、59 ;、60 <、61 =、62 >、63 ?、64 @,
> 123 {、124 |、125 }、126~
>
> 英字:
> 65 A、66 B、67 C、68 D、69 E、70 F、71 G、72 H、73 I、74 J、75 K、76 L、77 M、78 N、79 O、80 P、81 Q、82 R、83 S、84 T、85 U、86 V、87 W、88 X、89 Y、90 Z,
> 91 [、92 \、93 ]、94 ^、95 _、96 `、97 a、98 b、99 c、100 d、101 e、102 f、103 g、104 h、105 i、106 j、107 k、108 l、109 m、110 n、111 o、112 p、113 q、114 r、115 s、116 t、117 u、118 v、119 w、120 x、121 y、122 z,
>
> 数字:
> 48 0、49 1、50 2、51 3、52 4、53 5、54 6、55 7、56 8、57 9,

