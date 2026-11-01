#  04 - Datenbanken in verteilten Systemen
#  Aufgabe 02 - MongoDB-Datenbank mit Python ansprechen

# Notwendige Pakete installieren (im Root Verzeichnis ausführen):
#   pip install -r requirements.txt

# Weitere Infos: https://www.mongodb.com/docs/manual/crud/

from pymongo import MongoClient

HOST="localhost"
PORT=27017
USER="myuser"
PASSWORD="mypass"
DB_NAME="testdb"

# Verbindung zur MongoDB herstellen
client = MongoClient(
    host=HOST,
    port=PORT,
    username=USER,
    password=PASSWORD
)

# Wechsel auf die Datenbank "testdb"
db = client[DB_NAME]

######################################
#       BEISPIELE                    #
######################################

# CREATE - Neuen User anlegen
def create_user():
    # "Max Mustermann" hat "age"-Feld. Die vorhandenen Datensätze nicht. In MongoDB ist das erlaubt.
    user = {"name": "Max Mustermann", "email": "max@example.com", "age": 30}
    result = db.users.insert_one(user)
    print(f"Eingefügt: User-ID {result.inserted_id}")

# READ - Alle User abfragen
def read_users():
    users = db.users.find()
    for user in users:
        print(f"ID: {user.get('_id')}, Name: {user.get('name')}, Email: {user.get('email')}")

# UPDATE - User Email aktualisieren
def update_user():
    result = db.users.update_one(
        {"name": "Max Mustermann"},
        {"$set": {"email": "new.email@example.com"}}
    )
    print(f"Aktualisiert: {result.modified_count} User(s)")

# DELETE - User löschen
def delete_user():
    result = db.users.delete_one({"name": "Max Mustermann"})
    print(f"Gelöscht: {result.deleted_count} User(s)")

######################################
#       AUFGABEN                     #
######################################

# Aufgabe 1: Funktion zum Lesen aller Bestellungen
def read_orders():
    pass

# Aufgabe 2: Neue Bestellung anlegen für User "Robin" mit Produkt "Camera" und Amount 10
def create_order():
    pass

# Aufgabe 3: Bestimmten User anhand der Email löschen 
def delete_user_by_email(email):
    pass

# Aufgabe 4 (optional): Alle User mit ihren Bestellungen ausgeben (MongoDB $lookup)
# Tip: 
# pipeline = [ ... ]
# results = db.users.aggregate(pipeline)
# Infos:
# * https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.aggregate
# * https://www.mongodb.com/docs/manual/reference/operator/aggregation/lookup/
def read_users_and_orders():
    pass

####################################################
# Main Funktion zum Ausführen der CRUD-Operationen #
####################################################
if __name__ == "__main__":
    #######################################################
    # Beispieloperationen für die "user"-document-collection
    # read_users()
    # create_user()
    # read_users()
    # update_user()
    # read_users()
    # delete_user()
    # read_users()

    #########################################################
    # Aufgaben
    read_orders()   # (1)
    create_order()  # (2)
    try:
        delete_user_by_email("another.email@gmail.com")  # (3)
    except Exception as e:
        print(f"Fehler beim Löschen des Users: {e}")
    read_users_and_orders()  # (4)

    # Verbindung schließen
    client.close()