import requests as req, os, datetime, json, csv

# kobis_key = os.environ['KOBIS_API_KEY']
naver_id = 'P4D9WCjnpxnNOYvqBtLY'
naver_secret = '_zqTHn7XH5'

def naver_movie_details():
    url = f"https://openapi.naver.com/v1/search/movie.json?query="
    headers = {
        'X-Naver-Client-Id': naver_id,
        'X-Naver-Client-Secret': naver_secret
    }
    movie = []
    movie_name = __get_file_column_datas('movie.csv', 'movie_name')
    time = __get_file_column_datas('movie.csv', 'time')
    year = __get_file_column_datas('movie.csv', 'year')
    nation = __get_file_column_datas('movie.csv', 'nation')
    director = __get_file_column_datas('movie.csv', 'director')
    company = __get_file_column_datas('movie.csv', 'company')
    grade = __get_file_column_datas('movie.csv', 'grade')
    genre1 = __get_file_column_datas('movie.csv', 'genre1')
    genre2 = __get_file_column_datas('movie.csv', 'genre2')
    genre3 = __get_file_column_datas('movie.csv', 'genre3')
    actor1 = __get_file_column_datas('movie.csv', 'actor1')
    actor2 = __get_file_column_datas('movie.csv', 'actor2')
    actor3 = __get_file_column_datas('movie.csv', 'actor3')
    datas = list(zip(movie_name,time,year,nation,director,company,grade,genre1,genre2,genre3,actor1,actor2,actor3))
    for data in datas:        
        movie_data = req.get(url + data[0], headers=headers).json()
        print(movie_data)
        save_data = {
            'movie_name': data[0],
            'time': data[1],
            'year': data[2],
            'nation': data[3],
            'director': data[4],
            'company': data[5],
            'grade': data[6],
            'genre1': data[7],
            'genre2': data[8],
            'genre3': data[9],
            'actor1': data[10],
            'actor2': data[11],
            'actor3': data[12],
            'poster_url': movie_data['items'][0]['image'],
            'link_url': movie_data['items'][0]['link'],
            'user_rating': movie_data['items'][0]['userRating']
        }
        movie.append(save_data)
    __write_movie_file('movie_naver3.csv', save_data.keys(), movie)

def __get_file_column_datas(filename, column_name):
    movie_code_list = []
    with open(filename, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            movie_code_list.append(row[column_name])
    return movie_code_list

def __write_movie_file(filename, fieldnames, datas):
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for data in datas:
            writer.writerow(data)

def main():    
    naver_movie_details()    

if __name__ == "__main__":
    main()