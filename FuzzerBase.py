from time import time
import matplotlib.pyplot as plt
class FuzzerBase():
    def __init__(self, name = ""):
        """Passing in empty string for name will use the class name for the fuzzer. Otherwise, it will use the custom name"""

        if name == "":
            self.fuzzer_name = type(self).__name__
        else:
            self.fuzzer_name = name

        self.tries_until_success = []
        self.successful_combo_count = []
        self.time_to_fuzz = []

        self.failure_count = 0

    def record_fuzz(self, success: bool, time_to_fuzz: int, tries_until_success: int = 0, successful_combo_count: int = 0):
        """Records a fuzz attempt.
        
        success -- whether the run was successful
        time_to_fuzz -- how long (in seconds) it took to run the complete fuzz
        tries_until_success -- how many attempts it took the attempt to find a successful type combo
        successful_combo_count -- how many successful combos were generated
        """
        if not success:
            self.failure_count += 1
            self.time_to_fuzz.append(time_to_fuzz)
            self.successful_combo_count.append(0)
            return
        
        self.time_to_fuzz.append(time_to_fuzz)
        self.tries_until_success.append(tries_until_success)
        self.successful_combo_count.append(successful_combo_count)

    def display_all_plots(self):
        """Displays all plots related to this fuzzer."""
        self.plot_time_to_fuzz()
        self.plot_successful_combos()
        self.plot_tries_until_success()


    def plot_time_to_fuzz(self):
        """Plots the total time taken per fuzz attempt."""
        plt.title(self.fuzzer_name + " Time Taken Per Run")
        plt.xlabel('Attempt')
        plt.ylabel('Time Taken (s)')
        plt.scatter(list(range(len(self.time_to_fuzz))), self.time_to_fuzz)
        plt.show()

    def plot_successful_combos(self):
        """Plots the amount of successful combos generated per run."""
        plt.title(self.fuzzer_name + " Combos Generated Per Run")
        plt.xlabel('Attempt')
        plt.ylabel('Successful Combinations Generated')
        plt.scatter(list(range(len(self.successful_combo_count))), self.successful_combo_count)
        plt.show()

    def plot_tries_until_success(self):
        """Plots the tries until success required per successful run."""
        plt.title(self.fuzzer_name + " Tries Until Success Per Run")
        plt.xlabel('Successful Attempt')
        plt.ylabel('Tries until Success')
        plt.scatter(list(range(len(self.tries_until_success))), self.tries_until_success)
        plt.show()
