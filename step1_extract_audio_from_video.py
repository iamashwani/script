import subprocess
import os


def extract_audio(video_file, audio_file):
    # Step 1: Extract audio from the video file
    
    ffmpeg_path = r"C:\Program Files\ffmpeg-2023-05-31-git-baa9fccf8d-full_build\bin\ffmpeg.exe"
    subprocess.call([ffmpeg_path, '-i', video_file, '-vn', '-acodec', 'pcm_s16le', '-ar', '44100', '-ac', '2', audio_file])

    # Convert audio to mono
    mono_audio_file = audio_file.replace(".wav", "_mono.wav")
    subprocess.call([ffmpeg_path, '-i', audio_file, '-ac', '1', mono_audio_file])

    # Remove the original audio file
    os.remove(audio_file)

    # Rename the mono audio file to the original audio file name
    os.rename(mono_audio_file, audio_file)

if __name__ == "__main__":
    video_file = r"C:\Users\sashw\OneDrive\Desktop\New folder (2)\video\videoplayback.mp4"
    audio_file = r"C:\Users\sashw\OneDrive\Desktop\New folder (2)\audio\file.wav"

    extract_audio(video_file, audio_file)
