myc=mydb.cursor()
myc.execute("create table if not exists ParkingSpot(SrNum varchar(25),Spot varchar(25));")

data = [
    ('A1', None),
    ('A2', None),
    ('A3', 'Parked'),
    ('B1', 'Parked'),
    ('B2', None),
    ('B3', 'Parked')
]


query = "INSERT INTO ParkingSpot (srnum, spot) VALUES (%s, %s);"

for row in data:
    myc.execute(query, row)

mydb.commit()

myc.close()