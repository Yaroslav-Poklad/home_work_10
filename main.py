from flask import Flask
import utils

app = Flask(__name__)

#главная страница
@app.route("/")

def index():
    candidates = utils.candidates_all()
    result = "<bk>"
    for candidate in candidates:
        result += candidate['name'] + "<br>"
        result += candidate['position'] + "<br>"
        result += candidate['skills'] + "<br>"
        result += "<br>"

    return f"<pre> {result} </pre>"

#страница по номеру кандидата
@app.route("/candidate/<int:pk>")
def get_candidate(pk):
    candidate = utils.get_by_pk(pk)
    result = "<bk>"
    result += candidate['name'] + "<br>"
    result += candidate['position'] + "<br>"
    result += candidate['skills'] + "<br>"
    result += "<br>"
    return f""""
        <img src="{candidate['picture']}">        
        <pre> {result} </pre>
    """

#страница по скилам
@app.route("/candidate/<skill>")
def get_candidate_by_skill(skill):
    candidates = utils.get_by_skill(skill.lower())
    result = "<bk>"
    for candidate in candidates:
        result += candidate['name'] + "<br>"
        result += candidate['position'] + "<br>"
        result += candidate['skills'] + "<br>"
        result += "<br>"
    return f"<pre> {result} </pre>"

app.run()