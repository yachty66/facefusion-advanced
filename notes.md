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
    -s /Users/maxhager/projects/facefusion-advanced/source.png \
    -t /Users/maxhager/projects/facefusion-advanced/superman.mp4 \
    -o /Users/maxhager/projects/facefusion-advanced/result_new.mp4

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
    -t /Users/maxhager/projects/facefusion-advanced/superman.mp4 \
    -o /Users/maxhager/projects/facefusion-advanced/sink.mp4  

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
    -s /Users/maxhager/projects/facefusion-advanced/source.png \
    -t /Users/maxhager/projects/facefusion-advanced/target-superman.png \
    -o /Users/maxhager/projects/facefusion-advanced/target-time.png


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
    -o /Users/maxhager/projects/facefusion-advanced/sink.png

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
    -o /Users/maxhager/projects/facefusion-advanced/sink.png    

python facefusion.py headless-run \
    --keep-temp \
    --log-level debug \
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
<<<<<<< Updated upstream
    -s /Users/maxhager/projects/facefusion-advanced/source.png \
    -t /Users/maxhager/projects/facefusion-advanced/five_frame_superman.mp4 \
    -o /Users/maxhager/projects/facefusion-advanced/result_new.mp4
=======
    -s /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/source.png \
    -t /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/new_superman.mp4 \
    -o /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/result_new.mp4
>>>>>>> Stashed changes

this seems to work so the problem is that an error occurs with the original video 

so in the case the command throws and error we want ot run on

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
    --face-detector-angles 0 90 270 \
    -s /Users/maxhager/projects/facefusion/source.png \
    -t /Users/maxhager/projects/facefusion/fixed_superman.mp4 \
    -o /Users/maxhager/projects/facefusion/superman-with-angle-rotation.mp4

when running this command at which position does the error happen? i think at the 