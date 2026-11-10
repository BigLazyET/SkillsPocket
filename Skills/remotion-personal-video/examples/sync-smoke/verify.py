"""Check dimensions, frame count, and the audio/visual click in rendered fixtures."""
from array import array
import json
from pathlib import Path
import subprocess


def read(*command):
    return subprocess.check_output(command)


root = Path(__file__).resolve().parent
for name, dimensions in (("wide", (640, 360)), ("tall", (360, 640))):
    video_path = str(root / "out" / f"sync-{name}-v1.mp4")
    streams = json.loads(read("ffprobe", "-v", "error", "-show_streams", "-of", "json", video_path))["streams"]
    video, audio = streams
    assert video["codec_type"] == "video" and audio["codec_type"] == "audio", streams
    assert (video["width"], video["height"]) == dimensions, video
    assert (video["avg_frame_rate"], video["nb_frames"]) == ("30/1", "450"), video

    pixels = read(
        "ffmpeg", "-v", "error", "-i", video_path,
        "-vf", "select='eq(n,149)+eq(n,150)',crop=2:2:iw/2:ih*0.12+iw*0.225,format=rgb24",
        "-frames:v", "2", "-fps_mode", "passthrough", "-f", "rawvideo", "-",
    )
    assert len(pixels) == 24, len(pixels)
    assert pixels[2] > pixels[1] and pixels[13] > pixels[14], list(pixels)

    samples = array("f")
    samples.frombytes(read(
        "ffmpeg", "-v", "error", "-ss", "4.9", "-i", video_path, "-t", "0.25",
        "-vn", "-ar", "48000", "-ac", "1", "-f", "f32le", "-",
    ))
    onset = next(index for index, sample in enumerate(samples) if abs(sample) > 0.025)
    assert abs(4.9 + onset / 48000 - 5) < 1 / 30, onset
    print(f"{name}: 450 frames, visual click at frame 150, audible click within one frame")
