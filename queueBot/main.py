import sqlite3

# Connect to a database
playerbase = sqlite3.connect("queuebotdb.db")

# Create a cursor
c = playerbase.cursor()

# Create a Table
c.execute("""CREATE TABLE players (
    player_role DATATYPE,
    player_name DATATYPE,
    player_mmr DATATYPE
)""")