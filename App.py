from flask import Flask, request, render_template, session, redirect

App = Flask(__name__)
App.secret_key = 'SENHA-MUITO-SECRETA'
# Apesar de essa senha estar no código, ela ainda está no servidor,
# um lugar que deve ser seguro e que ninguém tem acesso


@App.route('/')
def index():
    return "Entrou aqui"


@App.route('/exemplo_get')
def exemplo_get():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')
    if usuario and senha:
        return "Os dados recebidos são: usuário={0} e senha={1}".format(
            usuario,
            senha
        )
    else:
        return render_template('exemplo_get.html')


@App.route('/exemplo_post')
def exemplo_post():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    if usuario and senha:
        return "Os dados recebidos são: usuário={0} e senha={1}".format(
            usuario,
            senha
        )
    else:
        return render_template('exemplo_get.html')


@App.route('/login', methods=["GET", "POST"])
def login():
    msg_erro = ''
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        if usuario == 'eduardo' and senha == '1234':
            # Somente exemplo para aprendizado
            session['usuario'] = 'eduardo'  # Armazenamos a sessão do eduardo
            # Redirecionaremos o Rafael para uma rota que somente ele verá
            return redirect('/area_logada')
        else:
            # Caso o usuário estiver incorreto, então exibe o erro e retorna
            # para a página de login
            msg_erro = 'Usuário e/ou senha inválidos'
    return render_template('login.html', erro=msg_erro)


@App.route('/area_logada')
def area_logada():
    if 'usuario' in session:  # Verificar se o usuário está logado
        nome = ''
        media_pessoa = 0.0
        if session['usuario'] == 'eduardo':  # Somente para fins de aprendizado
            nome = 'Eduardo'
            media_pessoa = 7.5
        return render_template(
            "area_logada.html",
            nome=nome,
            media=media_pessoa
        )
    else:
        # Caso o usuário não esteja logado, então redirecione
        # o mesmo para login
        return redirect('/login')


@App.route('/sair')
def sair():
    session.clear()
    return redirect('/login')


if __name__ == '__main__':
    App.run(debug=True, port=5002)
