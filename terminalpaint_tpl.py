from pathlib import Path
from termpaint_lib import *

def text_to_color(w, lib_text_string, index):
    #string input colors a specific cell based on its corresponding color index
    color_pairs = {'x':0, 'g':1, 'w':2, 'r':3, 'g':4, 'b':5, 'c':6, 'm':7, 'y':8, 'w':9, 'x':10}
    x_coord = 0

    for y_coord in range(index):
        if x_coord == 120:
            x_coord = 0
            for each_letter in lib_text_string[y_coord]:
                w.chgat(y_coord, x_coord, 1, curses.color_pair(color_pairs[each_letter]))
 
                x_coord += 1
        
        else:
            for each_letter in lib_text_string[y_coord]:
                w.chgat(y_coord, x_coord, 1, curses.color_pair(color_pairs[each_letter]))

                x_coord += 1

def color_to_text(w, row, column):
    #converts the color in the specific coord into string
    color_pairs = {0:'x', 1:'g', 2:'w', 3:'r', 4:'g', 5:'b', 6:'c', 7:'m', 8:'y', 9:'w', 10:'x'}

    for y_coord in range(27):
        for x_coord in range(120):
            coord = y_coord,x_coord
            color_index = get_color_pair_idx_at(w, tuple(coord))
            row.append(color_pairs[color_index])
                
        column.append("".join(row))
        row.clear()

def move_cursor(w, canvas_dim, key, now_coord):

    """Move the cursor one position in a certain direction

    This function receives an ASCII value of a key pressed
    from the keyboard. It dictates where the cursor will be
    moved from `now_coord`. The resulting coordinate will be
    clipped to one less than the the canvas dimensions.

    :param w: the `Window` object
    :type w: `class Window`
    :param canvas_dim: canvas dimensions as a 2-ary tuple `(row, column)`
    :type canvas_dim: tuple
    :param key: the key pressed
    :type key: int
    :param now_coord: current coordinate as a 2-ary tuple `(row, column)`
    :type now_coord: tuple
    :return: resulting coordinate as a 2-ary tuple `(row, column)`
    """
    #initialize the current coord
    paint_curs_y,paint_curs_x = now_coord

    #Move UP cursor 
    if key == curses.KEY_UP: 
        paint_curs_y -= 1
        if paint_curs_y < 0:
            paint_curs_y = 0

    #Move DOWN cursor 
    elif key == curses.KEY_DOWN:  
        paint_curs_y += 1
        if paint_curs_y > (canvas_dim[0] - 1):
            paint_curs_y = canvas_dim[0] - 1

    #Move RIGHT cursor 
    elif key == curses.KEY_RIGHT: 
        paint_curs_x += 1
        if paint_curs_x > (canvas_dim[1] - 1):
            paint_curs_x = canvas_dim[1] - 1

    #Move LEFT cursor 
    elif key == curses.KEY_LEFT:  
        paint_curs_x -= 1
        if paint_curs_x < 0:
            paint_curs_x = 0

    #Moving the cursor
    w.move(paint_curs_y, paint_curs_x)
    w.refresh()

    #Returning a coord in tuple
    paint_cur_pos = paint_curs_y,paint_curs_x
    return tuple(paint_cur_pos)
        


def pencil_canvas(w, canvas_dim, coord, color_pair_idx):
    """Color a single coordinate in the canvas

    This function accepts a `color_pair_idx` corresponding
    to the index of the color pair initialized from `init_color_pairs()`.

    :param w: the `Window` object
    :type w: `class Window`
    :param canvas_dim: canvas dimensions as a 2-ary tuple `(row, column)`
    :type canvas_dim: tuple
    :param coord: coordinate to color as a 2-ary tuple `(row, column)`
    :type coord: tuple
    :param color_pair_idx: index of the color-pair `coord` should be set to
    :type color_pair_idx: int
    """
    color_cell_at(w, coord, color_pair_idx , until_end=False)

    #raise Exception('Stub code!')

