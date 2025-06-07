from moviepy.editor import VideoFileClip
import os

def extract_audio(video_path, audio_output_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_output_path)
    return audio_output_path
