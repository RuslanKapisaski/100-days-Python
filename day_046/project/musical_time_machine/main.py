import requests
from bs4 import BeautifulSoup
from ytmusicapi import YTMusic
import datetime


def get_billboard_songs(url):
    try:
        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        website = requests.get(url, headers=header)
        website.raise_for_status()
        soup = BeautifulSoup(website.content, "html.parser")
        songs = soup.select("span.chart-element__information__song")

        if not songs:
            raise ValueError("No songs found. Try a different snapshot URL.")

        return [song.getText().strip() for song in songs]

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []

    except ValueError as e:
        print(e)
        return []


def create_playlist(song_names, date):
    formatted = datetime.datetime.strptime(date, "%Y%m%d").date()
    try:
        yt = YTMusic("/Users/ruslankapisaski/Code/100-days-Python/day_046/project/musical_time_machine/browser.json")
        playlist_id = yt.create_playlist(
            title=f"Billboard Hot 100 - {formatted.strftime('%d-%m-%Y')}",
            description=f"Top 100 from {formatted.strftime('%d-%m-%Y')}",
            privacy_status="PRIVATE"
        )
        video_ids = []

        for song in song_names:
            try:
                results = yt.search(song, filter="songs")
                if results:
                    video_ids.append(results[0]["videoId"])
                    print(f"Found: {song}")
                else:
                    print(f"Not found: {song}")
            except Exception as e:
                print(f"Error searching for '{song}': {e}")

        for video_id in video_ids:
            try:
                yt.add_playlist_items(playlist_id, [video_id], duplicates=True)
            except Exception as e:
                print(f"Skipping {video_id}: {e}")

        print(f"\nDone! {len(video_ids)} songs added to playlist.")

    except Exception as e:
        print(f"Error creating playlist: {e}")


def get_user_input():
    return input("Enter snapshot date in format YYYYMMDD (e.g. 20200225): ")


def get_url(date):
    return f"https://web.archive.org/web/{date}/https://www.billboard.com/charts/hot-100"


# Ask for user preference
while True:
    date = get_user_input()
    try:
        datetime.datetime.strptime(date, "%Y%m%d")
    except ValueError:
        print("Invalid date format. Please use YYYYMMDD.")
        continue

    formatted_date = datetime.datetime.strptime(date, "%Y%m%d").strftime("%d-%m-%Y")
    print(f"Fetching Billboard Hot 100 from {formatted_date}...")

    song_names = get_billboard_songs(get_url(date))

    if song_names:
        print(f"Found {len(song_names)} songs. Creating playlist...")
        create_playlist(song_names, date)
        break
    else:
        user_preference = input("No songs found. Press 'y' to try again or any other key to exit: ")
        if user_preference.lower() != "y":
            break