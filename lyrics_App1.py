import os
import re
import time
import requests
import pygame
import numpy as np
import librosa
from pathlib import Path
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

TOKEN = os.getenv("GENIUS_TOKEN")
headers = {"Authorization": f"Bearer {TOKEN}"}

def clean(name):
    return re.sub(r'[<>:"/\\|?*]', '', name)

song_name = input("Enter song name: ")

# ---------------- GENIUS SEARCH ----------------
res = requests.get(
    f"https://api.genius.com/search?q={song_name}",
    headers=headers
)

data = res.json()
song = data["response"]["hits"][0]["result"]

title = song["title"]
artist = song["artist_names"]
url = song["url"]

print("\nSong:", title)
print("Artist:", artist)

# ---------------- SCRAPE LYRICS ----------------
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

blocks = soup.find_all("div", {"data-lyrics-container": "true"})
raw = "\n".join([b.get_text("\n") for b in blocks])

lines = []
for l in raw.splitlines():
    l = l.strip()
    if not l:
        continue
    if "Contributor" in l:
        continue
    if l.startswith("[") and l.endswith("]"):
        continue
    lines.append(l)

# ---------------- LOAD AUDIO ----------------
audio_file = "song.mp3"

if not os.path.exists(audio_file):
    print("song.mp3 not found")
    exit()

y, sr = librosa.load(audio_file)

duration = librosa.get_duration(y=y, sr=sr)

# split song time evenly (approx sync)
time_per_line = duration / max(len(lines), 1)

# ---------------- PLAY AUDIO ----------------
pygame.mixer.init()
pygame.mixer.music.load(audio_file)
pygame.mixer.music.play()

print("\n" + "=" * 50)
print("AUTO SYNC LYRICS")
print("=" * 50)

start = time.time()

for i, line in enumerate(lines):
    target = i * time_per_line

    while time.time() - start < target:
        time.sleep(0.01)

    print(line)

print("=" * 50)
print("DONE")