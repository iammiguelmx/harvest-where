import psycopg2
from config import config

def create_tables():
	conn = None
	try:
		params = config()

		print('Connecting to the database...')
		conn = psycopg2.connect(**params)

		cur = conn.cursor()

		print('Creating table city')
		cur.execute('CREATE TABLE IF NOT EXISTS City ( city_id SERIAL PRIMARY KEY, name VARCHAR(150) NOT NULL, state VARCHAR(150) NOT NULL);')
		print('Creating table data')
		cur.execute('CREATE TABLE IF NOT EXISTS Data (data_id SERIAL PRIMARY KEY, maxTemp NUMERIC(5, 2), minTemp NUMERIC(5, 2), avgTemp NUMERIC(5, 2), avgRain NUMERIC(8,2));')
		print('Creating table city_data')
		cur.execute('CREATE TABLE IF NOT EXISTS City_data ( city_id INTEGER REFERENCES City(city_id), data_id INTEGER REFERENCES Data(data_id), year INTEGER NOT NULL, PRIMARY KEY (city_id, data_id) );')

		conn.commit()
		cur.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
			print('Database connection closed')

if __name__ == '__main__':
    create_tables()