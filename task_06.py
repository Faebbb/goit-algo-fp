import argparse


ITEMS = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(items, budget):
    ordered = sorted(items, key=lambda name: items[name]["calories"] / items[name]["cost"],
                     reverse=True)
    selected = []
    for name in ordered:
        cost = items[name]["cost"]
        if cost <= budget:
            selected.append(name)
            budget -= cost
    return selected


def dynamic_programming(items, budget):
    names = list(items)
    budget = min(budget, sum(item["cost"] for item in items.values()))
    best = [[0] * (budget + 1) for _ in range(len(names) + 1)]

    for index, name in enumerate(names, start=1):
        cost = items[name]["cost"]
        calories = items[name]["calories"]
        for limit in range(budget + 1):
            best[index][limit] = best[index - 1][limit]
            if cost <= limit:
                with_item = best[index - 1][limit - cost] + calories
                best[index][limit] = max(best[index][limit], with_item)

    selected = []
    remaining = budget
    for index in range(len(names), 0, -1):
        if best[index][remaining] != best[index - 1][remaining]:
            name = names[index - 1]
            selected.append(name)
            remaining -= items[name]["cost"]
    return selected[::-1]


def main():
    parser = argparse.ArgumentParser(description="Вибір страв у межах бюджету")
    parser.add_argument("--budget", type=int, default=100, help="Цілий невід’ємний бюджет")
    args = parser.parse_args()
    if args.budget < 0:
        parser.error("Бюджет не може бути від’ємним.")

    print(f"Бюджет: {args.budget}")
    for title, algorithm in (("Жадібний алгоритм", greedy_algorithm),
                             ("Динамічне програмування", dynamic_programming)):
        selected = algorithm(ITEMS, args.budget)
        cost = sum(ITEMS[name]["cost"] for name in selected)
        calories = sum(ITEMS[name]["calories"] for name in selected)
        print(f"{title}: {', '.join(selected) or 'порожній набір'}")
        print(f"  Вартість: {cost}, калорійність: {calories} ккал")


if __name__ == "__main__":
    main()
