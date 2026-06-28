from config import *
from datetime import datetime


def score_candidate(features):

    score = 0.0

    # ==================================================
    # REQUIRED SKILLS (25)
    # ==================================================

    required_matches = sum(
        1
        for skill in REQUIRED_SKILLS
        if skill.lower() in features["skills"]
    )

    score += (
        required_matches /
        len(REQUIRED_SKILLS)
    ) * 25


    # ==================================================
    # PREFERRED SKILLS (8)
    # ==================================================

    preferred_matches = sum(
        1
        for skill in PREFERRED_SKILLS
        if skill.lower() in features["skills"]
    )

    score += (
        preferred_matches /
        len(PREFERRED_SKILLS)
    ) * 8


    # ==================================================
    # EXPERIENCE (12)
    # ==================================================

    years = features["years"]

    if 5 <= years <= 9:

        score += 12

    elif 4 <= years < 5:

        score += 10

    elif 9 < years <= 12:

        score += 10

    elif 3 <= years < 4:

        score += 8

    elif 12 < years <= 15:

        score += 8

    elif years > 15:

        score += 6


    # ==================================================
    # OPEN TO WORK (3)
    # ==================================================

    if features["open_to_work"]:

        score += 3


    # ==================================================
    # RECRUITER RESPONSE RATE (4)
    # ==================================================

    response = max(
        0,
        min(
            features["response_rate"],
            1
        )
    )

    score += response * 4


    # ==================================================
    # INTERVIEW COMPLETION RATE (4)
    # ==================================================

    interview = max(
        0,
        min(
            features["interview_rate"],
            1
        )
    )

    score += interview * 4


    # ==================================================
    # GITHUB ACTIVITY (4)
    # ==================================================

    github = features["github"]

    if github != -1:

        github = max(
            0,
            min(
                github,
                100
            )
        )

        score += (
            github / 100
        ) * 4


    # ==================================================
    # PROFILE COMPLETENESS (4)
    # ==================================================

    profile = max(
        0,
        min(
            features["profile_completeness"],
            100
        )
    )

    score += (
        profile / 100
    ) * 4

    # ==================================================
    # LAST ACTIVE DATE (4)
    # ==================================================

    days = 9999

    try:

        last_active = datetime.strptime(
            features["last_active_date"],
            "%Y-%m-%d"
        )

        days = (
            datetime.now() -
            last_active
        ).days

        if days <= 7:

            score += 4

        elif days <= 30:

            score += 3

        elif days <= 90:

            score += 2

        elif days <= 180:

            score += 1

    except Exception:

        pass


    # ==================================================
    # NOTICE PERIOD (3)
    # ==================================================

    notice = features["notice_period"]

    if notice <= 15:

        score += 3

    elif notice <= 30:

        score += 2.5

    elif notice <= 60:

        score += 2

    elif notice <= 90:

        score += 1


    # ==================================================
    # SKILL ASSESSMENT (4)
    # ==================================================

    assessments = features["skill_assessments"]

    if assessments:

        avg = (
            sum(assessments.values()) /
            len(assessments)
        )

        score += (
            avg / 100
        ) * 4


    # ==================================================
    # SEARCH APPEARANCE (3)
    # ==================================================

    search = min(
        features["search_appearance"],
        100
    )

    score += (
        search / 100
    ) * 3


    # ==================================================
    # SAVED BY RECRUITERS (3)
    # ==================================================

    saved = min(
        features["saved_by_recruiters"],
        50
    )

    score += (
        saved / 50
    ) * 3


    # ==================================================
    # PROFILE VIEWS (2)
    # ==================================================

    views = min(
        features["profile_views"],
        100
    )

    score += (
        views / 100
    ) * 2


    # ==================================================
    # APPLICATIONS SUBMITTED (2)
    # ==================================================

    applications = min(
        features["applications"],
        50
    )

    score += (
        applications / 50
    ) * 2


    # ==================================================
    # CONNECTIONS (2)
    # ==================================================

    connections = min(
        features["connections"],
        500
    )

    score += (
        connections / 500
    ) * 2


    # ==================================================
    # ENDORSEMENTS (2)
    # ==================================================

    endorsements = min(
        features["endorsements"],
        100
    )

    score += (
        endorsements / 100
    ) * 2

    # ==================================================
    # OFFER ACCEPTANCE RATE (3)
    # ==================================================

    offer = features["offer_acceptance"]

    if offer >= 0:

        score += offer * 3


    # ==================================================
    # VERIFIED EMAIL (2)
    # ==================================================

    if features["verified_email"]:

        score += 2


    # ==================================================
    # VERIFIED PHONE (2)
    # ==================================================

    if features["verified_phone"]:

        score += 2


    # ==================================================
    # LINKEDIN CONNECTED (2)
    # ==================================================

    if features["linkedin"]:

        score += 2


    # ==================================================
    # WILLING TO RELOCATE (2)
    # ==================================================

    if features["relocate"]:

        score += 2


    # ==================================================
    # PREFERRED WORK MODE (2)
    # ==================================================

    if features["work_mode"] in [

        "remote",

        "hybrid",

        "flexible"

    ]:

        score += 2


    # ==================================================
    # RISK / HONEYPOT DETECTION
    # ==================================================

    penalty = 0
    risk = 0

    # Strong skills but very little experience
    if (
        required_matches >= len(REQUIRED_SKILLS) * 0.8
        and years < 2
    ):
        penalty += 8
        risk += 2

    # Unrealistic GitHub
    if (
        github >= 90
        and years < 1
    ):
        penalty += 5
        risk += 2

    # Poor profile
    if profile < 50:
        penalty += 5
        risk += 1

    # Recruiters ignore candidate
    if response < 0.20:
        penalty += 5
        risk += 2

    # Never completes interviews
    if interview < 0.20:
        penalty += 5
        risk += 2

    # Inactive account
    if days > 180:
        penalty += 4
        risk += 1

    # Keyword stuffing
    skill_count = len(features["skills"])

    if skill_count > 40:
        penalty += 4
        risk += 2

    # Missing verification
    if not features["verified_email"]:
        penalty += 2
        risk += 1

    if not features["verified_phone"]:
        penalty += 2
        risk += 1

    # Long notice period
    if notice > 90:
        penalty += 3
        risk += 1

    # Strong skills but invisible profile
    if (
        required_matches >= len(REQUIRED_SKILLS) * 0.8
        and search < 5
    ):
        penalty += 4
        risk += 2

    # Poor offer acceptance
    if (
        offer >= 0
        and offer < 0.30
    ):
        penalty += 3
        risk += 1

    # Applying everywhere but nobody replies
    if (
        applications > 30
        and response < 0.15
    ):
        penalty += 4
        risk += 2

    # Many profile views but almost no interviews
    if (
        views > 50
        and interview < 0.10
    ):
        penalty += 3
        risk += 1

    # Huge network but no endorsements
    if (
        connections > 300
        and endorsements < 5
    ):
        penalty += 2
        risk += 1

    # Excellent GitHub but no recruiter engagement
    if (
        github > 90
        and response < 0.20
    ):
        penalty += 3
        risk += 1

    # Apply fixed penalties
    score -= penalty

    if score < 0:
        score = 0


    # ==================================================
    # RISK MULTIPLIER
    # ==================================================

    if risk >= 8:

        score *= 0.65

    elif risk >= 6:

        score *= 0.75

    elif risk >= 4:

        score *= 0.85

    elif risk >= 2:

        score *= 0.93


    # ==================================================
    # FINAL NORMALIZATION
    # ==================================================

    MAX_SCORE = 106

    score = (score / MAX_SCORE) * 100

    score = max(
        0,
        min(score, 100)
    )

    return round(score, 2)