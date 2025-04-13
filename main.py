import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        data = json.load(file)

    for player in data:
        this_player_race = Race.objects.get_or_create(
            name=player["race"]["name"],
            description=player["race"]["description"])

        Skill.objects.get_or_create(
            name=player["race"]["skills"]["name"],
            bonus=player["race"]["skills"]["bonus"],
            race=this_player_race)

        Guild.objects.get_or_create(
            name=player["guild"]["name"],
            description=player["guild"]["description"])

        Player.objects.create(
            nickname=player[0],
            email=player["email"],
            bio=player["bio"],
            race=this_player_race,
            guild=Guild.objects.update_or_create(
                name=player["guild"]["name"],
                description=player["guild"]["description"]))


if __name__ == "__main__":
    main()
