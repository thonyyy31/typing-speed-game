from graphics import *
import time
import random

# Sliding transition for text
def sliding_text(text_obj, window, start_x, end_x, steps=20, delay=0.02):
    delta_x = (end_x - start_x) / steps
    for _ in range(steps):
        text_obj.move(delta_x, 0)
        window.update()
        time.sleep(delay)

# Fade-in transition for text
def fade_in_text(text_obj, window, steps=20, delay=0.05):
    for i in range(steps + 1):
        color_value = int(255 * (i / steps))
        text_obj.setFill(color_rgb(color_value, color_value, color_value))
        window.update()
        time.sleep(delay)

# Generate random words
def generate_word(used_words):
    words = ["Love", "Jollibee", "McDonalds", "Graphics", "Ice Cream", "Yummy", "Hakdog", "Computer", "Window", "Ring", "Dinosaur", "Christmas", "Camping", "Dog", "Nurse", "Juice", "History", "Hau", "Computing", "Teacher", "House", "University", "Lightning", "Thunder", "Water", "Keyboard", "Monitor", "Valorant", "Laptop"]
    word = random.choice(words)
    while word in used_words:
        word = random.choice(words)
    used_words.add(word)
    return word

# Create a star at a random position
def create_star(win):
    star = Circle(Point(random.randint(0, 600), random.randint(0, 400)), 2)
    star.setFill("yellow")
    star.draw(win)
    return star

# Animate stars moving down
def animate_stars(win, stars):
    for star in stars:
        star.move(0, 0.5)
        if star.getCenter().getY() > 400:
            star.move(0, -400)

# FRun the Typing Speed Game
def typing_speed_game(high_score=0):
    # Main window
    win = GraphWin("Typing Game", 600, 400)
    win.setBackground("midnight blue")
    
    # Background image
    background = Image(Point(300, 200), "C:/graphics/PICS/Arcade.png")
    background.draw(win)
    
    # Visual details (simple rectangle)
    detail_rect = Rectangle(Point(50, 50), Point(550, 100))
    detail_rect.setFill("light slate blue")
    detail_rect.draw(win)
    
    # Text for instructions and results
    instructions = Text(Point(300, 75), "How Fast Can You Type?")
    instructions.setSize(12)
    instructions.draw(win)

    # Level Selection
    level_text = Text(Point(300, 120), "Select Level: 10, 15, or 20 Words")
    level_text.setFill("white")
    level_text.setSize(12)
    level_text.draw(win)

    # Buttons for level selection
    level1_button = Rectangle(Point(150, 150), Point(450, 200))
    level1_button.setFill("light green")
    level1_button.draw(win)
    level1_text = Text(Point(300, 175), "Level 1: 10 Words")
    level1_text.setTextColor("black")
    level1_text.draw(win)

    level2_button = Rectangle(Point(150, 210), Point(450, 260))
    level2_button.setFill("light blue")
    level2_button.draw(win)
    level2_text = Text(Point(300, 235), "Level 2: 15 Words")
    level2_text.setTextColor("black")
    level2_text.draw(win)

    level3_button = Rectangle(Point(150, 270), Point(450, 320))
    level3_button.setFill("light coral")
    level3_button.draw(win)
    level3_text = Text(Point(300, 295), "Level 3: 20 Words")
    level3_text.setTextColor("black")
    level3_text.draw(win)

    # Create initial stars
    stars = [create_star(win) for _ in range(20)]

    # Wait for the level selection
    level_words = 0
    while True:
        click_point = win.getMouse()
        if 150 <= click_point.getX() <= 450:
            if 150 <= click_point.getY() <= 200:
                level_words = 10  # Level 1
                break
            elif 210 <= click_point.getY() <= 260:
                level_words = 15  # Level 2
                break
            elif 270 <= click_point.getY() <= 320:
                level_words = 20  # Level 3
                break

    # Remove level selection elements
    level1_button.undraw()
    level1_text.undraw()
    level2_button.undraw()
    level2_text.undraw()
    level3_button.undraw()
    level3_text.undraw()
    level_text.undraw()

    # Entry object for user input
    user_entry = Entry(Point(300, 150), 20)
    user_entry.draw(win)

    # Display the word to type
    word_display = Text(Point(-100, 200), "")
    word_display.setSize(18)
    word_display.setTextColor("white")
    word_display.draw(win)

    # Button to start the game
    start_button = Rectangle(Point(250, 300), Point(350, 340))
    start_button.setFill("green")
    start_button.draw(win)
    start_text = Text(Point(300, 320), "Start")
    start_text.setTextColor("white")
    start_text.draw(win)

    # Apply fade-in effect to the start text
    fade_in_text(start_text, win)

    # Wait for the start button to be clicked
    while True:
        click_point = win.getMouse()
        if 250 <= click_point.getX() <= 350 and 300 <= click_point.getY() <= 340:
            break

    # Remove the start button and text
    start_button.undraw()
    start_text.undraw()

    # Variables to track score and elapsed time
    correct_words = 0
    total_time = 0
    used_words = set()

    # Loop through the selected number of words
    for i in range(level_words):
        # Clear the entry box
        user_entry.setText("")

        # Generate a new word and display it
        word_to_type = generate_word(used_words)
        word_display.setText(word_to_type)
        word_display.move(-word_display.getAnchor().getX() + 100, 0)
        sliding_text(word_display, win, 100, 300)

        # Start the typing speed test
        start_time = time.time()
        while True:
            animate_stars(win, stars)
            key = win.checkKey()
            if key == "Return":
                typed_word = user_entry.getText()
                elapsed_time = time.time() - start_time
                total_time += elapsed_time
                break

        # Check if the typed word is correct
        if typed_word == word_to_type:
            correct_words += 1

        # Display the current result for a short time
        result_message = Text(Point(300, 250), "")
        result_message.setSize(16)
        if typed_word == word_to_type:
            result_message.setText(f"Correct! Time: {elapsed_time:.2f} seconds")
            result_message.setTextColor("green")
        else:
            result_message.setText(f"Wrong! The correct word was '{word_to_type}'")
            result_message.setTextColor("white")
        result_message.draw(win)
        win.update()
        time.sleep(1)
        result_message.undraw()

    # Update the high score
    if correct_words > high_score:
        high_score = correct_words

    # Remove the word display
    word_display.undraw()

    # Display the final score
    final_message = Text(Point(300, 200), f"Game Over! Correct Words: {correct_words} out of {level_words}\nTotal Time: {total_time:.2f} seconds\nHigh Score: {high_score}")
    final_message.setSize(18)
    final_message.setTextColor("ivory3")
    final_message.draw(win)

    # Play Again and Exit buttons
    play_again_button = Rectangle(Point(150, 300), Point(250, 340))
    play_again_button.setFill("yellow")
    play_again_button.draw(win)
    play_again_text = Text(Point(200, 320), "Play Again")
    play_again_text.setTextColor("black")
    play_again_text.draw(win)
    
    exit_button = Rectangle(Point(350, 300), Point(450, 340))
    exit_button.setFill("red")
    exit_button.draw(win)
    exit_text = Text(Point(400, 320), "Exit")
    exit_text.setTextColor("white")
    exit_text.draw(win)
    
    while True:
        click_point = win.getMouse()
        if 150 <= click_point.getX() <= 250 and 300 <= click_point.getY() <= 340:
            win.close()
            typing_speed_game(high_score)  # Restart the game
            break
        elif 350 <= click_point.getX() <= 450 and 300 <= click_point.getY() <= 340:
            win.close()  # Exit the game
            break

# Start the Typing Speed Game
typing_speed_game()
