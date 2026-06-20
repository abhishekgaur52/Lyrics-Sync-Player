import os
import re
import requests
import time
from pathlib import Path
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

TOKEN = os.getenv("GENIUS_TOKEN")

if not TOKEN:
    print("Missing GENIUS_TOKEN")
    exit()

headers = {"Authorization": f"Bearer {TOKEN}"}

def clean_filename(name):
    return re.sub(r'[<>:"/\\|?*]', '', name)

song_name = input("Enter song name: ")

# ---------------- SEARCH ----------------
url = f"https://api.genius.com/search?q={song_name}"
res = requests.get(url, headers=headers)

if res.status_code != 200:
    print("Search failed:", res.status_code)
    exit()

data = res.json()
hits = data["response"]["hits"]

if not hits:
    print("No song found")
    exit()

song = hits[0]["result"]

title = song["title"]
artist = song["artist_names"]
song_url = song["url"]

print("\nSong:", title)
print("Artist:", artist)

# ---------------- SCRAPE ----------------
page = requests.get(song_url)
soup = BeautifulSoup(page.text, "html.parser")

blocks = soup.find_all("div", {"data-lyrics-container": "true"})

if not blocks:
    print("Lyrics not found")
    exit()

raw = "\n".join([b.get_text("\n") for b in blocks])

# ---------------- CLEANING (PRO MODE) ----------------
clean_lines = []

for line in raw.splitlines():
    line = line.strip()

    # remove junk
    if not line:
        continue
    if "Contributor" in line:
        continue
    if "Lyrics" == line:
        continue
    if line.startswith("[") and line.endswith("]"):
        clean_lines.append(line)   # keep section tags
        continue

    clean_lines.append(line)

text = " ".join(clean_lines)

# ---------------- SAVE FILE ----------------
Path("lyrics").mkdir(exist_ok=True)

filename = clean_filename(f"{title} - {artist}.txt")
filepath = Path("lyrics") / filename

with open(filepath, "w", encoding="utf-8") as f:
    f.write(text)

# ---------------- STREAM MODE ----------------
print("\n" + "=" * 50)


words = text.split()

chunk = []
speed = 0.6   # PRO SPEED (tune: 0.4 fast, 0.8 slow)

for word in words:
    print(word, end=" ", flush=True)
    chunk.append(word)

    time.sleep(speed)

    if len(chunk) == 5:
        print("")
        chunk = []

# remaining words
if chunk:
    print("")

print("=" * 50)
print("Saved:", filepath)

