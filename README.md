<h1>🔰 ボイスジェネレーター</h1>

<h4>1. はじめに</h4>
	<p><font size="3">
		我々なとサンチームは，<b>VALL-E-X</b> という音声合成モデルを用いたWebアプリケーションの作成に取り組みました．
		<br>
		このWebアプリケーションでは，指定した声を複製して別のセリフを喋らせることができます．
		<br>
		Webページの公開には Streamlit, GitHub を用い，音声の生成はAmazon AWS の lamda, s3 を使用しています．（現在，音声生成はオンライン上で生成できません（未完成），3. にローカル環境で実行する方法が記載されています）
	</font></p>

<h4>2. VALL-E-X とは</h4>
	<p><font size="3">
		Microsoft が公開している VALL-E（英語のみに対応）という数秒の音声サンプルから音声を合成できる生成AIがあります．
		そのモデルを英語以外の言語（中国語・日本語）にも対応したモデルが VALL-E-X です．
		Microsoft は VALL-E-X のモデルを公開していないが，有志の方が論文をもとに独自にトレーニングしたモデルを GitHub に公開してくれています．
		<br>
		我々はそのモデルを使用し，わかりやすいUIでWEB上で完結する音声合成サービスを作成しました．（現在，音声生成はオンライン上で生成できません（未完成），3. にローカル環境で実行する方法が記載されています）
	</font></p>

<h4>3. ローカルでの環境構築</h4>
	<p><font size="3">
		ローカル環境で実行したい場合は，もとのモデルである<a href="https://github.com/Plachtaa/VALL-E-X">こちら</a>を参考にするか，以下のコマンドを実行して VALL-E-X を動かせる状態にしてください．
	</font></p>

```commandline
git clone https://github.com/Plachtaa/VALL-E-X.git
cd VALL-E-X
pip install -r requirements.txt
```

<p><font size="3">
	VALL-E-X が動くようになったら，本ページのコードを "VALL-E-X" ディレクトリ内にクローンしてください．"images" ディレクトリが競合を起こすと思いますが上書きしてください．
	<br>
	クローンが完了したら，以下のコマンドを実行してください．
</font></p>

```commandline
pip install streamlit
pip install streamlit-option-menu
```

<p><font size="3">
	<b>※注意!!!</b>：クローンをしたら，"audio_generation.py" のコメントアウトしている箇所（2~4, 7~14, 19行目）を<b>コメントアウト解除</b>してください．これをしないと音声合成が正常に機能しません．
</font></p>

<p><font size="3">
	以上がすべて済みましたら，以下のコマンドを実行してください．
	<br>
	実行すると，ローカル環境でページを閲覧・音声を合成できるようになります．
</font></p>

```commandline
streamlit run home.py
```
	
