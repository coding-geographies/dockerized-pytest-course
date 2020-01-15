from datetime import datetime
import pytest
from scripts.fitness_log import FitnessLog


@pytest.fixture(scope='function')
def create_tracker():
    fitness_tracker = FitnessLog()

    start_time = datetime(year=2017, month=1, day=1, hour=5, minute=12)
    end_time = datetime(year=2017, month=1, day=1, hour=5, minute=55)
    # breakpoint()
    fitness_tracker.log_activity("run", start_time, end_time)

    yield fitness_tracker


def test_add_valid_activities(create_tracker):
    fitness_tracker = create_tracker
    # breakpoint()
    activities = fitness_tracker.get_activities()

    assert len(activities) == 1
    assert activities[0][0] == 'run'


@pytest.fixture(scope='session')
def create_overlapping_times():
    overlapping_start_time = datetime(year=2017, month=1, day=1, hour=5, minute=14)
    overlapping_end_time = datetime(year=2017, month=1, day=1, hour=5, minute=53)

    return overlapping_start_time, overlapping_end_time


def test_add_invalid_activity(create_tracker, create_overlapping_times):
    fitness_tracker = create_tracker
    overlapping_start_time, overlapping_end_time = create_overlapping_times

    with pytest.raises(Exception) as exp:
        fitness_tracker.log_activity("run", overlapping_start_time, overlapping_end_time)

    assert str(exp.value) == ('A new activity must not conflict with a logged activity. ' +
                              'Please delete the old activity before proceeding')


# Newly added test
def test_delete_activity(create_tracker):
    fitness_tracker = create_tracker

    activities = fitness_tracker.get_activities()
    assert len(activities) == 1

    activity = activities[0][0]
    start_time = activities[0][1]
    end_time = activities[0][2]
    fitness_tracker.delete_activity(activity, start_time, end_time)

    activities = fitness_tracker.get_activities()
    assert len(activities) == 0
