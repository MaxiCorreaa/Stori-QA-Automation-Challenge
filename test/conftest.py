from pathlib import PurePosixPath, Path

import pytest


STATUS_TEST = PurePosixPath.joinpath(Path(__file__).parent.parent).joinpath('steps_rtm/step_rtm.txt')


@pytest.hookimpl(trylast=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    status = report.outcome

    if status is not None:
        with open(STATUS_TEST, "w") as s:
            s.write(str(status))
