
class AsyncService():
    """Hides the async features of the qi sdk to make our code testable.
    """
    def future(self, action, *args):
        """Executes the action and returns a future for tracking the progress.

        Args:
            action (lambda): the action to execute asynchronously
        """
        pass