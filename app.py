from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='REDACTED'
db = SQLAlchemy(app)

class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String(80), unique=True)
    score = db.Column(db.Integer)
    availabilityScore = db.Column(db.Integer)
    cleanlinessScore = db.Column(db.Integer)
    lightingScore = db.Column(db.Integer)
    scentScore = db.Column(db.Integer)

    def __init__(self, site, score, availabilityScore, cleanlinessScore, lightingScore, scentScore):
        self.site = site
        self.score = score
        self.availabilityScore = availabilityScore
        self.cleanlinessScore = cleanlinessScore
        self.lightingScore = lightingScore
        self.scentScore = scentScore

    def __repr__(self):
        return '<Site %r>' % self.site

@app.route('/')
def index():
    refSite = Site.query.limit(10).all()
    entries = Site.query.count()
    latest = Site.query.order_by(Site.id.desc()).first()
    return render_template('app.html', refSite=refSite, entries=entries, latest=latest)

@app.route('/new-site', methods=['POST'])
def newsite():
    site = Site(request.form['site'], request.form['score'], request.form['availabilityScore'], request.form['cleanlinessScore'], request.form['lightingScore'], request.form['scentScore'])
    db.session.add(site)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
