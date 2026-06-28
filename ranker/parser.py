import json


def load_candidates(path):

    with open(path, "r", encoding="utf-8") as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            try:
                yield json.loads(line)

            except json.JSONDecodeError:
                # Skip invalid JSON lines
                continue