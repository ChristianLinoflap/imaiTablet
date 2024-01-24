import os
import re
import pyodbc
import logging
from pytube import YouTube
from moviepy.editor import VideoFileClip
from config import db_server_name, db_name, db_username, db_password

class DatabaseManager:
    def __init__(self, server_name, database_name, username, password):
        self.server_name = server_name
        self.database_name = database_name
        self.username = username
        self.password = password
        self.connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.server_name};DATABASE={self.database_name};UID={self.username};PWD={self.password}"

    def connect(self):
        return pyodbc.connect(self.connection_string, timeout=5)

    def get_advertisement_videos_from_database(self):
        try:
            with self.connect() as conn, conn.cursor() as cursor:
                query = "SELECT AdvertisementVideoURL FROM AdvertisementVideos"
                cursor.execute(query)
                return [row.AdvertisementVideoURL for row in cursor.fetchall()]
        except Exception as e:
            logging.error(f"Error retrieving advertisement videos from the database: {e}")
            return []

    def validate_youtube_url(self, url):
        pattern = re.compile(r'^(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.*$')
        return pattern.match(url) is not None

    def download_and_convert_video(self, url, download_path):
        try:
            if not self.validate_youtube_url(url):
                logging.warning(f"Invalid YouTube video URL: {url}")
                return

            youtube_object = YouTube(url)
            video_stream = youtube_object.streams.filter(file_extension='mp4').get_highest_resolution()

            download_location = os.path.join(download_path, f"{video_stream.title}.mp4")

            if os.path.exists(download_location):
                logging.info(f"File already exists: {download_location}")
                return

            logging.info(f"Downloading: {video_stream.title}")
            video_stream.download(output_path=download_path, filename=f"{video_stream.title}.mp4")

            avi_file_path = os.path.join(download_path, f"{video_stream.title}.avi")

            clip = VideoFileClip(download_location)
            clip.write_videofile(avi_file_path, codec="libx264", audio_codec="aac")

            logging.info("Conversion to AVI completed successfully.")
            os.remove(download_location)
            logging.info(f"Removed: {download_location}")

        except Exception as e:
            logging.error(f"An error occurred during download and conversion: {e}")

class AdvertisementDownloader:
    def __init__(self):
        self.db_manager = DatabaseManager(db_server_name, db_name, db_username, db_password)

    def download_and_convert_videos_batch(self, video_urls, download_path):
        for url in video_urls:
            self.db_manager.download_and_convert_video(url, download_path)

    def start_download(self):
        logging.basicConfig(level=logging.INFO)
        
        # Specify the download location
        download_path = 'Assets'

        # Get the list of advertisement videos and download them in batches
        video_urls = self.db_manager.get_advertisement_videos_from_database()

        # Split the video URLs into batches (adjust the batch size as needed)
        batch_size = 5
        for i in range(0, len(video_urls), batch_size):
            batch_urls = video_urls[i:i + batch_size]
            self.download_and_convert_videos_batch(batch_urls, download_path)

if __name__ == "__main__":
    # Instantiate AdvertisementDownloader and start the download
    downloader = AdvertisementDownloader()
    downloader.start_download()
