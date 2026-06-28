from .feature_extractor import extract_features
from .scorer import score_candidate


def rank_candidates(candidates):

    results = []

    for candidate in candidates:

        features = extract_features(candidate)

        score = score_candidate(features)

        results.append(
            {
                # Basic
                "candidate_id": candidate["candidate_id"],
                "score": score,
                # Profile
                "experience": features["years"],
                "skills": features["skills"],
                # Behaviour
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
        )

    results.sort(
        key=lambda x: (
            x["score"],
            x["response_rate"],
            x["interview_rate"],
            x["github"],
            x["experience"],
        ),
        reverse=True,
    )

    return results[:100]
