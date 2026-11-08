import argparse
import math
import tkinter as tk


def branches(x, y, length, angle, depth):
    if depth == 0:
        return

    end_x = x + length * math.cos(angle)
    end_y = y + length * math.sin(angle)
    yield x, y, end_x, end_y

    child_length = length / math.sqrt(2)
    turn = math.pi / 4
    yield from branches(end_x, end_y, child_length, angle + turn, depth - 1)
    yield from branches(end_x, end_y, child_length, angle - turn, depth - 1)


def draw_fractal(canvas, depth):
    segments = list(branches(0, 0, 1, math.pi / 2, depth))
    width = int(canvas["width"])
    height = int(canvas["height"])
    margin = 24

    min_x = min(min(x, end_x) for x, _, end_x, _ in segments)
    max_x = max(max(x, end_x) for x, _, end_x, _ in segments)
    min_y = min(min(y, end_y) for _, y, _, end_y in segments)
    max_y = max(max(y, end_y) for _, y, _, end_y in segments)
    scale_x = (width - 2 * margin) / (max_x - min_x) if depth > 1 else math.inf
    scale_y = (height - 2 * margin) / (max_y - min_y)
    scale = min(scale_x, scale_y)
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2

    for x, y, end_x, end_y in segments:
        canvas.create_line(
            width / 2 + (x - center_x) * scale,
            height / 2 - (y - center_y) * scale,
            width / 2 + (end_x - center_x) * scale,
            height / 2 - (end_y - center_y) * scale,
            fill="#88433A",
            width=1.5,
        )


def main():
    parser = argparse.ArgumentParser(description="Фрактал «Дерево Піфагора»")
    parser.add_argument("--depth", type=int, default=8, help="Глибина від 1 до 14")
    args = parser.parse_args()
    if not 1 <= args.depth <= 14:
        parser.error("Глибина має бути від 1 до 14.")

    window = tk.Tk()
    window.title(f"Дерево Піфагора · глибина {args.depth}")
    window.resizable(False, False)
    canvas = tk.Canvas(window, width=640, height=640, background="white",
                       highlightthickness=0)
    canvas.pack()
    draw_fractal(canvas, args.depth)
    window.mainloop()


if __name__ == "__main__":
    main()
