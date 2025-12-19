import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO sys_command VALUES (null,'vlc', 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\VideoLAN\\VLC media player.lnk')"
cursor.execute(query)
con.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO web_command VALUES (null,'canva', 'https://www.canva.in/')"
cursor.execute(query)
con.commit()


query = "INSERT INTO web_command VALUES (null,'amzon', 'https://www.amazon.in/')"
cursor.execute(query)
con.commit()

query = "INSERT INTO web_command VALUES (null,'flipkart', 'https://www.flipkart.com/')"
cursor.execute(query)
con.commit()