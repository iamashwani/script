from google.cloud import speech
from google.oauth2 import service_account
import datetime

def format_timedelta(td):
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = td.microseconds // 1000
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

def transcribe_and_save(audio_file, transcript_file):
    # Step 2: Transcribe the audio file using Google Cloud Speech-to-Text API
    credentials = service_account.Credentials.from_service_account_file(r"C:\Users\sashw\OneDrive\Desktop\New folder (2)\google_cred.json")
    client = speech.SpeechClient(credentials=credentials)

    with open(audio_file, "rb") as audio:
        content = audio.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    lines = []
    line_number = 1
    for result in response.results:
        for alternative in result.alternatives:
            transcript = alternative.transcript
            confidence = alternative.confidence
            start_time = result.result_end_time
            end_time = result.result_end_time

            start_time_formatted = format_timedelta(start_time)
            end_time_formatted = format_timedelta(end_time)

            line = f"{line_number}\n{start_time_formatted} --> {end_time_formatted}\n{transcript}\n"
            lines.append(line)
            line_number += 1

    # Save the transcript to an SRT file
    with open(transcript_file, "w") as file:
        file.writelines(lines)

    return lines

if __name__ == "__main__":
    audio_file = r"C:\Users\sashw\OneDrive\Desktop\New folder (2)\audio\file.wav"
    transcript_file = r"C:\Users\sashw\OneDrive\Desktop\New folder (2)\transcript\file.srt"
    transcript = transcribe_and_save(audio_file, transcript_file)
    print("Transcript saved")
