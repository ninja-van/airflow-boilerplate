"""Test the validity of dags."""


def test_import_errors(dag_bag):
    """
    Tests that the DAG files can be imported by Airflow without errors.
    ie.
        - No exceptions were raised when processing the DAG files, be it timeout or other exceptions
        - The DAGs are indeed acyclic
            DagBag.bag_dag() checks for dag.test_cycle()
    """
    assert len(dag_bag.import_errors) == 0


def test_dags_has_task(dag_bag):
    for dag in dag_bag.dags.values():
        assert len(dag.tasks) > 0
