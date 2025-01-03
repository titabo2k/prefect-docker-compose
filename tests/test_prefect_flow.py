import pytest
import sys
import logging
from pathlib import Path

sys.path.insert(0, str(Path.joinpath(Path(__file__).parent, "../").resolve()))
from flows.flow import greetings

logger = logging.getLogger(__name__)


def test_flows_deployment():
    foo = greetings.from_source(
        source=str(Path.joinpath(Path(__file__).parent, "../flows").resolve()),
        entrypoint="flow.py:greetings",
    ).deploy(
        name="foo_deployment",
        parameters=dict(names=["arthur", "trillian", "ford", "marvin"]),
        work_pool_name="test_flow_pool",
    )
    logger.info(f"Deployment: {foo}")
