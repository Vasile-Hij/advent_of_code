class Ignore(Exception):
    """Raise this to stop the continuation"""
    pass

    
class ActionRequired(Exception):
    """Do the action specified in message!"""
    pass


class ActionInFuture(Exception):
    """
        You are trying to solve a future problem :)
        Have a little patient until that day.
    """
    pass

