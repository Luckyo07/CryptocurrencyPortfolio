import sqlite3
con = sqlite3.connect('mycompany.db')
cobj = con.cursor()

#cobj.execute("CREATE TABLE employees(id INTEGER PRIMARY KEY, name TEXT, salary REAL, department TEXT, position TEXT)")
#con.commit()

#cobj.execute("insert into employees values(?,?,?,?,?)",(2, 'Harshit', 5300, "JS", "Developer"))
#con.commit()

#cobj.execute("update employees set department=? where id = ?", ('php',2))
#con.commit()

# fetching data require 2 steps
cobj.execute("select * from employees")
r = cobj.fetchall()

print (r)

cobj.close()
con.close()