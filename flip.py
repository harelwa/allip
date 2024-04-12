import cv2


# Open the input video
print("Open the input video:")
cap = cv2.VideoCapture('/Users/harelw/Downloads/IMG_0290.mov')

# Get video properties
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("FUCK")

print(f'Video Properties: fourcc = {fourcc} , fps = {fps} , width = {width} height = {height}')

# Create a video writer for the output video
out = cv2.VideoWriter('/Users/harelw/Downloads/flipped_output.avi', fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Split the frame into upper and lower halves
    upper_half = frame[:height//2, :]
    lower_half = frame[height//2:, :]

    # Combine the halves in reversed order
    flipped_frame = cv2.vconcat([lower_half, upper_half])

    # Write the flipped frame to the output video
    out.write(flipped_frame)

# Release resources
cap.release()
out.release()
