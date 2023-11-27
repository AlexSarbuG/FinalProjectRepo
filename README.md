# Movie Recommendation App Documentation

## Project Title: Movie Recommendation App
## Description:
#### The Movie Recommendation App is designed to recommend movies based on a user's search query (e.g., "fast," "godfather"). Upon selecting a result, the app displays the movie's reviews (if available), its image, and a link to the image. Additionally, the app can provide a link to the movie trailer, which can be copied and pasted into a browser.

## Installation Instructions:
#### Dependencies do not need to be installed separately, as the project uses Poetry as a virtual environment, and all dependencies are listed in "pyproject.toml."

## Project Structure:
#### The project is organized into a "src" folder containing various files:
### 1. gui_images: 
#### Holds images used in the application interface.
### 2. dpi.py: 
#### Contains a function preventing the application from flickering on Windows 10.
### 3. PyProject.py: 
#### Contains the source code of the application, with two classes:
### 3.1. MovieRecommendationApp:
#### Includes functions and methods to extract and process necessary data for the application.
### 3.2. AdvancedSearchGenre (Enum):
#### Added to address display issues, recommending movies based on the genre of the searched movie.
### 4. gui.py:
#### Includes all functions and methods necessary for the graphical user interface.

## Usage Examples:
#### 1. In the "Search for a movie" field, enter the name of a movie or a keyword from the movie's title.
#### 2. Click the "Search for" button to display recommendations.
#### 3. To view reviews, click on a title in the recommendations.
#### 4. To view the movie's image, click the "Get Image" button, which displays the image in a popup and provides a link to the image in a text widget.
#### 5. The app also offers a "Get Trailer" button, which, when clicked, displays the link to the selected movie's trailer in the corresponding text widget.

## API Documentation:
#### The application calls multiple APIs, including:
### 1. SearchMovie API:
#### 1.1. Endpoint: (https://imdb-api.com/en/API/SearchMovie/{self.api_key}/{query}/)
#### 1.2. Purpose: Searches for movies based on the entered query.
### 2. Title API:
#### 2.1. Endpoint: (https://imdb-api.com/en/API/Title/{self.api_key}/{movie_id}/)
#### 2.2. Purpose: Searches all available titles for the movie ID, necessary for other functions.
### 3. AdvancedSearch API:
#### 3.1. Endpoint: (https://imdb-api.com/en/API/AdvancedSearch/{self.api_key}/?genres={genres_str}&limit=5)
#### 3.2. Purpose: Aids in recommending other movies with similar genres to the searched movie.
### 4. Reviews API:
#### 4.1. Endpoint: (https://imdb-api.com/en/API/Reviews/{self.api_key}/{movie_id}/)
#### 4.2. Purpose: Used to extract data for displaying reviews of the searched movies based on their IDs.
### 5. Images API:
#### 5.1. Endpoint: (https://imdb-api.com/en/API/Images/{self.api_key}/{movie_id}/)
#### 5.2. Purpose: Extracts data for displaying relevant images of the selected movie.
### 6. Trailer API:
#### 6.1. Endpoint: (https://imdb-api.com/en/API/Trailer/{self.api_key}/{movie_id}/)
#### 6.2. Purpose: Necessary for extracting data and display the link for the movie's trailer.

## License:
##### MIT License

##### Copyright (c) 2023

###### Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

###### The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

###### THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Code Samples:
### 1. MovieRecommendationApp Code:
#### (... The existing MovieRecommendationApp class ...)
### 2. MovieRecommendationGUI Code:
#### # (... The existing MovieRecommendationGUI class ...)

## Execution:
#### Run the application by executing the following script:
![Screenshot 2023-11-26 172537.png](src%2Fgui_images%2FScreenshot%202023-11-26%20172537.png)



## Process Flow diagram: 
![Process Flow diagram_4.jpg](src%2Fgui_images%2FProcess%20Flow%20diagram_4.jpg)


## Architecture diagram
![Architecture_diagram_0.jpg](src%2Fgui_images%2FArchitecture_diagram_0.jpg)