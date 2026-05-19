import subprocess
import json
import os

def test():
    user_message = "Hello, respond with JSON node: {'id': 'test'}"
    _EXTRACTION_SYSTEM = "You are a helpful assistant. Output JSON."
    
    envs_to_test = [
        {"CI": "true"},
        {"CLAUDE_CODE_SIMPLE": "1"},
        {"TERM": "dumb"},
        {"CI": "true", "CLAUDE_CODE_SIMPLE": "1"},
        {"FORCE_COLOR": "0", "CI": "true"},
    ]
    
    for idx, env_override in enumerate(envs_to_test):
        print(f"\n--- Testing Env {idx}: {env_override} ---")
        my_env = os.environ.copy()
        my_env.update(env_override)
        try:
            proc = subprocess.run(
                [
                    "claude", "-p",
                    "--output-format", "json",
                    "--no-session-persistence",
                    "--append-system-prompt", _EXTRACTION_SYSTEM,
                ],
                input=user_message,
                capture_output=True,
                text=True,
                encoding="utf-8",
                env=my_env,
                timeout=15, # Use a small timeout so we don't hang too long if it fails
                check=False,
            )
            print(f"Return code: {proc.returncode}")
            print(f"Stdout:\n{proc.stdout}")
            print(f"Stderr:\n{proc.stderr}")
        except subprocess.TimeoutExpired:
            print("TIMEOUT EXPIRED")

if __name__ == "__main__":
    test()
