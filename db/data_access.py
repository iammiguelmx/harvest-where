import psycopg2
from db.config import config

def getInfoOfYearData(year):
	conn = None
	try:
		params = config()

		print('Connecting to the database...')
		conn = psycopg2.connect(**params)

		cur = conn.cursor()
		print('Consulting data')
		cur.execute('''SELECT 
						C.name,
						C.state,
						C.latitude,
						C.longitude,
						D.maxtemp,
						D.mintemp,
						D.avgtemp
					FROM city AS C
						 INNER JOIN
						 city_data AS CD
						 ON C.city_id = CD.city_id
						 INNER JOIN
						 data AS D
						 ON CD.data_id = D.data_id
					WHERE
						CD.year = 2060''')

		ciudad = []
		for row in cur:
			ciudad.append(row)

		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed')

if __name__ == '__main__':
    getInfoOfYearData(2060)