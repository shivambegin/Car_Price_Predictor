from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)
data = pd.read_csv('Cleaned_Quikr_Car_Data.csv')

@app.route('/')
def index():
    companies = sorted(data['company'].unique())
    models = sorted(data['name'].unique())
    years = sorted(data['year'].unique(), reverse=True)
    fuel_type = data['fuel_type'].unique()
    return render_template('index.html', companies = companies, models = models, years = years, fuel_type = fuel_type)


if __name__ == '__main__':
    app.run(debug=True)