def fill_canvas(w, canvas_dim, start_coord, color_pair_idx):
    """Flood-fill a color starting at a coordinate in the canvas

    Given a `start_coord`, this function will try to fill this cell, its
    adjacent cells (north, east, west, south), the adjacent cells' adjacent
    cells, etc. with a similar color pair as itself to a new color pair until
    the color pair of the whole group of cells have been changed.

    :param w: the `Window` object
    :type w: `class Window`
    :param canvas_dim: canvas dimensions as a 2-ary tuple `(row, column)`
    :type canvas_dim: tuple
    :param start_coord: starting coordinate to color as a 2-ary tuple `(row, column)`
    :type start_coord: tuple
    :param color_pair_idx: index of the color-pair `start_coord` and its adjacent cells should be set to
    :type color_pair_idx: int
    """
    # HINT: Read on breadth-first search (BFS) on a grid.
    #       Make sure to keep track of the original color while doing the coloring.


    #Declaring list for storing coords
    queued = []
    visited = []

    #Adding the current_coord to the queued list
    queued.append(start_coord)

    #While loop for adding coords in visited list up until len(queued) > 0
    while len(queued) > 0:
        coord = queued.pop(0)
        visited.append(coord)

        #Getting the initial color of the current coord prior to filling in colors
        initial_coord_color = get_color_pair_idx_at(w, start_coord)
        
        #Conditional statements for appending adjacent coords

        #Upper-adjacent cell
        if coord[0] - 1 >= 0:
            adjacent_coord_y = coord[0] - 1
            adjacent_coord_x = coord[1]

            adjacent_vertex_coord = (adjacent_coord_y, adjacent_coord_x)

            adjacent_color = get_color_pair_idx_at(w, adjacent_vertex_coord)

            if adjacent_color == initial_coord_color: 
                if adjacent_vertex_coord not in visited:
                    visited.append(adjacent_vertex_coord)
                    queued.append(adjacent_vertex_coord)

        #Down-adjacent cell
        if coord[0] + 1 < canvas_dim[0]:
            adjacent_coord_y = coord[0] + 1
            adjacent_coord_x = coord[1]

            adjacent_vertex_coord = (adjacent_coord_y, adjacent_coord_x)

            adjacent_color = get_color_pair_idx_at(w, adjacent_vertex_coord)

            if adjacent_color == initial_coord_color: 
                if adjacent_vertex_coord not in visited:
                    visited.append(adjacent_vertex_coord)
                    queued.append(adjacent_vertex_coord)

        #Left-adjacent cell
        if coord[1] - 1 >= 0:
            adjacent_coord_y = coord[0]
            adjacent_coord_x = coord[1] - 1

            adjacent_vertex_coord = (adjacent_coord_y, adjacent_coord_x)

            adjacent_color = get_color_pair_idx_at(w, adjacent_vertex_coord)

            if adjacent_color == initial_coord_color:
                if adjacent_vertex_coord not in visited:
                    visited.append(adjacent_vertex_coord)
                    queued.append(adjacent_vertex_coord)

        #Right-adjacent cell
        if coord[1] + 1 < canvas_dim[1]:
            adjacent_coord_y = coord[0]
            adjacent_coord_x = coord[1] + 1

            adjacent_vertex_coord = (adjacent_coord_y, adjacent_coord_x)

            adjacent_color = get_color_pair_idx_at(w, adjacent_vertex_coord)

            if adjacent_color == initial_coord_color:
                if adjacent_vertex_coord not in visited:
                    visited.append(adjacent_vertex_coord)
                    queued.append(adjacent_vertex_coord)

    #Coloring all of the visited coords
    for each_coord in visited:
        color_cell_at(w, each_coord, color_pair_idx)

    #Cursor movements
    w.move(start_coord[0], start_coord[1])
    w.refresh()
    curses.curs_set(2)

def clear_canvas(w, term_dim, canvas_dim):
    """Clear canvas

    This function fills the whole of the canvas with color pair 0.
    After that, it will print a prompt.

    :param w: the `Window` object
    :type w: `class Window`
    :param canvas_dim: canvas dimensions as a 2-ary tuple `(row, column)`
    :type canvas_dim: tuple
    :param term_dim: terminal dimensions as a 2-ary tuple `(row, column)`
    :type term_dim: tuple
    """
    
    #For loop that colors the whole canvas to black
    for i in range(canvas_dim[0]):
        w.chgat(i, 0, curses.color_pair(0)) 


