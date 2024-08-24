import streamlit as st

# 空白を入れる関数
def add_spacer_bottom(height: int = 60, unique_id: str = "spacer"):
	st.markdown(f"""
		<style>
		.{unique_id} {{ margin-bottom: {height}px; }}
		</style>
		<div class="{unique_id}"></div>
	""", unsafe_allow_html=True)

def main_usage():
	st.title(":book:使い方")
	st.write("こちらは音声生成のやり方についての説明ページです．")

	# キャプション1
	st.markdown("""
		<h4>1. 音声ファイルのアップロード</h4>
		<p><font size="3">
			以下の画像のグレー部分に音声ファイルをドラッグアンドドロップ，もしくは "Browse files" を押してファイルを探してください．
		</font></p>
		""",
		unsafe_allow_html=True
	)
	st.image("images/upload.png", caption="実際のアップロード画面", output_format="png")
	st.markdown("""
		<p><font size="3">
			ただし，アップロードできる<b><font color='red'>ファイルは1つまで</font></b>で，それ以上選択しようとすると新しく選択したファイルが選ばれます．
			<br>
			また，アップロードできる音声ファイルは「<b><font color='red'>.wav</font></b>」「<b><font color='red'>.ogg</font></b>」「<b><font color='red'>.mp3</font></b>」です．
			<br>
			<b><font color='red'>注意!!!</font></b>：必ず音声ファイルは<b><font color='red'>4秒以下</font></b>のファイルにしてください．それ以上であると音声が生成できない可能性があります．
		</font></p>
		""",
		unsafe_allow_html=True
	)

	# 空白
	add_spacer_bottom(20, "spacer_20")

	# キャプション2
	st.markdown("""
		<h4>2. アップロードした音声ファイルの文字起こし</h4>
		<p><font size="3">
			以下の画像の「ここに記入」の場所にアップロードした音声ファイルの文字起こしをしてください．（音声ファイルを再生したときに喋っている内容をそのまま文字にするだけです）
		</font></p>
		""",
		unsafe_allow_html=True
	)
	st.image("images/transcript_input.png", caption="実際の入力画面", output_format="png")
	st.markdown("""
		<p><font size="3">
			注意していただきたいのが，入力が終了した際には<b><font color='red'>必ずエンターキーを押してください</font></b>．
			入力ができているのであれば，上記画像の青背景部分が消えます．
		</font></p>
		""",
		unsafe_allow_html=True
	)

	# 空白
	add_spacer_bottom(20, "spacer_20")

	# キャプション3
	st.markdown("""
		<h4>3. 喋らせたい内容の記入</h4>
		<p><font size="3">
			以下の画像の「ここに記入」の場所に合成した声に喋らせたい文章を記入してください．
		</font></p>
		""",
		unsafe_allow_html=True
	)
	st.image("images/generate_txt.png", caption="実際の入力画面", output_format="png")
	st.markdown("""
		<p><font size="3">
			こちらも，入力が終了した際には<b><font color='red'>必ずエンターキーを押してください</font></b>．
			入力ができているのであれば，上記画像の青背景部分が消えます．
		</font></p>
		""",
		unsafe_allow_html=True
	)

	# 空白
	add_spacer_bottom(20, "spacer_20")

	# キャプション4
	st.markdown("""
		<h4>4. 実際に生成しよう</h4>
		<p><font size="3">
			以上の３ステップがすべて終了したら，ページ一番下の生成ボタンが以下の画像のように赤く変化します．そのボタンを押せば<b><font color='red'>音声の生成が開始</font></b>されます．
		</font></p>
		""",
		unsafe_allow_html=True
	)
	st.image("images/generate_button.png", caption="実際の生成ボタン", output_format="png")

	# 空白
	add_spacer_bottom(20, "spacer_20")

	# キャプション5
	st.markdown("""
		<h4>5. 生成した音声を聞いてみよう・ダウンロードしてみよう</h4>
		<p><font size="3">
			生成が終了すれば以下の画像のような画面が新たに出てきます．
			<br>
			再生ボタンを押せば生成された音声を再生することができます．
			<br>
			右下のダウンロードボタンを押せば，生成した音声を実際にダウンロードすることができます．
		</font></p>
		""",
		unsafe_allow_html=True
	)
	st.image("images/download.png", caption="実際の生成後の画面", output_format="png")

