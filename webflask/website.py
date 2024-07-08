from flask import Flask
app = Flask(__name__)

# cria 1° pagina do site
#route -> www.seusite.com/website
#função -> oque vc quer exibir na plataforma
#colocar o site no ar

@app.route("/")
def homepage():
    return "Bem vindo"   
 


app.run