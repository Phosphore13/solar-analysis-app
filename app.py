from flask import Flask, render_template, g
import psycopg2
import os
import pandas as pd
import plotly.express as px

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            host="db",
            database="mydb",
            user="myuser",
            password="mypassword"
        )
    return g.db

def get_df():
    if 'df' not in g:
        conn = get_db()
        df = pd.read_sql_query("SELECT Datetime, Sirta_GHI FROM mytable;", conn)

        """# create a date range from the start to the end date
        date_range = pd.date_range(start=df['datetime'].min().date(), end=df['datetime'].max().date(), freq='D')

        # iterate over each date in the date range
        for date in date_range:
            # check if there is no data for this date
            if not df['datetime'].dt.date.eq(date).any():
                # get the month and day of the missing date
                month = date.month
                day = date.day

                # filter the dataframe to only include dates with the same month and day
                filtered_df = df[(df['datetime'].dt.month == month) & (df['datetime'].dt.day == day)]

                # check if there is data for this month and day in other years
                if len(filtered_df) > 0:
                    # calculate the average value for this month and day
                    avg_value = filtered_df['sirta_ghi'].mean()

                    # create a new dataframe with the missing date and the calculated average value
                    new_data = pd.DataFrame({'datetime': [pd.Timestamp(date)], 'sirta_ghi': [avg_value]})

                    # add the new data to the original dataframe
                    df = pd.concat([df, new_data], ignore_index=True)

                    # sort the dataframe by datetime_col
                    df = df.sort_values('datetime')"""

        df = df.sort_values(by='datetime')
        df = df.fillna(method='bfill')
        g.df = df
    return g.df

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)

    if db is not None:
        db.close()

@app.route("/")
def index():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM mytable LIMIT 5;")
    rows = cur.fetchall()
    headers = [desc[0] for desc in cur.description]
    return render_template("index.html", headers=headers, rows=rows)

@app.route("/graph")
def graph():
    df = get_df()
    fig = px.line(df, x='datetime', y='sirta_ghi')
    graphJSON = fig.to_json()
    return render_template("graph.html", graphJSON=graphJSON)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
