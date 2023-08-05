from lyricsgenius import Genius
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Genius API access key
access_token = os.getenv("NEXT_PUBLIC_GENIUS_ACCESS_TOKEN")

# Create Genius object
genius = Genius(access_token)
