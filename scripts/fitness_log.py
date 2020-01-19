from datetime import datetime

class FitnessLog:
    def __init__(self, activities=None):
        self._activities = activities if activities is not None else []


    def log_activity(self, kind, start_time, end_time):
        if self.validate_entry(start_time, end_time) and not self.overlapping_entry(start_time, end_time):
            self._activities.append([kind, start_time, end_time])
        else:
            raise Exception('A new activity must not conflict with a logged activity. ' +
                             'Please delete the old activity before proceeding')


    def validate_entry(self, start_time, end_time):
        if start_time.year == end_time.year and \
                start_time.month == end_time.month and \
                start_time.day == end_time.day and \
                    start_time < end_time:
                    return True
        else:
            return False


    def overlapping_entry(self, start_time, end_time):
        if self._activities == []:
            return False
        else:
            not_overlapping = True
            for exercise in self._activities:
                logged_start = exercise[1]
                logged_end = exercise[2]
                not_overlapping = (start_time < logged_end) and (end_time > logged_start)
                if not_overlapping == False:
                    return not_overlapping
            return not_overlapping


    def delete_activity(self, kind, start_time, end_time):
        for idx, activity in enumerate(self._activities):
            if activity[0] == kind and activity[1] == start_time and activity[2] == end_time:
                del self._activities[idx]


    def get_activities(self):
        return self._activities
