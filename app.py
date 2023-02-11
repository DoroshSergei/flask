from flask import Flask, json, render_template

app = Flask(__name__)

data = json.load(open('candidates.json', encoding='utf-8'))


@app.route('/')
def index():
    return render_template('index.html', data=data)


@app.route('/candidate/<int:id>')
def page_candidate(id):
    return render_template('candidate.html', data=data, id=id)


@app.route('/skill/<skills>')
def page_skill(skills):
    return render_template('skill.html', data=data, skills=skills)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
