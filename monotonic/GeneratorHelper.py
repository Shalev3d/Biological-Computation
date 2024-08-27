class GeneratorHelper:

    def generate_combinations_dict_list(self, number_of_a_r : int) -> list[tuple[int, int]]:
        """
        Generates a list of dictionaries, where each dictionary contains the number of active
        activators and active repressors for a system with `n` activators and `n` repressors.

        Each dictionary has keys 'activators' and 'repressors'.

        :param n: Number of activators and repressors
        :return: List of dictionaries with 'activators' and 'repressors' keys
        """
        combinations_list = [
            (a,  r)
            for a in range(number_of_a_r + 1) for r in range(number_of_a_r + 1)
        ]
        return combinations_list

    def print_combinations(self, combinations_list: list[tuple[int, int]]) -> None:
        for combo in combinations_list:
            print(combo)

    def is_monotonic(self, func, states: list[tuple[int,int]], n):
        """
        Checks if a given Boolean function is monotonic with respect to activators and repressors.

        A function is monotonic if:
        - It does not decrease as activators are turned on.
        - It does not decrease as repressors are turned on.

        :param function: Dictionary where keys are (activators, repressors) and values are 0 or 1
        :return: True if the function is monotonic, False otherwise
        """
        # Check monotonicity with respect to activators
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                (a1, r1) = states[i]
                (a2, r2) = states[j]
                if (a1 <= a2 and r1 == r2) and func[(a1, r1)] > func[(a2, r2)]:
                    return False

        # Check monotonicity with respect to repressors
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                (a1, r1) = states[i]
                (a2, r2) = states[j]
                if (a1 == a2 and r1 <= r2) and func[(a1, r1)] < func[(a2, r2)]:
                    return False

        return True


