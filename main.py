import tkinter as tk
import math
from tkinter import messagebox
from datetime import datetime

#generate a sudoku board that is of size 9x9
def generate_board():
  base  = 3
  side  = base*base
  # pattern for a baseline valid solution
  def pattern(r,c): 
    return (base*(r%base)+r//base+c)%side
  
  # randomize rows, columns and numbers (of valid base pattern)
  def shuffle(s):
    from random import sample
    return sample(s,len(s)) 
    
  rBase = range(base) 
  rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
  cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
  nums  = shuffle(range(1,base*base+1))
  
  # produce board using randomized baseline pattern
  board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
  
  return board

#remove random spaces on the board so that it can be completed
def remove_numbers(board, remove_amount):
    from random import choice
    h, w= len(board), len(board[0])
    co_ords = [[x, y] for x in range(h) for y in range(w)]
    for k in range(remove_amount):
        co_ord_removed = choice(co_ords)  
        board[co_ord_removed[0]][co_ord_removed[1]] = 0
        co_ords.remove(co_ord_removed) #remove the co-ord picked to be replaced so that it wont be picked again
    return board

#find the empty spaces on the board
def find_empty(board):
  empty_slots=[]
  for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == 0:
          empty_slots.append((i, j))  # row, col

  return empty_slots

#function that runs when the easy difficuly button is selected
def easy_game():
    global comp_grid, grid, starting_grid, difficulty
    difficulty='easy'
    #completed grid that the player is trying to fill
    comp_grid1= generate_board()
    #the players grid that they are trying to fill that can be edited by the players input
    comp_grid=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    #recreate a completed grid
    for i in range(9):
        for j in range(9):
            comp_grid[i][j]=comp_grid1[i][j]

    #this grid will remain untouched, it is to check which parts of the original grid remain as a '0'
    #as to locate the values which are found or still to be found
    #starting_grid=(remove_numbers(comp_grid1, 1))
    starting_grid=(remove_numbers(comp_grid1, 37))

    grid=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
          
    #the players grid that they are trying to fill that can be edited by the players input
    for i in range(9):
        for j in range(9):
            grid[i][j]=starting_grid[i][j]
    
#function that runs when the medium difficuly button is selected
def med_game():
    global comp_grid, grid, starting_grid, difficulty
    difficulty='medium'
    #completed grid that the player is trying to fill
    comp_grid1= generate_board()
    #the players grid that they are trying to fill that can be edited by the players input
    comp_grid=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    #recreate a completed grid
    for i in range(9):
        for j in range(9):
            comp_grid[i][j]=comp_grid1[i][j]

    #this grid will remain untouched, it is to check which parts of the original grid remain as a '0'
    #as to locate the values which are found or still to be found
    starting_grid=(remove_numbers(comp_grid1, 45))

    grid=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
          
    #the players grid that they are trying to fill that can be edited by the players input
    for i in range(9):
        for j in range(9):
            grid[i][j]=starting_grid[i][j]
    
#function that runs when the hard difficuly button is selected    
def hard_game():
    global comp_grid, grid, starting_grid, difficulty
    difficulty='hard'
    #completed grid that the player is trying to fill
    comp_grid1= generate_board()
    #the players grid that they are trying to fill that can be edited by the players input
    comp_grid=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    #recreate a completed grid
    for i in range(9):
        for j in range(9):
            comp_grid[i][j]=comp_grid1[i][j]

    #this grid will remain untouched, it is to check which parts of the original grid remain as a '0'
    #as to locate the values which are found or still to be found
    starting_grid=(remove_numbers(comp_grid1, 53))

    grid=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
          
    #the players grid that they are trying to fill that can be edited by the players input
    for i in range(9):
        for j in range(9):
            grid[i][j]=starting_grid[i][j]

#function to clear all variables and will draw the starting grid 
def new_game():   
    global starting_grid, newGame_date, newGame_time, counter, incorrect_guess, timerCheck, user_input
    # datetime object containing current date and time to initiate the file
    newgameTime = datetime.now()
    newGame_date = newgameTime.strftime("%Y/%m/%d")  
    newGame_time = newgameTime.strftime("%H:%M:%S")        
    #print(newGame_date)
    #print(newGame_time)
    
    #reset counters
    counter=0
    incorrect_guess=0
    pause_counter=0
    hint_counter=0
    user_input=0
    timerCheck==False
    
    #roll new grid using functions and set up the correct variables for each on press
    #main_canvas.delete('numbers')
    #main_canvas.delete('highlight')
    #main_canvas.delete('missing')
    #main_canvas.delete('winner')
    #main_canvas.delete('attempts')
    #main_canvas.delete('victory')
    #main_canvas.delete('inc_attempts')
    main_canvas.delete('all')
    
    draw_grid()
    draw_grid_numbers(starting_grid)

#function that will begin the timer and can be pressed again once pressed to reset timer
def start_timer():
    import numpy as np
    import time
    global minute, second, user_input, timerCheck, mins, secs
    # setting the default value as 0
    minute=0
    second=0
    #get the time left
    user_input =np.round(minute*60 + second,1)
    
    #begin timer by setting gateway to true ao that the timer will run
    timerCheck=True
    while timerCheck==True:
        mins,secs = np.round(divmod(user_input,60), 1)
        # store the value up to two decimal places and change the display
        minute=mins
        second=secs
        mins_box["text"]=mins
        sec_box["text"]=secs
        # updating the GUI window 
        window.update()
        time.sleep(0.1)
        user_input = np.round(user_input+0.1,1)

#function that will pause the timer when the key 'P' is pressed and can unpause the timer when 'P' is pressed again.
def pause_timer(event):
    global pause_counter, timerCheck, mins, sec, user_input
    pause_counter += 1
    #'even number of times clicked = keep timer running
    if pause_counter %2 == 0 or pause_counter == 0 :
        timerCheck=True
        while timerCheck==True:
            import numpy as np
            import time
            mins,secs = np.round(divmod(user_input,60), 1)
            # store the value up to two decimal places and change the display
            minute=mins
            second=secs
            mins_box["text"]=mins
            sec_box["text"]=secs
            # updating the GUI window 
            window.update()
            time.sleep(0.1)
            user_input = np.round(user_input+0.1,1)
    else:   #odd number of times clicked = pause timer
        timerCheck=False

#function that will display infomation at the end of the game
def victory_scene():
    #stop timer
    global timerCheck, mins, secs, starting_grid, comp_grid
    timerCheck=False    #stop timer
    #print('minutes:', mins)
    #print('seconds:', secs)
    
    #end game data collection sent to txt file.
    endgameTime = datetime.now()
    endGame_time = endgameTime.strftime("%H:%M:%S")
    raw_data=open('sudoku_raw_data.txt',"a")
    raw_data.write("\n"+newGame_date+','+newGame_time+','+endGame_time+','+difficulty+','+str(counter)+","+str(incorrect_guess)+','+str(hint_counter)+','+str(pause_counter) +','+str(mins)+':'+str(secs)) 
    raw_data.close()   
    
    #collect data on the grid and store in a text file
    raw_grid_data=open('sudoku_grid_data.txt',"a")
    raw_grid_data.write("\n"+newGame_date+','+newGame_time+','+endGame_time+','+str(starting_grid)+':'+str(comp_grid)) 
    raw_grid_data.close()   
    
    # create a circle
    xc0 = yc0 = MARGIN + cell_width * 2
    xc1 = yc1 = MARGIN + cell_width * 7
    main_canvas.create_oval(xc0, yc0, xc1, yc1, tags="victory", fill=victory_colors[1], outline=victory_colors[1])
    
    # create text in the correct locations
    x = y = MARGIN + 4 * cell_width + cell_width / 2
    main_canvas.create_text(x, y, text="You win!", tags="winner", fill=victory_colors[0], font=("Arial", 32))
    main_canvas.create_text(x, y+5+(cell_width/2), text="Attempts: "+str(counter), tags="attempts", fill=victory_colors[0], font=("Arial", 12))
    main_canvas.create_text(x, y+(cell_width), text="Incorrect Attempts: "+str(incorrect_guess), tags="inc_attempts", fill=victory_colors[0], font=("Arial", 10))

#create the grid outline for the canvas that will be there as a background
def draw_grid():
    for i in range(9+1):
        #draw the blue outlines every 3rd across
        color=''
        width=''
        if i % 3 == 0:
            color='#B0C4DE'
            width=2
        else:
            color='grey'
            width=1
        
        #vertical lines
        xv0=MARGIN + (i*cell_width)
        yv0=MARGIN
        xv1=MARGIN + (i*cell_width)
        yv1=WIN_HEIGHT  - MARGIN
        main_canvas.create_line(xv0, yv0, xv1, yv1, fill=color, width=width)
        
        #horizontal lines
        xh0= MARGIN
        yh0= MARGIN + (i*cell_width)
        xh1= WIN_WIDTH - MARGIN
        yh1 = MARGIN + (i*cell_width)
        main_canvas.create_line(xh0, yh0, xh1, yh1, fill=color, width=width)

#draw the numbers from the grid onto the canvas in the right place and check for where missing numbers are
def draw_grid_numbers(grid):
    for i in range(9):
        for j in range(9):
            number=grid[i][j]
            original_value=starting_grid[i][j]
            color=''
            color='black' if original_value == number else user_number_color   #checks weather one of the numbers draw is in a '0' spot
            #print(number)
            if number !=0:
                x_loc=MARGIN + (j * cell_width + cell_width/2)
                y_loc=MARGIN + (i * cell_width + cell_width/2)
                main_canvas.create_text(x_loc, y_loc, text=number,font=("Lucida Sans Typewriter", 16), tags='numbers', fill=color)
            else:
                x0 = MARGIN + j * cell_width + 1
                y0 = MARGIN + i * cell_width + 1
                x1 = MARGIN + (j + 1) * cell_width - 1
                y1 = MARGIN + (i + 1) * cell_width - 1
                #main_canvas.create_rectangle(x0, y0, x1, y1, outline=missing_color, tags='missing')    #uncomment this to highlight missing

#function that will be used everytime a cell is clicked
def cell_clicked(event):
    x,y=event.x, event.y
    #print(x,y)
    #check that the location clicked is on the board
    if MARGIN < x < WIN_WIDTH - MARGIN and MARGIN < y < WIN_HEIGHT - MARGIN:
        #get row and column index from position
        global row, col, x0, y0, x1, y1
        row, col = math.floor((y - MARGIN) / cell_width), math.floor((x - MARGIN) / cell_width)
        
        #print(row, col)
        x0 = MARGIN + col * cell_width + 1
        y0 = MARGIN + row * cell_width + 1
        x1 = MARGIN + (col + 1) * cell_width - 1
        y1 = MARGIN + (row + 1) * cell_width - 1
        
        if starting_grid[row][col] == 0:
            main_canvas.delete('highlight')
            main_canvas.delete('hint')
            main_canvas.create_rectangle(x0, y0, x1, y1, outline=highlight_color, width=2, tags="highlight")

#right click function that will allow the user to delete the value that they have input into a square
def cell_right_click(event):
    x,y=event.x, event.y
    main_canvas.delete('highlight')
    #print(x,y)
    #check that the location clicked is on the board
    if MARGIN < x < WIN_WIDTH - MARGIN and MARGIN < y < WIN_HEIGHT - MARGIN:
        #get row and column index from position
        global grid, starting_grid  
        i, j = math.floor((y - MARGIN) / cell_width), math.floor((x - MARGIN) / cell_width) 
        if starting_grid[i][j] == 0:    #only allow anything to happen if the button pressed is originally an area to find
            main_canvas.delete('numbers')
            grid[i][j]=0
            draw_grid_numbers(grid)

#function that will draw on the value pressed at the correct location based on where the cell has been clicked
def key_pressed(event):
    global guessed_value, grid, counter, incorrect_guess, current_position
    #counter is how many gueses have been taken in total.
    counter +=1
    #print(counter)
    #print('row:',row,'col:', col)
    guessed_value=event.char
    #print('guessed_value:', guessed_value)
    #print('comp_grid number:', comp_grid[row][col])
    
    if 0<=row<=8  and 0<=col<=8 and event.char in "123456789": #check input and location are valid before drawing the attempt
        guessed_value=int(guessed_value)
        x_loc=MARGIN + (col * cell_width + cell_width/2)
        y_loc=MARGIN + (row * cell_width + cell_width/2)
        
        #print('guess = correct')
        #print('comp_grid:',comp_grid[row][col])
        current_position.append((row,col))
        grid[row][col]=guessed_value
        main_canvas.create_text(x_loc, y_loc, text=guessed_value,font=("Lucida Sans Typewriter", 16), tags='numbers', fill=user_number_color)
        #main_canvas.create_rectangle(x0, y0, x1, y1, outline="green", width=2, tags="cursor highlight")
        main_canvas.delete('numbers')
        draw_grid_numbers(grid)
        
        #check if the key entered matches the original full grid, if not add one to incorrect_guess to keep track
        if guessed_value != comp_grid[row][col]:
            incorrect_guess += 1
        
        #check that that was the last number to be filled in. if so play the victory scene and store data.
        def compare_two_grids(comp_grid, grid):
            diff_cells=0
            for i in range(9):
                for j in range(9):
                    if comp_grid[i][j] != grid[i][j]:
                        diff_cells += 1
            return diff_cells
        
        left_to_get= compare_two_grids(comp_grid, grid)
        if left_to_get == 0: #GAME IS COMPLETED WITH 0 DIFFERENT TYPES
            victory_scene()
                
    else:
        messagebox.showinfo(title="Input Error", message="You can only input number values")

#space key will offer as a hint and recolor boxes that are correct to green.
def space_pressed(event):
    global grid, comp_grid, starting_grid
    main_canvas.delete('missing')
    main_canvas.delete('highlight')
    for i in range(9):
        for j in range(9):
            number=grid[i][j]
            original_value=starting_grid[i][j]
            target_value=comp_grid[i][j]
            #print('player grid', number)
            #print('starting grid', original_value)
            #print('target value', target_value)
            if number == target_value and original_value == 0:
                x0 = MARGIN + j * cell_width + 1
                y0 = MARGIN + i * cell_width + 1
                x1 = MARGIN + (j + 1) * cell_width - 1
                y1 = MARGIN + (i + 1) * cell_width - 1
                main_canvas.create_rectangle(x0, y0, x1, y1, outline=correct_color, width=2, tags='completed')
            elif original_value == 0:   #ensure the entire grid isnt highlighted and just where the empsy spaces were orignally
                x0 = MARGIN + j * cell_width + 1
                y0 = MARGIN + i * cell_width + 1
                x1 = MARGIN + (j + 1) * cell_width - 1
                y1 = MARGIN + (i + 1) * cell_width - 1
                #main_canvas.create_rectangle(x0, y0, x1, y1, outline=missing_color, tags='missing')    #uncomment this line to higlight missing sqaures

#a hint function that will reveal one unknown number that will be an empty square in the players grid
def hint(event):
    from random import choice
    global starting_grid, grid, comp_grid, hint_counter
    hint_counter += 1
    positions=find_empty(starting_grid) #find all of the missing spaces at the start of the game
    player_positions=find_empty(grid)   #find all of the empty spaces in the players grid
    #print(player_positions)
    reveal_position=choice(player_positions)   #random sqaure to be revealed
    hint_row, hint_col=reveal_position
    #print(reveal_position)
    #print(hint_row, hint_col)
    number_revealed=comp_grid[hint_row][hint_col]
    grid[hint_row][hint_col]=number_revealed
    #print(row, col)
    hx0 = MARGIN + hint_col * cell_width + 1
    hy0 = MARGIN + hint_row * cell_width + 1
    hx1 = MARGIN + (hint_col + 1) * cell_width - 1
    hy1 = MARGIN + (hint_row + 1) * cell_width - 1
    main_canvas.delete('highlight')  
    main_canvas.delete('numbers')  
    draw_grid_numbers(grid)
    main_canvas.delete('hint')
    main_canvas.create_rectangle(hx0, hy0, hx1, hy1, outline=hint_color, width=2, tags="hint")   

    #check that that was the last number to be filled in. if so play the victory scene and store data.
    def compare_two_grids(comp_grid, grid):
        diff_cells=0
        for i in range(9):
            for j in range(9):
                if comp_grid[i][j] != grid[i][j]:
                        diff_cells += 1
        return diff_cells
        
    left_to_get= compare_two_grids(comp_grid, grid)
    if left_to_get == 0: #GAME IS COMPLETED WITH 0 DIFFERENT TYPES
        victory_scene()    

#function that will clear the game and all inputs and restart everything
def clear_game():
    global grid, starting_grid, counter
    main_canvas.delete('numbers')
    main_canvas.delete('victory')
    main_canvas.delete('highlight')
    main_canvas.delete('completed')
    main_canvas.delete('hint')
    draw_grid()
    draw_grid_numbers(starting_grid)    #draw the starting grid instead of the grid the player has been editing.
    counter=0                           #reset the counter 
    
    #replace each spot in the players grid with a 0 where the starting grid is also 0. this resets all progress.
    for i in range(9):
        for j in range(9):
            if starting_grid[i][j] == 0:
                grid[i][j] = 0

#function that will return the users current 'score' ie how many more boxes need to be filled correctly.
def check_game():
    global comp_grid, grid
    #input the completed grid and the users grid and return a value of how many cells are different, therefore incorect
    def compare_two_grids(comp_grid, grid):
        diff_cells=0
        for i in range(9):
            for j in range(9):
                if comp_grid[i][j] != grid[i][j]:
                    diff_cells += 1
        return diff_cells
    
    left_to_get= compare_two_grids(comp_grid, grid)
    if left_to_get == 0: #GAME IS COMPLETED
        victory_scene()
    else:
        messagebox.showinfo(title="Check Game", message="There are currently "+str(left_to_get)+" values that are incorrect")



# ---------- DATA COLLECTING VARIABLES ---------
global counter, incorrect_guess, current_position, difficulty, pause_counter, hint_counter, mins, secs, timerCheck
counter=0
incorrect_guess=0
current_position=[]
difficulty=''
pause_counter=0
hint_counter=0
mins=0
secs=0
timerCheck=False



# ------------------------------------ ALL APP FORMATTING -------------------------------------------
#variables for app size and also drawing the grid
global WIN_HEIGHT, WIN_WIDTH, MARGIN, cell_width
MARGIN=20
cell_width=50
WIN_HEIGHT=MARGIN * 2 + cell_width * 9
WIN_WIDTH=MARGIN * 2 + cell_width * 9

#ALL OF THE BELOW IS FORMATING FOR THE GUI AND ITS DISPLAYS
# Create instance
window = tk.Tk()
# Disable resizing the GUI
window.resizable(0,0)  #(x,y)

#define the colors of the app, changing them here change everything quickly.
main_colors=["#FFFAF0", "#000000"]      	#text and background for app
user_number_color="#4169E1"					#color of numbers entered by user
missing_color="#F08080" 			 	    #color of grid highlighted when value hasnt been ipnut
highlight_color="#FF7F50"     	 			#color to highlight grid when user clicks onto grid
correct_color="#9ACD32"      		 		#color used to highlight grid with correct number
hint_color="#9370DB"      		 		    #color used to highlight grid when a hint is revealed
button_colors=["#FAEBD7", "#708090"]      	#text and background for buttons
victory_colors=["#FFFAF0", "#D8BFD8"]      	#text and background for victory scene

# Add a title
window.title("Sudoku - APP (jlf)")

#LABEL - holds infomation about the game
lbl_info=tk.Label(master=window, 
                text="Click a difficulty then press start game to begin", font=("Lucida Sans Typewriter", 11, 'bold'),
                foreground=main_colors[1], background=main_colors[0])
lbl_info.grid(row=0, column=0, sticky="ew", pady=(5,0))

#FRAME TO HOLD GAME BUTTONS
frm_game_button=tk.Frame(background=main_colors[0])
frm_game_button.grid(row=1, column=0, sticky="ew")
frm_game_button.grid_rowconfigure(0, weight=1)
frm_game_button.grid_columnconfigure([0,1,2], weight=1)

#EASY GAME BUTTON
btn_easy_game=tk.Button(master=frm_game_button, text='Easy', font=("Lucida Sans Typewriter", 12), fg=button_colors[0], bg= button_colors[1],
                        relief=tk.RIDGE, borderwidth=3, command=easy_game)
btn_easy_game.grid(row=0, column=0, padx=(40,0), pady=(5,0))

#MED GAME BUTTON
btn_med_game=tk.Button(master=frm_game_button, text='Medium', font=("Lucida Sans Typewriter", 12), fg=button_colors[0], bg= button_colors[1],
                       relief=tk.RIDGE, borderwidth=3, command=med_game)
btn_med_game.grid(row=0, column=1, padx=0, pady=(5,0))

#HARD GAME BUTTON
btn_hard_game=tk.Button(master=frm_game_button, text='Hard', font=("Lucida Sans Typewriter", 12), fg=button_colors[0], bg= button_colors[1],
                        relief=tk.RIDGE, borderwidth=3, command=hard_game)
btn_hard_game.grid(row=0, column=2, padx=(0,40), pady=(5,0))

#FRAME TO HOLD NEW GAME BUTTON
frm_new_game_button=tk.Frame(background=main_colors[0])
frm_new_game_button.grid(row=2, column=0, sticky="ew")
frm_new_game_button.grid_rowconfigure(0, weight=1)
frm_new_game_button.grid_columnconfigure([0,1,3], weight=1)

#NEW GAME BUTTON
btn_new_game=tk.Button(master=frm_new_game_button, text='Start Game', font=("Lucida Sans Typewriter", 11), fg=button_colors[0], bg= button_colors[1],
                       relief=tk.RIDGE, borderwidth=3, command = new_game)
btn_new_game.grid(row=0, column=0, padx=(55,0), pady=(10,5))

#BUTTON THAT WILL INITIATE THE TIMER
btn_start_timer=tk.Button(master=frm_new_game_button, text='Start Timer', font=("Lucida Sans Typewriter", 11), fg=button_colors[0], bg= button_colors[1],
                       relief=tk.RIDGE, borderwidth=3, command = start_timer)
btn_start_timer.grid(row=0, column=1, padx=(35,0), pady=(10,5))

#MINUTE BOX
mins_box = tk.Label(master=frm_new_game_button, width=4, 	font=("Arial",16),	text=0, relief=tk.SUNKEN, borderwidth=2)
mins_box.grid(row=0,column=2,padx=(40,0), pady=(10,5))
  
sec_box = tk.Label(master=frm_new_game_button,	width=4, 	font=("Arial",16),	text=0, relief=tk.SUNKEN, borderwidth=2)
sec_box.grid(row=0,column=3,padx=(1,30), pady=(10,5))

#FRAME TO HOLD CANVAS AND SUDOKU GRID
frm_grid=tk.Frame(background=main_colors[0])
frm_grid.grid(row=3, column=0, sticky="ew")
frm_grid.grid_rowconfigure(0, weight=1)

#canvas where the board will be drawn
main_canvas=tk.Canvas(master=frm_grid, width=WIN_WIDTH, height=WIN_HEIGHT, bg=main_colors[0], highlightthickness=0)
main_canvas.grid(row=0, column=0)
#define which buttons and events can be used when interacting with the canvas
main_canvas.bind("<Button-1>", cell_clicked)   #bind left mouse click to the canvas with a command to follow
main_canvas.bind("<Button-3>", cell_right_click)   #bind right mouse click to the canvas with a command to follow
main_canvas.bind("<Key>", key_pressed)        #bind a key which will be numbers to the canvas with a command to draw the number on the canvas
main_canvas.bind("<space>", space_pressed)        #bind a key which will be numbers to the canvas with a command to draw the number on the canvas
main_canvas.bind("<p>", pause_timer)        #bind P key which will be pause the timer and press again to unpause the timer
main_canvas.bind("<h>", hint)        #bind H key which will randomly choose one unknown value and fill it with the correct value
main_canvas.focus_set() #set focus of canvas here so when a key is pressed it can be used

#FRAME TO HOLD END GAME BUTTONS
frm_end_game_button=tk.Frame(background=main_colors[0])
frm_end_game_button.grid(row=4, column=0, sticky="ew", pady=(0,5))
frm_end_game_button.grid_rowconfigure(0, weight=1)
frm_end_game_button.grid_columnconfigure([0,1], weight=1)

#CLEAR GAME BUTTON
btn_clear_game=tk.Button(master=frm_end_game_button, text='Clear Grid', font=("Lucida Sans Typewriter", 12), fg=button_colors[0], bg= button_colors[1],
                       relief=tk.RIDGE, borderwidth=3, command =clear_game)
btn_clear_game.grid(row=0, column=0, padx=(40,0), pady=(5,5))

#CHECK GAME BUTTON
btn_check_game=tk.Button(master=frm_end_game_button, text='Check Grid', font=("Lucida Sans Typewriter", 12), fg=button_colors[0], bg= button_colors[1],
                       relief=tk.RIDGE, borderwidth=3, command=check_game)
btn_check_game.grid(row=0, column=1, padx=(0,40), pady=(5,5))

# Run the application
window.mainloop()
