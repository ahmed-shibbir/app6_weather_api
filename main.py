from flask import Flask, render_template
import pandas as pd

# app = Flask("Website")

app = Flask(__name__)

filename = "data_small/stations.txt"
df = pd.read_csv(filename, skiprows=17)
stations = df[["STAID", "STANAME                                 "]]
stations = stations.to_html()


@app.route('/')
def home():
    return render_template("home.html", data=stations)

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze()/10
    return {"station": station,
            "date": date,
            "temperature": temperature}\

@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])

    return df.to_html()\

@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    df_year = df[df["    DATE"].str.startswith(str(year))]
    df_year = df_year.to_dict(orient="records")
    return df_year


if __name__ == '__main__':
    app.run(debug=True, port=5000)



# @app.route("/api/v1")
# def stations():
#     filename = "data_small/stations.txt"
#     df = pd.read_csv(filename, skiprows=17)
#     results = df[["STAID", "STANAME                                 "]]
#     results = results.to_html()
#     return results





# @app.route('/')
# def hello():
#     return 'Hello, World!'
#
#
# if __name__ == '__main__':
#     app.run()

