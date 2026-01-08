import tkinter as tk
import math
import time
import threading

NODE_RADIUS = 20
LEVEL_HEIGHT = 80

tree_array = [1, 2, 3, 4, 5, 6, 7]  # starting tree

highlighted = None  # index of highlighted node


def draw_tree(canvas, array):
    canvas.delete("all")
    width = canvas.winfo_width()

    for i, value in enumerate(array):
        level = math.floor(math.log2(i + 1))
        index_in_level = i - (2**level - 1)
        nodes_in_level = 2**level

        x = width / (nodes_in_level + 1) * (index_in_level + 1)
        y = LEVEL_HEIGHT * (level + 1)

        # Draw connecting line to parent
        if i != 0:
            parent = (i - 1) // 2
            parent_level = math.floor(math.log2(parent + 1))
            parent_index = parent - (2**parent_level - 1)
            parent_x = width / (2**parent_level + 1) * (parent_index + 1)
            parent_y = LEVEL_HEIGHT * (parent_level + 1)

            canvas.create_line(x, y, parent_x, parent_y, width=2)

        # Highlight color
        fill_color = "yellow" if highlighted == i else "lightblue"

        # Draw node
        canvas.create_oval(
            x - NODE_RADIUS, y - NODE_RADIUS,
            x + NODE_RADIUS, y + NODE_RADIUS,
            fill=fill_color, tags=f"node_{i}"
        )

        canvas.create_text(x, y, text=str(value), font=("Arial", 12, "bold"))

        # Bind hover event
        canvas.tag_bind(f"node_{i}", "<Enter>", lambda e, idx=i: highlight_node(idx, canvas))
        canvas.tag_bind(f"node_{i}", "<Leave>", lambda e: clear_highlight(canvas))


def highlight_node(index, canvas):
    global highlighted
    highlighted = index
    draw_tree(canvas, tree_array)


def clear_highlight(canvas):
    global highlighted
    highlighted = None
    draw_tree(canvas, tree_array)


def insert_node(canvas, entry):
    try:
        value = int(entry.get())
        tree_array.append(value)
        draw_tree(canvas, tree_array)
    except:
        pass


def remove_last_node(canvas):
    if tree_array:
        tree_array.pop()
        draw_tree(canvas, tree_array)


def animate_build(canvas):
    def run_animation():
        global tree_array
        original = tree_array.copy()
        tree_array = []
        draw_tree(canvas, tree_array)
        time.sleep(0.3)

        for value in original:
            tree_array.append(value)
            draw_tree(canvas, tree_array)
            time.sleep(0.3)

    threading.Thread(target=run_animation).start()


def main():
    root = tk.Tk()
    root.title("Enhanced Array-Based Binary Tree Visualizer")

    canvas = tk.Canvas(root, width=800, height=600, bg="white")
    canvas.pack(fill="both", expand=True)

    # Controls
    control_frame = tk.Frame(root)
    control_frame.pack()

    entry = tk.Entry(control_frame, width=10)
    entry.grid(row=0, column=0)

    tk.Button(control_frame, text="Insert Node",
              command=lambda: insert_node(canvas, entry)).grid(row=0, column=1)

    tk.Button(control_frame, text="Remove Last Node",
              command=lambda: remove_last_node(canvas)).grid(row=0, column=2)

    tk.Button(control_frame, text="Animate Build",
              command=lambda: animate_build(canvas)).grid(row=0, column=3)

    canvas.bind("<Configure>", lambda e: draw_tree(canvas, tree_array))
    draw_tree(canvas, tree_array)

    root.mainloop()


if __name__ == "__main__":
    main()
