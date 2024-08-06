from pymongo import MongoClient

# Cadena de conexión proporcionada
connection_string = "mongodb+srv://anelmartez18:NPsCQPVYRHhhOczM@tenkaitechdb.o8qlj.mongodb.net/?retryWrites=true&w=majority&appName=tenkaitechDB"

# Crear cliente de MongoDB
client = MongoClient(connection_string)

# Seleccionar la base de datos
db = client.tenkaitechDB  # Asegúrate de que el nombre coincida con tu base de datos

# Ejemplo: listar las colecciones en la base de datos
print("Colecciones en la base de datos:", db.list_collection_names())
