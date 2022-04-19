import json

from flask import Flask, render_template

app = Flask(__name__)

with open('candidates.json', 'r', encoding='utf8') as file:
    user_dict = json.load(file)


def iteration_list():
    """Делает вложенный словарь с ключем id"""
    id_dict = {}
    for o in user_dict:
        id = o.get('id')
        del o["id"]
        id_dict[id] = o
    return id_dict


new_dict = iteration_list()


def add_skills_dict(sk):
    """Выполняет поиск навыков в skills"""
    skill_dict = []
    sk = sk.lower()
    for key, value in new_dict.items():
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
    skills = new_dict[index]["skills"]
    name = new_dict[index]["name"]
    position = new_dict[index]["position"]
    picture = new_dict[index]["picture"]
    return f"<img src={picture}><pre><b>{name}</b>\n{position}\n{skills}"


@app.route("/skills/<string:skill>")
def user_skill(skill):
    skills = add_skills_dict(skill)
    return render_template('skills.html', skill=skills)


if __name__ == "__main__":
    app.run(host='127.0.0.2', port=80)

"""смотрим оцениваем"""