# Sp0tify LG LyricsGenius API

Sp0tify LG wraps LyricsGenius into a user-friendly REST-API that simplifies the process of accessing song, artist, album, and lyrics data from Genius.com. This integration bridges the gap between the Genius website and developers who want to programmatically access valuable music-related information.

## Key Features and Functionalities

The REST-API offers a range of functionalities that enable users to interact with Genius.com's data conveniently and efficiently. The API provides endpoints to perform the following actions:

1. **Search:** Easily search for albums, artists, songs, lyrics, and videos on Genius.com. This empowers developers to quickly retrieve relevant content.

2. **Song Details:** Retrieve detailed information about songs, including song activity, annotations, and comments from Genius.com. This allows for deeper insights into the context of songs.

3. **Artist Insights:** Access comprehensive artist information, albums, and songs associated with a specific artist. This aids in building comprehensive profiles of artists.

4. **Album Data:** Retrieve album details, cover arts, and tracks, facilitating exploration of an artist's discography.

5. **Lyrics Extraction:** Utilize BeautifulSoup4 to obtain song lyrics, enhancing the value of the API by providing access to the core content of songs.

6. **Video Search:** Search for videos related to an album, enriching the user experience with multimedia content.

7. **Genius.com Charts:** Get access to charts available on Genius.com, providing insights into trending songs and artists.

## Authentication and Access

To ensure secure and authorized access to the Sp0tify LG REST-API, users are required to follow these steps:

1. **Obtain Deta Space API Key:**
   - Install the Sp0tify LG app on your Deta Space.
   - Create an API key specific to the app within your Deta Space account.
   - This generated Deta Space API Key needs to be included in the header of your API requests as "X-Space-App-Key."

2. **Genius Client API Key:**
   - Create an API client in the Genius API by visiting [Genius API Clients](https://genius.com/api-clients).
   - Once the API client is created, you will be provided with a Genius client API key.
   - Store this Genius client API key as an environment variable named "NEXT_PUBLIC_GENIUS_ACCESS_TOKEN."

By combining the Deta Space API Key for Deta Space authentication and the Genius client API key for Genius.com authorization, users can securely access the REST-API's functionalities and retrieve music-related data seamlessly.

## Data Formats and Accuracy

The data formats returned by the API align closely with what the LyricsGenius Python package provides. The data is sourced either directly from the Genius API or via web scraping from the Genius.com website. This approach ensures accuracy and reliability of the information provided.

## Documentation and Usage

For developers interested in leveraging the capabilities of the Sp0tify LG REST-API, comprehensive documentation is available at [Sp0tify LG Documentation](https://sp0tifylg-1-k4999508.deta.app/docs). This documentation provides detailed guidance on how to use the API effectively, including information on endpoints, authentication, data formats, and examples of usage scenarios.

**GitHub Repository:** [Link to GitHub Repository](https://github.com/lonewanderer27/sp0tify-lg)

Feel free to contribute to the project and make the most of this powerful integration of LyricsGenius into a REST-API.

---
