# importanto o Flask para criarmos um mini servidor para a página ir pra a web, o render template para carregar os arquivos de html e o request para salvar os dados que estão nos formularios das páginas
from flask import Flask, render_template, request

# criando a variavel da aplicação
app = Flask(__name__)

# definindo as rotas:
# rota para a página inicial

@app.route('/') # caminho padrão para a página inicial
def index(): # função index para carregar a página inicial
    return render_template('index.html') # arquivo html da página inicial

# rota para a página de cadastro

@app.route('/cadastro') # caminho que sera acessado, usando o método GET, que é o padrão
def cadastro(): # função para irmos para a página de cadastro
    return render_template('cadastro.html') # arquivo html da página de cadastro

# rota para irmos para a página onde vai mostrar os dados que foram colocados no formulario

@app.route('/cadastro', methods=['POST']) # usando o mesmo caminho, porem com o método POST
def informacoes(): # função para mostrar os dados em uma nova página

# dicionário para guardar as informações do formulário, tendo 2 chaves
    dados = {
        'nome': request.form.get('nome'), # variavel para salvar a informção de nome, usando o request para pegar os dados do formulario

        'email': request.form.get('email')# variavel para salvar a informção do email, usando o request para pegar os dados do formulario
    }
    
    # rederincionando para uma nova página onde vai ter as informações salvos acima
    return render_template('informações_login.html', dados = dados) # arquivo html da página onde vai mostrar os dados, mais a variavel dados, onde guarda as informações do formulario