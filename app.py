import os
import requests
from flask import Flask, jsonify, send_file
from flask_cors import CORS
import pandas as pd

from ranker.parser import load_candidates
from ranker.rank import rank_candidates

from ranker.feature_extractor import extract_features
from ranker.scorer import score_candidate

app = Flask(__name__)
CORS(app)

DATASET_PATH = "data/candidates.jsonl"

DATASET_URL = "https://huggingface.co/datasets/WHITE3HACKER/Baldevchauhan_redrob-dataset/resolve/main/candidates.jsonl"


def download_dataset():

    print("Downloading dataset...")

    os.makedirs("data", exist_ok=True)

    response = requests.get(DATASET_URL, stream=True)

    response.raise_for_status()

    total = 0

    with open(DATASET_PATH, "wb") as file:

        for chunk in response.iter_content(1024 * 1024):

            if chunk:

                file.write(chunk)

                total += len(chunk)

                print(f"\rDownloaded: {total / 1024 / 1024:.2f} MB", end="")

    print("\nDataset downloaded successfully.")


if not os.path.exists(DATASET_PATH):
    download_dataset()


top100 = None


def generate_reasoning(candidate):

    reasons = []

    if candidate["experience"] >= 5:
        reasons.append(f"{candidate['experience']} years of relevant experience")

    important = [
        "python",
        "retrieval",
        "ranking",
        "embeddings",
        "llm",
        "rag",
        "faiss",
        "pinecone",
        "weaviate",
        "qdrant",
    ]

    matched = [skill for skill in candidate["skills"] if skill in important]

    if matched:
        reasons.append("Strong skills in " + ", ".join(matched[:3]))

    if candidate["github"] >= 70:
        reasons.append("High GitHub activity")

    if candidate["response_rate"] >= 0.8:
        reasons.append("Excellent recruiter response rate")

    if candidate["interview_rate"] >= 0.8:
        reasons.append("Strong interview completion record")

    if candidate["profile_completeness"] >= 80:
        reasons.append("Highly complete profile")

    if candidate["verified_email"]:
        reasons.append("Verified email")

    if candidate["verified_phone"]:
        reasons.append("Verified phone")

    if candidate["linkedin"]:
        reasons.append("LinkedIn connected")

    if candidate["open_to_work"]:
        reasons.append("Open to work")

    if not reasons:
        return "Reasonable overall candidate profile."

    return ". ".join(reasons) + "."


top100 = None

@app.route("/api/candidates")
def get_candidates():

    df = pd.read_csv("output/registration-.csv")

    return jsonify(
        df.to_dict(orient="records")
    )


@app.route("/api/candidate/<candidate_id>")
def get_candidate(candidate_id):

    candidates = load_candidates(DATASET_PATH)

    for candidate in candidates:

        if candidate["candidate_id"] == candidate_id:

            features = extract_features(candidate)

            score = score_candidate(features)

            return jsonify(
                {"candidate_id": candidate["candidate_id"], "score": score, **features}
            )

    return jsonify({"error": "Candidate not found"}), 404


@app.route("/api/export")
def export_csv():

    global top100

    if top100 is None:

        candidates = load_candidates(DATASET_PATH)

        top100 = rank_candidates(candidates)

    rows = []

    for index, candidate in enumerate(top100, start=1):

        rows.append(
            {
                "candidate_id": candidate["candidate_id"],
                "rank": index,
                "score": candidate["score"],
                "reasoning": generate_reasoning(candidate),
            }
        )

    os.makedirs("output", exist_ok=True)

    csv_file = "output/registration-no.csv"

    df = pd.DataFrame(rows)

    df.to_csv(csv_file, index=False)

    return send_file(csv_file, as_attachment=True)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)
