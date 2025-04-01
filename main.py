import os
import sys

DEFAULT_VARS = ["DB_HOST", "API_KEY", "SECRET_KEY"]

def check_env_vars(vars_to_check):
    missing = []
    for var in vars_to_check:
        if not os.getenv(var):
            missing.append(var)
    return missing