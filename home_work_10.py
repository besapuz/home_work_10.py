import json

from flask import Flask, render_template

app = Flask(__name__)

with open('candidates.json', 'r', encoding='utf8') as file:
    user_dict = json.load(file)


def iteration_list(index):
    """Делает вложенный словарь с ключем id"""
    for r in user_dict:
        if index == r["id"]:
            skills = r["skills"]
            name = r["name"]
            position = r["position"]
            picture = r["picture"]
            return picture, name, position, skills


def add_skills_dict(sk):
    """Выполняет поиск навыков в skills"""
    skill_dict = []
    sk = sk.lower()
    for value in user_dict:
        b = value["skills"].lower()
        s = b.split(", ")
        if sk in s:
            skill_dict.append(value)
    return skill_dict


@app.route("/")
def return_index():
    return f"<h1>Гавная страница</h1> {render_template('index.html', user=user_dict)}"


@app.route("/candidate/<int:index>")
def outputs_user(index):
    set_ = iteration_list(index)
    return f"{render_template('user_id.html', set=set_)}"


@app.route("/skills/<string:skill>")
def user_skill(skill):
    skills = add_skills_dict(skill)
    return render_template('skills.html', skill=skills)


if __name__ == "__main__":
    app.run(host='127.0.0.2', port=80)

"""смотрим оцениваем"""
