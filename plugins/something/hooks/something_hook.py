from airflow.hooks.base_hook import BaseHook


class SomethingHook(BaseHook):
    def __init__(self, *args, **kwargs):
        pass

    def get_conn(self):
        pass

    def get_records(self, sql):
        pass

    def get_pandas_df(self, sql):
        pass

    def run(self, sql):
        pass
