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

    images = ''
    if 'http' in items_list[0]:
        if 'http' in items_list[1]:
            images = items_list[0] + ' ' + items_list[1] + ' '
            items_list = items_list[2:]
        else:
            images = items_list[0] + ' '
            items_list = items_list[1:]


    ret = ' '.join([images, context, movie, (', '.join(parsed_movie))])
    
    ret += ' --raw'

    return ret 



movie_title = input("Enter prompt: ")
print(create_query(movie_title))

