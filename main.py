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

    print(
        f"years_total_revenue:"
        f"\n\tyears={years}"
        f"\n\ttotal_revenue={total_revenue}"
    )


def companies_by_movies_number(cur):
    cur.execute('select movies_number, market_share from top_revenue_distributor;')

    movies_number = []
    market_share = []
    for result in cur.fetchall():
        movies_number.append(int(result['movies_number']))
        market_share.append(float(result['market_share']))

    print(
        f"companies_by_movies_number:"
        f"\n\tmovies_number={movies_number}"
        f"\n\tmarket_share={market_share}"
    )


def distributors_by_market_share(cur):
    cur.execute('select name, market_share from top_revenue_distributor;')

    name = []
    market_share = []
    for result in cur.fetchall():
        name.append(result['name'])
        market_share.append(float(result['market_share']))

    print(
        f"distributors_by_market_share:"
        f"\n\tname={name}"
        f"\n\tmarket_share={market_share}"
    )


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
