import cv2
import numpy as np

# Load the YOLOv3 weights and configuration files
model = cv2.dnn.readNetFromDarknet('yolov3-spp.cfg', 'yolov3-spp.weights')

# Get the names of the output layers
layer_names = model.getLayerNames()
output_layers_indexes = model.getUnconnectedOutLayers()
output_layers = []
for output_layer_index in output_layers_indexes:
    output_layers.append(layer_names[output_layer_index - 1])


# Capture video from webcam
cap = cv2.VideoCapture(0)

while True:
    ret, image = cap.read()

    # Resize the image to the YOLOv3 input size
    height, width, _ = image.shape
    new_width = int(height * (416/height))
    new_height = int(width * (416/width))
    image_resized = cv2.resize(image, (new_height, new_width))

    # Prepare the image for detection by converting it to a blob
    blob = cv2.dnn.blobFromImage(image_resized, 1/255.0, (416, 416), swapRB=True, crop=False)

    # Set the blob as input to the model
    model.setInput(blob)

    # Run forward pass through the model to get the detections
    detections = model.forward(output_layers)

    # Loop through the detections and draw bounding boxes around the detected humans
    for detection in detections:
        for detected_object in detection:
            scores = detected_object[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if class_id == 0 and confidence > 0.5:
                center_x = int(detected_object[0] * width)
                center_y = int(detected_object[1] * height)
                w = int(detected_object[2] * width)
                h = int(detected_object[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the output image
    cv2.imshow('Human Detection', image)

    # Quit on pressing "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
