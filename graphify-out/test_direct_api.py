import os
import sys
import json
from pathlib import Path
from graphify.llm import extract_files_direct

# Copy ANTHROPIC_AUTH_TOKEN to ANTHROPIC_API_KEY
if "ANTHROPIC_AUTH_TOKEN" in os.environ:
    os.environ["ANTHROPIC_API_KEY"] = os.environ["ANTHROPIC_AUTH_TOKEN"]

def main():
    test_file = Path("projects/1_app/app.py")
    if not test_file.exists():
        print(f"Test file {test_file} does not exist!")
        return

    print("Attempting to run extract_files_direct on projects/1_app/app.py using backend='claude'...")
    try:
        res = extract_files_direct(
            files=[test_file],
            backend="claude",
            root=Path("c:/Users/Apu Ghanti/Desktop/docker")
        )
        print("Success!")
        print(f"Nodes found: {len(res.get('nodes', []))}")
        print(f"Edges found: {len(res.get('edges', []))}")
    except Exception as e:
        import traceback
        print("Failed with exception:")
        traceback.print_exc()

if __name__ == "__main__":
    main()
