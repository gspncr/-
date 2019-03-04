import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
print(os.environ['FS_DB'])
app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI']=os.environ['FS_DB']
app.config['JSON_SORT_KEYS'] = False
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

@app.route('/api/latest-10')
def latestTen():
    refSite = Site.query.limit(10).all()
    return jsonify("latest-10",
        [dict(site=refSite[0].site, score=refSite[0].score, availability=refSite[0].availabilityScore, cleanliness=refSite[0].cleanlinessScore, lighting=refSite[0].lightingScore, space=refSite[0].spaciousScore),
        dict(site=refSite[1].site, score=refSite[1].score, availability=refSite[1].availabilityScore, cleanliness=refSite[1].cleanlinessScore, lighting=refSite[1].lightingScore, space=refSite[1].spaciousScore),
        dict(site=refSite[2].site, score=refSite[2].score, availability=refSite[2].availabilityScore, cleanliness=refSite[2].cleanlinessScore, lighting=refSite[2].lightingScore, space=refSite[2].spaciousScore),
        dict(site=refSite[3].site, score=refSite[3].score, availability=refSite[3].availabilityScore, cleanliness=refSite[3].cleanlinessScore, lighting=refSite[3].lightingScore, space=refSite[3].spaciousScore),
        dict(site=refSite[4].site, score=refSite[4].score, availability=refSite[4].availabilityScore, cleanliness=refSite[4].cleanlinessScore, lighting=refSite[4].lightingScore, space=refSite[4].spaciousScore),
        dict(site=refSite[5].site, score=refSite[5].score, availability=refSite[5].availabilityScore, cleanliness=refSite[5].cleanlinessScore, lighting=refSite[5].lightingScore, space=refSite[5].spaciousScore),
        dict(site=refSite[6].site, score=refSite[6].score, availability=refSite[6].availabilityScore, cleanliness=refSite[6].cleanlinessScore, lighting=refSite[6].lightingScore, space=refSite[6].spaciousScore),
        dict(site=refSite[7].site, score=refSite[7].score, availability=refSite[7].availabilityScore, cleanliness=refSite[7].cleanlinessScore, lighting=refSite[7].lightingScore, space=refSite[7].spaciousScore),
        dict(site=refSite[8].site, score=refSite[8].score, availability=refSite[8].availabilityScore, cleanliness=refSite[8].cleanlinessScore, lighting=refSite[8].lightingScore, space=refSite[8].spaciousScore),
        dict(site=refSite[9].site, score=refSite[9].score, availability=refSite[9].availabilityScore, cleanliness=refSite[9].cleanlinessScore, lighting=refSite[9].lightingScore, space=refSite[9].spaciousScore)
        ]
    )

@app.route('/api/cleanest-10')
def cleanestTen():
    #results = db.session.query(User).filter(User.name == "Bob").order_by(User.age.desc()).limit(10)
    refSite = Site.query.order_by(Site.cleanlinessScore.desc()).limit(10).all()
    return jsonify("cleanest-10",
        [dict(site=refSite[0].site, score=refSite[0].score, availability=refSite[0].availabilityScore, cleanliness=refSite[0].cleanlinessScore, lighting=refSite[0].lightingScore, space=refSite[0].spaciousScore),
        dict(site=refSite[1].site, score=refSite[1].score, availability=refSite[1].availabilityScore, cleanliness=refSite[1].cleanlinessScore, lighting=refSite[1].lightingScore, space=refSite[1].spaciousScore),
        dict(site=refSite[2].site, score=refSite[2].score, availability=refSite[2].availabilityScore, cleanliness=refSite[2].cleanlinessScore, lighting=refSite[2].lightingScore, space=refSite[2].spaciousScore),
        dict(site=refSite[3].site, score=refSite[3].score, availability=refSite[3].availabilityScore, cleanliness=refSite[3].cleanlinessScore, lighting=refSite[3].lightingScore, space=refSite[3].spaciousScore),
        dict(site=refSite[4].site, score=refSite[4].score, availability=refSite[4].availabilityScore, cleanliness=refSite[4].cleanlinessScore, lighting=refSite[4].lightingScore, space=refSite[4].spaciousScore),
        dict(site=refSite[5].site, score=refSite[5].score, availability=refSite[5].availabilityScore, cleanliness=refSite[5].cleanlinessScore, lighting=refSite[5].lightingScore, space=refSite[5].spaciousScore),
        dict(site=refSite[6].site, score=refSite[6].score, availability=refSite[6].availabilityScore, cleanliness=refSite[6].cleanlinessScore, lighting=refSite[6].lightingScore, space=refSite[6].spaciousScore),
        dict(site=refSite[7].site, score=refSite[7].score, availability=refSite[7].availabilityScore, cleanliness=refSite[7].cleanlinessScore, lighting=refSite[7].lightingScore, space=refSite[7].spaciousScore),
        dict(site=refSite[8].site, score=refSite[8].score, availability=refSite[8].availabilityScore, cleanliness=refSite[8].cleanlinessScore, lighting=refSite[8].lightingScore, space=refSite[8].spaciousScore),
        dict(site=refSite[9].site, score=refSite[9].score, availability=refSite[9].availabilityScore, cleanliness=refSite[9].cleanlinessScore, lighting=refSite[9].lightingScore, space=refSite[9].spaciousScore)
        ]
    )

