# Desafio_Onovolab
Desafio Onovolab

A descrição de todas as análises realizada pode ser encontrada no arquivo jupyter: Desafio Onovolab Cientista de dados_jupyter.ipynb, o código gerador de todas as análises pode ser encontrado em: projeto_onovolab.py.

Os modelos serializados gerados são: MLPRegressor_credit_model.sav para determinação da quantidade de empréstimo e floresta_credit_model.sav para determinar se o cliente irá pagar ou não o empréstimo.

Devido a dificultado de se calibrar um modelo de machine learning a acurácio dos modelos nãoforam otimizadas, é preferível em um ambiente de produção real a utilização de algoritmos de otimização como Algoritmos Genéticos, enxames de partículas, entre outros para o ajuste destes modelos.

A base de dados contém um problema que é a falta de informação em alguns pontos que pode interferir na qualidade do modelo.
                                                  
                                                  ***
                                                  
Para a utilização da API basta executar o arquivo API.py

OBS: 
Para validação fiz testes utilizando o Postman - Request POST em:
http://127.0.0.1:5000/get_credit

Passando no Body as informações do cliente.

Exemplo de resposta obtida:

{
  "Amount": 77,
  "Status": "Yes"
}


Com o API.py executando (servidor), executar o arquivo Desafio_Response_mongoDB.py, que fará a requisição a API receberá a resposta eincluirá em uma base de dados MongoDB. Para validação deste processo utilizei um cluster do mongoBD cloud, para testar basta inserir uma Connexion String válida.
