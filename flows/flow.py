from prefect import flow, task
from pathlib import Path


@task
def say_hello(name):
    print(f"hello {name}")


@task
def say_goodbye(name):
    print(f"goodbye {name}")


@flow(name="test flow")
def greetings(names=["arthur", "trillian", "ford", "marvin"]):
    for name in names:
        say_hello(name)
        say_goodbye(name)


if __name__ == "__main__":
    greetings.from_source(
        source=str(Path(__file__).parent),
        entrypoint="flow.py:greetings",
    ).deploy(
        name="foo_deployment",
        parameters=dict(names=["arthur", "trillian", "ford", "marvin"]),
        work_pool_name="test_flow_pool",
    )