@app.route('/api/top-overall-10')
def topOverallTen():
    #results = db.session.query(User).filter(User.name == "Bob").order_by(User.age.desc()).limit(10)
    refSite = Site.query.order_by(Site.score.desc()).limit(10).all()
    return jsonify("top-overall-10",
        [dict(site=refSite[0].site, score=refSite[0].score, availability=refSite[0].availabilityScore, cleanliness=refSite[0].cleanlinessScore, lighting=refSite[0].lightingScore, space=refSite[0].spaciousScore),
        dict(site=refSite[1].site, score=refSite[1].score, availability=refSite[1].availabilityScore, cleanliness=refSite[1].cleanlinessScore, lighting=refSite[1].lightingScore, space=refSite[1].spaciousScore),
        dict(site=refSite[2].site, score=refSite[2].score, availability=refSite[2].availabilityScore, cleanliness=refSite[2].cleanlinessScore, lighting=refSite[2].lightingScore, space=refSite[2].spaciousScore),
        dict(site=refSite[3].site, score=refSite[3].score, availability=refSite[3].availabilityScore, cleanliness=refSite[3].cleanlinessScore, lighting=refSite[3].lightingScore, space=refSite[3].spaciousScore),
        dict(site=refSite[4].site, score=refSite[4].score, availability=refSite[4].availabilityScore, cleanliness=refSite[4].cleanlinessScore, lighting=refSite[4].lightingScore, space=refSite[4].spaciousScore),
        dict(site=refSite[5].site, score=refSite[5].score, availability=refSite[5].availabilityScore, cleanliness=refSite[5].cleanlinessScore, lighting=refSite[5].lightingScore, space=refSite[5].spaciousScore),
        dict(site=refSite[6].site, score=refSite[6].score, availability=refSite[6].availabilityScore, cleanliness=refSite[6].cleanlinessScore, lighting=refSite[6].lightingScore, space=refSite[6].spaciousScore),
        dict(site=refSite[7].site, score=refSite[7].score, availability=refSite[7].availabilityScore, cleanliness=refSite[7].cleanlinessScore, lighting=refSite[7].lightingScore, space=refSite[7].spaciousScore),
        dict(site=refSite[8].site, score=refSite[8].score, availability=refSite[8].availabilityScore, cleanliness=refSite[8].cleanlinessScore, lighting=refSite[8].lightingScore, space=refSite[8].spaciousScore),
        dict(site=refSite[9].site, score=refSite[9].score, availability=refSite[9].availabilityScore, cleanliness=refSite[9].cleanlinessScore, lighting=refSite[9].lightingScore, space=refSite[9].spaciousScore)
        ]
    )

