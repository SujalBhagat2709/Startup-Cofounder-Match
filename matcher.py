from profile import Founder

def find_match(founder1, founder2):

    common_skills = set(founder1.skills) & set(founder2.skills)

    common_interests = (
        set(founder1.interests)
        & set(founder2.interests)
    )

    score = (
        len(common_skills) * 2
        + len(common_interests)
    )

    return {
        "match_score": score,
        "common_skills": list(common_skills),
        "common_interests": list(common_interests)
    }


if __name__ == "__main__":

    founder1 = Founder(
        "Sujal",
        ["Python", "AI", "Flask"],
        ["EdTech", "Startups"]
    )

    founder2 = Founder(
        "Rahul",
        ["Python", "React", "AI"],
        ["Startups", "FinTech"]
    )

    result = find_match(
        founder1,
        founder2
    )

    print("\nMatch Result")
    print(result)