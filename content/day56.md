# 👉 Day 56 Challenge: Music Streaming Service

<a href="https://youtu.be/aahj2VWYra4" target="_blank">📹 Dāvida video</a>

Today is a project day where you will be using your newly acquired csv reading and file management powers to work with data about a music streaming service.

**To run this day's code use terminal and run the file 😎**


### Now head over to the challenge for the details.

I've included a csv file ('100MostStreamedSongs.csv') under files directory that contains data from a music streaming service.

Your program should:
1. Read in the data.
2. Categorize the songs by artist, like this:
    - Create one empty folder per artist.
    - Create one blank text file per song by that artist in the relevant folder. The file name of the text file should be the name of the song.

<details>
<summary>💡 Hints</summary>

- For each artist, check the directory to see if they already have a folder. If they do, use it. If not, create it.

</details>


## Solution (No Peeking!)

<a href="https://youtu.be/dJ-7HVsAP3I" target="_blank">Solution video</a>

<details>
<summary>👀 Answer</summary>

```python
import csv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
artists_dir = os.path.join(script_dir, "files", "artists")

# Ensure the 'files/artists' directory exists
os.makedirs(artists_dir, exist_ok=True)

# Construct the path to the 'files/100MostStreamedSongs.csv' file
csv_file_path = os.path.join(script_dir, "files", "100MostStreamedSongs.csv")

with open(csv_file_path, mode='r') as file: 
    reader = csv.DictReader(file)

    for row in reader: 
        # Get the artist's name and song name, formatted properly
        artist = row["Artist(s)"].title().replace('/', '-')  # Replace slashes in artist name
        song = row["Song"].title().replace('/', '-')  # Replace slashes in song name

        # Construct the path to the artist's directory inside 'files/artists'
        artist_folder_path = os.path.join(artists_dir, artist)

        # Create the artist's folder if it doesn't already exist
        if not os.path.exists(artist_folder_path):
            os.mkdir(artist_folder_path)

        # Construct the full path for the song file inside the artist's folder
        song_file_path = os.path.join(artist_folder_path, f"{song}.txt")

        # Create an empty text file for the song
        with open(song_file_path, "w") as song_file:
            pass 

        print(f"Created file for: {artist} - {song}")
```

</details>