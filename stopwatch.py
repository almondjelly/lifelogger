import datetime

class Stopwatch(object):
    """Stopwatch."""

    def __init__(self):
        pass


    def start_time(self):
        """Start the timer and note the current date and time."""
        
        self.start = datetime.datetime.now()

    
    def stop_time(self):
        """Stops the time and returns a message noting how much time passed."""

        self.stop = datetime.datetime.now()
        self.duration = self.stop - self.start
        self.hours, self.remainder = divmod(self.duration.seconds, 3600)
        self.minutes, self.seconds = divmod(self.remainder, 60) 
        self.message = "Duration: {}h {}m {}s".format(self.hours, 
                                                      self.minutes,
                                                      self.seconds)
        return self.duration


    def describe_task(self):
        """Asks user to describe the task associated with this time entry."""

        self.description = raw_input("Describe this task: ")
        return self.description


class ManualEntry(object):
    """Manual time entry."""

    def __init__(self):
        pass


    def start(self):
        """Enter start time."""

        self.start_tokens = raw_input("Start (Year Month Day Hour Minute): ")
        self.start_tokens = self.start_tokens.split()
        self.start_year = int(self.start_tokens[0])
        self.start_month = int(self.start_tokens[1])
        self.start_day = int(self.start_tokens[2])
        self.start_hour = int(self.start_tokens[3])
        self.start_minute = int(self.start_tokens[4])

        self.start = datetime.datetime(self.start_year, self.start_month, self.start_day, self.start_hour, self.start_minute)

        return self.start


    def stop(self):
        """Enter stop time."""

        self.stop_tokens = raw_input("Stop (Year Month Day Hour Minute): ")
        self.stop_tokens = self.stop_tokens.split()
        self.stop_year = int(self.stop_tokens[0])
        self.stop_month = int(self.stop_tokens[1])
        self.stop_day = int(self.stop_tokens[2])
        self.stop_hour = int(self.stop_tokens[3])
        self.stop_minute = int(self.stop_tokens[4])

        self.stop = datetime.datetime(self.stop_year, self.stop_month, self.stop_day, self.stop_hour, self.stop_minute)

        return self.stop


    def calculate_duration(self):
        """Calculates duration."""

        self.duration = self.stop - self.start
        self.hours, self.remainder = divmod(self.duration.seconds, 3600)
        self.minutes, self.seconds = divmod(self.remainder, 60) 
        self.message = "Duration: {}h {}m {}s".format(self.hours, 
                                                      self.minutes,
                                                      self.seconds)

        return self.duration


    def describe_task(self):
        """Asks user to describe the task associated with this time entry."""

        self.description = raw_input("Describe this task: ")
        return self.description


class Log(object):
    """Time entry log."""

    def __init__(self):
        self.entry_counter = 0
        self.entry_log = {}


    def create_stopwatch_entry(self):
        """Create a new time entry using the timer."""

        self.entry = Stopwatch()
        self.entry.start_time()
        self.stop_timer = raw_input("Press enter to stop the timer.")
        self.entry.describe_task()
        
        self.entry_counter += 1
        self.entry_log[self.entry_counter] = (self.entry.stop(), self.entry.description)

        return self.entry.message


    def create_manual_entry(self):
        """Create a new time entry manually."""

        self.entry = ManualEntry()
        self.entry.start_time()
        self.entry.stop_time()
        self.entry.describe_task()

        self.entry_counter += 1
        self.entry_log[self.entry_counter] = (self.entry.calculate_duration(), self.entry.description)

        return self.entry.message


    def print_log(self):

        for k, v in self.entry_log.items():
            print k, format_duration(v[0]), v[1]

        return


def format_duration(duration):
    """Formats duration to a friendly string."""

    hours, remainder = divmod(duration.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    duration_str = "{}h {}m {}s".format(hours, minutes, seconds)

    return duration_str




# log = Log()

def display_menu():
    """Displays menu to user and asks them to select an option."""

    menu = {1: "Create a new stopwatch entry",
                 2: "Create a new manual entry",
                 3: "Display your time report",
                 "exit": "Exit"}

    for k, v in menu.items():
        print k, "|", v

    print "Select an action from the menu"
    user_action = raw_input("> ")

    return user_action


def start_user_mode():
    """Starts user interface for time logging."""

    
    stop_program = False

    while stop_program == False:

        user_action = display_menu()

        if user_action == '1':
            log.create_stopwatch_entry()
            print
            print

        elif user_action == '2':
            log.create_manual_entry()
            print
            print
            
        elif user_action == '3':
            log.print_log()
            print
            print

        elif user_action == "exit":
             stop_program = True

    return

# start_user_mode()
