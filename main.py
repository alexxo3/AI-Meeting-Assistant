import os
from utils.audio_utils import extract_audio
from utils.transcription import transcribe_audio
from utils.summarizer import summarize_transcript
from utils.exporter import save_as_txt, save_as_docx

INPUT_VIDEO = "input/meeting_video.mp4"
AUDIO_PATH = "output/meeting_audio.wav"
TRANSCRIPT_PATH = "output/transcript.txt"
SUMMARY_TXT_PATH = "output/summary.txt"
SUMMARY_DOCX_PATH = "output/summary.docx"

def main():
    print("🔊 Extracting audio...")
    extract_audio(INPUT_VIDEO, AUDIO_PATH)

    print("📝 Transcribing...")
    transcript = transcribe_audio(AUDIO_PATH)
    save_as_txt(transcript, TRANSCRIPT_PATH)

    print("🧠 Summarizing...")
    summary = summarize_transcript(transcript)
    save_as_txt(summary, SUMMARY_TXT_PATH)
    save_as_docx(summary, SUMMARY_DOCX_PATH)

    print("✅ Process complete! Check the output folder.")

if __name__ == "__main__":
    main()
