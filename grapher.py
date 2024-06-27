import tkinter as tk

class GraphDrawer:
    def __init__(self, master):
        self.master = master
        self.master.title("Graph Drawer")
        self.canvas = tk.Canvas(self.master, width=800, height=600, bg="white")
        self.canvas.pack()

        # Create input fields and buttons
        self.entry_label = tk.Label(self.master, text="Enter graph edges (e.g., A-B,B-C,C-D):")
        self.entry_label.pack()
        self.entry = tk.Entry(self.master, width=50)
        self.entry.pack()
        self.draw_button = tk.Button(self.master, text="Draw Graph", command=self.draw_graph)
        self.draw_button.pack()

    def draw_graph(self):
        # Clear the canvas
        self.canvas.delete("all")

        # Read input and parse it
        edges = self.entry.get().split(',')
        nodes = set()
        for edge in edges:
            nodes.update(edge.split('-'))

        # Simple layout algorithm
        positions = self.calculate_positions(nodes)

        # Draw nodes
        for node, pos in positions.items():
            self.canvas.create_oval(pos[0]-20, pos[1]-20, pos[0]+20, pos[1]+20, fill="lightblue")
            self.canvas.create_text(pos[0], pos[1], text=node)

        # Draw edges
        for edge in edges:
            node1, node2 = edge.split('-')
            pos1 = positions[node1]
            pos2 = positions[node2]
            self.canvas.create_line(pos1, pos2)

    def calculate_positions(self, nodes):
        # For simplicity, layout nodes in a circle
        import math
        center_x, center_y = 400, 300
        radius = 200
        angle_step = 2 * math.pi / len(nodes)
        positions = {}
        for i, node in enumerate(nodes):
            angle = i * angle_step
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            positions[node] = (x, y)
        return positions

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphDrawer(root)
    root.mainloop()
