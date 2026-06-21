# 🎵 Lyrics Sync Player

A Python-based Lyrics Sync Player that allows users to search for a song, fetch lyrics, save them locally, and display them in a synchronized flow while the song is playing.

## ✨ Features
```

- Search songs using the Genius API
- Fetch song details (Title, Artist, Lyrics URL)
- Extract lyrics automatically
- Save lyrics as `.txt` files
- Display lyrics in a flowing stream mode
- MP3 playback support
- Foundation for karaoke-style synchronization

```

## 📸 Demo
```
Enter song name: Shape of You

Song: Shape of You
Artist: Ed Sheeran

The club isn't the best place
to find a lover so the bar
is where I go...
```
## 🛠️ Tech Stack
```
Python
Requests
BeautifulSoup4
python-dotenv
Pygame
Genius API
```

## 📂 Project Structure
```
Lyrics_App/
│
├── lyrics_App.py
├── .env
├── song.mp3
├── lyrics/
│   └── SongName - Artist.txt
│
└── README.md
```

## 🔑 Genius API Setup
```
Create an account on Genius.
Go to the API Clients page.
Create a new API Client.
Generate a Client Access Token.
Create a .env file:    GENIUS_TOKEN=YOUR_ACCESS_TOKEN
```

## 🚀 Usage
```

Run:

python lyrics_App.py

Enter:

Enter song name: Shape of You

The application will:

Search the song.
Fetch lyrics.
Save lyrics to a text file.
Display lyrics in the terminal.

📁 Output Example
lyrics/
└── Shape of You - Ed Sheeran.txt
```

## 📜 License

This project is intended for educational and personal use.

Please respect copyright laws and music licensing requirements when using song lyrics and audio files.
