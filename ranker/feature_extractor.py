def extract_features(candidate):

    profile = candidate["profile"]

    skills = [
        s["name"].lower()
        for s in candidate["skills"]
    ]

    signals = candidate["redrob_signals"]

    return {

        # --------------------------
        # Profile
        # --------------------------
        "years":
            profile.get("years_of_experience", 0),

        "skills":
            skills,

        # --------------------------
        # Existing Signals
        # --------------------------
        "github":
            signals.get("github_activity_score", -1),

        "open_to_work":
            signals.get("open_to_work_flag", False),

        "response_rate":
            signals.get("recruiter_response_rate", 0),

        "interview_rate":
            signals.get("interview_completion_rate", 0),

        # --------------------------
        # Additional Behavioural Signals
        # --------------------------
        "profile_completeness":
            signals.get("profile_completeness_score", 0),

        "signup_date":
            signals.get("signup_date"),

        "last_active_date":
            signals.get("last_active_date"),

        "profile_views":
            signals.get("profile_views_received_30d", 0),

        "applications":
            signals.get("applications_submitted_30d", 0),

        "avg_response_time":
            signals.get("avg_response_time_hours", 999),

        "skill_assessments":
            signals.get("skill_assessment_scores", {}),

        "connections":
            signals.get("connection_count", 0),

        "endorsements":
            signals.get("endorsements_received", 0),

        "notice_period":
            signals.get("notice_period_days", 180),

        "salary":
            signals.get(
                "expected_salary_range_inr_lpa",
                {}
            ),

        "work_mode":
            signals.get(
                "preferred_work_mode",
                ""
            ),

        "relocate":
            signals.get(
                "willing_to_relocate",
                False
            ),

        "search_appearance":
            signals.get(
                "search_appearance_30d",
                0
            ),

        "saved_by_recruiters":
            signals.get(
                "saved_by_recruiters_30d",
                0
            ),

        "offer_acceptance":
            signals.get(
                "offer_acceptance_rate",
                -1
            ),

        "verified_email":
            signals.get(
                "verified_email",
                False
            ),

        "verified_phone":
            signals.get(
                "verified_phone",
                False
            ),

        "linkedin":
            signals.get(
                "linkedin_connected",
                False
            )
    }