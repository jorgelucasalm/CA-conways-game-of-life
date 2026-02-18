import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 100  # Tamanho do grid
ON = 255
OFF = 0

def add_gosper_gun(grid, r, c):
    # Coordenadas relativas do Gosper Glider Gun
    gun_pattern = [
        (5, 1), (5, 2), (6, 1), (6, 2),                  
        (5, 11), (6, 11), (7, 11), (4, 12), (8, 12),      
        (3, 13), (9, 13), (3, 14), (9, 14), (6, 15),
        (4, 16), (8, 16), (5, 17), (6, 17), (7, 17), (6, 18),
        (3, 21), (3, 22), (4, 21), (4, 22), (5, 21), (5, 22),
        (2, 23), (6, 23), (1, 25), (2, 25), (6, 25), (7, 25), 
        (3, 35), (3, 36), (4, 35), (4, 36)                
    ]

    for dr, dc in gun_pattern:
        if 0 <= r+dr < grid.shape[0] and 0 <= c+dc < grid.shape[1]:
            grid[r+dr, c+dc] = ON

def create_4_guns_grid(N):
    quad_size = N // 2
    quadrant = np.zeros((quad_size, quad_size))

    add_gosper_gun(quadrant, 1, 1)

    top_left = quadrant
    top_right = np.fliplr(quadrant)  
    bottom_left = np.flipud(quadrant)  
    bottom_right = np.fliplr(bottom_left)

    top = np.hstack((top_left, top_right))
    bottom = np.hstack((bottom_left, bottom_right))
    full_grid = np.vstack((top, bottom))

    return full_grid

def update(frameNum, img, grid, N):
    newGrid = grid.copy()

    total = (np.roll(grid, 1, 0) + np.roll(grid, -1, 0) +
             np.roll(grid, 1, 1) + np.roll(grid, -1, 1) +
             np.roll(np.roll(grid, 1, 0), 1, 1) +
             np.roll(np.roll(grid, 1, 0), -1, 1) +
             np.roll(np.roll(grid, -1, 0), 1, 1) +
             np.roll(np.roll(grid, -1, 0), -1, 1)) / 255

    newGrid[:] = OFF
    newGrid[(grid == ON) & ((total == 2) | (total == 3))] = ON
    newGrid[(grid == OFF) & (total == 3)] = ON

    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

grid = create_4_guns_grid(N)

fig, ax = plt.subplots(figsize=(6, 6))
img = ax.imshow(grid, interpolation='nearest', cmap='binary')
ax.grid(True, color='lightgray', linewidth=0.5)
ax.set_xticks([])
ax.set_yticks([])

ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N),
                              frames=150, interval=50, blit=True)

plt.show()