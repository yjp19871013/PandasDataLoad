from .AbstractDataSet import AbstractDataSet


class DataAdapter:

    def __init__(self, repo_name):
        self._repo_name = repo_name
        self._opened_data_set = []

    '''
    连接数据源，必须调用
    '''
    def connect(self, **kargs):
        pass

    '''
    与数据源断开连接，connect后必须调用
    '''
    def disconnect(self):
        for ds in self._opened_data_set:
            self.close_data_set(ds)

    '''
    打开数据集，connect后调用
    '''
    def open_data_set(self, data_set_name, **kargs):
        data_set = AbstractDataSet(self._repo_name, data_set_name)
        self._opened_data_set.append(data_set)
        return data_set

    '''
    关闭数据集，打开后调用
    '''
    def close_data_set(self, data_set):
        if data_set in self._opened_data_set:
            self._opened_data_set.remove(data_set)

    '''
    请求数据
    '''
    def query_data(self, data_set, **kargs):
        pass
