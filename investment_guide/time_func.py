import datetime


def added_time(mins):
    """
    Gets the immediate time and adds some minutes to the current time
    """
    time_ = datetime.datetime.now()
    new_time = (time_ + datetime.timedelta(minutes=mins))
    return new_time

# print(added_time(30))


def time_difference(open_time, close_time):
    format = "%H:%M"
    time_delta = datetime.datetime.strptime(close_time, format) - \
        datetime.datetime.strptime(open_time, format)
    return time_delta.seconds


# print(time_difference("10:33:26", "11:15:49"))
# print(datetime.datetime.now())