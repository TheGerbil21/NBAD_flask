from flask import Blueprint, render_template

app_projects = Blueprint('projects', __name__,
                url_prefix='/projects',
                template_folder='templates/bp_projects/')

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/portfolio/')
def portfolio():
    return render_template("portfolio.html")

# connects /kangaroos path to render kangaroos.html
@app_projects.route('/james/')
def james():
    return render_template("james.html")

@app_projects.route('/ethan/')
def ethan():
    return render_template("ethan.html")

@app_projects.route('/jeffrey/')
def jeffrey():
    return render_template("jeffrey.html")