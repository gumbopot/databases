import _sqlite3 as sql


def create_table():
	# OPEN connection of CREATE database
	conn = sql.connect("little.db")
	# create cursor object
	cur = conn.cursor()
	#cur.execute("CREATE TABLE store (item TEXT, quantity INTEGER, price REAL)")
	cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
	cur.execute("INSERT INTO store VALUES ('Wine Glass', 8, 10.5)")
	# commit to db
	conn.commit()
	# close connection
	conn.close()


def insert(item, quantity, price):
	conn = sql.connect("little.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO store VALUES (?,?,?)", (item, quantity, price))
	conn.commit()
	conn.close()


def view():
	conn = sql.connect("little.db")
	cur = conn.cursor()

	cur.execute("SELECT * FROM store")
	rows = cur.fetchall()
	conn.close()
	return rows


def delete(item):
	conn = sql.connect("little.db")
	cur = conn.cursor()

	cur.execute("DELETE FROM store WHERE item=?", (item,))#comma for singel
	conn.commit()
	conn.close()


def update(quant, price, item):
	conn = sql.connect("little.db")
	cur = conn.cursor()

	cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quant, price, item))#no comma for multiple
	conn.commit()
	conn.close()

#insert('Coffee Cup', 10, 5)
#delete("Wine Glass")
update(11, 6, "Water Glass")

print(view())
