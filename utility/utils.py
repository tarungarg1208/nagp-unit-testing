import datetime


class Utility:

    @staticmethod
    def get_current_time():
        """return the current hour and minute in a dict """
        hour = datetime.datetime.now().hour
        min = datetime.datetime.now().minute
        return dict(hour=hour, min=min)

    @staticmethod
    def is_trading_allowed():
        """returns True if trading is allowed at current time"""
        start = datetime.time(9, 0, 0)
        end = datetime.time(17, 0, 0)
        current = get_time()
        dow = get_dow()
        return (start <= current <= end) and (0 <= dow <= 4)

def get_time():
    """returns current time"""
    return datetime.datetime.now().time()

def get_dow():
    """returns dow"""
    return datetime.datetime.now().weekday()