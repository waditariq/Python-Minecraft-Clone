# Import the Ursina engine and its first-person controller
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# Initialize the Ursina application
app = Ursina()

# Create a player with first-person controls
player = FirstPersonController()

# Add a sky to the scene
Sky()

# List to store all the blocks in the world
boxes = []

# Create a 20x20 grid of blocks
for i in range(20):
    for j in range(20):
        # Create a block with:
        # - White color
        # - Cube model
        # - Position based on grid coordinates
        # - Grass texture
        # - Parent to the main scene
        # - Origin at the bottom center
        box = Button(color=color.white, model='cube', position=(j,0,i),
              texture='grass.png', parent=scene, origin_y=0.5)
        boxes.append(box)

def input(key):
    # Handle player input
    if key == 'q':  # Add escape functionality with 'q' key
        application.quit()
        
    # Check each block for interaction
    for box in boxes:
        if box.hovered:  # If the player is looking at this block
            if key == 'left mouse down':  # Place a new block
                # Create a new block at the position the player is looking at
                new = Button(color=color.white, model='cube', position=box.position + mouse.normal,
                            texture='grass.png', parent=scene, origin_y=0.5)
                boxes.append(new)
            if key == 'right mouse down':  # Remove the block
                boxes.remove(box)
                destroy(box)

# Start the game loop
app.run()