@app.route('/api/most-available-10')
def mostAvailableTen():
    #results = db.session.query(User).filter(User.name == "Bob").order_by(User.age.desc()).limit(10)
    refSite = Site.query.order_by(Site.availabilityScore.desc()).limit(10).all()
    return jsonify("most-available-10",
        [dict(site=refSite[0].site, score=refSite[0].score, availability=refSite[0].availabilityScore, cleanliness=refSite[0].cleanlinessScore, lighting=refSite[0].lightingScore, space=refSite[0].spaciousScore),
        dict(site=refSite[1].site, score=refSite[1].score, availability=refSite[1].availabilityScore, cleanliness=refSite[1].cleanlinessScore, lighting=refSite[1].lightingScore, space=refSite[1].spaciousScore),
        dict(site=refSite[2].site, score=refSite[2].score, availability=refSite[2].availabilityScore, cleanliness=refSite[2].cleanlinessScore, lighting=refSite[2].lightingScore, space=refSite[2].spaciousScore),
        dict(site=refSite[3].site, score=refSite[3].score, availability=refSite[3].availabilityScore, cleanliness=refSite[3].cleanlinessScore, lighting=refSite[3].lightingScore, space=refSite[3].spaciousScore),
        dict(site=refSite[4].site, score=refSite[4].score, availability=refSite[4].availabilityScore, cleanliness=refSite[4].cleanlinessScore, lighting=refSite[4].lightingScore, space=refSite[4].spaciousScore),
        dict(site=refSite[5].site, score=refSite[5].score, availability=refSite[5].availabilityScore, cleanliness=refSite[5].cleanlinessScore, lighting=refSite[5].lightingScore, space=refSite[5].spaciousScore),
        dict(site=refSite[6].site, score=refSite[6].score, availability=refSite[6].availabilityScore, cleanliness=refSite[6].cleanlinessScore, lighting=refSite[6].lightingScore, space=refSite[6].spaciousScore),
        dict(site=refSite[7].site, score=refSite[7].score, availability=refSite[7].availabilityScore, cleanliness=refSite[7].cleanlinessScore, lighting=refSite[7].lightingScore, space=refSite[7].spaciousScore),
        dict(site=refSite[8].site, score=refSite[8].score, availability=refSite[8].availabilityScore, cleanliness=refSite[8].cleanlinessScore, lighting=refSite[8].lightingScore, space=refSite[8].spaciousScore),
        dict(site=refSite[9].site, score=refSite[9].score, availability=refSite[9].availabilityScore, cleanliness=refSite[9].cleanlinessScore, lighting=refSite[9].lightingScore, space=refSite[9].spaciousScore)
        ]
    )

@app.route('/api/top-lighting-10')
def topLightingTen():
    #results = db.session.query(User).filter(User.name == "Bob").order_by(User.age.desc()).limit(10)
    refSite = Site.query.order_by(Site.lightingScore.desc()).limit(10).all()
    return jsonify("top-lighting-10",
        [dict(site=refSite[0].site, score=refSite[0].score, availability=refSite[0].availabilityScore, cleanliness=refSite[0].cleanlinessScore, lighting=refSite[0].lightingScore, space=refSite[0].spaciousScore),
        dict(site=refSite[1].site, score=refSite[1].score, availability=refSite[1].availabilityScore, cleanliness=refSite[1].cleanlinessScore, lighting=refSite[1].lightingScore, space=refSite[1].spaciousScore),
        dict(site=refSite[2].site, score=refSite[2].score, availability=refSite[2].availabilityScore, cleanliness=refSite[2].cleanlinessScore, lighting=refSite[2].lightingScore, space=refSite[2].spaciousScore),
        dict(site=refSite[3].site, score=refSite[3].score, availability=refSite[3].availabilityScore, cleanliness=refSite[3].cleanlinessScore, lighting=refSite[3].lightingScore, space=refSite[3].spaciousScore),
        dict(site=refSite[4].site, score=refSite[4].score, availability=refSite[4].availabilityScore, cleanliness=refSite[4].cleanlinessScore, lighting=refSite[4].lightingScore, space=refSite[4].spaciousScore),
        dict(site=refSite[5].site, score=refSite[5].score, availability=refSite[5].availabilityScore, cleanliness=refSite[5].cleanlinessScore, lighting=refSite[5].lightingScore, space=refSite[5].spaciousScore),
        dict(site=refSite[6].site, score=refSite[6].score, availability=refSite[6].availabilityScore, cleanliness=refSite[6].cleanlinessScore, lighting=refSite[6].lightingScore, space=refSite[6].spaciousScore),
        dict(site=refSite[7].site, score=refSite[7].score, availability=refSite[7].availabilityScore, cleanliness=refSite[7].cleanlinessScore, lighting=refSite[7].lightingScore, space=refSite[7].spaciousScore),
        dict(site=refSite[8].site, score=refSite[8].score, availability=refSite[8].availabilityScore, cleanliness=refSite[8].cleanlinessScore, lighting=refSite[8].lightingScore, space=refSite[8].spaciousScore),
        dict(site=refSite[9].site, score=refSite[9].score, availability=refSite[9].availabilityScore, cleanliness=refSite[9].cleanlinessScore, lighting=refSite[9].lightingScore, space=refSite[9].spaciousScore)
        ]
    )

