#  04 - Datenbanken in verteilten Systemen
#  Aufgabe 01 - MySQL-Datenbank mit Python ansprechen

# Notwendige Pakete installieren (im Root Verzeichnis ausführen):
#   pip install -r requirements.txt

import mysql.connector

HOST="localhost"
PORT=3306
USER="myuser"
PASSWORD="mypass"
DATABASE="testdb"

# Verbindung zur Datenbank
connection = mysql.connector.connect(
    host=HOST,
    port=PORT,
    user=USER,
    password=PASSWORD,
    database=DATABASE
)

cursor = connection.cursor()
print("Verbindung erfolgreich!")

######################################
#       BEISPIELE                    #
######################################

# CREATE - Neuen User anlegen
def create_user():
    sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
    values = ["Max Mustermann", "max@example.com"]

    cursor.execute(sql, values)
    connection.commit()

    print(f"Eingefügt: {cursor.rowcount} Zeile(n)")

# READ - Alle User abfragen
def read_users():
    cursor.execute("SELECT id,name,email FROM users")
    results = cursor.fetchall()
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")

# UPDATE - User Email aktualisieren
def update_user():
    sql = "UPDATE users SET email = %s WHERE name = %s"
    values = ["new.email@example.com", "Max Mustermann"]

    cursor.execute(sql, values)
    connection.commit()

    print(f"Aktualisiert: {cursor.rowcount} Zeile(n)")

# DELETE - User löschen
def delete_user():
    sql = "DELETE FROM users WHERE name = %s"
    value = ["Max Mustermann"]

    cursor.execute(sql, value)
    connection.commit()

    print(f"Gelöscht: {cursor.rowcount} Zeile(n)")

###########################
# SQL Injection Beispiel  #
###########################

def sql_injection_example(user_name, email):
    # Unsichere Methode (nicht verwenden!). 
    sql = "INSERT INTO users (name, email) VALUES (" + user_name + ", " + email + ")"
    cursor.execute(sql)
    connection.commit() # Commit wird Fehler auslösen (siehe https://dev.mysql.com/doc/refman/8.4/en/commands-out-of-sync.html), aber Tabelle wurde trotzdem gelöscht!

def sql_injection_example_safe(user_name, email):
    # Stattdessen immer "Prepared Statements" nutzen 
    # (Werte als Platzhalter in String definieren und als separates Argument übergeben).
    sql_safe = "INSERT INTO users (name, email) VALUES (%s, %s)"
    cursor.execute(sql_safe, [user_name, email])
    connection.commit()

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
# Aufruf in Main mit "ro.windey@gmail.com"
# Analysiere das Ergebnis. Warum wird eine Exception ausgelöst?
def delete_user_by_email(email):
    pass

# Aufgabe 4 (optional): Alle User mit ihren Bestellungen ausgeben (LEFT JOIN)
# Wie sieht das Ergebnis aus? Was fällt auf?
#
# Hinweis: JOIN-syntax lautet wie folgt:
# SELECT a.<feld1>, a.<feld2>,...,b.<feld1>, b.<feld2>,...
# FROM a
# LEFT JOIN b ON a.<primary_key> = b.<foreign_key>;
def read_users_and_orders():
    pass

####################################################
# Main Funktion zum Ausführen der CRUD-Operationen #
####################################################
if __name__ == "__main__":
    #######################################################
    # Beispieloperationen für die "User"-Relation
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
        delete_user_by_email("ro.windey@gmail.com")  # (3)
    except Exception as e:
        print(f"Fehler beim Löschen des Users: {e}")
    read_users_and_orders()  # (4)
    
    ##########################################################
    # SQL Injection Demonstration
    user = "'Max Mustermann'"
    malicious_email = "'some@mail.com'); DROP TABLE orders; SELECT ('dummy'"
    sql_injection_example(user, malicious_email)
    read_orders()  # Prüfen, ob Tabelle noch existiert

    # Verbindung schließen
    cursor.close()
    connection.close()
    print("Verbindung geschlossen.")