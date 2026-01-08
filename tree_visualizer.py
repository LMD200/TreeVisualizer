import tkinter as tk
import math

# Example array-based binary tree
tree_array = [1, 2, 3, 4, 5, 6, 7]

NODE_RADIUS = 20
LEVEL_HEIGHT = 80

def draw_tree(canvas, array):
    canvas.delete("all")
    if not array:
        return

    n = len(array)
    levels = math.floor(math.log2(n)) + 1

    width = canvas.winfo_width()

    for i, value in enumerate(array):
        level = math.floor(math.log2(i + 1))
        index_in_level = i - (2**level - 1)
        nodes_in_level = 2**level

        # Horizontal spacing
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

        # Draw node circle
        canvas.create_oval(
            x - NODE_RADIUS, y - NODE_RADIUS,
            x + NODE_RADIUS, y + NODE_RADIUS,
            fill="lightblue"
        )

        # Draw value text
        canvas.create_text(x, y, text=str(value), font=("Arial", 12, "bold"))

def main():
    root = tk.Tk()
    root.title("Array-Based Binary Tree Visualizer")

    canvas = tk.Canvas(root, width=800, height=600, bg="white")
    canvas.pack(fill="both", expand=True)

    # Redraw tree when window is resized
    canvas.bind("<Configure>", lambda event: draw_tree(canvas, tree_array))

    draw_tree(canvas, tree_array)
    root.mainloop()

if __name__ == "__main__":
    main()
