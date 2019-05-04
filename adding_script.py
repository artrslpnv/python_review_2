from BD import add_matches,get_match
import sqlite3
conn = sqlite3.connect('mthcs.db')
cur=conn.cursor()
add_matches(cur,conn,'Barcelona - Liverpool', '01.05.2019','3:0','Suarez 26, Messi 75,82')
add_matches(cur,conn, 'Tottenham - Ajax', '30.04.2019','0:1', 'Van de Beek 15')
add_matches(cur,conn,'Barcelona - Manchester United' , '16.04.2000' ,'3:0'," Messi 16,20 Coutinho 61")
add_matches(cur,conn,'Manchester United - Barcelona', '10.04.2000','0:1','Show 12 (AG)')

conn.commit()

