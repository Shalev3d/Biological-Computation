A Python tool for generating and filtering monotonic Boolean functions based on the number of activators and repressors.

The code works generically for any number of activators and repressors (n). In the provided tests, we verified the implementation with n = 2, but you can adjust n in MonotonicFunctionGenerator to test with different values.


### Running the Project

To run the project, execute the `main.py` file:

```bash
python main.py
```

### This project provides two main classes:

1. **GeneratorHelper**: Generates combinations of activators and repressors and checks for monotonicity in Boolean functions.
2. **MonotonicFunctionGenerator**: Utilizes `GeneratorHelper` to generate all possible Boolean functions and filter out those that are monotonic.

## Key MethodsM

- `generate_combinations_dict_list(n)`: Generates combinations of activators and repressors.
- `is_monotonic(func, states, n)`: Checks if a Boolean function is monotonic.
- `generate_all_functions()`: Generates all possible Boolean functions for given states.
- `generate_monotonic_functions()`: Filters and returns monotonic Boolean functions.


