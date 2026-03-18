from faker import Faker
from letters_mapping import runic_letters
import file_operations
import random
import os


SKILLS = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд",
]


def main():
    fake = Faker("ru_RU")
    runic_skills = []
    for skill in SKILLS:
        for old, new in runic_letters.items():
            skill = skill.replace(old, new)
        runic_skills.append(skill)
    for i in range(10):
        character_skills = random.sample(runic_skills, 3)
        context = {
            "first_name": fake.first_name_male(),
            "last_name": fake.last_name_male(),
            "job": fake.job(),
            "town": fake.city(),
            "strength": random.randint(3, 18),
            "agility": random.randint(3, 18),
            "endurance": random.randint(3, 18),
            "intelligence": random.randint(3, 18),
            "luck": random.randint(3, 18),
            "skill_1": character_skills[0],
            "skill_2": character_skills[1],
            "skill_3": character_skills[2]
        }
        os.makedirs("characters", exist_ok=True)
        output = "characters/character_{}.svg".format(i)
        file_operations.render_template("charsheet.svg", output, context)


if __name__ == "__main__":
    main()
