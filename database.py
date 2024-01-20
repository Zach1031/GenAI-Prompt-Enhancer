import sqlite3
import scrape

db, cur = None, None

# DO NOT CALL MORE THAN ONCE
def __intialize_db():
    global db, cur
    db = sqlite3.connect("movies.db")

    cur = db.cursor()

    cur.execute("CREATE TABLE movies( "
        "ID string NOT NULL, "
        "DIRECTOR string, "
        "GENRES string, "
        "ACQUISITION string, "
        "CAMERA_MODEL string, "
        "FILM_STOCK string, "
        "FILM_WIDTH string, "
        "ASPECT_RATIO string, "
        "COLOR string, "
        "IMAGE1 string, "
        "IMAGE2 string, "
        "PRIMARY KEY (ID))")

def __start_db():
    global db, cur

    db = sqlite3.connect("movies.db")

    cur = db.cursor()


def search_movie(movie_title: str):
    movieID = scrape.search_movie_title(movie_title)
    result = cur.execute(f"SELECT * FROM movies WHERE ID = {movieID}").fetchone()

    return result

__start_db()

movie_title = input("Enter movie title: ")

search_movie(movie_title)
