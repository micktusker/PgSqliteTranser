import psycopg2
class PgConnectionCreator:
    def __init__(self, host, port, user, dbname):
        '''

        :param host: str
        :param port: int
        :param user: str
        :param dbname: str
        '''
        self._conn = psycopg2.connect("dbname=%s user=%s host=%s port=%d" % (dbname, user, host, port))
    def get_pg_connection(self):
        '''
        Return the connection created at initialization
        :return: Connection
        '''
        return self._conn
if __name__ == '__main__':
    pg_conn_creator = PgConnectionCreator('localhost', 5433, 'micktusker', 'cd38')
    pg_conn = pg_conn_creator.get_pg_connection()
    print("ok!")
    pg_conn.close()