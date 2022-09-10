import json

def load_candidates():
    """"загрузка данных"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def candidates_all():
    """"возвращаем загруженные данные"""
    return load_candidates()

def get_by_pk(pk):
    """"возвращаем кандидата по заданному pk"""
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['pk'] == pk:
            return candidate
    return "Not found"

def get_by_skill(skill):
    """"возвращаем кандидата по заданному скилу"""
    result = []
    for candidate in load_candidates():
        skills = candidate["skills"].lower().split(', ')
        if skill in skills:
            result.append(candidate)
    return result





