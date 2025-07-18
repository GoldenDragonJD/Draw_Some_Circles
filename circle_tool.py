import numpy as np
import matplotlib.pyplot as plt
import json
import tools
import os

# Added a helper function to plot the circle
def plot_a_circle_on_fig(x, y, radius, plt):
    line_list = np.linspace(0, 2 * np.pi, 100)
    cos_output = tools.get_cos_x(line_list, radius, x)
    sin_output = tools.get_sin_y(line_list, radius, y)
    plt.plot(cos_output, sin_output)

def plot_the_circles():
    """Plot circles from circle_data.json and save as circle_plot.png"""
    try:
        # Check if circle_data.json exists, create if not
        if not os.path.exists("circle_data.json"):
            with open("circle_data.json", "w") as f:
                json.dump({}, f)
        
        # Load circle data
        with open("circle_data.json", "r") as f:
            circles_data = json.load(f)
        
        # Create a new plot
        plt.figure(figsize=(10, 10))
        plt.axis('equal')
        plt.grid(True, alpha=0.3)
        
        # Plot each circle
        for _, circle_info in circles_data.items():
            center_x = circle_info["x"]
            center_y = circle_info["y"]
            radius = circle_info["radius"]
            
            # Run the helper function with the correct parameters
            plot_a_circle_on_fig(center_x, center_y, radius, plt)
        
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Circles Plot')
        plt.legend()
        
        # Save the plot
        plt.savefig('circle_plot.png', dpi=150, bbox_inches='tight')
        plt.close()  # Close to free memory
        
    except Exception as e:
        print(f"Error plotting circles: {e}")
        # Create a blank plot if there's an error
        plt.figure(figsize=(10, 10))
        plt.text(0.5, 0.5, f'Error: {str(e)}', ha='center', va='center', transform=plt.gca().transAxes)
        plt.savefig('circle_plot.png', dpi=150, bbox_inches='tight')
        plt.close()

if __name__ == "__main__":
    plot_the_circles()