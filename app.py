from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/roadmaps')
def roadmaps():
    return render_template('roadmaps.html')

@app.route('/roadmap-python')
def roadmap_python():
    return render_template('road-python.html')

@app.route('/roadmap-aptitude')
def roadmap_aptitude():
    return render_template('roadmap-aptitude.html')

@app.route('/roadmap-dsa')
def roadmap_dsa():
    return render_template('roadmap-dsa.html')

@app.route('/roadmap-webdev')
def roadmap_webdev():
    return render_template('roadmap-webdev.html')

@app.route('/roadmap-reasoning')
def roadmap_reasoning():
    return render_template('roadmap-reasoning.html')

if __name__ == '__main__':
    app.run(debug=True)
