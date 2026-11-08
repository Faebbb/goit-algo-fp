import argparse
import random


def simulate_rolls(rolls, seed=None):
    rng = random.Random(seed)
    counts = dict.fromkeys(range(2, 13), 0)
    for _ in range(rolls):
        total = rng.randint(1, 6) + rng.randint(1, 6)
        counts[total] += 1
    return counts


def exact_probability(total):
    return (6 - abs(7 - total)) / 36


def main():
    parser = argparse.ArgumentParser(description="Моделювання кидків двох кубиків")
    parser.add_argument("--rolls", type=int, default=1_000_000, help="Кількість кидків")
    parser.add_argument("--seed", type=int, default=42, help="Початкове зерно генератора")
    args = parser.parse_args()
    if args.rolls < 1:
        parser.error("Кількість кидків має бути додатною.")

    counts = simulate_rolls(args.rolls, args.seed)
    print(f"Кидків: {args.rolls:,}, seed: {args.seed}")
    print(f"{'Сума':>4} | {'Кількість':>10} | {'Симуляція':>10} | {'Теорія':>9} | {'Різниця, в.п.':>13}")
    print("-" * 59)
    for total, count in counts.items():
        estimate = count / args.rolls
        exact = exact_probability(total)
        difference = 100 * (estimate - exact)
        print(f"{total:4} | {count:10} | {estimate:10.4%} | {exact:9.4%} | {difference:+13.4f}")


if __name__ == "__main__":
    main()
