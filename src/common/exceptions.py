class Ignore(Exception):
    """Raise this to stop the continuation"""


class ActionRequired(Exception):
    """Do the action specified in message!"""


class ActionInFuture(Exception):
    """
        You are trying to solve a future problem :)
        Have a little patient until that day.
    """
