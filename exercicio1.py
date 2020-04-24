import sqlite3
conn = sqlite3.connect('exercicio1.db')

c = conn.cursor()

c.execute('''CREATE TABLE allan(
                id integer,
                nome text not null,
                email text,
                primary key (id) )'''
                )

c.execute("INSERT INTO allan VALUES (1,'Allan Calixto','allan.calixto@aluno.faculdadeimpacta.com.br')")

conn.commit()

conn.close()