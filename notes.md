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
    -t /Users/maxhager/projects/facefusion/target-superman.png \
    -o /Users/maxhager/projects/facefusion/target-time.png





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
    -s /Users/maxhager/projects/facefusion-advanced/source.png \
    -t /Users/maxhager/projects/facefusion-advanced/target-superman.png \
    -o /Users/maxhager/projects/facefusion-advanced/target-time.png