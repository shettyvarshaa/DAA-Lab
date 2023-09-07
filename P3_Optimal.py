
def find_optimal_route(streets, money_collected):
    current_money = 0
    optimal_route = []
    sorted_streets = sorted(zip(streets, money_collected), key=lambda x: x[1], reverse=True)
    for street, money in sorted_streets:
        if street not in optimal_route:
            optimal_route.append(street)
            current_money += money  
    return optimal_route, current_money
streets = ["Street A", "Street B", "Street C", "Street D"]
money_collected = [10, 15, 5, 20]
optimal_route, total_money = find_optimal_route(streets, money_collected)
print("Optimal Route:", optimal_route)
print("Total Money Collected:", total_money)