import cv2
import numpy as np

# Parameters
frame_size = (800, 600)
input_video_path = '/Users/harelwahnich/Documents/works.and.docs/2024.amot/pawns.court/altar.aleph/exports/D01.HAND.w.LAMP_1.mp4'
output_file = 'D01.HAND.w.LAMP_1__FULL_FRAME.mp4'

y_err = 36  
x_err = 0

# Coordinates for placing video segments
rect1_pos = (500 + x_err, 368 + y_err)
rect2_pos = (596 + x_err, 176 + y_err)

# Open the input video
cap = cv2.VideoCapture(input_video_path)
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get the frame rate of the input video
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"Input video frame rate: {fps}")

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 files
out = cv2.VideoWriter(output_file, fourcc, fps, frame_size)

# Process each frame
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Resize the frame to 96x192 if necessary
    frame = cv2.resize(frame, (96, 192))
    
    # Create a new frame with a white background
    output_frame = np.full((frame_size[1], frame_size[0], 3), (255, 255, 255), np.uint8)
    
    # Extract upper and lower halves
    upper_half = frame[:96, :]
    lower_half = frame[96:, :]
    
    # Place upper half in rect1_pos
    output_frame[rect1_pos[1]:rect1_pos[1]+96, rect1_pos[0]:rect1_pos[0]+96] = upper_half
    
    # Place lower half in rect2_pos
    output_frame[rect2_pos[1]:rect2_pos[1]+96, rect2_pos[0]:rect2_pos[0]+96] = lower_half
    
    # Write the frame to the video
    out.write(output_frame)

# Release everything when done
cap.release()
out.release()

print(f"Video saved as {output_file}")
