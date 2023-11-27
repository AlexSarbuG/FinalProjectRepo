import requests
from enum import Enum, auto


class AdvancedSearchGenre(Enum):
    """Enumerație pentru genurile de filme în căutarea avansată."""
    Action = auto()
    Adventure = auto()
    Animation = auto()
    Biography = auto()
    Comedy = auto()
    Crime = auto()
    Documentary = auto()
    Drama = auto()
    Family = auto()
    Fantasy = auto()
    Film_Noir = auto()
    Game_Show = auto()
    History = auto()
    Horror = auto()
    Music = auto()
    Musical = auto()
    Mystery = auto()
    News = auto()
    Reality_TV = auto()
    Romance = auto()
    Sci_Fi = auto()
    Sport = auto()
    Talk_Show = auto()
    Thriller = auto()
    War = auto()
    Western = auto()


class MovieRecommendationApp:
    """Clasă pentru aplicația de recomandare a filmelor."""

    def __init__(self):
        """Inițializează instanța aplicației cu cheia API și URL-ul de bază."""
        self.api_key = "k_pmwcqsvy"
        self.base_url = "https://imdb-api.com/en"

    def search_movie(self, query):
        """
        Caută un film în baza de date IMDB.

        Parameters:
        - query (str): Cuvântul cheie pentru căutarea filmului.

        Returns:
        - dict or None: Dicționarul cu rezultatele căutării sau None în caz de eroare.
        """
        endpoint = f"/API/SearchMovie/{self.api_key}/{query}/"

        try:
            response = requests.get(f"{self.base_url}{endpoint}")
            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the request: {e}")
            return None

        else:
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Received a non-200 status code: {response.status_code}")
                return None

    def get_movie_recommendations(self, movie_id):
        """
        Obține recomandările pentru un film pe baza ID-ului filmului.

        Parameters:
        - movie_id (str): ID-ul unic al filmului.

        Returns:
        - dict: Dicționarul cu recomandările sau o listă goală dacă nu există recomandări.
        """
        # Obține detalii despre filmul curent
        current_movie_info = self.search_movie_details(movie_id)
        if current_movie_info is None or "genres" not in current_movie_info:
            return {"items": []}  # În lipsa informațiilor necesare, returnează o listă goală

        # Extrage genurile filmului curent
        current_genres = current_movie_info["genres"]
        print(f"Current genres: {current_genres}")  # Adăugat print aici

        # Caută alte filme cu genuri similare
        similar_movies = self.search_movies_by_genres(current_genres)
        print(f"Similar movies: {similar_movies}")  # Adăugat print aici

        # Formatează rezultatele în formatul așteptat
        recommendations = [{"title": movie["title"], "additional_info": f"Genres: {', '.join(movie['genres'])}"} for
                           movie in similar_movies]

        return {"items": recommendations}

    def search_movie_details(self, movie_id):
        """
        Caută detaliile unui film pe baza ID-ului filmului.

        Parameters:
        - movie_id (str): ID-ul unic al filmului.

        Returns:
        - dict or None: Dicționarul cu detaliile filmului sau None în caz de eroare.
        """
        endpoint = f"/API/Title/{self.api_key}/{movie_id}/"

        try:
            response = requests.get(f"{self.base_url}{endpoint}")
            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the request: {e}")
            return None

        else:
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Received a non-200 status code: {response.status_code}")
                return None

    def search_movies_by_genres(self, genres):
        """
        Caută filme cu genuri similare pe baza unei liste de genuri.

        Parameters:
        - genres (list): Lista de genuri (enum-uri AdvancedSearchGenre).

        Returns:
        - list: Lista cu filmele găsite sau o listă goală dacă nu sunt găsite filme similare.
        """
        # Transformă enum-urile în șiruri pentru a le utiliza în URL
        genres_str = ",".join(genre.name.lower() for genre in genres)

        # Construiește URL-ul pentru căutare avansată bazată pe genuri
        endpoint = f"/API/AdvancedSearch/{self.api_key}/?genres={genres_str}&limit=5"

        try:
            response = requests.get(f"{self.base_url}{endpoint}")
            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the request: {e}")
            return []

        else:
            if response.status_code == 200:
                search_results = response.json().get("results", [])
                print(f"Search results: {search_results}")  # Adăugat print aici pentru verificarea codului
                return search_results
            else:
                print(f"Received a non-200 status code: {response.status_code}")
                return []

    def get_movie_reviews(self, movie_id):
        """
        Obține recenziile pentru un film pe baza ID-ului filmului.

        Parameters:
        - movie_id (str): ID-ul unic al filmului.

        Returns:
        - dict or None: Dicționarul cu recenziile sau None în caz de eroare.
        """
        endpoint = f"/API/Reviews/{self.api_key}/{movie_id}/"

        try:
            response = requests.get(f"{self.base_url}{endpoint}")
            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the request: {e}")
            return None

        else:
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Received a non-200 status code: {response.status_code}")
                return None

    def get_movie_posters(self, movie_id):
        """
        Obține posterele pentru un film pe baza ID-ului filmului.

        Parameters:
        - movie_id (str): ID-ul unic al filmului.

        Returns:
        - dict or None: Dicționarul cu link-uri către postere sau None în caz de eroare.
        """
        endpoint = f"/API/Images/{self.api_key}/{movie_id}/"

        try:
            response = requests.get(f"{self.base_url}{endpoint}")
            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the request: {e}")
            return None

        else:
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Received a non-200 status code: {response.status_code}")
                return None

    def get_movie_trailer(self, movie_id):
        """
        Obține trailer-ul pentru un film pe baza ID-ului filmului.

        Parameters:
        - movie_id (str): ID-ul unic al filmului.

        Returns:
        - dict or None: Dicționarul cu link-ul trailer-ului sau None în caz de eroare.
        """
        endpoint = f"/API/Trailer/{self.api_key}/{movie_id}/"

        try:
            response = requests.get(f"{self.base_url}{endpoint}")
            response.raise_for_status()

        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the request: {e}")
            return None

        else:
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Received a non-200 status code: {response.status_code}")
                return None


