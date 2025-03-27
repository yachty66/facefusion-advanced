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
    -s /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/image.png \
    -t /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/4s_superman.mp4 \
    -o /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/result.mp4


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
    --processors face_swapper \
    --face-enhancer-model gfpgan_1.4 \
    --face-enhancer-blend 80 \
    --face-swapper-model inswapper_128 \
    --face-detector-model retinaface \
    -s /Users/maxhager/projects/facefusion-advanced/source.png \
    -t /Users/maxhager/projects/facefusion-advanced/superman_fixed.mp4 \
    -o /Users/maxhager/projects/facefusion-advanced/result_new.mp4


python facefusion.py headless-run \
    --keep-temp \
    --log-level debug \
    --execution-providers cpu \
    --execution-thread-count 16 \
    --execution-queue-count 2 \
    --temp-frame-format png \
    --face-selector-mode many \
    --face-mask-types box occlusion \
    --processors face_swapper \
    --face-enhancer-model gfpgan_1.4 \
    --face-enhancer-blend 80 \
    --face-swapper-model inswapper_128 \
    --face-detector-model retinaface \
    -s /Users/maxhager/projects/facefusion-advanced/source.png \
    -t /Users/maxhager/projects/facefusion-advanced/fixed_tiffanys.mp4 \
    -o /Users/maxhager/projects/facefusion-advanced/result_tiffany.mp4

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
    <!-- --face-detector-angles 0 90 270 \ -->
    -s /Users/maxhager/projects/facefusion/source.png \
    -t /Users/maxhager/projects/facefusion/fixed_superman.mp4 \
    -o /Users/maxhager/projects/facefusion/superman-with-angle-rotation.mp4

when running this command at which position does the error happen? i think at the 


roland:

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
    -s /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/image.png \
    -t /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/superman_4sec_fixed.mp4 \
    -o /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/result.mp4


runbo's v2 command

command = [
    "python",
    "ff.py",
    "headless-run",
    "--keep-temp",
    "--log-level",
    os.getenv("LOG_LEVEL", "warn"),
    "--execution-providers",
    os.getenv("EXECUTION_PROVIDER", "cuda"),
    "--execution-thread-count",
    "16",
    "--execution-queue-count",
    "1",  # Using the original command's queue count  
    "--video-memory-strategy",
    "moderate",
    "--temp-frame-format",
    "png",
    "--face-selector-mode",
    "reference",  # Matches the original command
    "--face-mask-types",
    "box",
    "occlusion",
    "--processors",
    "face_swapper",
    "face_enhancer",
    "--face-enhancer-model",
    "gfpgan_1.4",
    "--face-enhancer-blend",
    "80",
    "--face-swapper-model",
    # "inswapper_128",
    "ghost_3_256",
    "--face-detector-model",
    "yoloface",  # Matches the original command
    "--face-detector-score",
    "0.5",
    "--reference-face-distance",
    "0.5",
    "--face-landmarker-score",
    "0.5",
    # Removed '--headless' as it's not recognized by ff.py
    "--source-paths",
    final_image_path,
    "--target-path",
    final_video_path,
    "--output-path",
    output_path,
]


optimized command (from Runbo's v2 command, translated into v3):

for gui:

python facefusion.py run
--keep-temp
--log-level warn
--execution-providers cpu
--execution-thread-count 16
--execution-queue-count 1
--temp-frame-format png
--face-selector-mode reference
--face-mask-types box occlusion
--processors face_swapper face_enhancer
--face-enhancer-model gfpgan_1.4
--face-enhancer-blend 80
--face-swapper-model ghost_3_256
--face-detector-model yoloface
--face-detector-score 0.5
--reference-face-distance 0.5
--face-landmarker-score 0.5
--face-swapper-pixel-boost 1024x1024
-s /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/image.png \
-t /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/4s_superman.mp4 \
-o /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/result.mp4


for cli:

python facefusion.py headless-run \
--keep-temp \
--log-level info \
--execution-providers cpu \
--execution-thread-count 8 \
--execution-queue-count 1 \
--temp-frame-format png \
--face-selector-mode reference \
--face-mask-types box \
--processors face_swapper \
--face-swapper-model ghost_3_256 \
--face-detector-model yoloface \
--face-detector-score 0.5 \
--reference-face-distance 0.5 \
--face-landmarker-score 0.5 \
--face-swapper-pixel-boost 512x512 \
-s /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/image.png \
-t /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/4s_superman.mp4 \
-o /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/result.mp4

error: The error is coming from the face swapper model - specifically a TypeError: 'NoneType' object is not iterable when trying to process inputs. This typically means the model wasn't loaded correctly.
The issue is likely with --face-swapper-model ghost_3_256. Try changing back to the model you were using before:

fix:

python facefusion.py headless-run \
--keep-temp \
--log-level info \
--execution-providers cpu \
--execution-thread-count 16 \
--execution-queue-count 2 \
--video-memory-strategy moderate \
--temp-frame-format jpg \
--face-selector-mode reference \
--face-mask-types box \
--processors face_swapper \
--face-swapper-model inswapper_128_fp16 \
--face-swapper-pixel-boost 512x512 \
--face-detector-model yoloface \
--face-detector-size 640x640 \
--face-detector-score 0.5 \
--face-detector-angles 0 \
--reference-face-position 0 \
--reference-face-distance 0.5 \
--output-video-preset veryfast \
-s /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/image.png \
-t /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/superman_4sec_fixed.mp4 \
-o /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/result.mp4


old command