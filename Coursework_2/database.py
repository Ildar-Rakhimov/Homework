import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://py47:123456@localhost:5432/VKinder')

try:
    connection = engine.connect()
except Exception as error:
    print('Ошибка подключения к базе данных', {error})


def insert_user(user_info):
    info = f"""INSERT INTO User (ID, Name, Surname, City, Sex, Age) VALUES(
      '{user_info.get('user_id')}', 
      '{user_info.get('user_name')}', 
      '{user_info.get('user_surname')}', 
      '{user_info.get('user_city')}',
      '{user_info.get('user_sex')}',
      '{user_info.get('user_age')}'
    );"""
    return connection.execute(info)


def insert_candidate(candidate_info):
    info = f"""INSERT INTO Candidate (ID, Name, Surname, Sex, City, Age) VALUES(
      '{candidate_info.get('candidate_id')}',
      '{candidate_info.get('candidate_name')}',
      '{candidate_info.get('candidate_surname')}',    
      '{candidate_info.get('candidate_sex')}',
      '{candidate_info.get('candidate_city')}',
      '{candidate_info.get('candidate_age')}'
    );"""
    return connection.execute(info)


def insert_photo(photo_info):
    for element in photo_info:
        info = f"""INSERT INTO Photos (Candidate_ID, URL, Popularity) VALUES(
          '{element.get('candidate_id')}',
          '{element.get('photo_url')}',
          '{element.get('popularity')}'
        );"""
        connection.execute(info)


def insert_user_candidate(user_candidate_info):
    info = f"""INSERT INTO User_Candidate (User_ID, Candidate_ID) VALUES(
      '{user_candidate_info['user_info']['user_id']}',
      '{user_candidate_info['candidate_info']['candidate_id']}'
    );"""
    return connection.execute(info)