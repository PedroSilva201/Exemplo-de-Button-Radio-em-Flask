from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

# Conexão com o banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Tabela"
)

app = Flask(__name__)

# Função para salvar a seleção no banco de dados
def salvar_selecao(valor_selecionado):
    cursor = db.cursor()
    query = "INSERT INTO tabela (coluna) VALUES (%s)"
    cursor.execute(query, (valor_selecionado,))
    db.commit()  # Confirma a transação no banco
    cursor.close()

# Rota para a página inicial (agora chamada 'inicio.html')
@app.route('/')
def inicio():
    return render_template('index.html')

# Rota para a página do formulário
@app.route('/inicio', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        valor_selecionado = request.form.get('opcao')
        if valor_selecionado:
            salvar_selecao(valor_selecionado)
            return redirect(url_for('inicio'))  # Redirecionar para a página inicial

    return render_template('inicio.html')  # Supondo que o formulário esteja em 'formulario.html'

@app.route('/resultados')
def resultados():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tabela")  # Query para buscar os registros
    resultados = cursor.fetchall()  # Recupera todos os registros
    
    # Contar todas as respostas
    cursor.execute("SELECT coluna, COUNT(*) FROM tabela GROUP BY coluna")
    escolhas = cursor.fetchall()  # Retorna uma lista de tuplas (opção, contagem)

    # Contar o total de respostas
    cursor.execute("SELECT COUNT(*) FROM tabela")
    total_respostas = cursor.fetchone()[0]
    
    # Contar todas as respostas para cada opção
    cursor.execute("SELECT coluna, COUNT(*) FROM tabela GROUP BY coluna")
    escolhas = cursor.fetchall()  # Retorna uma lista de tuplas (opção, contagem)
    
    # Contar o total de uma opção específica
    opcao_especifica = "opcao_1"  # Substitua com a opção que você deseja contar
    cursor.execute("SELECT COUNT(*) FROM tabela WHERE coluna = %s", (opcao_especifica,))
    total_opcao_especifica = cursor.fetchone()[0]
    
        # Contar o total de uma opção específica
    opcao_especifica = "opcao_2"  # Substitua com a opção que você deseja contar
    cursor.execute("SELECT COUNT(*) FROM tabela WHERE coluna = %s", (opcao_especifica,))
    total_opcao_especifica = cursor.fetchone()[0]
    
        # Contar o total de uma opção específica
    opcao_especifica = "opcao_3"  # Substitua com a opção que você deseja contar
    cursor.execute("SELECT COUNT(*) FROM tabela WHERE coluna = %s", (opcao_especifica,))
    total_opcao_especifica = cursor.fetchone()[0]
    
        # Contar o total de uma opção específica
    opcao_especifica = "opcao_4"  # Substitua com a opção que você deseja contar
    cursor.execute("SELECT COUNT(*) FROM tabela WHERE coluna = %s", (opcao_especifica,))
    total_opcao_especifica = cursor.fetchone()[0]
    
    # Calcular as porcentagens
    porcentagens = [(opcao, (contagem / total_respostas) * 100) for opcao, contagem in escolhas]
    
    # Calcular a quantidade de registros por cada opção.
    total_opcao_especifica = [(total_respostas/ 4) in escolhas]
    
    cursor.close()

    return render_template('resultados.html', resultados=resultados, porcentagens=porcentagens, total_respostas=total_respostas, total_opcao_especifica=total_opcao_especifica)


if __name__ == '__main__':
    app.run(debug=True, port=8081)
