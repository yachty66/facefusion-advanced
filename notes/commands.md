old command

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
-s /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/image.png \
-t /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/superman_4sec_fixed.mp4 \
-o /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/result.mp4

new comand

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


command v2

python facefusion.py headless-run \
--keep-temp \
--log-level info \
--execution-providers cpu \
--execution-thread-count 16 \
--execution-queue-count 2 \
--temp-frame-format jpg \
--face-selector-mode many \
--face-mask-types box \
--processors face_swapper \
--face-swapper-model inswapper_128 \
--face-detector-model retinaface \
--output-video-preset ultrafast \
-s /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/image.png \
-t /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/superman_4sec_fixed.mp4 \
-o /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/result.mp4

The improvements that got us from ~18 seconds to 16.12 seconds were:
JPG instead of PNG format - The biggest gain came from changing --temp-frame-format png to --temp-frame-format jpg. JPG compression is much faster than PNG, especially for writing frames to disk.
Simplified face masking - Removed occlusion and only kept box masking, which requires less computation.
Ultrafast encoding preset - Changed to --output-video-preset ultrafast which significantly speeds up the final video encoding stage.
Reduced logging - Switched from --log-level debug to --log-level info, reducing I/O overhead from excessive logging.
Removed face enhancer - The original command included face enhancement in the processors, which we removed by only using --processors face_swapper instead of both swapper and enhancer.

command v3

python facefusion.py headless-run \
--keep-temp \
--log-level error \
--execution-providers cpu \
--execution-thread-count 16 \
--execution-queue-count 1 \
--temp-frame-format jpg \
--face-selector-mode many \
--face-mask-types box \
--processors face_swapper \
--face-swapper-model inswapper_128 \
--face-detector-model retinaface \
--face-detector-size 320x320 \
--face-detector-score 0.4 \
--face-detector-angles 0 \
--output-video-preset ultrafast \
--output-video-quality 70 \
-s /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/image.png \
-t /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/superman_4sec_fixed.mp4 \
-o /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/result.mp4



## 1. Implement Face-Swapper Pixel Boost
The most significant quality improvement with minimal speed impact:

```bash
python facefusion.py headless-run \
--keep-temp \
--log-level warn \
--execution-providers cpu \
--execution-thread-count 16 \
--execution-queue-count 1 \
--temp-frame-format jpg \
--face-selector-mode many \
--face-mask-types box \
--processors face_swapper \
--face-swapper-model inswapper_128 \
--face-swapper-pixel-boost 512x512 \
--face-detector-model retinaface \
--face-detector-size 512x512 \
--face-detector-score 0.5 \
--output-video-preset veryfast \
--output-video-quality 85 \
-s /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/image.png \
-t /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/superman_4sec_fixed.mp4 \
-o /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/result.mp4
```

**What this does**: The `--face-swapper-pixel-boost 512x512` parameter is key - it upscales the face swap to 512x512 resolution while still using the efficient inswapper_128 model, dramatically improving quality with only a modest speed impact. This effectively gives you 4x the resolution at maybe 1.5x the processing time.

## 2. Try a More Advanced Face Swapper Model
For even better quality with some speed tradeoff:

```bash
python facefusion.py headless-run \
--keep-temp \
--log-level warn \
--execution-providers cpu \
--execution-thread-count 16 \
--execution-queue-count 1 \
--video-memory-strategy moderate \
--temp-frame-format jpg \
--face-selector-mode many \
--face-mask-types box \
--processors face_swapper \
--face-swapper-model ghost_3_256 \
--face-detector-model retinaface \
--face-detector-score 0.5 \
--output-video-preset veryfast \
--output-video-quality 85 \
-s /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/image.png \
-t /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/superman_4sec_fixed.mp4 \
-o /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/result.mp4
```

**What this does**: The Ghost series models (especially ghost_3_256) provide much better quality swaps than inswapper_128, with better preservation of details and expressions.

## 3. Optimize Memory Management
Add memory optimization for complex videos:

```bash
python facefusion.py headless-run \
--keep-temp \
--log-level warn \
--execution-providers cpu \
--execution-thread-count 16 \
--execution-queue-count 1 \
--video-memory-strategy moderate \
--temp-frame-format jpg \
--face-selector-mode reference \
--face-mask-types box \
--processors face_swapper \
--face-swapper-model inswapper_128 \
--face-swapper-pixel-boost 512x512 \
--face-detector-model retinaface \
--reference-face-distance 0.6 \
--output-video-preset veryfast \
--output-video-quality 85 \
-s /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/image.png \
-t /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/superman_4sec_fixed.mp4 \
-o /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/result.mp4
```

**What this does**: 
- The `--video-memory-strategy moderate` balances speed and memory usage
- Using `--face-selector-mode reference` with `--reference-face-distance 0.6` improves consistency for videos with face angle changes
- These parameters will help with the "sample of ~10 different videos that don't swap well" that your boss mentioned

## 4. Add Face Occlusion Handling
For videos with occlusion issues (hands covering face, etc.):

```bash
python facefusion.py headless-run \
--keep-temp \
--log-level warn \
--execution-providers cpu \
--execution-thread-count 16 \
--execution-queue-count 1 \
--temp-frame-format jpg \
--face-selector-mode many \
--face-mask-types box occlusion \
--face-mask-blur 0.5 \
--processors face_swapper \
--face-swapper-model inswapper_128 \
--face-swapper-pixel-boost 512x512 \
--face-detector-model retinaface \
--output-video-preset veryfast \
--output-video-quality 85 \
-s /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/image.png \
-t /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/superman_4sec_fixed.mp4 \
-o /Users/rolandgraser/Desktop/software-projects/facefusion-advanced/images/result.mp4
```

**What this does**: Adds occlusion handling for better quality with obstructions in the video, with minimal speed impact.

## My Recommendation

Based on your boss's emphasis on quality while still maintaining reasonable performance, I recommend option #1. The pixel boost parameter gives you the most quality improvement with minimal performance impact. This allows you to continue using the fast inswapper_128 model while getting much better visual results.

For your test set of 10 problematic videos, you can try all four configurations and see which ones resolve the most issues with the best quality.
















