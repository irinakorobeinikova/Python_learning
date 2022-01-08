import psycopg2      # todo (Connect to the DBeaver)
conn = psycopg2.connect(dbname='qa_ddl_24_140', user='user_24_140', password='123', host='159.69.151.133', port='5056')
cursor = conn.cursor()
if conn:
    print('Connection qa_ddl_24_140')



