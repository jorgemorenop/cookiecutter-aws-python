import os
from dotenv import load_dotenv


def load_environment_vars():
    load_dotenv()


def setup_test_environment(function_name):
    load_environment_vars()
    sources_dir = os.path.join(os.path.dirname(__file__), "..", "..",
                               "functions", function_name)
    # sys.path.append(sources_dir)
    os.chdir(sources_dir)
