import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
print(os.environ['FS_DB'])
app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI']=os.environ['FS_DB']
db = SQLAlchemy(app)

class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String(80), unique=True)
    score = db.Column(db.Integer)
    availabilityScore = db.Column(db.Integer)
    cleanlinessScore = db.Column(db.Integer)
    lightingScore = db.Column(db.Integer)
    spaciousScore = db.Column(db.Integer)

    def __init__(self, site, score, availabilityScore, cleanlinessScore, lightingScore, spaciousScore):
        self.site = site
        self.score = score
        self.availabilityScore = availabilityScore
        self.cleanlinessScore = cleanlinessScore
        self.lightingScore = lightingScore
        self.spaciousScore = spaciousScore

    def __repr__(self):
        return '<Site %r>' % self.site

@app.route('/')
def index():
    refSite = Site.query.limit(10).all()
    entries = Site.query.count()
    latest = Site.query.order_by(Site.id.desc()).first()
    return render_template('app.html', refSite=refSite, entries=entries, latest=latest)

@app.route('/site/<sitename>')
def site(sitename):
    oneSite = Site.query.filter_by(site=sitename).first()
    return render_template('site.html', oneSite=oneSite)

@app.route('/new-site', methods=['POST'])
def newsite():
    try:
        site = Site(request.form['site'].replace(' ','-'), request.form['score'], request.form['availabilityScore'], request.form['cleanlinessScore'], request.form['lightingScore'], request.form['spaciousScore'])
        db.session.add(site)
        db.session.commit()
        return redirect(url_for('index'))
    except exc.IntegrityError as e:
        e = "Site already exists!"
        return render_template('error.html', error=e)


app.run(host='0.0.0.0', port=8080)
