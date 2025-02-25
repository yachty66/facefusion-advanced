## command for video

python facefusion.py headless-run \
    --keep-temp \
    --log-level warn \
    --execution-providers cpu \
    --execution-thread-count 16 \
    --execution-queue-count 2 \
    --temp-frame-format png \
    --face-selector-mode many \
    --face-mask-types box occlusion \
    --processors face_swapper face_enhancer \
    --face-enhancer-model gfpgan_1.4 \
    --face-enhancer-blend 80 \
    --face-swapper-model inswapper_128 \
    --face-detector-model retinaface \
    -s /Users/maxhager/projects/facefusion/source.png \
    -t /Users/maxhager/projects/facefusion/fixed_superman.mp4 \
    -o /Users/maxhager/projects/facefusion/result.mp4

## command for face swap

python facefusion.py headless-run \
    --keep-temp \
    --log-level warn \
    --execution-providers cpu \
    --execution-thread-count 16 \
    --execution-queue-count 2 \
    --temp-frame-format png \
    --face-selector-mode many \
    --face-mask-types box occlusion \
    --processors face_swapper face_enhancer \
    --face-enhancer-model gfpgan_1.4 \
    --face-enhancer-blend 80 \
    --face-swapper-model inswapper_128 \
    --face-detector-model retinaface \
    --face-detector-angles 0 90 180 270 \
    -s /Users/maxhager/projects/facefusion/source.png \
    -t /Users/maxhager/projects/facefusion/fixed_superman.mp4 \
    -o /Users/maxhager/projects/facefusion/superman-with-angle-rotation.mp4

python facefusion.py headless-run \
    --keep-temp \
    --log-level warn \
    --execution-providers cpu \
    --execution-thread-count 16 \
    --execution-queue-count 2 \
    --temp-frame-format png \
    --face-selector-mode many \
    --face-mask-types box occlusion \
    --processors face_swapper face_enhancer \
    --face-enhancer-model gfpgan_1.4 \
    --face-enhancer-blend 80 \
    --face-swapper-model inswapper_128 \
    --face-detector-model retinaface \
    -s /Users/maxhager/projects/facefusion/source.png \
    -t /Users/maxhager/projects/facefusion/target.png \
    -o /Users/maxhager/projects/facefusion/target-time.png


i need to track the time how long it takes to process one frame with the angle command vs without and then i can calculate how much time can be saved

- find a frame where the face detection doesnt work
- try to play around with that frame and try to find a way how this frame can be detected

every time a face is not getting detected we could try to rotate the face to a new angle - we could try this with each angle and then we eventually could find a angle which works


1. find a frame which doesnt work by running a video through the pipeline 
2. take this frame and try to run this frame through the face swap pipeline and run it with each possible angle until the frame is getting detected