@app.route('/api/most-spacious-10')
def mostSpaciousTen():
    #results = db.session.query(User).filter(User.name == "Bob").order_by(User.age.desc()).limit(10)
    refSite = Site.query.order_by(Site.spaciousScore.desc()).limit(10).all()
    return jsonify("most-spacious-10",
        [dict(site=refSite[0].site, score=refSite[0].score, availability=refSite[0].availabilityScore, cleanliness=refSite[0].cleanlinessScore, lighting=refSite[0].lightingScore, space=refSite[0].spaciousScore),
        dict(site=refSite[1].site, score=refSite[1].score, availability=refSite[1].availabilityScore, cleanliness=refSite[1].cleanlinessScore, lighting=refSite[1].lightingScore, space=refSite[1].spaciousScore),
        dict(site=refSite[2].site, score=refSite[2].score, availability=refSite[2].availabilityScore, cleanliness=refSite[2].cleanlinessScore, lighting=refSite[2].lightingScore, space=refSite[2].spaciousScore),
        dict(site=refSite[3].site, score=refSite[3].score, availability=refSite[3].availabilityScore, cleanliness=refSite[3].cleanlinessScore, lighting=refSite[3].lightingScore, space=refSite[3].spaciousScore),
        dict(site=refSite[4].site, score=refSite[4].score, availability=refSite[4].availabilityScore, cleanliness=refSite[4].cleanlinessScore, lighting=refSite[4].lightingScore, space=refSite[4].spaciousScore),
        dict(site=refSite[5].site, score=refSite[5].score, availability=refSite[5].availabilityScore, cleanliness=refSite[5].cleanlinessScore, lighting=refSite[5].lightingScore, space=refSite[5].spaciousScore),
        dict(site=refSite[6].site, score=refSite[6].score, availability=refSite[6].availabilityScore, cleanliness=refSite[6].cleanlinessScore, lighting=refSite[6].lightingScore, space=refSite[6].spaciousScore),
        dict(site=refSite[7].site, score=refSite[7].score, availability=refSite[7].availabilityScore, cleanliness=refSite[7].cleanlinessScore, lighting=refSite[7].lightingScore, space=refSite[7].spaciousScore),
        dict(site=refSite[8].site, score=refSite[8].score, availability=refSite[8].availabilityScore, cleanliness=refSite[8].cleanlinessScore, lighting=refSite[8].lightingScore, space=refSite[8].spaciousScore),
        dict(site=refSite[9].site, score=refSite[9].score, availability=refSite[9].availabilityScore, cleanliness=refSite[9].cleanlinessScore, lighting=refSite[9].lightingScore, space=refSite[9].spaciousScore)
        ]
    )

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

@app.route('/api/update/<sitename>', methods=['PUT'])
def apiUpdateSite(sitename):
    try:
        db.session.query(Site).filter_by(site=sitename).update({'score': request.json.get('score'), 'availabilityScore': request.json.get('availabilityScore'), 'cleanlinessScore': request.json.get('cleanlinessScore'), 'lightingScore': request.json.get('lightingScore'), 'spaciousScore': request.json.get('spaciousScore')})
        db.session.commit()
        return jsonify("site updated")
    except exc.IntegrityError as e:
        e = "unhandled"
        return jsonify("site does not exist or other error")

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
