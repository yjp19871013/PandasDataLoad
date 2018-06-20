import pandas as pd
import pymysql

from .DataAdapter import DataAdapter


class MysqlAdapter(DataAdapter):

    def __init__(self, repo_name):
        super(MysqlAdapter, self).__init__(repo_name)
        self.conn = None

    def connect(self, **kargs):
        print(kargs)
        host = kargs.get("host", "")
        port = kargs.get("port", "")
        user = kargs.get("user", "")
        passwd = kargs.get("passwd", "")
        db = kargs.get("db", "")
        charset = kargs.get("charset", "")
        self.conn = pymysql.connect(host=host,
                                    port=port,
                                    user=user,
                                    passwd=passwd,
                                    db=db,
                                    charset=charset)

    def disconnect(self):
        super().disconnect()

        if self.conn is not None:
            self.conn.close()

    def query_data(self, data_set, **kargs):
        if data_set in self._opened_data_set:
            if kargs is not None:
                sql = kargs.get("sql", "")
                if sql == "":
                    df = pd.read_sql("select * from " + data_set.data_set_name, con=self.conn)
                else:
                    df = pd.read_sql(sql, con=self.conn)
            else:
                df = pd.read_sql("select * from " + data_set.data_set_name, con=self.conn)

            data_set.data_set = df
