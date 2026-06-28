from flask import Flask, jsonify, send_file
import pandas as pd

from ranker.parser import load_candidates
from ranker.rank import rank_candidates

app = Flask(__name__)

candidates = load_candidates("data/candidates.jsonl")
top100 = rank_candidates(candidates)


@app.route("/api/candidates")
def candidates_api():
    return jsonify(top100)


@app.route("/api/export")
def export_csv():

    rows = []

    for idx, candidate in enumerate(top100, start=1):
        rows.append(
            {
                "candidate_id": candidate["candidate_id"],
                "rank": idx,
                "score": candidate["score"],
            }
        )

    df = pd.DataFrame(rows)

    csv_path = "output/top100.csv"
    df.to_csv(csv_path, index=False)

    return send_file(csv_path, as_attachment=True, download_name="changetoregistration.csv")


if __name__ == "__main__":
    app.run(debug=True)
