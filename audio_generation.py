import os
import numpy as np
import tempfile

def generate_audio_from_text(audio_prompt_path, transcript, text_prompt):
    # 生成された音声をファイルに書き込む
    with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_file:
    # temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
        temp_file_path = temp_file.name

    return temp_file_path
