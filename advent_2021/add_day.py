import sys

if __name__ == "__main__":
    day = sys.argv[1]
    
    
    with open(f"inputs/{day}", "w"), open(f"tests/test_day_{day}.py", "w"), open(f"day_{day}.py", "w") as d:
        d.write("""
from typing import Any

def run(input_text: str) -> Any:
    return         
""")