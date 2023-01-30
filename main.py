chickens = {
    "Rhode Island Red": {
        "chick_price": 5.0,
        "starter_duration": 6,
        "grower_duration": 10,
        "layer_duration": 104,
        "eggs_per_year": 280,
    }
}

layer_feed_costs = {"starter": 40.0, "grower": 40.0, "layer": 34.0}


def total_cost_of_feeding(type_of_poultry, num_poultry):
    total_cost = 0
    total_food = 0

    weekly_feed_costs = {
        "starter": layer_feed_costs["starter"] / 50 * (7 / 16),
        "grower": layer_feed_costs["grower"] / 50 * (20 / 16),
        "layer": layer_feed_costs["layer"] / 50 * (28 / 16),
    }

    for i in range(chickens[type_of_poultry]["starter_duration"]):
        total_cost += weekly_feed_costs["starter"]
        total_food += 7 / 16

    for i in range(chickens[type_of_poultry]["grower_duration"]):
        total_cost += weekly_feed_costs["grower"]
        total_food += 20 / 16

    for i in range(chickens[type_of_poultry]["layer_duration"]):
        total_cost += weekly_feed_costs["layer"]
        total_food += 28 / 16

    total_cost += total_cost * num_poultry
    total_food += total_food * num_poultry
    return total_cost, total_food


def total_cost(type_of_poultry, num_poultry):
    total_cost = 0

    feed_cost, food_consumed = total_cost_of_feeding(type_of_poultry, num_poultry)

    total_cost += chickens[type_of_poultry]["chick_price"] * num_poultry
    total_cost += feed_cost

    return total_cost, food_consumed


def total_eggs(type_of_poultry, num_poultry):
    total_dozens_of_eggs = 0

    for i in range(chickens[type_of_poultry]["layer_duration"]):
        total_dozens_of_eggs += (
            chickens[type_of_poultry]["eggs_per_year"] / 52 / 12 * num_poultry
        )
    return total_dozens_of_eggs


def egg_sales(type_of_poultry, num_poultry):
    total_dozens_of_eggs = total_eggs(type_of_poultry, num_poultry)
    total_sales = total_dozens_of_eggs * 7.0
    return total_sales


num_poultry = 100

feed_cost, food_consumed = total_cost_of_feeding("Rhode Island Red", num_poultry)
print(f"The total feed cost is: ${feed_cost:.2f}")
print(f"The total food consumed is: {food_consumed:.2f} lbs")

total_cost, food_consumed = total_cost("Rhode Island Red", num_poultry)
print(f"The total cost is: ${total_cost:.2f}")
print(f"The total food consumed is: {food_consumed:.2f} lbs")

print(
    f"The total eggs produced in dozens is: {total_eggs('Rhode Island Red', num_poultry)}"
)

print(f"The total sales is: ${egg_sales('Rhode Island Red', num_poultry):.2f}")

print(
    f"The total profit is: ${egg_sales('Rhode Island Red', num_poultry) - total_cost:.2f}"
)
