import numpy as np

def display_data(data_list, cv2):

    if cv2.d_show_rec_data:
        # Create a blank image
        img_height = 25 * (len(data_list[-10:]) + 1)
        img_width = 900
        img = 255 * np.ones((img_height, img_width, 3), dtype=np.uint8)

        # Define font and other parameters
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.5
        font_thickness = 1
        text_height = 20

        # Display column headers
        headers = ['Index', 'Initial_Coordinate', 'Final_Coordinate', 'Distance', 'Time', 'Velocity', 'Angle']
        for i, header in enumerate(headers):
            cv2.putText(img, header, (i * 150 + 10, text_height), font, font_scale, (0, 0, 0), font_thickness, cv2.LINE_AA)

        # Display data
        #for row, data in enumerate(data_list):
        for row, data in enumerate(reversed(data_list[-10:])):
            row_text = [f"{int(data[header]):d}" if header == 'Index' else f"{data[header]:.4f}" if isinstance(data[header], (float, int)) else str(data[header]) for header in headers]
            for col, text in enumerate(row_text):
                cv2.putText(img, text, (col * 150 + 10, (row + 1) * text_height + 20), font, font_scale, (0, 0, 0), font_thickness, cv2.LINE_AA)

        # Display the image
        cv2.imshow("Recorded_Data Table", img)
