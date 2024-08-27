from itertools import product

from monotonic.GeneratorHelper import GeneratorHelper


class MonotonicFunctionGenerator:
    def __init__(self, n_of_a_r):
        self.n = n_of_a_r
        self.helper = GeneratorHelper()
        self.states_list = self.helper.generate_combinations_dict_list(n_of_a_r)
        self.mono = []

    def print_states(self) -> None:
        for combo in self.states_list:
            print(combo)

    def generate_all_functions(self):
        """
        Generate all possible Boolean functions for given state combinations.

        :param states: List of state combinations, e.g., [(0, 0), (0, 1), ...]
        :return: List of dictionaries where each dictionary represents a Boolean function
        """
        num_states = len(self.states_list)
        all_functions = []

        # Generate all possible mappings for the states to either 0 or 1
        for values in product([0, 1], repeat=num_states):
            function = dict(zip(self.states_list, values))
            all_functions.append(function)

        return all_functions

    def print_all_functions(self):
        for idx, func in enumerate(self.generate_all_functions()):
            print(f"Function {idx + 1}: {func}")

    def generate_monotonic_functions(self):
        for idx, func in enumerate(self.generate_all_functions()):
            if (self.helper.is_monotonic(func, self.states_list, self.n)):
                self.mono.append(func)

        # remove 0 and 1:
        self.mono.pop(0)
        self.mono.pop()
        self.mono = sorted(self.mono, key=lambda d: [d[key] for key in sorted(d.keys())])

        return self.mono

    def print_mono(self):
        for idx, func in enumerate(self.mono):
            print(f"Function {idx + 1}: {func}")


    # Example usage:
mono = MonotonicFunctionGenerator(2)

mono.generate_monotonic_functions()
mono.print_mono()
print(mono.mono)