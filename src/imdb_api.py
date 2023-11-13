import requests

# File to handle requests to the IMDb API

# imdb_api = IMDbAPI(api_key = "k_pmwcqsvy")
# reviews = imdb_api.get_movie_reviews(movie_id)

class IMDbAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url_1 = "https://imdb-api.com/en/API/Top250Movies/k_pmwcqsvy"
        # self.base_url_2 = "https://imdb-api.com/en/API/MostPopularMovies/k_pmwcqsvy"
        # self.base_url_3 = "https://imdb-api.com/en/API/ComingSoon/k_pmwcqsvy"

    def search_movie(self, query):
        endpoint = "/search/movie"
        params = {"api_key": self.api_key, "query": query}
        response = requests.get(f"{self.base_url_1}{endpoint}", params=params)
        return response.json()

    def get_movie_details(self, movie_id):
        endpoint = f"/movie/{movie_id}"
        params = {"api_key": self.api_key}
        response = requests.get(f"{self.base_url_1}{endpoint}", params=params)
        return response.json()
