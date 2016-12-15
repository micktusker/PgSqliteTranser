class DataRetriever:
    '''
    Provides methods to execute SELECT SQL for a given Connection.
    '''
    def __init__(self, conn):
        '''
        Initialize with a Connection object. This can be for SQLite or PostgreSQL
        :param conn: Connection
        '''
        self._conn = conn
    def execute_sql(self, sql, params = tuple()):
        '''
        Create a cursor and execute the SELECT SQL argument
        :param sql
        :param  tuple
        :return: Cursor
        '''
        self._cur = self._conn.cursor()
        self._cur.execute(sql, params)
        return self._cur
    def get_column_names(self):
        '''
        Return a list of column names for the last executed SELECT in "execute_sql()".
        :return: list
        '''
        return [desc[0] for desc in self._cur.description]

if __name__ == '__main__':
    from pg_connection_creator import PgConnectionCreator
    pg_conn_creator = PgConnectionCreator('localhost', 5433, 'micktusker', 'cd38')
    pg_conn = pg_conn_creator.get_pg_connection()
    data_rtvr = DataRetriever(pg_conn)
    cur = data_rtvr.execute_sql('SELECT * FROM  lookups.tcga_cancer_codes WHERE tcga_cancer_code = %s', ('LAML',))
    print(data_rtvr.get_column_names())
    print(cur.fetchall())