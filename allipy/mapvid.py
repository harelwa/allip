import cv2
import numpy as np

# Parameters
frame_size = (800, 600)
# mapping for pie's HDMI_0 port! it's different between ports
# diff between processing calibration. god know why.
y_err = 35  
x_err = 0

x_015, y_015 = 500 + x_err, 368 + y_err  # module no. 015
x_182, y_182 = 596 + x_err, 176 + y_err  # module no. 182

rect1 = (x_015, y_015, x_015 + 96, y_015 + 96)
rect2 = (x_182, y_182, x_182 + 96, y_182 + 96)

colors = {'rect1': (0, 0, 255), 'rect2': (255, 0, 0), 'background': (255, 255, 255)}

frame_rate = 23.976
length = 0.5 # sec

num_frames = int(length * frame_rate)
output_file = 'output.mp4'

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 files
out = cv2.VideoWriter(output_file, fourcc, 23.976, frame_size)

for _ in range(num_frames):
    # Create a new frame with a white background
    frame = np.full((frame_size[1], frame_size[0], 3), colors['background'], np.uint8)
    
    # Draw rectangles
    cv2.rectangle(frame, rect1[:2], rect1[2:], colors['rect1'], -1)
    cv2.rectangle(frame, rect2[:2], rect2[2:], colors['rect2'], -1)
    
    # Write the frame to the video
    out.write(frame)

# Release everything when done
out.release()

print(f"Video saved as {output_file}")
