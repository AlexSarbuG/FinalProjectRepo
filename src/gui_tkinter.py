import tkinter as tk
import tkinter.ttk as ttk
from PyProject import MovieRecommendationApp
from dpi import set_dpi_awareness
import requests
from io import BytesIO
from PIL import Image, ImageTk

set_dpi_awareness()
line_number = 0

class MovieRecommendationGUI:
    """Interfață grafică pentru aplicația de recomandare de filme."""
    def __init__(self, root, movie_app):
        """
        Inițializează interfața grafică.

        Parameters:
        - root (tk.Tk): Obiectul principal al ferestrei Tkinter.
        - movie_app (MovieRecommendationApp): Instanța aplicației de recomandare de filme.
        """
        self.root = root
        self.root.title("Movie Recommendation App")
        self.app = movie_app  # Adaugă instanța MovieRecommendationApp

        self.label = tk.Label(root, text="Search for a movie: ", background="lightyellow")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.search_button = tk.Button(root, text="Search for", command=self.search_movie)
        self.search_button.pack(padx=5, pady=5)

        self.recommendations_label = tk.Label(root, text="Recommendation: ", background="lightyellow")
        self.recommendations_label.pack()

        # Adaugă un frame pentru a grupa textul și bara de derulare in recommendations text
        frame_recommendations = ttk.Frame(root)
        frame_recommendations.pack()

        # Adaugă widget-ul Text pentru prima secțiune de recomandări
        self.recommendations_text = tk.Text(frame_recommendations, height=10, width=60, wrap=tk.WORD)
        self.recommendations_text.pack(side=tk.LEFT, fill=tk.Y)

        # Adaugă bara de derulare pentru recommendations text
        scrollbar_recommendations = ttk.Scrollbar(frame_recommendations, orient=tk.VERTICAL,
                                                  command=self.recommendations_text.yview)
        scrollbar_recommendations.pack(side=tk.RIGHT, fill=tk.Y)
        self.recommendations_text.config(yscrollcommand=scrollbar_recommendations.set)

        self.reviews_label = tk.Label(root, text="Reviews: ", background="lightyellow")
        self.reviews_label.pack()

        # Adaugă un alt widget Text pentru a doua secțiune de reviews text
        frame_second_reviews = ttk.Frame(root)
        frame_second_reviews.pack()

        self.second_reviews_text = tk.Text(frame_second_reviews, height=5, width=60, wrap=tk.WORD)
        self.second_reviews_text.pack(side=tk.LEFT, fill=tk.Y)

        # Adaugă bara de derulare pentru reviews text
        scrollbar_second_reviews = ttk.Scrollbar(frame_second_reviews, orient=tk.VERTICAL,
                                                 command=self.second_reviews_text.yview)
        scrollbar_second_reviews.pack(side=tk.RIGHT, fill=tk.Y)
        self.second_reviews_text.config(yscrollcommand=scrollbar_second_reviews.set)

        self.posters_label = tk.Label(root, text="Click here to see the picture: ", background="lightyellow")
        self.posters_label.pack()

        # Adaugă butonul pentru a obține poster-ul/imaginea filmului selectat
        self.get_posters_button = tk.Button(root, text="Get Image", command=self.get_posters)
        self.get_posters_button.pack(padx=5, pady=5)

        # Adaugă butonul pentru a obține trailer-ul
        self.get_trailer_button = tk.Button(root, text="Get Trailer", command=self.get_trailer)
        self.get_trailer_button.pack(padx=5, pady=5)

        # Adaugă un nou frame pentru widget-ul Text cu link-ul trailer-ului
        frame_trailer = ttk.Frame(root)
        frame_trailer.pack()

        # Adaugă widget-ul Text pentru link-ul trailer-ului
        self.trailer_text = tk.Text(frame_trailer, height=1, width=60, wrap=tk.WORD)
        self.trailer_text.pack(side=tk.LEFT, fill=tk.Y)

        # Adaugă eveniment pentru selectarea textului în recommendations_text
        self.recommendations_text.bind("<ButtonRelease-1>", self.select_recommendation)

    def select_recommendation(self, event):
        """
        Afiseaza review-urile asociate recomandării selectate.

        Parameters:
        - event: Evenimentul declanșat de către utilizator.
        """
        # Obține poziția clicului în text
        index = self.recommendations_text.index(tk.CURRENT)

        # Obține numărul liniei la care s-a făcut clic
        global line_number
        line_number = int(index.split(".")[0])

        # Obține textul recomandării la linia respectivă
        selected_recommendation = self.recommendations_text.get(f"{line_number}.0", f"{line_number + 1}.0").strip()

        # Afiseaza review-urile asociate in second_reviews_text
        self.display_reviews_for_recommendation(selected_recommendation.strip())

        # Obține ID-ul filmului pentru titlul recomandării date
        movie_id = self.get_movie_id_for_recommendation(selected_recommendation)

        # Obține link-ul trailer-ului pentru filmul selectat
        trailer = self.app.get_movie_trailer(movie_id)

    def display_reviews_for_recommendation(self, selected_recommendation):
        """
        Afișează revizuirile pentru filmul selectat.

        Parameters:
        - selected_recommendation (str): Titlul recomandării selectate.
        """
        if selected_recommendation:
            # Obține revizuirile pentru filmul selectat
            movie_id = self.get_movie_id_for_recommendation(selected_recommendation)
            reviews = self.app.get_movie_reviews(movie_id)

            # Afișează revizuirile în second_reviews_text
            self.second_reviews_text.delete(1.0, tk.END)
            if reviews and "items" in reviews:
                for review in reviews["items"]:
                    self.second_reviews_text.insert(tk.END, review["title"] + "\n")
            else:
                self.second_reviews_text.insert(tk.END, "No reviews available.")

    def get_movie_id_for_recommendation(self, recommendation_title):
        """
        Obține ID-ul filmului pentru titlul recomandării date.

        Parameters:
        - recommendation_title (str): Titlul recomandării.

        Returns:
        - str or None: ID-ul filmului sau None dacă nu a fost găsit.
        """
        # Obține ID-ul filmului pentru titlul recomandării date
        search_result = self.app.search_movie(recommendation_title)
        if search_result and "results" in search_result and search_result["results"]:
            return search_result["results"][0]["id"]
        return None

    def search_movie(self):
        """
        Caută un film pe baza textului introdus de utilizator.
        """
        query = self.entry.get()
        search_result = self.app.search_movie(query)  # Apelează funcția din MovieRecommendationApp
        secondtext = ''

        if search_result and "results" in search_result and search_result["results"]:
            for movie in search_result["results"]:
                movie_id = movie["id"]

                movietitle = movie["title"]
                reviews = self.app.get_movie_reviews(movie_id)

                if reviews and "items" in reviews:
                    # Șterge conținutul secțiunii a doua
                    self.second_reviews_text.delete(1.0, tk.END)

                    # Adaugă review-urile în secțiunea a doua
                    secondtext += movietitle + "\n"

                    # Șterge conținutul secțiunii de recomandări
                    self.recommendations_text.delete(1.0, tk.END)
                    # self.recommendations_text.insert(tk.END, "No recommendations available.")
                else:
                    # Șterge conținutul secțiunii a doua
                    self.second_reviews_text.delete(1.0, tk.END)
                    self.second_reviews_text.insert(tk.END, "No reviews available.")

                    # Șterge conținutul secțiunii de recomandări
                    self.recommendations_text.delete(1.0, tk.END)
            else:
                # Șterge conținutul secțiunii a doua
                self.second_reviews_text.delete(1.0, tk.END)
                self.second_reviews_text.insert(tk.END, "Search request failed.")

                # Șterge conținutul secțiunii de recomandări
                self.recommendations_text.delete(1.0, tk.END)
            self.recommendations_text.insert(tk.END, secondtext)

    def get_recommendations(self):
        query = self.entry.get()
        search_result = self.app.search_movie(query)

        if search_result and "results" in search_result and search_result["results"]:
            # Șterge conținutul secțiunii de recomandări
            self.recommendations_text.delete(1.0, tk.END)

            for movie in search_result["results"]:
                movie_id = movie["id"]
                recommendations = self.app.get_movie_recommendations(movie_id)

                if recommendations and "items" in recommendations:
                    for recommendation in recommendations["items"]:
                        # Adaugă fiecare recomandare pe un rând nou în self.recommendations_text
                        self.recommendations_text.insert(tk.END, recommendation["title"] + "\n")

            # Șterge conținutul secțiunii a doua
            self.second_reviews_text.delete(1.0, tk.END)
            self.second_reviews_text.insert(tk.END, "No additional info available.\n")
        else:
            # Șterge conținutul secțiunii a doua
            self.second_reviews_text.delete(1.0, tk.END)
            self.second_reviews_text.insert(tk.END, "No results found for your search.")

            # Șterge conținutul secțiunii de recomandări
            self.recommendations_text.delete(1.0, tk.END)

    def get_reviews(self):
        query = self.entry.get()
        search_result = self.app.search_movie(query)

        if search_result and "results" in search_result and search_result["results"]:
            first_movie = search_result["results"][0]
            movie_id = first_movie["id"]
            reviews = self.app.get_movie_reviews(movie_id)

            if reviews and "items" in reviews:
                # Șterge conținutul secțiunii a doua
                self.second_reviews_text.delete(1.0, tk.END)

                for recommendation in reviews["items"]:
                    # Adaugă review-urile în secțiunea a doua
                    self.second_reviews_text.insert(tk.END, recommendation["title"] + "\n")

                # Șterge conținutul secțiunii de recomandări
                self.recommendations_text.delete(1.0, tk.END)
                self.recommendations_text.insert(tk.END, "No recommendations available.")
            else:
                # Șterge conținutul secțiunii a doua
                self.second_reviews_text.delete(1.0, tk.END)
                self.second_reviews_text.insert(tk.END, "No reviews available.")

                # Șterge conținutul secțiunii de recomandări
                self.recommendations_text.delete(1.0, tk.END)
        else:
            # Șterge conținutul secțiunii a doua
            self.second_reviews_text.delete(1.0, tk.END)
            self.second_reviews_text.insert(tk.END, "Search request failed.")

            # Șterge conținutul secțiunii de recomandări
            self.recommendations_text.delete(1.0, tk.END)

    def show_poster_popup(self, poster_url):
        # Creează o nouă fereastră pentru afișarea imaginii
        popup = tk.Toplevel(self.root)
        popup.title("Movie Poster")

        # Folosește un Label pentru a afișa imaginea
        poster_label = tk.Label(popup)
        poster_label.pack(padx=10, pady=10)

        # Descarcă imaginea și afișeaz-o în Label
        response = requests.get(poster_url)
        if response.status_code == 200:
            image_data = response.content

            # Deschide imaginea folosind PIL
            image = Image.open(BytesIO(image_data))

            # Redimensionează imaginea la o dimensiune fixă
            new_width, new_height = 800, 1200
            image = image.resize((new_width, new_height))

            # Convertște imaginea la formatul acceptat de Tkinter
            photo = ImageTk.PhotoImage(image)

            # Afișează imaginea în Label
            poster_label.config(image=photo)
            poster_label.image = photo
        else:
            poster_label.config(text="No poster available.")

        # Buton pentru închiderea popup-ului
        close_button = tk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack(pady=10)

    def get_posters(self):
        query = self.entry.get()
        search_result = self.app.search_movie(query)

        if line_number != 0:  # Verifică dacă line_number este diferit de zero
            list = search_result["results"]
            for i in range(1, len(list) + 1):
                if i == line_number:
                    movie = list[i - 1]
                    imagelink = movie["image"]

                    # Afiseaza pop-up cu imaginea
                    self.show_poster_popup(imagelink)
                    return
        else:
            print("Select a movie recommendation first.")

    def get_trailer(self):
        query = self.entry.get()
        search_result = self.app.search_movie(query)

        if search_result and "results" in search_result and search_result["results"]:
            list_1 = search_result["results"]
            for i in range(1, len(list_1) + 1):
                if i == line_number:
                    movie = list_1[i - 1]
                    movie_id = movie["id"]
                    trailer = self.app.get_movie_trailer(movie_id)

                    if trailer and "link" in trailer:
                        # Șterge conținutul din trailer_text
                        self.trailer_text.delete(1.0, tk.END)

                        # Adaugă link-ul în trailer_text
                        self.trailer_text.insert(tk.END, "Movie trailer: " + trailer["link"] + "\n")
                        break

                    else:
                        # Șterge conținutul din trailer_text
                        self.trailer_text.delete(1.0, tk.END)
                        self.trailer_text.insert(tk.END, "No trailer available.")
        else:
            # Șterge conținutul din trailer_text
            self.trailer_text.delete(1.0, tk.END)
            self.trailer_text.insert(tk.END, "No results found for your search.")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Movie Recommendation App")

    # Crează instanța MovieRecommendationApp
    movie_app = MovieRecommendationApp()

    # Pasează instanța către MovieRecommendationGUI
    app = MovieRecommendationGUI(root, movie_app)

    # Setează dimensiunile ferestrei în funcție de conținut
    width = max(1500, app.recommendations_text.winfo_reqwidth() + 20)  # Ajustează la o lățime minimă de 1000
    height = max(1200, app.recommendations_text.winfo_reqheight() + 20)  # Ajustează la o înălțime minimă de 600

    root.geometry(f"{width}x{height}")
    root.resizable(True, True)
    root.config(background="lightyellow")
    root.iconbitmap("src/gui_images/Movies.ico")

    root.mainloop()
