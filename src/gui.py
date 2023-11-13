import tkinter as tk
import tkinter.ttk as ttk
from PyProject import MovieRecommendationApp

from dpi import set_dpi_awareness

set_dpi_awareness()

class MovieRecommendationGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Movie Recommendation App")

        self.app = MovieRecommendationApp()

        self.label = tk.Label(root, text="Search for a movie: ")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.search_button = tk.Button(root, text="Search for", command=self.search_movie)
        self.search_button.pack()

        self.recommendations_label = tk.Label(root, text="Recommendation: ")
        self.recommendations_label.pack()

        self.recommendations_text = tk.Text(root, height=10, width=40)
        self.recommendations_text.pack()

    def search_movie(self):
        query = self.entry.get()
        # Apeleaza functia de cautare a filmelor din `PyProject.py`
        search_result = self.app.search_movie(query)
        print("###", search_result)

        if search_result:
            if "results" in search_result and search_result["results"]:
                first_movie = search_result["results"][0]
                movie_id = first_movie["id"]
                recommendations = self.app.get_movie_recommendations(movie_id)

                if recommendations and "items" in recommendations:
                    self.recommendations_text.delete(1.0, tk.END)  # Sterge textul anterior din recommendations_text
                    for recommendation in recommendations["items"]:
                        self.recommendations_text.insert(tk.END, recommendation["title"] + "\n")
                else:
                    self.recommendations_text.delete(1.0, tk.END)
                    self.recommendations_text.insert(tk.END, "No recommendations available.")
            else:
                self.recommendations_text.delete(1.0, tk.END)
                self.recommendations_text.insert(tk.END, "No results found for your search.")
        else:
            self.recommendations_text.delete(1.0, tk.END)
            self.recommendations_text.insert(tk.END, "Search request failed.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x600")
    root.resizable(True, True)
    root.iconbitmap("src/gui_images/Movies.ico")  # Icon image
    app = MovieRecommendationGUI(root)
    root.mainloop()