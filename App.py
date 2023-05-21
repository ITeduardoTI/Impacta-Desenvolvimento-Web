from flask import Flask, render_template
from classes.curso import Curso

App = Flask(__name__)

@App.route('/')
def index():
    string_qualquer = 'Página inicial'
    conteudo = 'Olha que legal, agora sabemos criar páginas dinâmicas'
    return render_template("index.html", titulo=string_qualquer, conteudo=conteudo)

@App.route('/cursos')
def cursos():
    lista_de_cursos = ['Desenvolvimento Web', 'Programação Orientada a Objetos']
    return render_template("cursos.html", lista=lista_de_cursos)


@App.route('/curso/<nome>')
def curso_por_nome(nome):
    if nome == 'devweb':
        info = Curso("Desenvolvimento Web", "Disciplina que lida com as tecnologias da web")
        habilidades = ['HTML', 'CSS', 'JavaScript']
        return render_template("info_curso.html", objeto=info, habilidades=habilidades, dificuldade=2)
    elif nome == "poo":
        info = Curso("Programação Orientada a Objetos", "Disciplina que ensina o paradigma orientado a objetos")
        habilidades = ['Dicionários', 'Tratamento de exceções', 'Classes', 'Herança']
        return render_template("info_curso.html", objeto=info, habilidades=habilidades, dificuldade=1)
    else:
        return "Curso inexistente"
    
if __name__ == '__main__':
    App.run(debug=True)