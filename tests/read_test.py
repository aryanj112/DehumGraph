import sqlite3

def read_from_sqlite(df_file,table_name):
    conn = sqlite3.connect(df_file)
    c = conn.cursor()
    query = f"SELECT * FROM {table_name}"
    c.execute(query)
    result = c.fetchall()

    for row in result:
        print(row)

    conn.close()

if __name__ == "__main__":
    df_file = r"C:\Users\ajayj\DehumGraph\database.sqlite3"
    table_name = "solaredge"
    read_from_sqlite(df_file,table_name)