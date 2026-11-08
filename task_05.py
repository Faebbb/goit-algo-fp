from collections import deque
import heapq
import tkinter as tk

from task_04 import draw_tree, heap_to_tree


def dfs(root):
    if root is None:
        return

    stack = [root]
    while stack:
        node = stack.pop()
        yield node
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)


def bfs(root):
    if root is None:
        return

    queue = deque([root])
    while queue:
        node = queue.popleft()
        yield node
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


def visit_colors(order):
    colors = {}
    for index, node in enumerate(order):
        fraction = index / max(1, len(order) - 1)
        red = round(17 + 169 * fraction)
        green = round(43 + 187 * fraction)
        blue = round(83 + 170 * fraction)
        fill = f"#{red:02X}{green:02X}{blue:02X}"
        text = "#FFFFFF" if fraction < 0.45 else "#0F172A"
        colors[node] = (fill, text)
    return colors


def main():
    heap = [9, 4, 10, 1, 7, 3, 8, 1, 6]
    heapq.heapify(heap)
    root = heap_to_tree(heap)

    window = tk.Tk()
    window.title("Обхід бінарного дерева")
    window.resizable(False, False)
    panels = tk.Frame(window)
    panels.pack(padx=12, pady=(10, 0))

    views = []
    for column, (name, walk) in enumerate((("DFS · у глибину", dfs), ("BFS · у ширину", bfs))):
        panel = tk.Frame(panels)
        panel.grid(row=0, column=column, padx=5)
        tk.Label(panel, text=name, font=("Segoe UI", 13, "bold")).pack(pady=(0, 6))
        canvas = tk.Canvas(panel, width=460, height=296, background="white",
                           highlightthickness=0)
        canvas.pack()
        status = tk.Label(panel, width=45, pady=5)
        status.pack()
        order = list(walk(root))
        views.append((canvas, status, order, visit_colors(order)))

    def show_step(value):
        step = int(float(value))
        for canvas, status, order, palette in views:
            visited = order[:step]
            draw_tree(canvas, root, {node: palette[node] for node in visited})
            sequence = " → ".join(str(node.value) for node in visited)
            status.configure(text=sequence or "Початок обходу")

    slider = tk.Scale(window, from_=0, to=len(heap), orient="horizontal", length=500,
                      label="Кількість відвіданих вузлів", command=show_step)
    slider.pack(pady=(0, 10))
    slider.set(len(heap))
    show_step(len(heap))
    window.mainloop()


if __name__ == "__main__":
    main()
