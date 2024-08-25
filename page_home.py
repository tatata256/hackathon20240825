import streamlit as st

def main_home():
	st.title(":beginner: ボイスジェネレーター")
	
	st.markdown("""
		<h4>1. はじめに</h4>
		<p><font size="3">
			我々なとサンチームは，<b>VALL-E-X</b> という音声合成モデルを用いたWebアプリケーションの作成に取り組んだ．
			<br>
			このWebアプリケーションでは，指定した声を複製して別のセリフを喋らせることができる．
			<br>
			Webページの公開には Streamlit, GitHub を用い，音声の生成は<s>Amazon AWS の lamda, s3 を使用している．</s>（現在，音声生成はオンライン上で生成できません（未完成），GitHub にローカル環境で実行する方法が記載されています）
		</font></p>
		""",
		unsafe_allow_html=True
	)

	st.markdown("""
		<h4>2. VALL-E-X とは</h4>
		<p><font size="3">
			Microsoft が公開している VALL-E（英語のみに対応）という数秒の音声サンプルから音声を合成できる生成AIがある．
			そのモデルを英語以外の言語（中国語・日本語）にも対応したモデルが VALL-E-X である．
			Microsoft は VALL-E-X のモデルを公開していないが，有志の方が論文をもとに独自にトレーニングしたモデルを GitHub に公開してくれている．
			<br>
			我々はそのモデルを使用し，わかりやすいUIで<s>WEB上で完結する</s>音声合成サービスを作成した．（現在，音声生成はオンライン上で生成できません（未完成），GitHub にローカル環境で実行する方法が記載されています）
		</font></p>
		""",
		unsafe_allow_html=True
	)

