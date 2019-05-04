import sqlite3
def create_tables(cur, conn):
    cur.execute('''
        CREATE TABLE if Not EXISTS matches(
            nms VARCHAR(255) ,
            d VARCHAR (200),
            score varchar (200),
            goals varchar (250)
           
        )''')
    conn.commit()
def add_matches(cur,conn,fnms,fd,fscore,fgoals ):
    query="""
        INSERT INTO matches (nms,
            d ,score ,goals  )
            values ( '%(nms)s','%(d)s','%(score)s','%(goals)s')
        """ %{"nms":fnms,"d":fd,"score":fscore,"goals":fgoals}
    cur.execute(query)
    conn.commit()
def get_match(conn,fnms,fd):
    query = '''SELECT nms,score,goals
                   FROM matches 
                   WHERE nms = '%(nms)s'  and d = '%(d)s' '''% {"nms":fnms,"d":fd}
    cur = conn.cursor()
    cur.execute(query)
    list=cur.fetchmany(1)
    return list
def addind(cur,conn):
    add_matches(cur,conn,'Barcelona - Liverpool', '01.05.2019','3:0','Suarez 26, Messi 75,82')
    add_matches(cur,conn, 'Tottenham - Ajax', '30.04.2019','0:1', 'Van de Beek 15')
    add_matches(cur,conn,'Barcelona - Manchester United' , '16.04.2000' ,'3:0'," Messi 16,20 Coutinho 61")
    add_matches(cur,conn,'Manchester United - Barcelona', '10.04.2000','0:1','Show 12 (AG)')
    conn.commit()


