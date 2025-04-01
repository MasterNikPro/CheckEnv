import os
import sys

DEFAULT_VARS = ["DB_HOST", "API_KEY", "SECRET_KEY"]

def check_env_vars(vars_to_check):
    missing = []
    for var in vars_to_check:
        if not os.getenv(var):
            missing.append(var)
    return missing
    
if __name__ == "__main__":
    vars_to_check = sys.argv[1:] if len(sys.argv) > 1 else DEFAULT_VARS
    missing = check_env_vars(vars_to_check)
    if missing:
        print("❌ Missing environment variables:")
        for var in missing:
            print(f" - {var}")
        exit(1)
    else:
        print("✅ All environment variables are set.")