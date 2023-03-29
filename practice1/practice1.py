import cv2
import numpy as np



chess_board = np.zeros((320, 320), dtype="uint8")
for row in range(0,280,80):
        for i in range(0,280,80):
            chess_board[row:row+40 , i:i+40]=255
            
for row in range(40,320,80):        
    for j in range(40,320,80):    
            chess_board[row:row+40 , j:j+40]=255

    
cv2.imshow("Chess Board", chess_board)
cv2.imwrite("chess_board.jpg",chess_board)
cv2.waitKey()