import os
import subprocess
from datetime import datetime, timedelta

def convert_time_to_seconds(time_str):
    if ',' in time_str:
        time_format = "%H:%M:%S,%f"
    else:
        time_format = "%H:%M:%S"

    time_obj = datetime.strptime(time_str, time_format)
    total_seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second + time_obj.microsecond / 1e6
    return total_seconds

def cut_video_clips(video_file, matches, output_folder):
    # Step 6: Cut video clips and export SRT file
    os.makedirs(output_folder, exist_ok=True)
    for i, match in enumerate(matches):
        start_time, end_time, quote = match
        clip_file = os.path.join(output_folder, f"clip_{i}.mp4")
        srt_file = os.path.join(output_folder, f"clip_{i}.srt")

        # Convert start and end time to seconds
        start_seconds = convert_time_to_seconds(start_time)
        end_seconds = convert_time_to_seconds(end_time)

        # Calculate duration in seconds
        duration = end_seconds - start_seconds

        # Format duration as HH:MM:SS
        duration_str = str(timedelta(seconds=duration))

        # Cut the video clip and re-encode
        ffmpeg_path = r"C:\Program Files\ffmpeg-2023-05-31-git-baa9fccf8d-full_build\bin\ffmpeg.exe"

        subprocess.call([ffmpeg_path, '-ss', start_time, '-i', video_file, '-t', duration_str, '-c:v', 'libx264', '-c:a', 'aac', '-strict', '-2', clip_file])

        # Generate SRT file
        with open(srt_file, "w") as file:
            file.write(f"1\n{start_time} --> {end_time}\n{quote}")

        print(f"Exported clip {i+1}: {clip_file}")

if __name__ == "__main__":
    matches = [('00:01:34,000', '00:02:40,000', "how much do you think of ksi's Ruffin we might have been somewhere")]
    video_file = r"C:\Users\sashw\OneDrive\Desktop\New folder (2)\video\videoplayback.mp4"
    output_folder = r"C:\Users\sashw\OneDrive\Desktop\New folder (2)\output"
    cut_video_clips(video_file, matches, output_folder)
