from flask import Flask, jsonify, request
from flask_cors import CORS 
from DB import add_developer,add_genders,add_game,list_developers,list_games,list_genders,delete_developer,delete_game,delete_gender,alter_developer,alter_game,alter_gender

app = Flask(__name__) 
CORS(app)

@app.get('/all')
def return_all():
    search = request.args.get('search')
    if search == 'developer':
        data_return = list_developers()
    elif search == 'gender':
        data_return = list_genders()
    elif search == 'games':
        data_return = list_games()
    elif search is None:
        response = {'message': 'Informe um parâmetro de busca válido (developer, gender ou games)'}
        return jsonify(response), 400
    else:
        response = {'message': 'Busca inválida. Parâmetro de busca deve ser "developer", "gender" ou "games"'}
        return jsonify(response), 400
    response = {
        "search":search,
        "data":data_return
    }
    return jsonify(response), 200

@app.get('/find')
def find():
    search = request.args.get('search')
    id = request.args.get('id')
    if search == 'developer':
        data_return = list_developers()
    elif search == 'gender':
        data_return = list_genders()
    elif search == 'games':
        data_return = list_games()
    elif search is None:
        response = {'message': 'Informe um parâmetro de busca válido (developer, gender ou games)'}
        return jsonify(response), 400
    else:
        response = {'message': 'Busca inválida. Parâmetro de busca deve ser "developer", "gender" ou "games"'}
        return jsonify(response), 400
    if id.isdigit():
        for i in data_return:
            if i['id']==int(id):
                data_return = i
        response = {
        "search":search,
        "data":data_return
        }
    
    return jsonify(response), 200

@app.post('/add')
def add():
    search = request.args.get('search')
    request_data = request.get_json()
    if request_data:
        if search == 'developer':
            if 'developer' in request_data:
                developer = request_data['developer']
                add_developer(developer)
                res = list_developers()
                for i in res:
                    if i['developer'] == developer:
                        response = i
            else:
                return jsonify('Para adicionar uma desenvolvedora precisa do nome da desenvolvedora'),400
        elif search == 'gender':
            if 'gender' in request_data:
                gender = request_data['gender']
                add_genders(gender)
                res = list_genders()
                for i in res:
                    if i['gender'] == gender:
                        response = i
            else:
                return jsonify('Para adicionar uma genero precisa do nome do genero'),400    
        elif search == 'games':
            if 'title' in request_data:
                title = request_data['title']
            else:
                return jsonify('Para adicionar um jogo precisa de um titulo'),400
            if 'description' in request_data:
                description = request_data['description']
            else:
                return jsonify('Para adicionar um jogo precisa de uma descricao'),400
            if 'lauch_date' in request_data:
                launch_date = request_data['lauch_date']
            else:
                return jsonify('Para adicionar um jogo precisa do ano de lancamento'),400
            if 'developer' in request_data:
                developer = request_data['developer']
            else:
                return jsonify('Para adicionar um jogo precisa do nome da desenvolvedora'),400
            if 'genders' in request_data:
                genders = request_data['genders']
                if len(genders) == 5:
                    gender = genders[0]
                    genderII = genders[1]
                    genderIII = genders[2]
                    genderIV = genders[3]
                    genderV = genders[4]
                else:
                    return jsonify('Preciso de pelo menos 5 generos ao qual o jogo esta vinculado'),400
            add_game(title,description,launch_date,developer,gender,genderII,genderIII,genderIV,genderV)
            res = list_games()
            for i in res:
                if i['title'] == title:
                    response = i
        else:
            return jsonify('Busca invalida'),400
    else:
        return jsonify('precisa de um json com os dados para adicionar os dados'),400 
    if type(response) == str:
        return jsonify(response),400
    return jsonify(response),200

@app.post('/update')
def update():
    search = request.args.get('search')
    request_data = request.get_json()
    if request_data:
        if 'id' in request_data:
            id = request_data['id']
        else:
            return jsonify('Para alterar precisa do id'),400
        if search == 'developer':
            if 'developer' in request_data:
                developer = request_data['developer']
            else:
                return jsonify('Para alterar o nome da desenvolvedora precisa do nome atual'),400
            alter_developer(id,developer)
            res = list_developers()
            for i in res:
                if i['id'] == id:
                    response = i
        elif search == 'gender':
            if 'gender' in request_data:
                gender = request_data['gender']
            else:
                return jsonify('Para alterar o nome do genero precisa do nome atual'),400
            alter_gender(id,gender)
            res = list_genders()
            for i in res:
                if i['id'] == id:
                    response = i
        elif search == 'games':
            if 'title' in request_data:
                title = request_data['title']
            else:
                return jsonify('Para adicionar um jogo precisa de um titulo'),400
            if 'description' in request_data:
                description = request_data['description']
            else:
                return jsonify('Para adicionar um jogo precisa de uma descricao'),400
            if 'lauch_date' in request_data:
                launch_date = request_data['lauch_date']
            else:
                return jsonify('Para adicionar um jogo precisa do ano de lancamento'),400
            if 'developer' in request_data:
                developer = request_data['developer']
            else:
                return jsonify('Para adicionar um jogo precisa do nome da desenvolvedora'),400
            if 'genders' in request_data:
                genders = request_data['genders']
                if len(genders) == 5:
                    gender = genders[0]
                    genderII = genders[1]
                    genderIII = genders[2]
                    genderIV = genders[3]
                    genderV = genders[4]
                else:
                    return jsonify('Preciso de pelo menos 5 generos ao qual o jogo esta vinculado'),400
            alter_game(id,title,description,launch_date,developer,gender,genderII,genderIII,genderIV,genderV)
            res = list_games()
            for i in res:
                if i['id'] == id:
                    response = i
        else:
            return jsonify('Busca invalida'),400
    else:
        return jsonify('precisa de um json com os dados para adicionar os dados'),400 
    if type(response) == str:
        return jsonify(response),400
    
    return jsonify(response),200

@app.delete('/delete')
def delete():
    search = request.args.get('search')
    request_data = request.get_json()
    if request_data:
        if 'type' in request_data:
            type_alteration = request_data['type']
        else:
            return jsonify('Para deletar precisa informar o ID ou o nome de genero para apagar os generos, titulo ou data de lancamento para jogos e desenvolvedora serve para adesenvolvedora ou jogos,'),400
        if 'selection' in request_data:
            selection = request_data['selection']
        else:
            return jsonify('Para deletar precisa de informacao para selecionar o que sera deletado'),400
        if search == 'developer':
            response = delete_developer(type_alteration,selection)
        elif search == 'gender':
            response = delete_gender(type_alteration,selection)
        elif search == 'games':
            response = delete_game(type_alteration,selection)
        else:
            return jsonify('Busca invalida'),400
    else:
        return jsonify('precisa de um json com os dados para adicionar os dados'),400
    if type(response) == str:
        return jsonify(response),400
    return jsonify('sucess'),200

if __name__ == '__main__': 
    app.run(debug = True) 