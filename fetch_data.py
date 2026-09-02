import requests

def get_differentials(max_ownership=10):
    """
    Fetches current FPL player data and returns a list of 'differential'
    players - low ownership, sorted by points-per-million value.

    max_ownership: only include players owned by fewer than this % of managers
    """
    url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    response = requests.get(url)
    data = response.json()
    players = data['elements']

    differentials = []

    for player in players:
        ownership = float(player['selected_by_percent'])
        cost = player['now_cost'] / 10
        points = player['total_points']

        if cost == 0 or points == 0:
            continue

        points_per_million = points / cost

        if ownership < max_ownership:
            differentials.append({
                'name': player['web_name'],
                'ownership': ownership,
                'cost': cost,
                'points': points,
                'points_per_million': round(points_per_million, 2)
            })

    differentials.sort(key=lambda p: p['points_per_million'], reverse=True)
    return differentials


# This block only runs if you execute this file directly
# (it won't run if another file imports get_differentials from this one)
if __name__ == "__main__":
    results = get_differentials(max_ownership=10)
    print(f"Found {len(results)} low-ownership players\n")
    for p in results[:15]:
        print(f"{p['name']:15} £{p['cost']}m  {p['ownership']}% owned  {p['points']} pts  ({p['points_per_million']} pts/£m)")