from flask import Flask, render_template, redirect, request, send_file, flash
from flask_wtf.file import FileField, FileAllowed
from flask_wtf import FlaskForm
import pandas as pd



# Configura pastas e extensões permitidas para o programa
app = Flask(__name__, static_folder='static', template_folder='templates')


app.config['SECRET_KEY'] = "37n53782o2w2m9id2d4z327112ys2g62"


# Definindo o formulário base de upload
class UploadForm(FlaskForm):
    file = FileField('Arquivo',
                     validators=[
                         FileAllowed(
                             ['pdf', 'xlsx'],
                             'Somente arquivos PDF, e XLSX são permitidos!'
                             )])





@app.route('/')
def index():
    # Carregar o arquivo Excel
    excel_file = 'JJE_Pontuação.xlsx'  # Substitua pelo caminho do seu arquivo Excel
    df = pd.read_excel(excel_file)
    df_ger = df.sort_values(by = ['Geral'], ascending=False)
    print(df_ger)
    def_nat_masc = df.sort_values(by = ['Natação Masc'], ascending=False)



    # Extrair dados para a tabela (supondo que as colunas se chamem "Atletica" e "Pontuacao")
    # atleticas_ger = df_ger['Atletica'].tolist()
    # geral = df_ger['Geral'].tolist()
    # print(atleticas_ger)
    # print(geral)

    # Extrair dados para a tabela e combiná-los em uma lista de tuplas
    atleticas_pontuacoes_ger = list(zip(df_ger['Atletica'], df_ger['Geral']))
    atleticas_pontuacoes_nat_masc = list(zip(def_nat_masc['Atletica'], def_nat_masc['Natação Masc']))
    # Passar os dados para o template
    return render_template('index.html', atleticas_pontuacoes_ger=atleticas_pontuacoes_ger,atleticas_pontuacoes_nat_masc = atleticas_pontuacoes_nat_masc )

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == "__main__":
    app.run()