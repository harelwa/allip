import os
import cv2
import numpy as np

# Parameters
frame_size = (800, 600)
input_video_dir = '/Users/harelwahnich/Documents/works.and.docs/2024.amot/pawns.court/altar.aleph/exports/'
input_video_name = 'D01.HAND.w.LAMP__HAND.and.WHITE.mp4'
input_video_path = os.path.join(input_video_dir, input_video_name)
output_file = f'{input_video_name}__FULL_FRAME.mp4'
alpha = 0.5  # Alpha value for blending (0.0 is fully transparent, 1.0 is fully opaque)

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

# Get the frame size of the input video
input_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
input_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"Input video size: {input_width}x{input_height}")

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 files
out = cv2.VideoWriter(output_file, fourcc, fps, frame_size)

# Process each frame
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Ensure the frame is the expected size
    if frame.shape[1] != input_width or frame.shape[0] != input_height:
        frame = cv2.resize(frame, (input_width, input_height))
    
    # Create a new frame with a white background and an alpha channel
    output_frame = np.full((frame_size[1], frame_size[0], 4), (255, 255, 255, int(alpha * 255)), np.uint8)
    
    # Convert the input frame to include an alpha channel
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    
    # Extract upper and lower halves
    upper_half = frame[:96, :]
    lower_half = frame[96:, :]
    
    # Place upper half in rect1_pos with alpha blending
    output_frame[rect1_pos[1]:rect1_pos[1]+96, rect1_pos[0]:rect1_pos[0]+96, :3] = upper_half[:, :, :3]
    output_frame[rect1_pos[1]:rect1_pos[1]+96, rect1_pos[0]:rect1_pos[0]+96, 3] = int(alpha * 255)
    
    # Place lower half in rect2_pos with alpha blending
    output_frame[rect2_pos[1]:rect2_pos[1]+96, rect2_pos[0]:rect2_pos[0]+96, :3] = lower_half[:, :, :3]
    output_frame[rect2_pos[1]:rect2_pos[1]+96, rect2_pos[0]:rect2_pos[0]+96, 3] = int(alpha * 255)
    
    # Convert the output frame back to BGR before writing
    output_frame_bgr = cv2.cvtColor(output_frame, cv2.COLOR_BGRA2BGR)
    
    # Write the frame to the video
    out.write(output_frame_bgr)

# Release everything when done
cap.release()
out.release()

print(f"Video saved as {output_file}")
