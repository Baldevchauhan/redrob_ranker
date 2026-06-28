import heapq

from .feature_extractor import extract_features
from .scorer import score_candidate


def rank_candidates(candidates):

    top100 = []

    for candidate in candidates:

        features = extract_features(candidate)

        score = score_candidate(features)

        result = {
            "candidate_id": candidate["candidate_id"],
            "score": score,

            "experience": features["years"],
            "skills": features["skills"],

            "github": features["github"],
            "open_to_work": features["open_to_work"],
            "response_rate": features["response_rate"],
            "interview_rate": features["interview_rate"],
            "profile_completeness": features["profile_completeness"],
            "last_active_date": features["last_active_date"],
            "notice_period": features["notice_period"],
            "applications": features["applications"],
            "profile_views": features["profile_views"],
            "search_appearance": features["search_appearance"],
            "saved_by_recruiters": features["saved_by_recruiters"],
            "connections": features["connections"],
            "endorsements": features["endorsements"],
            "offer_acceptance": features["offer_acceptance"],
            "verified_email": features["verified_email"],
            "verified_phone": features["verified_phone"],
            "linkedin": features["linkedin"],
            "relocate": features["relocate"],
            "work_mode": features["work_mode"],
            "skill_assessments": features["skill_assessments"],
        }

        priority = (
            score,
            features["response_rate"],
            features["interview_rate"],
            features["github"],
            features["years"],
        )

        if len(top100) < 100:

            heapq.heappush(
                top100,
                (priority, result)
            )

        else:

            if priority > top100[0][0]:

                heapq.heapreplace(
                    top100,
                    (priority, result)
                )

    top100.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [
        item[1]
        for item in top100
    ]