import json

def load_candidates(path):

    candidates = []

    with open(path, "r", encoding="utf-8") as f:

        for line in f:

            if line.strip():
                candidates.append(
                    json.loads(line)
                )

    return candidates