import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def db_conection():
    return mysql.connector.connect(host = os.getenv('DB_ADDR'),user=os.getenv('DB_USER'),password=os.getenv('PASSW'),database=os.getenv('DB_NAME'))

def db_close(conection):
    return conection.close()

def create_BD():
    conection = mysql.connector.connect(host = os.getenv('DB_ADDR'),user=os.getenv('DB_USER'),password=os.getenv('PASSW'))
    cursor = conection.cursor()
    sql = "CREATE DATABASE IF NOT EXISTS  desafio_ciee;"
    cursor.execute(sql)
    db_close(conection)

def create_table_developer(conection):
    cursor = conection.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS DEVELOPER(ID INT AUTO_INCREMENT PRIMARY KEY,DEVELOPER_NAME VARCHAR(255) UNIQUE NOT NULL);'
    cursor.execute(sql)
    cursor.close()
    conection.commit()

def create_table_gender(conection):
    cursor = conection.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS GENDER(ID INT AUTO_INCREMENT PRIMARY KEY,GENDER VARCHAR(100) UNIQUE NOT NULL);'
    cursor.execute(sql)
    cursor.close()
    conection.commit()

def create_table_game(conection):
    cursor = conection.cursor()
    sql = 'CREATE TABLE IF NOT EXISTS GAME(ID INT AUTO_INCREMENT PRIMARY KEY ,TITLE VARCHAR(100) UNIQUE NOT NULL,DESCRIPTION VARCHAR(255) NOT NULL,LAUNCH_DATE YEAR NOT NULL,DEVELOPER INT NOT NULL,GENDER INT NOT NULL,GENDERII INT ,GENDERIII INT ,GENDERIV INT ,GENDERV INT ,FOREIGN KEY(DEVELOPER) REFERENCES DEVELOPER(ID),FOREIGN KEY(GENDER) REFERENCES GENDER(ID),FOREIGN KEY(GENDERII) REFERENCES GENDER(ID),FOREIGN KEY(GENDERIII) REFERENCES GENDER(ID),FOREIGN KEY(GENDERIV) REFERENCES GENDER(ID),FOREIGN KEY(GENDERV) REFERENCES GENDER(ID));'
    cursor.execute(sql)
    cursor.close()
    conection.commit()

def create_table(conection):
    create_BD()
    create_table_developer(conection)
    create_table_gender(conection)
    create_table_game(conection)

def add_developer(name):
    conection = db_conection()
    create_table(conection)
    cursor = conection.cursor()
    sql = f'INSERT INTO `developer` (`DEVELOPER_NAME`) VALUES ("{name}")'
    try:
        cursor.execute(sql)
        cursor.close()
        conection.commit()
    except:
        return f'Essa Desenvolvedora {name} ja existe'
    db_close(conection)

def add_genders(gender):
    conection = db_conection()
    create_table(conection)
    cursor = conection.cursor()
    sql = f'INSERT INTO `gender` (`GENDER`) VALUES ("{gender}")'
    try:
        cursor.execute(sql)
        cursor.close()
        conection.commit()
    except:
        db_close(conection)
        return f'Esse Genero {gender} ja existe'
    db_close(conection)

def add_game(game,description,lauch_date,developer,gender,genderII,genderIII,genderIV,genderV):
    conection = db_conection()
    create_table(conection)
    cursor = conection.cursor()
    sql = f'INSERT INTO `game` (`TITLE`, `DESCRIPTION`, `LAUNCH_DATE`, `DEVELOPER`, `GENDER`, `GENDERII`, `GENDERIII`, `GENDERIV`, `GENDERV`) VALUES ("{game}", "{description}", "{lauch_date}", {developer}, {gender}, {genderII}, {genderIII}, {genderIV}, {genderV});'
    try:
        cursor.execute(sql)
        cursor.close()
        conection.commit()
    except:
        db_close(conection)
        return f'Esse Game {game} ja existe'
    db_close(conection)

def list_developers():
    conection = db_conection()
    create_table(conection)
    cursor = conection.cursor()
    sql = 'SELECT * FROM `developer`'
    cursor.execute(sql)
    developers = []
    for id,developer in cursor:
        dict_developer={
            "id":id,
            "developer":developer
        }
        developers.append(dict_developer)
    db_close(conection)
    return developers

def list_genders():
    conection = db_conection()
    create_table(conection)
    cursor = conection.cursor()
    sql = 'SELECT * FROM `gender`'
    cursor.execute(sql)
    genders = []
    for id,gender in cursor:
        dict_gender = {
            "id":id,
            "gender":gender
        }
        genders.append(dict_gender)
    db_close(conection)
    return genders

