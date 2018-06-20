import pandas as pd

from .DataAdapter import DataAdapter


class ExcelAdapter(DataAdapter):

    def __init__(self, repo_name):
        super(ExcelAdapter, self).__init__(repo_name)

    def query_data(self, data_set, **kargs):
        if data_set in self._opened_data_set:
            df = pd.read_excel(self._repo_name, data_set.data_set_name)
            data_set.data_set = df
