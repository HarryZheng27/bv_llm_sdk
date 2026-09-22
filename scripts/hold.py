"""Hold the vehicle's position for 10 seconds.

Usage:
    uv run scripts/hold.py
"""

from bv_llm_sdk import hold

if __name__ == "__main__":
    hold()
    print("held position for 10s")
