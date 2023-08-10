import sqlite3

def test_connection(df_file):
    conn = sqlite3.connect(df_file)
    conn.close()


if __name__ == "__main__":
    df_file = r"C:\Users\ajayj\DehumGraph\database.sqlite3"
    test_connection(df_file)