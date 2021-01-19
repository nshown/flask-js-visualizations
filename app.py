from flask import Flask, jsonify, render_template, redirect
import sqlite3

# Create an instance of Flask
app = Flask(__name__)

# Route to render most basic index.html template
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

# Route to create an HTML table by passing a list of dictionaries to the template
@app.route("/html-templating")
def html_templating():
    color_data_from_db = get_color_data_dict_from_db()

    return render_template("html-templating.html", color_data=color_data_from_db)

# Route to illustrate how JavaScript variables are shared between scripts
@app.route("/js-variables")
def js_variables():
    return render_template("js-variables.html")

# Route to create an Plotly Chart using data through JS Templating
@app.route("/js-templating")
def js_templating():
    color_data_from_db = get_color_data_dict_from_db()

    return render_template("js-templating.html", color_data=color_data_from_db)


# Route that will return Web API JSON data
@app.route("/raw-web-api")
def scrape():
    color_data_from_db = get_color_data_dict_from_db()

    return jsonify(color_data_from_db)

# Route to render visualization by querying web api from JavaScript
@app.route("/js-using-web-api")
def js_using_web_api():
    return render_template("js-using-web-api.html")


# Function that queries database and returns a dictionary
def get_color_data_dict_from_db():
    table_name = "color_votes"
    conn = sqlite3.connect('db/favorite_color.db')

    cursor = conn.cursor()

    cursor.execute(f'''SELECT VOTES, COLOR from {table_name}''')

    results = cursor.fetchall()
    result_dicts = [ {"votes": result[0], "color": result[1]} for result in results]

    conn.close()

    return result_dicts


if __name__ == "__main__":
    app.run(debug=True)
