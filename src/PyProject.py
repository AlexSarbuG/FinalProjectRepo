import requests

class MovieRecommendationApp:
    def __init__(self):
        self.api_key = "k_pmwcqsvy"
        self.base_url = "https://imdb-api.com/en"  # Trebuie schimbat linkul, pentru a putea implementa restul functiilor

    def search_movie(self, query):  # Functionalitatea de cautare a filmelor in API-ul IMDb
        # Utilizeaza requests pentru a face cererea API
        endpoint = "/API/SearchMovie/" + self.api_key + "/" + query + "/"

        try:
            response = requests.get(f"{self.base_url}{endpoint}")
            response.raise_for_status()  # Ridica o exceptie daca cererea a esuat
            print(response.request.url)

        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the request: {e}")
            return None

        else:
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Recived a non-200 status code: {response.status_code}")
                return None

        finally:
            pass

    def get_movie_recommendations(self, movie_id):  # Functionalitatea de obtinere a recomandarilor pentru un film dat
        endpoint = f"/API/Recommendations/{movie_id}"
        params = {"api_key": self.api_key}

        try:
            response = requests.get(f"{self.base_url}{endpoint}", params=params)
            response.raise_for_status()  # Ridica o exceptie daca cererea a esuat

        except requests.exceptions.RequestException as e:
            print(f"An error occurred during the request: {e}")
            return None

        else:
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Recived a non-200 status code: {response.status_code}")
                return None

        finally:
            pass

if __name__ == "__main__":
    app = MovieRecommendationApp()
    # Exemplu de utilizare pentru a cauta un film si obtine recomandari pentru el
    movie_search_result = app.search_movie("fast")

    if movie_search_result is not None:
        if "results" in movie_search_result and movie_search_result["results"]:
            first_movie = movie_search_result["results"][0]
            movie_id = first_movie["id"]
            recommendations = app.get_movie_recommendations(movie_id)
            if recommendations is not None:
                print(f"Movie recommendations '{first_movie['title']}':")
                for recommendation in recommendations.get("items", []):
                    print(recommendation["title"])
            else:
                print("Failed to get movie recommendations.")
        else:
            print("No results found for your search.")
    else:
        print("Search request failed.")
