import os
from pytube import YouTube
import re
import pyodbc
from config import db_server_name, db_name, db_username, db_password
from moviepy.editor import VideoFileClip

class DatabaseManager:
    # Database Initializations
    def __init__(self, server_name, database_name, username, password):
        self.server_name = server_name
        self.database_name = database_name
        self.username = username
        self.password = password
        self.conn = self.connect()
        self.cursor = self.conn.cursor()  

    # Database Connection
    def connect(self):
        driver_name = 'ODBC Driver 17 for SQL Server'
        connection_string = f"DRIVER={{{driver_name}}};SERVER={self.server_name};DATABASE={self.database_name};UID={self.username};PWD={self.password}"

        try:
            with pyodbc.connect(connection_string, timeout=5) as conn:
                return conn
        except pyodbc.OperationalError as e:
            print(f"Error connecting to the database: {e}")
            raise

    def getAdvertisementVideosFromDatabase(self):
        videos = []
        try:
            with self.conn.cursor() as cursor:
                query = """
                    SELECT AdvertisementVideoURL
                    FROM AdvertisementVideos
                """
                cursor.execute(query)
                videos = [row.AdvertisementVideoURL for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error retrieving advertisement videos from database: {e}")
        return videos
        
    def validate_youtube_url(self, url):
        pattern = re.compile(r'^(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.*$')
        return pattern.match(url) is not None

    def download_and_convert_videos(self, download_path):
        video_urls = self.getAdvertisementVideosFromDatabase()

        for url in video_urls:
            if not self.validate_youtube_url(url):
                print(f"Invalid YouTube video URL: {url}")
                continue

            try:
                youtube_object = YouTube(url)
                video_stream = youtube_object.streams.get_highest_resolution()

                # Set the download location
                download_location = os.path.join(download_path, f"{video_stream.title}.mp4")

                # Check if the file already exists in the download path
                if os.path.exists(download_location):
                    print(f"File already exists: {download_location}")
                    continue

                print(f"Downloading: {video_stream.title}")
                video_stream.download(output_path=download_path, filename=f"{video_stream.title}.mp4")

                avi_file_path = os.path.join(download_path, f"{video_stream.title}.avi")

                # Convert the downloaded MP4 file to AVI using moviepy with a different codec
                clip = VideoFileClip(download_location)
                clip.write_videofile(avi_file_path, codec="libx264", audio_codec="aac")

                print("Conversion to AVI completed successfully.")

                # Remove the downloaded MP4 file
                os.remove(download_location)
                print(f"Removed: {download_location}")

            except Exception as e:
                print(f"An error occurred during download and conversion: {e}")

# Specify the download location
# download_path = 'C:\\Users\\orqui\\OneDrive\\Documents\\GitHub\\imaiTablet\\Assets'
download_path = 'Assets'

# Create an instance of DatabaseManager
db_manager = DatabaseManager(
    server_name=db_server_name,
    database_name=db_name,
    username=db_username,
    password=db_password, 
)

# Get the list of advertisement videos and download it
db_manager.download_and_convert_videos(download_path)

