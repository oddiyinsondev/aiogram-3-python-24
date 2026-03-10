from sqlite3 import connect


c = connect("test.db")
cursor = c.cursor()
cursor.execute("""
               create table obuna(
                   id integer primary key not null,
                   kanal_id int not null unique,
                   nomi text not null,
                   link text not null
               );
               """)
c.commit()
print('bajarildi')