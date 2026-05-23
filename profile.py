class Founder:

    def __init__(self, name, skills, interests):

        self.name = name
        self.skills = skills
        self.interests = interests

    def display_profile(self):

        print("\nFounder Profile")
        print("Name:", self.name)
        print("Skills:", ", ".join(self.skills))
        print("Interests:", ", ".join(self.interests))


if __name__ == "__main__":

    founder = Founder(
        "Sujal",
        ["Python", "AI", "Flask"],
        ["EdTech", "Startups"]
    )

    founder.display_profile()