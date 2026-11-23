"""Display your Homework 2 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "8543a3204fdb42d91d8ffaa30a70c2b0"
GRADE_HASH = "e4eac33a15b305b7308325a69a1a29ddd3e938f6898e790a3e6314d9bbd235e1"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 2: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
