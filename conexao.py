import psycopg2
con = psycopg2.connect(host='localhost', database='read_pdf', user='postgres', password='laisa22')
cur = con.cursor()