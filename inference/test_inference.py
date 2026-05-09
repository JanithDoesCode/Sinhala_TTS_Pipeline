from TTS.utils.synthesizer import Synthesizer

model_path = r"D:\a_PERSONAL\LMS\SELF_PROJECT\STT test2\SEt\Sinhala_TTS_Pipeline\model\best_model_272.pth"

config_path = r"D:\a_PERSONAL\LMS\SELF_PROJECT\STT test2\SEt\Sinhala_TTS_Pipeline\config.json"

tts = Synthesizer(
    tts_checkpoint=model_path,
    tts_config_path=config_path,
)

wav = tts.tts("මම සිංහලෙන් කතා කරනවා")

tts.save_wav(wav, "test_output.wav")

print("DONE")