from airflow.plugins_manager import AirflowPlugin

from something.hooks import SomethingHook
from something.operators import SomethingToSomethingOperator


class SomethingPlugin(AirflowPlugin):
    name = "something_plugin"
    operators = [SomethingToSomethingOperator]
    hooks = [SomethingHook]
    # Leave in for explicitness
    executors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []
