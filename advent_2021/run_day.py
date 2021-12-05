import sys
from importlib import import_module

if __name__ == "__main__":
    day = sys.argv[1]
    with open(f"inputs/{day}") as f:
        run = getattr(import_module(f"day_{day}"), "run")
        print(run(f.read().strip()))