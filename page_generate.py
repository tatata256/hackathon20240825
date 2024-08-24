import streamlit as st
import os
import time
import tempfile
from audio_generation import generate_audio_from_text

# 一時ファイルを作成し、そのパスを取得
def write_temp_file(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.getvalue())
        temp_file_path = temp_file.name
    return temp_file_path


# ダウンロードボタン関数（ボタンを押してもページが更新されないようにする）
@st.fragment
def fragment_download(count, generate_audio_path):
    # ダウンロードボタンのレイアウト調整
    st.markdown("""
        <style>
        .stDownloadButton > button {
            float: right;
            width: 150px;
            height: 30px;
            font-size: 12px;
            background-color: #FF4B4B;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: -8mm;
        }
        .stDownloadButton > button:hover {
            background-color: #FF4B4B; /* ホバー時の背景色 */
            color: white;  /* ホバー時の文字色 */
        }
        </style>
    """, unsafe_allow_html=True)

    # 一時ファイルを読み込む
    with open(generate_audio_path, 'rb') as file:
        generate_audio = file.read()

    # ダウンロードボタン
    st.download_button(
        label="ダウンロード",
        data=generate_audio,
        file_name=f"cloned{count}.wav",
        mime="audio/wav",
        type="primary"
    )


# 空白を入れる関数
def add_spacer_bottom(height: int = 60, unique_id: str = "spacer"):
    st.markdown(f"""
        <style>
        .{unique_id} {{ margin-bottom: {height}px; }}
        </style>
        <div class="{unique_id}"></div>
    """, unsafe_allow_html=True)


# キャプションとテキストインプットの行間を詰める関数
def add_custom_label(label_text, color, margin_bottom_cm=0):
    st.markdown(f"""
        <div style="color: {color}; font-size: 14px; margin-bottom: {margin_bottom_cm}cm;">
            {label_text}
        </div>
    """, unsafe_allow_html=True)

# メイン画面
def main_generate():
	st.title(":microphone:音声生成")
	st.write("""
          こちらは音声生成ページです．
		  <br>
		  合成したい人物の<b><font color='red'>音声ファイル</font></b>，<b><font color='red'>ファイルの文字起こし</font></b>，<b><font color='red'>喋らせたい内容</font></b>を以下に記入してください．""",
		  unsafe_allow_html=True
		  )

	# 空白
	add_spacer_bottom(20, "spacer_20")

	# 音声ファイルのアップロード
	with st.container(): # 一つの塊として表示（オプション：border=True で境界線が表示）
		# キャプション
		add_custom_label(
			"合成したい人物の音声ファイルを選択してください（1つまで）：",
			"#888888",
			margin_bottom_cm=0.1
		)
		# ファイルアップローダー
		uploaded_file = st.file_uploader(
			"ファイルを選択（1つまで）",
			type=['wav', 'ogg', 'mp3'],
			help=".wav や .ogg などの音声ファイルをアップロード",
			label_visibility="collapsed"
		)
		# ファイルの情報を表示
		if uploaded_file is not None:
			st.audio(uploaded_file, format=uploaded_file.type) # アップロードした音声ファイルを再生できるようにした
		else:
			st.info('☝️ 音声ファイルをアップロードしてください')

	# 空白
	add_spacer_bottom(20, "spacer_20")

	# 音声ファイルの文字起こし
	with st.container():
		# キャプション
		add_custom_label(
			"選択した音声ファイルの文字起こしをしてください：",
			"#888888",
			margin_bottom_cm=0.1
		)
		# テキストエリア
		transcript = st.text_input(
			label="音声ファイルの文字起こし",
			placeholder="ここに記入",
			help="音声ファイルに含まれている声をそのまま文字にする",
			label_visibility="collapsed"
		)
		if transcript == "":
			st.info('☝️ テキストを入力してエンターキーを押してください')

	# 空白
	add_spacer_bottom(20, "spacer_20")

	# 喋らせたい言葉
	with st.container():
		# キャプション
		add_custom_label(
			"喋らせたい言葉を記入してください：",
			"#888888",
			margin_bottom_cm=0.1
		)
		# テキストエリア
		generate_txt = st.text_input(
			label="喋らせたい言葉を入力",
			placeholder="ここに記入",
			help="喋らせたい言葉をそのまま文字にする",
			label_visibility="collapsed"
		)
		if generate_txt == "":
			st.info('☝️ テキストを入力してエンターキーを押してください')

	# 空白
	add_spacer_bottom(40, "spacer_40")

	# 単一要素コンテナ
	placeholder = st.empty()

	# ボタンが押された回数を保持する
	if "count" not in st.session_state:
		st.session_state.count = 0

	# 生成ボタンの有効/無効を設定
	is_ready = uploaded_file is not None and transcript != "" and generate_txt != ""

	# 生成ボタン
	if is_ready:
		submit_button = placeholder.button("生成", type="primary", use_container_width=True, key="generate_button")
	else:
		submit_button = placeholder.button("生成", disabled=True, use_container_width=True, key="generate_button")

	# ボタンが押された後の処理
	if submit_button and is_ready:
		placeholder.button("生成", disabled=True, use_container_width=True) # "生成"ボタンを押せなくする
		# placeholder.empty() # "生成"ボタンを非表示にする
		# ぐるぐるマークの表示
		with st.spinner('生成中...'):
			st.toast('生成が開始されました')
			st.session_state.count += 1 # 生成ボタンが押された回数をカウント

			# アップロードファイルのパスを獲得
			temp_file_path = write_temp_file(uploaded_file)

			# audio_generation.py の関数を呼び出す
			generate_audio_path = generate_audio_from_text(
				audio_prompt_path=temp_file_path,
				transcript=transcript,
				text_prompt=generate_txt
			)

		# 水平線
		st.divider()

		successful_display = st.empty() # メッセージの一時表示
		successful_display.success("音声の生成が完了しました") # 成功メッセージを表示
		placeholder.button("生成", type="primary", use_container_width=True) # "生成"ボタンをもとに戻す

		# 生成した音声ファイルを出力
		st.caption("生成された音声：")
		st.audio(generate_audio_path)

		# ダウンロードボタン（ボタンを押してもページが更新されないようにする）
		fragment_download(st.session_state.count, generate_audio_path)

		time.sleep(3) # 3秒待機
		successful_display.empty() # メッセージを消去

		os.remove(temp_file_path)

