import datetime
from typing import List
import json

import mysql.connector

PAG_SIZE = 6


def connect():
    return mysql.connector.connect(
        user='root',
        host='127.0.0.1',
        password='m4a1hpxw',
        database='mydb'
    )


# TODO: works
def get_all_movies() -> dict:
    db = connect()
    sql = 'SELECT * FROM movies;'
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    cursor.close()
    db.close()
    return json.dumps(res)


# TODO: works
def get_movies_by_title(title: str) -> dict:
    from urllib import parse
    title = parse.unquote(title)
    db = connect()
    cursor = db.cursor()
    sql = 'SELECT * FROM movies WHERE movie_name=%s;'
    val = (title,)
    print(val)
    try:
        cursor.execute(sql, val)
    except Exception as e:
        print(e)
        print('failed to find movies by title {}'.format(title))
        cursor.close()
        db.close()
        return False

    res = cursor.fetchall()
    cursor.close()
    db.close()
    return json.dumps(res)


# TODO: works
def get_movies_by_genre(genre: str = None) -> dict:
    db = connect()
    cursor = db.cursor()
    if genre is not None:
        sql = 'SELECT * FROM movies WHERE genre=%s;'
        val = (genre,)
        try:
            cursor.execute(sql, val)
        except Exception as e:
            print(e)
            print('failed to find movies by genre {}'.format(genre))
            cursor.close()
            db.close()
            return False
    else:
        sql = 'SELECT * FROM movies;'
        cursor.execute(sql)

    res = cursor.fetchall()
    cursor.close()
    db.close()
    return json.dumps(res)


def get_movie_by_id(id: int) -> List[str]:

    pass


# TODO: works
def get_genres() -> List[str]:
    db = connect()
    sql = 'SELECT distinct(genre) FROM movies;'
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    cursor.close()
    db.close()
    return json.dumps(res)


# TODO: check
def add_movie(movie_name: str, genre:str, length: str) -> dict:
    db = connect()
    sql = 'INSERT INTO movies (genre, length, movie_name) VALUES (%s, %s, %s);'
    val = (genre, length, movie_name,)
    cursor = db.cursor()
    try:
        cursor.execute(sql, val)
        cursor.close()
        db.close()
        return {'status': f'{movie_name} added'}
    except Exception as e:
        print(e)
        print(f'{movie_name} not added due to error')
        cursor.close()
        db.close()
        return False


def get_shows_by_movie(movie_name: str = None) -> dict:
    if movie_name is not None:
        db = connect()
        cursor = db.cursor()
        sql = 'SELECT idmovies FROM movies WHERE movie_name=%s;'
        val = (movie_name,)
        try:
            cursor.execute(sql, val)
            res = cursor.fetchall()[0]
            print(res)
            cursor.close()
            db.close()
            movie_id = int(res[0])
        except Exception as e:
            print(e)
            print('failed to find shows by name {}'.format(movie_name))
            cursor.close()
            db.close()
            return False
    else:
        print('no movie specified')
        return False

    db = connect()
    cursor = db.cursor()
    sql = 'SELECT * FROM showings WHERE movies_idmovies=%s;'
    val = (movie_id,)
    try:
        cursor.execute(sql, val)
        res = cursor.fetchall()
        print(res)
        return json.dumps(res)
    except Exception as e:
        print(e)
        return False


def get_reservations_per_showing(show_id: int) -> json:
    db = connect()
    cursor = db.cursor()

    sql = 'SELECT seat_id FROM reservations WHERE showings_idshowing = %s'
    val = (show_id, )
    cursor.execute(sql, val)
    i = 0
    res = []
    for row in cursor.fetchall():
        res[i] = {'idreservations': row[0], 'showings_idshowing': row[1], 'seat_id': row[2]}
    return json.dumps(res)


def get_free_seats_per_showing(show_id: int) -> List[str]:
    db = connect()
    cursor = db.cursor()
    sql = """SELECT s.seat_id FROM seats s 
    WHERE s.auditoriums_idauditorium = (SELECT auditoriums_idauditorium FROM showings WHERE idshowing = %s)
     AND seat_id != ALL(SELECT r.seat_id FROM reservations r WHERE r.showings_idshowing =  %s)"""
    val = (show_id, show_id)
    cursor.execute(sql, val)
    return [x[0] for x in cursor.fetchall()]


def book_a_seat(show_id: int, seat_id: int) -> bool:
    db = connect()
    cursor = db.cursor()
    sql = """"""

def get_showings_per_auditiorium(aud_id: int) -> List[str]:
    pass


def add_ticket(show_id: int, seat_id: int, name: str) -> bool:
    pass


def get_showing_per_movie(title: str):
    db = connect()
    cursor = db.cursor()
    sql="""SELECT s.time, s.auditoriums_idauditorium, s.idshowing FROM showings s WHERE s.movies_idmovies = (SELECT idmovies FROM movies WHERE movie_name = %s)"""
    val = (title,)
    cursor.execute(sql, val)
    res = {f'{x[0]}: {x[1]}': x[2] for x in cursor.fetchall()}
    return res

def usiadz_na_m(seat_id: int, showing_id: int):
    db = connect()
    cursor = db.cursor()
    sql = """INSERT INTO reservations (showings_idshowing, seat_id) VALUES (%s, %s)"""
    val = (showing_id, seat_id)
    cursor.execute(sql, val)


def get_titles() -> List[str]:
    db = connect()
    cursor = db.cursor()
    sql = """SELECT movie_name FROM movies"""
    cursor.execute(sql)
    return [x[0] for x in cursor.fetchall()]


def get_movie_id(title: str) -> int:
    db = connect()
    cursor = db.cursor(buffered=True)
    sql = """SELECT idmovies FROM movies WHERE title = %s"""
    val = (title,)
    cursor.execute(sql, title)
    return cursor.fetchone()[0]