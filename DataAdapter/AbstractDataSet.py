class AbstractDataSet:

    def __init__(self, repo_name, data_set_name):
        self.repo_name = repo_name
        self.data_set_name = data_set_name
        self.data_set = None

    def __str__(self):
        return str(self.data_set)
