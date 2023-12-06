
import numpy as np
import time
class Button_Window:
    def __init__(self, cv2):
        self.cv2 = cv2
        cv2.namedWindow('Buttons')
        cv2.setMouseCallback('Buttons', self.button_click)

        # Initialize button colors
        self.button1_color = (255, 0, 0)
        self.button2_color = (255, 0, 0)

        self.rec_btn_state = False
        self.reset_btn_state = False

        # Create a black image with two buttons
        self.img_buttons = np.zeros((200, 400, 3), dtype=np.uint8)

        # Button 1 rectangle coordinates (x1, y1, x2, y2)
        self.button1_rect = (50, 50, 150, 100)

        # Button 2 rectangle coordinates (x1, y1, x2, y2)
        self.button2_rect = (200, 50, 300, 100)
        self.update_buttons()

    # Function to handle button clicks
    # Reset Button
    def button_click(self, event, x, y, flags, param):
        if event == self.cv2.EVENT_LBUTTONDOWN:
            if self.button1_rect[0] < x < self.button1_rect[2] and self.button1_rect[1] < y < self.button1_rect[3]:
                self.button1_color = (0, 255, 0)
                self.reset_btn_state = True

            # Record Button
            elif self.button2_rect[0] < x < self.button2_rect[2] and self.button2_rect[1] < y < self.button2_rect[3]:
                self.button2_color = (0, 255, 0)
                self.rec_btn_state = True


        elif event == self.cv2.EVENT_LBUTTONUP:
            self.button1_color = (255, 0, 0)
            self.button2_color = (255, 0, 0)
            self.rec_btn_state = False
            self.reset_btn_state = False


        self.update_buttons()

    # Function to update button colors
    def update_buttons(self):
        self.img_buttons[:] = 255  # Reset image
        self.cv2.rectangle(self.img_buttons, (self.button1_rect[0], self.button1_rect[1]), (self.button1_rect[2], self.button1_rect[3]),
                      self.button1_color, -1)
        self.cv2.putText(self.img_buttons, 'Reset', (self.button1_rect[0] + 10, self.button1_rect[1] + 30), self.cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255), 1, self.cv2.LINE_AA)

        self.cv2.rectangle(self.img_buttons, (self.button2_rect[0], self.button2_rect[1]), (self.button2_rect[2], self.button2_rect[3]),
                      self.button2_color, -1)
        self.cv2.putText(self.img_buttons, 'Record', (self.button2_rect[0] + 10, self.button2_rect[1] + 30), self.cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 255, 255), 1, self.cv2.LINE_AA)

        self.cv2.imshow('Buttons', self.img_buttons)

    def show_window(self,cv2):

        self.cv2.imshow('Buttons', self.img_buttons)
        cv2.d_rec_button = self.rec_btn_state
        cv2.d_reset_button = self.reset_btn_state
        self.rec_btn_state = False
        self.reset_btn_state = False


