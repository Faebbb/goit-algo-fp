import heapq
import tkinter as tk


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def heap_to_tree(heap):
    nodes = [Node(value) for value in heap]
    for index in range(1, len(nodes)):
        parent = nodes[(index - 1) // 2]
        if index % 2 == 1:
            parent.left = nodes[index]
        else:
            parent.right = nodes[index]
    return nodes[0] if nodes else None


def draw_tree(canvas, root, colors=None):
    canvas.delete("all")
    if root is None:
        return

    width = int(canvas["width"])
    positions = {}
    edges = []
    stack = [(root, width / 2, 45, (width - 32) / 4)]
    while stack:
        node, x, y, offset = stack.pop()
        positions[node] = (x, y)
        if node.right is not None:
            edges.append((node, node.right))
            stack.append((node.right, x + offset, y + 73, offset / 2))
        if node.left is not None:
            edges.append((node, node.left))
            stack.append((node.left, x - offset, y + 73, offset / 2))

    for parent, child in edges:
        canvas.create_line(*positions[parent], *positions[child], fill="#94A3B8", width=2)

    radius = 18
    for node, (x, y) in positions.items():
        color, text_color = "#BAE6FD", "#0F172A"
        if colors is not None:
            color, text_color = colors.get(node, ("#E2E8F0", "#0F172A"))
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius,
                           fill=color, outline="#64748B")
        canvas.create_text(x, y, text=node.value, fill=text_color,
                           font=("Segoe UI", 11, "bold"))


def visualize_heap(values):
    heap = list(values)
    heapq.heapify(heap)

    window = tk.Tk()
    window.title("Бінарна мін-купа")
    window.resizable(False, False)
    tk.Label(window, text=f"Масив купи: {heap}", padx=16, pady=12).pack()
    canvas = tk.Canvas(window, width=550, height=340, background="white",
                       highlightthickness=0)
    canvas.pack()
    draw_tree(canvas, heap_to_tree(heap))
    window.mainloop()


if __name__ == "__main__":
    visualize_heap([9, 4, 10, 1, 7, 3, 8, 1, 6])
