import psycopg2      # todo (connect to the DBeaver)
conn = psycopg2.connect(dbname='qa_ddl_24_140', user='user_24_140', password='123', host='159.69.151.133', port='5056')
cursor = conn.cursor()
# if conn:
#     print('Connection qa_ddl_24_140')
#
#     select_query = 'select * from public.salary_2;'  # todo (select from public.salary_2)
#     execute_q = cursor.execute(select_query)
#
#     get_query_result = cursor.fetchall()
#     print('execute_q =', get_query_result)
#
#     for i in get_query_result:
#         # print('iq =', i)
#         print('iq =', i[0], 'salary =', i[1])

for i in range(0, 10):      # todo (insert to public.salary_2)
    if conn:
        print('Connection Insert qa_ddl_24_140')
        salary = 4000 + i * 100
        insert_query = 'insert info public.salary_2(monthly_salary)' \ 'values (' + str(salary) + ')'
        cursor.execute(insert_query)
        conn.commit()
cursor.close()
















