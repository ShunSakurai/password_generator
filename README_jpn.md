﻿# Password Generator
簡素なパスワード生成ツール

[英語のREADME](https://github.com/ShunSakurai/password_generator/blob/master/README.md)もあります。

![UI](https://raw.github.com/wiki/ShunSakurai/password_generator/password_ui.png)

## 説明
1クリックでクリップボードにパスワードをコピーできるような、**シンプルな**パスワード生成ツールを作りたいと思い、このツールを開発しました。
既存のプログラムやウェブサイトの多くは、パスワードをコピーするために(パスワードをドラッグして選択、右クリック、コピーの)3アクションが必要です。

このツールは、Pythonとtkinterを使用してコーディングし、[PyInstaller](http://www.pyinstaller.org/)と[Verpatch](https://ddverpatch.codeplex.com/releases)を使用して.exe形式で配布、[PyInstaller](http://www.pyinstaller.org/)を使用してMacの.app形式で配布するものです。

## インストール
現在、WindowsとMacに対応しています。インストーラーと実行可能ファイルは[Releases(リリース)](https://github.com/ShunSakurai/password_generator/releases)で入手できます。iOS版も、[Pythonista](http://omz-software.com/pythonista/)のコードとして入手できます。URLスキームのpythonista://password_iphone.pyを使用して実行したり、ホーム画面に追加することができます。

Python環境をインストールしている場合、`python(3) password_generator.py`または`import password_generator`でソースコードをMacなど任意のOSで実行できます。

### Windows
インストーラーをダウンロードして実行するだけで、インストールやアップデートを行えます。

### Mac
- Password.Generator.app.zipをダウンロードし、解凍します
- .appファイルを「アプリケーション」フォルダーに移動します。アプリが含まれていたフォルダーは削除してかまいません

アプリケーション単体で動作しない場合は、次を実行してください。

- .appファイルをお好みの場所に移動します。アプリが含まれていたフォルダーは削除してかまいません
- Password Generator.appを右クリックして、「パッケージの内容を表示」をクリックし、Password Generator.app/Contents/MacOS/Password Generatorのエイリアスを作成します
- エイリアスを「アプリケーション」フォルダーに移動します。

### iOS
- まず、Pythonistaを購入してください
- コードをアプリ内にコピーアンドペーストします
- iPhone 5/SEの画面に合うようにコードを書きました。なるべく比率でサイズが決まるようにしていますが、お使いのデバイスのサイズに応じて、必要な場合にパラメーターを変更してください
- パスワードの長さと数は、手動で変更してください

Pythonistaで「レンチ」アイコン>[Home Screen]を選択するか、Safariで次のリンクを開いて「ホーム画面に追加」を選択することにより、ホーム画面にショートカットを作成することができます。
```
data:text/html;charset=UTF-8,<title>Password</title><meta name="apple-mobile-web-app-capable" content="yes"><link rel="apple-touch-icon" href="https://raw.github.com/wiki/ShunSakurai/password_generator/home_icon.png"><script>navigator.standalone?location="pythonista://password_iphone.py":alert("Add to home screen.")</script>
```

## ビルド

### Windows
Pythonコードを.exeファイルに変換し、インストーラーを作成するには、次の手順に従います。

### 要件
- [Python 3](https://www.python.org/downloads/)
- [PyInstaller](http://www.pyinstaller.org/)
- [Verpatch](https://ddverpatch.codeplex.com/releases)、パスを通してください
- [Inno Setup](http://www.jrsoftware.org/isdl.php)

### 手順
- Windows環境で、`py -B setup_win.py`を実行します。`-B`はオプションです
- py = python3となるように、エイリアスを設定する必要があるかもしれません

### Mac
Pythonコードを.appファイルに変換するには、次の手順に従います。

### 要件
- [Python 3](https://www.python.org/downloads/)
- [PyInstaller](http://www.pyinstaller.org/)
- [Verpatch](https://ddverpatch.codeplex.com/releases)、パスを通してください
- [Inno Setup](http://www.jrsoftware.org/isdl.php)

### 手順
- Windows環境で、`py -B setup_win.py`を実行します。`-B`はオプションです
- py = python3となるように、エイリアスを設定する必要があるかもしれません

## 使用方法
プログラムを開くには、Password Generator.exeまたはPassword Generatorをダブルクリックします。

画面右側で選択肢の一つをクリックします。これで、クリップボードにコピーされます。
画面左側で、設定を変更します。記号、英字、数字の入切を切り替えることができます。生成されるパスワードの長さと選択肢の数は、1から20までの任意の数に設定できます。

![Selected](https://raw.github.com/wiki/ShunSakurai/password_generator/password_selected.png)

このツールは、パスワードを生成し、クリップボードにコピーする機能のみを提供します。保存機能は用意されておらず、今後追加する予定もありません。

## 今後追加予定の機能
### 開発中の機能
- コードの[リーダブル](http://www.amazon.co.jp/dp/4873115655)化
- 設定を保存する機能

### 棚上げ中の機能
- キーボードショートカットを追加(例: 1から10)

すぐに使用したい機能がある場合は、[Github Issues](https://github.com/ShunSakurai/password_generator/issues)または[Asana](https://app.asana.com/0/264055467962183/list)からご連絡ください。

## 履歴
履歴の詳細は、[Releases(リリース)](https://github.com/ShunSakurai/password_generator/releases)でご覧ください。

文頭の「*」は、バグ修正を示します。

## 貢献
これは個人的なプロジェクトにすぎませんが、[Github Issues](https://github.com/ShunSakurai/password_generator/issues)または[Asana](https://app.asana.com/0/264055467962183/list)から、どんなご意見や貢献でもいただけると幸いです。

## 使用権限
このツールは無料でお使いいただけます。個人利用のみに限定します。このプログラムの使用によって生じるいかなる損害についても責任は持ちません。

Pythonのrandomモジュールの擬似乱数生成器をセキュリティ目的に使用してはいけませんという注意書きがあることにご注意ください。
https://docs.python.org/3/library/random.html#module-random

© 2016-2018 Shun Sakurai

## 基本的な考え方
- このプログラムでは4グループの文字列を使用します(デフォルトは以下のとおりです)
- 文字列の各グループから、ランダムに文字を1つずつ選択します
- パスワードの長さを埋めるように、残りの文字を選択します
- パスワードが文字列の合計長さより長い場合を除いては、**パスワード中で同じ文字が重複して使用されることはありません**。安全性は劣るかもしれませんが、個人的にこちらのパスワードの見た目を気に入っています

> string = [chr(c) for c in range(33, 127)]
>
> 記号:
> 33 !, 34 ", 35 #, 36 $, 37 %, 38 &, 39 ', 40 (, 41 ), 42 *, 43 +, 44 ,, 45 -, 46 ., 47 /,
> 58 :、59 ;、60 <、61 =、62 >、63 ?、64 @,
> 123 {、124 |、125 }、126~
>
> 大文字:
> 65 A、66 B、67 C、68 D、69 E、70 F、71 G、72 H、73 I、74 J、75 K、76 L、77 M、78 N、79 O、80 P、81 Q、82 R、83 S、84 T、85 U、86 V、87 W、88 X、89 Y、90 Z,
>
> 小文字:
> 91 [、92 \、93 ]、94 ^、95 _、96 `、97 a、98 b、99 c、100 d、101 e、102 f、103 g、104 h、105 i、106 j、107 k、108 l、109 m、110 n、111 o、112 p、113 q、114 r、115 s、116 t、117 u、118 v、119 w、120 x、121 y、122 z,
>
> 数字:
> 48 0、49 1、50 2、51 3、52 4、53 5、54 6、55 7、56 8、57 9,
