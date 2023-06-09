import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.ndimage import convolve
import matplotlib.colors as mcolors

# Set the size of the grid
N = 200

# Initialize the random state for reproducibility
np.random.seed(0)

# Set up the initial state of the grid
grid = np.random.choice([0, 1], size=(N, N), p=[0.5, 0.5]).astype(np.uint8)

# Define the neighborhood kernel: 3x3 matrix with 1s surrounding a 0
kernel = np.array([[1, 1, 1],
                   [1, 0, 1],
                   [1, 1, 1]])

def compute_next_generation(grid):
    """Return the next generation of the grid in the Game of Life."""
    # Count the number of live neighbors for each cell
    num_neighbors = convolve(grid, kernel, mode='wrap')

    # Apply the rules of the Game of Life using logical operations
    return ((grid == 1) & (num_neighbors >= 2) & (num_neighbors <= 3)) | ((grid == 0) & (num_neighbors == 3))

# Set up the plot
fig, ax = plt.subplots(figsize=(8, 8))

# Use a colormap to make the plot more colorful
cmap = mcolors.LinearSegmentedColormap.from_list("MyCmap", ["black", "green"])

image = ax.imshow(grid, cmap=cmap, interpolation='nearest')
ax.set_xticks([])
ax.set_yticks([])

# Add a colorbar
cbar = plt.colorbar(image, ax=ax, ticks=[0, 1])
cbar.ax.set_yticklabels(['Dead', 'Alive'])

def update_image(frame, grid, image):
    """Update the image for a new frame."""
    grid[:] = compute_next_generation(grid)
    image.set_array(grid)
    return [image]

# Start the animation
ani = animation.FuncAnimation(fig, update_image, frames=1000, interval=50, blit=True, fargs=(grid, image))

# Display the animation
plt.show()
