import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
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

@app.route('/api/new', methods=['GET','POST'])
def apiNewsite():
    try:
        site = Site(request.json.get('site').replace(' ','-'), request.json.get('score'), request.json.get('availabilityScore'), request.json.get('cleanlinessScore'), request.json.get('lightingScore'), request.json.get('spaciousScore'))
        db.session.add(site)
        db.session.commit()
        return jsonify("success")
    except exc.IntegrityError as e:
        return jsonify("site exists")

@app.route('/update/<sitename>', methods=['POST'])
def updateSite(sitename):
    try:
        db.session.query(Site).filter_by(site=sitename).update({'score': request.form['score'], 'availabilityScore': request.form['availabilityScore'], 'cleanlinessScore': request.form['cleanlinessScore'], 'lightingScore': request.form['lightingScore'], 'spaciousScore': request.form['spaciousScore']})
        db.session.commit()
        return redirect('site/'+sitename)
    except exc.IntegrityError as e:
        e = "unhandled"
        return render_template('error.html', error=e)

@app.route('/remove/<sitename>', methods=['DELETE'])
def removeSite(sitename):
    try:
        site = Site.query.filter_by(site=sitename).delete()
        db.session.commit()
        return jsonify("removed")
    except exc.IntegrityError as e:
        e = "Site already exists!"
        return jsonify("error")

@app.route('/top', methods=['GET'])
def bestOverall():
    latest = Site.query.order_by(Site.score.desc())
    return render_template('app.html', overall=latest, refSite=latest)

@app.route('/most-clean', methods=['GET'])
def mostClean():
    latest = Site.query.order_by(Site.cleanlinessScore.desc())
    return render_template('app.html', cleanest=latest, refSite=latest)

@app.route('/most-available', methods=['GET'])
def mostAvailable():
    latest = Site.query.order_by(Site.availabilityScore.desc())
    return render_template('app.html', available=latest, refSite=latest)

@app.route('/best-lighting', methods=['GET'])
def bestLighting():
    latest = Site.query.order_by(Site.lightingScore.desc())
    return render_template('app.html', lighting=latest, refSite=latest)

@app.route('/most-space', methods=['GET'])
def mostSpace():
    latest = Site.query.order_by(Site.spaciousScore.desc())
    return render_template('app.html', space=latest, refSite=latest)

@app.route('/site/<sitename>', methods=['GET'])
def site(sitename):
    oneSite = Site.query.filter_by(site=sitename).first()
    return render_template('site.html', oneSite=oneSite)

@app.route('/api/site/<sitename>', methods=['GET'])
def sitelookup(sitename):
    oneSite = Site.query.filter_by(site=sitename).first()
    return jsonify(name=oneSite.site, overall=oneSite.score, availability=oneSite.availabilityScore, cleanliness=oneSite.cleanlinessScore, lighting=oneSite.lightingScore, space=oneSite.spaciousScore)

@app.route('/api/score/<sitename>', methods=['GET'])
def sitescore(sitename):
    oneSite = Site.query.filter_by(site=sitename).first()
    return jsonify(overall=oneSite.score)

@app.route('/api/availability/<sitename>', methods=['GET'])
def availability(sitename):
    oneSite = Site.query.filter_by(site=sitename).first()
    return jsonify(availability=oneSite.availabilityScore)

@app.route('/api/cleanliness/<sitename>', methods=['GET'])
def cleanliness(sitename):
    oneSite = Site.query.filter_by(site=sitename).first()
    return jsonify(cleanliness=oneSite.cleanlinessScore)

@app.route('/api/lighting/<sitename>', methods=['GET'])
def lighting(sitename):
    oneSite = Site.query.filter_by(site=sitename).first()
    return jsonify(lighting=oneSite.lightingScore)

@app.route('/api/space/<sitename>', methods=['GET'])
def space(sitename):
    oneSite = Site.query.filter_by(site=sitename).first()
    return jsonify(space=oneSite.spaciousScore)

app.run(host='0.0.0.0', port=8080)
