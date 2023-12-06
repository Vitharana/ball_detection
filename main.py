import cv2

cv2.Window1_Name_Ball_Tracker = 'Ball_Tracker'
cv2.Window2_Name_Track_Bars = 'Track_Bars'



# main data
cv2.d_radius = 0
cv2.d_center = (0, 0)
cv2.d_key = 'no_press'
cv2.d_hsv_state = True
cv2.d_data_table_state = True
cv2.d_avg_coordinate = (0,0)
cv2.d_ball_mov = True
cv2.all_data_ok = False
cv2.d_draw_illustration = True


# for the data_saver use
cv2.d_record_data = False
cv2.d_data_point_count = 0
cv2.d_data_points = []
cv2.d_folder_no = 0


# show the recorded data table
cv2.d_show_rec_data = True



#Data_Saved
cv2.d_initial_coordinate = (-1,-1)
cv2.d_final_coordinate = (-1,-1)
cv2.d_radius_1 = 0
cv2.d_radius_2 = 0
cv2.d_ball_time = 0
cv2.d_ball_angle = 0
cv2.d_ball_dist = 0
cv2.d_ball_vel = 0

# Button data
cv2.d_rec_button = False
cv2.d_reset_button = False

# create the main window and sets the size

from initialize_opencv import create_main_window

cap = create_main_window(cv2)

# create the window for track bars
from trackbars import add_track_bars

add_track_bars(cv2)


from main_program import run_main_program

# load the files
from trackbars import load_trackbar_values, save_trackbar_values

# ball analyser functions
from data_analyser import run_data_analyser



from display_current_data import show_data_table



from button_check import Button_Window
btn_win = Button_Window(cv2)


# Show recorded data
from show_recorded_data_list import  display_data



while True:

    # lock windows

    btn_win.show_window(cv2)
    if cv2.d_rec_button:
        print(f"Record -> {cv2.d_rec_button}")

    if cv2.d_reset_button:
        print(f"Reset -> {cv2.d_reset_button}")

    run_main_program(cv2, cap)
    run_data_analyser(cv2)

    # quit the program
    if cv2.d_key == 'q':
        break

    # load saved profile
    elif cv2.d_key == 'l':
        try:
            load_trackbar_values(cv2)
        except:
            print("Loading Fail")

    # save detection profile
    elif cv2.d_key == 's':
        try:
            save_trackbar_values(cv2)

        except:
            print("Detection Profile Saving Failed")

    show_data_table(cv2)

    # Show recorded data
    display_data(cv2.d_data_points,cv2)








# End the resources allocated
cap.release()
cv2.destroyAllWindows()
