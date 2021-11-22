import psycopg2
import psycopg2.extras
import plotly.graph_objects as go


def years_total_revenue(cur):
    cur.execute('select year, total_revenue from top_revenue_movie;')

    years = []
    total_revenue = []
    for result in cur.fetchall():
        years.append(int(result['year']))
        total_revenue.append(float(result['total_revenue']))

    fig = go.Figure(data=go.Scatter(x=years, y=total_revenue))
    fig.update_layout(
        xaxis_title='year',
        yaxis_title='revenue',
    )
    fig.write_image('years_total_revenue.jpeg')


def companies_by_movies_number(cur):
    cur.execute('select movies_number, market_share from top_revenue_distributor;')

    movies_number = []
    market_share = []
    for result in cur.fetchall():
        movies_number.append(int(result['movies_number']))
        market_share.append(float(result['market_share']))

    fig = go.Figure(data=go.Bar(x=movies_number, y=market_share))
    fig.update_layout(
        xaxis_title='movies number',
        yaxis_title='market share',
    )
    fig.write_image('companies_by_movies_number.jpeg')


def distributors_by_market_share(cur):
    cur.execute('select name, market_share from top_revenue_distributor;')

    name = []
    market_share = []
    for result in cur.fetchall():
        name.append(result['name'])
        market_share.append(float(result['market_share']))

    fig = go.Figure(data=go.Pie(labels=name, values=market_share))
    fig.update_layout(
        xaxis_title='distributor',
        yaxis_title='market share',
    )
    fig.write_image('distributor_by_movies_number.jpeg')


if __name__ == "__main__":
    conn = psycopg2.connect(
        dbname='lab_2', user='admin',
        password='12345', host='localhost'
    )
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        years_total_revenue(cursor)
        companies_by_movies_number(cursor)
        distributors_by_market_share(cursor)

    conn.close()