def list_games():
    conection = db_conection()
    create_table(conection)
    cursor = conection.cursor()
    sql = 'SELECT G.ID,G.TITLE, G.DESCRIPTION,G.LAUNCH_DATE,DEV.DEVELOPER_NAME AS DEVELOPER,GEN.GENDER AS GENDER,GENII.GENDER AS GENDERII,GENIII.GENDER AS GENDERIII,GENIV.GENDER AS GENDERIV,GENV.GENDER AS GENDERV FROM  game as G INNER JOIN developer AS DEV ON G.DEVELOPER = DEV.ID INNER JOIN gender AS GEN ON G.GENDER = GEN.ID INNER JOIN gender AS GENII ON G.GENDERII = GENII.ID INNER JOIN gender AS GENIII ON G.GENDERIII = GENIII.ID INNER JOIN gender AS GENIV ON G.GENDERIV = GENIV.ID INNER JOIN gender AS GENV ON G.GENDERV = GENV.ID'
    cursor.execute(sql)
    games = []
    for id,game,description,lauch_date,developer,gender,genderII,genderIII,genderIV,genderV in cursor:
        genders_list = []
        genders_list.append(gender)
        genders_list.append(genderII)
        genders_list.append(genderIII)
        genders_list.append(genderIV)
        genders_list.append(genderV)
        dict_games ={
            "id":id,
            "title":game,
            "description":description,
            "year":lauch_date,
            "developer":developer,
            "genders":genders_list
        }
        games.append(dict_games)
    db_close(conection)
    return games

def delete_developer(type,developer):
    conection = db_conection()
    create_table(conection)
    cursor = conection.cursor()
    if type == 'name':
        sql = f'DELETE FROM developer WHERE developer.DEVELOPER_NAME = "{developer}";'
    elif type == 'id':
        sql = f'DELETE FROM developer WHERE developer.ID = {developer};'
    try:
        cursor.execute(sql)
        cursor.close()
        conection.commit()
    except:
        db_close(conection)
        return 'Ouve um problema ao excluir o registro'
    db_close(conection)

def delete_gender(type,gender):
    conection = db_conection()
    create_table(conection)
    cursor = conection.cursor()
    if type == 'name':
        sql = f'DELETE FROM gender WHERE gender.GENDER = "{gender}";'
    elif type == 'id':
        sql = f'DELETE FROM gender WHERE gender.ID = {gender};'
    try:
        cursor.execute(sql)
        cursor.close()
        conection.commit()
    except:
        db_close(conection)
        return 'Ouve um problema ao excluir o registro'
    db_close(conection)

def delete_game(type,game):
    conection = db_conection()
    create_table(conection)
    cursor = conection.cursor()
    if type == 'id':
        sql = f'DELETE FROM game WHERE game.ID = {game};'
    elif type == 'title':
        sql = f'DELETE FROM game WHERE game.TITLE = "{game}";'
    elif type == 'lauch_date':
        sql = f'DELETE FROM game WHERE game.LAUNCH_DATE = "{game}";'
    elif type == 'developer':
        sql = f'DELETE FROM game WHERE game.DEVELOPER = {game};'
    try:
        cursor.execute(sql)
        cursor.close()
        conection.commit()
    except:
        db_close(conection)
        return 'Ouve um problema ao excluir o registro'
    db_close(conection)

def alter_developer(id,developer):
    conection = db_conection()
    create_table(conection)
    cursor = conection.cursor()
    sql = f'UPDATE developer SET DEVELOPER_NAME = "{developer}" WHERE developer.ID = {id};'
    try:
        cursor.execute(sql)
        cursor.close()
        conection.commit()
    except:
        db_close(conection)
        return 'Ouve um problema ao editar o registro'
    db_close(conection)

def alter_gender(id,gender):
    conection = db_conection()
    create_table(conection)
    cursor = conection.cursor()
    sql = f'UPDATE gender SET GENDER = "{gender}" WHERE gender.ID = {id};'
    try:
        cursor.execute(sql)
        cursor.close()
        conection.commit()
    except:
        db_close(conection)
        return 'Ouve um problema ao editar o registro'
    db_close(conection)

def alter_game(id, type, game):
    conection = db_conection()
    create_table(conection)
    cursor = conection.cursor()
    if type == 'title':
        sql = f"UPDATE game SET TITLE = '{game}' WHERE game.ID = {id};"
    elif type== 'description':
        sql = f"UPDATE game SET DESCRIPTION = '{game}' WHERE game.ID = {id};"
    elif type == 'lauch_date':
        sql = f"UPDATE game SET LAUNCH_DATE = '{game}' WHERE game.ID = {id};"
    elif type == 'developer':
        sql = f"UPDATE game SET DEVELOPER = '{game}' WHERE game.ID = {id};"
    elif type == 'gender':
        sql = f'UPDATE game SET GENDER = "{game}" WHERE game.ID = {id};'
    elif type == 'genderII':
        sql = f'UPDATE game SET GENDERII = "{game}" WHERE game.ID = {id};'
    elif type == 'genderIII':
        sql = f'UPDATE game SET GENDERIII = "{game}" WHERE game.ID = {id};'
    elif type == 'genderIV':
        sql = f'UPDATE game SET GENDERIV = "{game}" WHERE game.ID = {id};'
    elif type == 'genderV':
        sql = f'UPDATE game SET GENDERV = "{game}" WHERE game.ID = {id};'
    try:
        cursor.execute(sql)
        cursor.close()
        conection.commit()
    except:
        db_close(conection)
        return 'Ouve um problema ao editar o registro'
    db_close(conection)