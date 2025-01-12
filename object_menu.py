from ursina import ButtonList, color

class ObjectMenu:
    """A right-click menu for selecting object types."""
    
    #==============================
    def __init__(self):
        self.visible = False
        self.current_type = "cube"
        
        # Create menu using ButtonList
        self.menu = ButtonList(
            button_dict={
                'Cube': self.select_cube,
                'Sphere': self.select_sphere,
                'Triangle': self.select_triangle
            },
            position=(.4, 0),
            button_height=1.5,
            width=.2,
            color=color.black66,
            highlight_color=color.azure,
            visible=False
        )
    
    #==============================
    def toggle(self):
        """Toggle menu visibility."""
        self.visible = not self.visible
        self.menu.visible = self.visible
    
    #==============================
    def select_cube(self):
        """Select cube as the current object type."""
        self.current_type = "cube"
        self.toggle()
    
    #==============================
    def select_sphere(self):
        """Select sphere as the current object type."""
        self.current_type = "sphere"
        self.toggle()
    
    #==============================
    def select_triangle(self):
        """Select triangle as the current object type."""
        self.current_type = "triangle"
        self.toggle()
    
    #==============================
    def handle_click(self, position):
        """Handle click on menu options."""
        # ButtonList handles its own clicks
        pass
