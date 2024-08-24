import os
import numpy as np
import tempfile
from utils.prompt_making import make_prompt
from utils.generation import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

def generate_audio_from_text(audio_prompt_path, transcript, text_prompt):
    # 与えられた文字起こしを使用する
    make_prompt(name="hoge", audio_prompt_path=audio_prompt_path, transcript=transcript)
    
    # モデルをダウンロードしてロードする
    preload_models()
    
    # 音声を生成する
    audio_array = generate_audio(text_prompt)
    
    # 生成された音声をファイルに書き込む
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_file:
    # temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
        temp_file_path = temp_file.name
        write_wav(temp_file_path, SAMPLE_RATE, audio_array)
        temp_file.close()

    return temp_file_path