def open_drawing(w, canvas_dim, fpath='sample.paint'):
    """Open a drawing file

    Open a .paint file specified in `fpath`. `fpath` is specified
    relative to the current working directory.

    If successful, it will return a 2-ary tuple (`is_success`, `str_info`)
    relating to the result of the file open. If successful, `is_success` is
    `True` and `str_info` contains `fpath`. Otherwise, `is_success` is `False`
    and `str_info` will either return an error message as a string or `None`.
    
    In addition, this function will clear the canvas and draw the contents
    of the file on it if the file is found and reading is successful.

    :param w: the `Window` object
    :type w: `class Window`
    :param canvas_dim: canvas dimensions as a 2-ary tuple `(row, column)`
    :type canvas_dim: tuple
    :param fpath: path to the paint file relative to the current working directory
    :type fpath: string
    :return: `tuple` (`bool`, `str`) of the status of opening
    """
    # HINT: Read on the `with` construct and `open()` function somewhere to open a file
    #raise Exception('Stub code!')
    
    color_to_text_lib = []

    try:
        #Read a file
        with open(fpath,'r') as fh:
                fpath = fh.readline()

                if 'EEE111_PAINT1234' in fpath:
                    fpath = fh.readlines()
                    clear_canvas(w, get_term_dim(), canvas_dim)

                    #Color-to-text conversion
                    index = len(fpath)
                    for i in range(index):
                        color_to_text_lib.append(fpath[i].replace('\n','')) 

                    text_to_color(w, color_to_text_lib, index)

                    return (True, 'Drawing Opened!')

                else:
                    return (False,'Wrong or Missing magic string!')
    except Exception:
        return (False, 'File cannot be found!')

        
def save_drawing(w, canvas_dim, fpath):
    """Save a drawing file

    Save the drawing on the canvas to the file path specified in `fpath`.
    `fpath` is specified relative to the current working directory. If
    the file exists, it will be overwritten. If `fpath` does not end with
    `.paint`, the function will append `.paint` to the path before saving.

    If successful, it will return a 2-ary tuple (`is_success`, `str_info`)
    relating to the result of the file open. If successful, `is_success` is
    `True` and `str_info` contains `fpath`. Otherwise, `is_success` is `False`
    and `str_info` will either return an error message as a string or `None`.
    
    In addition, this function will clear the canvas and draw the contents
    of the file on it if the file is found and reading is successful.

    :param w: the `Window` object
    :type w: `class Window`
    :param canvas_dim: canvas dimensions as a 2-ary tuple `(row, column)`
    :type canvas_dim: tuple
    :param fpath: path to the paint file relative to the current working directory
    :type fpath: string
    :return: `tuple` (`bool`, `str`) of the status of opening
    """
    # HINT: Read on the `with` construct and `open()` function somewhere to open a file
    row = []
    column = []

    try:

        color_to_text(w, row, column)

        with open(fpath,'w') as fh:
            fh.writelines("EEE111_PAINT1234" + "\n")

            for item in column:
                fh.write(item + "\n")
            
            return (True, "File saved!")
    
    except Exception:
        return(False,"File NOT saved!")

