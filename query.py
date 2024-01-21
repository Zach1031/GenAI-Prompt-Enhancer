import database
import scrape

def split_query(query: str) -> [str]:
    q_arr = query.split(' ')

    left, right = [], []
    found = False

    for word in q_arr:
        if not found:
            left.append(word)
            if word == 'in':
                found = True
        
        else:
            right.append(word)
    
    return (left, right)

def create_query(query: str) -> str:
    q_arr_tup = split_query(query)
    context, movie = ' '.join(q_arr_tup[0]), ' '.join(q_arr_tup[1])

    items_list = list(database.search_movie(movie))[1:] 

    if not items_list: 
        return "it's over"

    parsed_movie = [val for val in items_list if val is not None]

    year = parsed_movie[0]
    parsed_movie = parsed_movie[1:]

    images = ''
    if 'http' in parsed_movie[0]:
        if 'http' in parsed_movie[1]:
            images = parsed_movie[0] + ' ' + parsed_movie[1] + ' '
            parsed_movie = parsed_movie[2:]
        else:
            images = parsed_movie[0] + ' '
            parsed_movie = parsed_movie[1:]


    ret = ' '.join(['film still,', images, context, movie, year + ',', (', '.join(parsed_movie))])
    
    ret += ' --style raw' + ' --stylize 0'

    return ret 



#movie_title = input("Enter prompt: ")
#print(create_query(movie_title))

