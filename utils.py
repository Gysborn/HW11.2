import json


def load_candidates_from_json():  # которая загрузит данные из файла
    """
    Загружает из файла список кандидатов
    Возвращает list[dict]
    """
    with open('candidates.json', encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates


def get_candidate(pk: int) -> str:  # которая вернет кандидата по pk
    """

    :param pk: id candidate
    :return: форматированную колонку кандидата по id
    """
    candidates = load_candidates_from_json()
    for cand in candidates:
        if cand['pk'] == pk:
            return cand


def get_candidates_by_name(candidate_name):
    result = []
    for cand in load_candidates_from_json():
        if candidate_name in cand['name']:
            result.append(cand)
    return result


def get_candidates_by_skill(skill_name):
    result = []
    for cand in load_candidates_from_json():
        if skill_name.lower() in cand['skills'].lower().strip(', '):
            result.append(cand)
    return result


