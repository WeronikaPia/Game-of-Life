import pygame
from colors import Colors
class Grid:
    def __init__(self, tile_size, width, height):
        self.tile_size = tile_size 
        self.grid_width = width // tile_size
        self.grid_height = height // tile_size
        self.width = width
        self.height = height

    def draw_grid(self, screen, positions):
        for position in positions:
            col, row = position 
            top_left = (col * self.tile_size, row * self.tile_size) 
            pygame.draw.rect(screen, Colors.PURPLE, (*top_left, self.tile_size, self.tile_size)) 

        for row in range(self.grid_height):
            pygame.draw.line(screen, Colors.WHITE, (0, row * self.tile_size), (self.width, row * self.tile_size))
        
        for col in range(self.grid_width):
            pygame.draw.line(screen, Colors.WHITE, (col * self.tile_size, 0), (col * self.tile_size, self.height))

    def get_neighbors(self, pos):
        x, y = pos 
        neighbors = []
        for dx in [-1, 0, 1]:  
            if x + dx < 0 or x + dx > self.grid_width: 
                continue
            for dy in [-1, 0, 1]:
                if y + dy < 0 or y + dy > self.grid_height: 
                    continue
                if dx == 0 and dy == 0: 
                    continue 

                neighbors.append((x + dx, y + dy))

        return neighbors
   
    # Updating grid

    def adjust_grid(self, positions):
        all_neighbors = set() 
        new_positions = set() 

        for position in positions:
            neighbors = self.get_neighbors(position) 
            all_neighbors.update(neighbors) 

            neighbors = list(filter( lambda x: x in positions, neighbors))
            if len(neighbors) in [2, 3]: 
                new_positions.add(position)

        for position in all_neighbors:
            neighbors = self.get_neighbors(position)
            neighbors = list(filter( lambda x: x in positions, neighbors))

            if len(neighbors) == 3:
                new_positions.add(position)

        return new_positions