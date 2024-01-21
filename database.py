import sqlite3
import scrape

db, cur = None, None

# DO NOT CALL MORE THAN ONCE
def __intialize_db():
    global db, cur
    db = sqlite3.connect("movies.db")

    cur = db.cursor()

    cur.execute("CREATE TABLE movies( "
        "id string NOT NULL, "
        "image1 string, "
        "image2 string, "
        "director string, "
        "genres string, "
        "acquisition string, "
        "camera_model string, "
        "film_stock string, "
        "film_width string, "
        "color string, "
        "aspect_ratio string, "
        "primary KEY (ID))")


# DESTROYS THE DATABASE
def __nuke_db():
    cur.execute("DROP TABLE movies")


def __start_db():
    global db, cur

    db = sqlite3.connect("movies.db")

    cur = db.cursor()
    
def search_movie(movie_title: str):
    movie_data = scrape.search_movie_title(movie_title)
    movieID, movie_object = movie_data[0], movie_data[1]
    result = cur.execute(f"SELECT * FROM movies WHERE id = {movieID}").fetchone()

    # if movie is in the DB return the movie
    if result:
        return result

    # otherwise scrape the movie data and add result to database
    item_dict = scrape.scrape_movie(movie_object)

    column_str, value_str = "id", movieID

    for col, val in item_dict.items():
        column_str += ", " + col.strip()

        value_str += ", '" + val.strip() + "'"

    sql_query = f"INSERT INTO movies ({column_str}) VALUES ({value_str})"

    cur.execute(sql_query)
    db.commit()

    return search_movie(movie_title)

__start_db()