def ui_main(w):
    # Init color pairs
    init_ui(w)
    print_command_cheatsheet(w, get_term_dim())
    print_status_bar(w, get_term_dim(), msg=f'> Pencil Mode')

    #Initial Paint Mode
    now_paint_mode = 'p'
    #Calling out functions
    canvas_dim = get_canvas_dim()
    term_dim = get_term_dim()


    while True:
        key = w.getch()

        #Cursor movements
        move_cursor(w, get_canvas_dim(), key, get_cursor_pos())
    
        #Pencil Mode
        if curses.ascii.unctrl(key) == '^P':
            now_paint_mode = 'p'
            print_status_bar(w, get_term_dim(), msg=f'> Pencil Mode')
        
        #Fill Mode
        elif curses.ascii.unctrl(key) =='^F':
            now_paint_mode = 'f'
            print_status_bar(w, get_term_dim(), msg=f'> Fill Mode')
                    
        #Clear Mode
        elif curses.ascii.unctrl(key) == '^X':
            if show_yn_prompt(w, term_dim = get_term_dim(), size=(8, 40), msg='Clear the Canvas?'):
                print_status_bar(w, get_term_dim(), msg=f'Canvas Cleared!')
                clear_canvas(w, term_dim, canvas_dim)

                w.move(0,0)
                curses.curs_set(2)
                w.refresh()
                
            else:
                curses.curs_set(2)
                w.refresh()
        
        #Open Mode
        elif curses.ascii.unctrl(key) == '^O':
            #Asking for a file input
            text_prompt = collect_text_prompt(w, get_term_dim(), lines_from_end=2, msg='Enter drawing to open: ')
            
            #Checks the file input extension
            if text_prompt.endswith('.paint'):
                fpath = Path.cwd().joinpath("paint_files").joinpath(text_prompt)
                output_bool, output_string_message = open_drawing(w, canvas_dim, fpath)

                if output_bool:
                    print_status_bar(w, get_term_dim(), msg=f'{output_string_message}')

                else:
                    print_status_bar(w, get_term_dim(), msg=f'Drawing NOT opened! [{output_string_message}]')

                move_cursor(w, get_canvas_dim(), key, get_cursor_pos())
                curses.curs_set(2)
                w.refresh()

            else:
                print_status_bar(w, get_term_dim(), msg=f'Drawing NOT opened! [Wrong or missing file extension]')

                move_cursor(w, get_canvas_dim(), key, get_cursor_pos())
                curses.curs_set(2)
                w.refresh()

        #Save Mode
        elif curses.ascii.unctrl(key) == '^S':
            #Asking for a file input
            text_prompt = collect_text_prompt(w, get_term_dim(), lines_from_end=2, msg='Enter path to save drawing: ')

            #Checks the file input extension, append if .paint extension is not found
            if text_prompt.endswith('.paint'):
                fpath = Path.cwd().joinpath("paint_files").joinpath(text_prompt)
                output_bool, output_string_message = save_drawing(w, get_canvas_dim(), fpath)
                
                if output_bool:
                    print_status_bar(w, get_term_dim(), msg=f'{output_string_message}')

                else:
                    print_status_bar(w, get_term_dim(), msg=f'{output_string_message}')
                
                move_cursor(w, get_canvas_dim(), key, get_cursor_pos())
                curses.curs_set(2)
                w.refresh()

            #Append .paint file extension
            else:
                text_prompt += '.paint'
                fpath = Path.cwd().joinpath("paint_files").joinpath(text_prompt)
                output_bool, output_string_message = save_drawing(w, get_canvas_dim(), fpath)
                    
                if output_bool:
                    print_status_bar(w, get_term_dim(), msg=f'{output_string_message}')

                    curses.curs_set(2)
                    w.refresh()

                else:
                    print_status_bar(w, get_term_dim(), msg=f'{output_string_message}')
                
                move_cursor(w, get_canvas_dim(), key, get_cursor_pos())
                curses.curs_set(2)
                w.refresh()


        #Quit Mode
        elif curses.ascii.unctrl(key) == '^Q':
            if show_yn_prompt(w, term_dim = get_term_dim(), size=(8, 40), msg='Exit TerminalPaint?'):
                break

            else:   
                curses.curs_set(2)
                w.refresh()


    #Code for pencil and fill mode 

        #Pencil Mode
        if now_paint_mode == 'p':
            coord = get_cursor_pos()
            #Conditional Statement for calling out Pencil function with different color modes based on the key press/input

            key_dict = {119:2, 87:2, 114:3, 82:3, 103:4, 71:4, 98:5, 66:5, 99:6, 67:6, 109:7, 77:7, 121:8, 89:8, 120:10, 88:10}
            #color_key_lib = ['w','W','r','R','g','G','b','B','c','C','m','M','y','Y','x','X'] : Corresponding key press for key_dict

            if key in key_dict.keys():
                pencil_canvas(w, canvas_dim, coord, key_dict[key])
        
        #Fill Mode
        elif now_paint_mode == 'f':
            coord = get_cursor_pos()
            #Conditional Statement for calling out Fill function with different color modes based on the key press/input

            key_dict = {119:2, 87:2, 114:3, 82:3, 103:4, 71:4, 98:5, 66:5, 99:6, 67:6, 109:7, 77:7, 121:8, 89:8, 120:10, 88:10}
            #color_key_lib = ['w','W','r','R','g','G','b','B','c','C','m','M','y','Y','x','X'] : Corresponding key press for key_dict
    
            if key in key_dict.keys():
                fill_canvas(w, canvas_dim, coord, key_dict[key])
        

    #raise Exception('Stub code!')

def main():
    curses.wrapper(ui_main)

if __name__ == '__main__':
    main()
