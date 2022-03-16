from flask import Flask, render_template

from utils import *

app = Flask(__name__)


@app.route('/candidates')
@app.route('/')
def candidates():  # put application's code here
    return render_template('list.html', candidates=load_candidates_from_json())


@app.route('/candidate/<int:id>')
def candidate(id):
    return render_template('card.html', candidate=get_candidate(id))


@app.route('/search/<candidate_name>')
def names(candidate_name):
    return render_template('search.html', candidates=get_candidates_by_name(candidate_name),
                           length_list=len(get_candidates_by_name(candidate_name)))


@app.route('/skill/<skill_name>')
def skills(skill_name):
    return render_template('skill.html', candidates=get_candidates_by_skill(skill_name),
                           length_list=len(get_candidates_by_skill(skill_name)), skill=skill_name)


@app.route('/ex_1')
def ex_1():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
