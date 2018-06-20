import os

from .MysqlAdapter import MysqlAdapter
from .ExcelAdapter import ExcelAdapter


class AdapterFactory:

    @staticmethod
    def create(repo_name):
        repo_name = repo_name.lower()
        extension = os.path.splitext(repo_name)[1]
        if extension == ".xlsx" or extension == ".xls":
            if os.path.exists(repo_name):
                adapter = ExcelAdapter(repo_name)
            else:
                raise Exception("文件不存在")
        elif repo_name == "mysql":
            adapter = AdapterFactory._create_db_adapter(repo_name)
        else:
            raise Exception("不支持的类型")

        return adapter

    @staticmethod
    def _create_db_adapter(db_name):
        adapter = None
        if db_name == "mysql":
            adapter = MysqlAdapter(db_name)

        return adapter
