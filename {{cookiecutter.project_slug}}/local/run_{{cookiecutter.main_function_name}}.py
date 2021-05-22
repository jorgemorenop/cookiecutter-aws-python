from common_local.environment import setup_test_environment
from common_local.events import load_sample

FUNCTION_NAME = "{{cookiecutter.main_function_name}}"
setup_test_environment(FUNCTION_NAME)

def load_event(event_name):
    return load_sample(FUNCTION_NAME, event_name)

# TESTS

SAMPLE_1 = load_event("event_1")

if __name__ == '__main__':
    # Local test
    from f_{{cookiecutter.main_function_name}}.__main__ import main
    main(SAMPLE_1)
