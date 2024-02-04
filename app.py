from flask import Flask, render_template, request
app = Flask(__name__)

from app_packages import main, zoning
import numpy as np

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/process_form', methods=['POST'])
def process_form():
    width = request.form['width']
    population = request.form['population']
    commercial = request.form['commercial']
    community = request.form['community']
    parks = request.form['parks']

    print(f"Form values: Width={width}, Population={population}, Commercial={commercial}, Community={community}, Parks={parks}")
    
    main.main(zoning.blocsAPlacer(
        np.ones((int(width), int(width))), 
        int(population), 
        float(commercial)/100, 
        float(community)/100, 
        float(parks)/100, 
        10, 20))

    return render_template("index.html", width=width, population=population, commercial=commercial, community=community, parks=parks)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=42069)