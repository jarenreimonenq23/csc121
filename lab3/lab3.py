import arcade

 # Open up a window.
 # From the "arcade" library, use a fucntion called "open_window"
 #Set the window title to "Drawing Example"
 #Set the and dimensions (width and height)
arcade.open_window(800, 600, "Drawing Example")
 
 # Set the background color 
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

 # Get ready to draw 
arcade.start_render()

 #Draw the Sun 
arcade.draw_circle_filled(100,300,100, arcade.color.YELLOW)

 #Draw the grass 
arcade.draw_lrtb_rectangle_filled(0,800,200,0, arcade.color.BITTER_LIME)

 # - - - Draw the house - - -

 # - - - Finish drawing - - -
arcade.finish_render()

 # Keep the window up until someone closes it. 
arcade.run()