if __name__ == "__main__":
    app = MovieRecommendationApp()
    movie_search_result = app.search_movie("fast")

    # Creați o listă de enum-uri AdvancedSearchGenre
    genres_to_search = [AdvancedSearchGenre.Action, AdvancedSearchGenre.Adventure]

    # Apelați funcția search_movies_by_genres cu lista de enum-uri
    similar_movies = app.search_movies_by_genres(genres_to_search)

    # Utilizează similar_movies cum dorești
    if similar_movies:
        print("Similar movies:")
        for movie in similar_movies:
            print(f"Title: {movie['title']}, Genres: {', '.join(movie['genres'])}")
    else:
        print("No similar movies found.")

    if movie_search_result is not None:
        if "results" in movie_search_result and movie_search_result["results"]:
            first_movie = movie_search_result["results"][0]
            movie_id = first_movie["id"]

            # Obțineți recomandări pentru film
            recommendations = app.get_movie_recommendations(movie_id)
            if recommendations is not None and "items" in recommendations:
                print(f"Movie recommendations for '{first_movie['title']}':")
                for recommendation in recommendations["items"]:
                    print(f"{recommendation['title']}: {recommendation['additional_info']}")
            else:
                print("Failed to get movie recommendations.")

            # Obțineți posterul pentru film
            posters = app.get_movie_posters(movie_id)
            if posters is not None:
                print("Movie posters:")
                for poster in posters.get("items", []):
                    print(poster["link"])
            else:
                print("Failed to get movie posters.")

            # Obțineți trailerul pentru film
            trailer = app.get_movie_trailer(movie_id)
            if trailer is not None:
                print("Movie trailer:")
                print(trailer.get("link", "No trailer link available"))
            else:
                print("Failed to get movie trailer.")

        else:
            print("No results found for your search.")
    else:
        print("Search request failed.")
