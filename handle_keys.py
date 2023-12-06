from data_saver import  save_data_point


def key_press(cv2):

    # get the key pressed
    key = cv2.waitKey(1)


    if key & 0xFF == ord('q'):
        cv2.d_key = 'q' #quits the program
        print("Program Quited")


    elif key & 0xFF == ord('l'):
        cv2.d_key = 'l' # load detection profile


    elif key & 0xFF == ord('s'):
        cv2.d_key = 's' # save a detection profile

    elif key & 0xFF == ord('h'):
        #print("hsv mode") # Control the visibility of the HSV Mask Image


        cv2.d_hsv_state = not cv2.d_hsv_state
        if cv2.d_hsv_state:
            print("HSV Output Enabled")
        if not cv2.d_hsv_state:
            cv2.destroyWindow("HSV")
            print("HSV Output Disabled")

    elif key & 0xFF == ord('t'):
    #print("hsv mode") # Control the visibility of the HSV Mask Image



        cv2.d_data_table_state = not cv2.d_data_table_state
        if cv2.d_data_table_state:
            print("Data TableView Enabled")
        if not cv2.d_data_table_state:
            cv2.destroyWindow("Table_Window")
            print("Data TableView Disabled")

    elif key & 0xFF == ord('1') or cv2.d_reset_button:
        cv2.d_key = '1' # for recording initial coordinates

    elif key & 0xFF == ord('d'):
        cv2.d_draw_illustration = not cv2.d_draw_illustration

    elif key & 0xFF == ord('r') or cv2.d_rec_button:
        cv2.d_record_data = True
        save_data_point(cv2)


    elif key & 0xFF == ord('c'):

        cv2.d_folder_no += 1
        print(f"Folder Changed from {cv2.d_folder_no-1} ---> {cv2.d_folder_no}")

    # show the recorded data table
    elif key & 0xFF == ord('p'):
    # To show the recorded data

        cv2.d_show_rec_data = not cv2.d_show_rec_data
        if cv2.d_show_rec_data:
            print("Recorded Data View Enabled")
        if not cv2.d_show_rec_data:
            cv2.destroyWindow("Recorded_Data Table")
            print("Recorded Data View Disabled")




    else:
        cv2.d_key = 'no_press'

