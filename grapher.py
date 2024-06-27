import matplotlib.pyplot as plt
import numpy as np

def plot_graph_from_equation(equation, x_min, x_max):
    # Generate x values
    x = np.linspace(x_min, x_max, 400)
    
    try:
        # Evaluate the equation to get y values
        y = eval(equation)
        
        # Plot the graph
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label=equation, color='blue')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Graph of ' + equation)
        plt.grid(True)
        plt.legend()
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.show()
        
    except Exception as e:
        print(f"Error plotting graph: {e}")

if __name__ == "__main__":
    equation = input("Enter a mathematical equation (ex: x**2 + 2*x+ 1 : use 'np' for numpy functions like sin, cos, exp): ")
    x_min = float(input("Enter the minimum value of x: "))
    x_max = float(input("Enter the maximum value of x: "))
    
    plot_graph_from_equation(equation, x_min, x_max)
