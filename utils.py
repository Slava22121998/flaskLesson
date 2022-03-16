import json


def load_candidates_from_json():
    with open('static/candidates.json', encoding="UTF-8") as file_json:
        return json.load(file_json)


def get_candidate(candidate_id):
    for candidate in load_candidates_from_json():
        if candidate_id == candidate["id"]:
            return candidate


def get_candidates_by_name(candidate_name):
    names_list = list()
    for candidate in load_candidates_from_json():
        if candidate_name.lower() == candidate["name"].lower().split(" ")[0]:
            names_list.append(candidate)

    return names_list


def get_candidates_by_skill(skill_name):
    skills_list = list()
    for candidate in load_candidates_from_json():
        if skill_name.lower() in candidate["skills"].lower().split(", "):
            skills_list.append(candidate)

    return skills_list
