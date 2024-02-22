from pymongo import MongoClient 
client = MongoClient()
client = MongoClient("mongodb://root:senac1234@127.0.0.1:37452")

# Selecionando o banco de dados loja_db
db = client.lojaDB

# Estamos obtendo os dados que estão cadastrados na tabela(coleção) usuario.
# Usamos db[""].find(). O comando find localiza os dados e retorna com 
# todos eles para a variável us. Depois fazemos a leitura de todas 
# as linhas com o for e exibimos na tela. 
# for us in db["usuario"].find():
#     print(us)

# usuario_id = db["usuario"].insert_one({"nomeusuario":"carina", "senha":"123", "nivel":"usuario"}).inserted_id
# print(usuario_id)

# rs = db["usuario"].find.one()


for rs in db["usuario"].find_one({"nivel":"usuario"}):
    print(rs)