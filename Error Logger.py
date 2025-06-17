import functools

class LoggerWithHistory():
    def __init__(self, name, max_entries=5):
        # TODO: Initialize LoggerWithHistory object
        self.name = name
        self.max_entries = max_entries
        self.log_entries = []
        self.serial = 0

    def write(self, message):
        # TODO: Process the message input
        if len(self.log_entries) >= self.max_entries:
            self.log_entries.pop(0)
        self.log_entries.append(tuple((self.serial, message)))
        self.serial +=1

    def __getitem__(self, key):
        # TODO: Return the log message at index `key`
        return self.log_entries[key]


    def __iter__(self):
        # No need to change this part of the code!
        # This is a big hint.
        return self.log_entries.__iter__()

    def __str__(self):
        # TODO: Return a string containing information about this logger in the
        #       specified format
        return f'Logger "{self.name}" with {len(self.log_entries)} message(s)'

def log_error(logger):
    def d_log_error(fcn):
        @functools.wraps(fcn)
        def wrapper(*args, **kwargs):
            # TODO: Write contents of this wrapper function.
            #
            try:
                fcn(*args, **kwargs)
            except Exception as e:
                logger.write(f'Error encountered in function {fcn.__name__}: {str(e)}')
            # HINT: We want to execute the function and handle
            #       any exceptions that it may encounter.
            #       If there is an exception, we should write the
            #       error in `logger`.
            #
            # HINT: The name of a function can be accessed using
            #       the `__name__` property.
            #
            # HINT: Don't forget to pass the parameters of the function
            #       to decorate! They are contained in *args and **kwargs.

        return wrapper
    
    return d_log_error

def main():
    print('into the sky')

if __name__ == '__main__':
    main()