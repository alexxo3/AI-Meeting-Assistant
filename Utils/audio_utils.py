from moviepy.editor import VideoFileClip
import os

def extract_audio(video_path, audio_output_path):
    """
    Extracts audio from a video file and saves it as an audio file.

    Args:
        video_path (str): Path to the video file.
        audio_output_path (str): Desired path for the output audio file.

    Returns:
        str: Path to the saved audio file.
    """
    try:
        print(f"[INFO] Loading video file from: {video_path}")
        video = VideoFileClip(video_path)

        if not video.audio:
            raise Exception("No audio stream found in the video.")

        print(f"[INFO] Extracting audio to: {audio_output_path}")
        video.audio.write_audiofile(audio_output_path)

        print("[INFO] Audio extraction complete.")
        return audio_output_path

    except Exception as e:
        print(f"[ERROR] Failed to extract audio: {e}")
        return None
