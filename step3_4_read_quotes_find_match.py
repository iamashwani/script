# import os
# def read_quotes_and_find_matches(transcript_file, quotes_folder):
#     # Step 3: Read transcript from the SRT file
#     with open(transcript_file, "r") as file:
#         lines = file.readlines()

#     transcript = ""
#     for line in lines:
#         if not line.strip().isdigit() and "-->" not in line:
#             transcript += line.strip() + " "

#     # Step 4: Read quotes from the quotes folder
#     quote_files = os.listdir(quotes_folder)
#     quotes = []
#     for quote_file in quote_files:
#         with open(os.path.join(quotes_folder, quote_file), "r") as file:
#             quote = file.read().strip()
#             quotes.append(quote)

#     # Step 5: Find matches between quotes and transcript
#     matches = []
#     for quote in quotes:
#         if quote in transcript:
#             start_time = transcript.index(quote)
#             end_time = start_time + len(quote)
#             matches.append((start_time, end_time, quote))

#     return matches

# if __name__ == "__main__":
#     transcript_file = r"C:\Users\sashw\OneDrive\Desktop\New folder (2)\transcript\file.srt"
#     quotes_folder = r"C:\Users\sashw\OneDrive\Desktop\New folder (2)\quotes"
#     matches = read_quotes_and_find_matches(transcript_file, quotes_folder)
#     print(matches)


import os
import re

def convert_time_to_seconds(time_str):
    # Convert time in HH:MM:SS,mmm format to seconds
    hours, minutes, seconds = re.split(r"[:,]", time_str)
    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)

def convert_seconds_to_time(seconds):
    # Convert seconds to time in HH:MM:SS,mmm format
    milliseconds = int((seconds % 1) * 1000)
    time_str = f"{int(seconds // 3600):02d}:{int((seconds // 60) % 60):02d}:{int(seconds % 60):02d},{milliseconds:03d}"
    return time_str

def read_quotes_and_find_matches(transcript_file, quotes_folder):
    # Step 3: Read transcript from the SRT file
    with open(transcript_file, "r") as file:
        lines = file.readlines()

    transcript = ""
    for line in lines:
        if not line.strip().isdigit() and "-->" not in line:
            transcript += line.strip() + " "

    # Step 4: Read quotes from the quotes folder
    quote_files = os.listdir(quotes_folder)
    quotes = []
    for quote_file in quote_files:
        with open(os.path.join(quotes_folder, quote_file), "r") as file:
            quote = file.read().strip()
            quotes.append(quote)

    # Step 5: Find matches between quotes and transcript
    matches = []
    for quote in quotes:
        if quote in transcript:
            start_time = transcript.index(quote)
            end_time = start_time + len(quote)
            matches.append((convert_seconds_to_time(start_time), convert_seconds_to_time(end_time), quote))

    return matches

if __name__ == "__main__":
    transcript_file = r"C:\Users\sashw\OneDrive\Desktop\New folder (2)\transcript\file.srt"
    quotes_folder = r"C:\Users\sashw\OneDrive\Desktop\New folder (2)\quotes"
    matches = read_quotes_and_find_matches(transcript_file, quotes_folder)
    print(matches)
