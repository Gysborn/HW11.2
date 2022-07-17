from flask import Flask, render_template

from utils import get_candidates_by_name, load_candidates_from_json, get_candidate, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def index_page():
    candidate = load_candidates_from_json()
    return render_template("index.html", candidate=candidate)


@app.route('/candidate/<int:pk>')
def candidate_page(pk):
    candidate = get_candidate(pk)
    return render_template("list.html", candidate=candidate)


@app.route('/search/<candidate_name>')
def candidate_search(candidate_name):
    candidate = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidate=candidate)


@app.route('/skill/<skill_name>')
def candidate_skill(skill_name):
    candidate = get_candidates_by_skill(skill_name)
    return render_template("skill.html", candidate=candidate, skill_name=skill_name)


if __name__ == '__main__':
    app.run()
