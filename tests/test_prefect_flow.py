import pytest
import sys
import logging
from pathlib import Path
from uuid import UUID
from prefect.deployments import run_deployment
from icecream import ic

sys.path.insert(0, str(Path.joinpath(Path(__file__).parent, "../").resolve()))
from flows.flow import greetings

logger = logging.getLogger(__name__)


def test_flows_deployment():
    foo_deployment_uuid = greetings.from_source(
        source=str(Path.joinpath(Path(__file__).parent, "../flows").resolve()),
        entrypoint="flow.py:greetings",
    ).deploy(
        name="foo_deployment",
        parameters=dict(names=["arthur", "trillian", "ford", "marvin"]),
        work_pool_name="test_pool",
    )

    ic(foo_deployment_uuid)

    assert isinstance(foo_deployment_uuid, UUID)

    # Run the deployment
    flow_run = run_deployment(
        name="test_flow/foo_deployment",
        parameters=dict(names=["arthur", "trillian"]),
    )

    ic(flow_run)

    assert foo_deployment_uuid == flow_run.deployment_id
