"""Generate local test media with macOS say and FFmpeg."""
import json
from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory


def run(*args):
    subprocess.run(args, check=True)


def srt_time(ms):
    seconds, millis = divmod(ms, 1000)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02},{millis:03}"


def srt(cues):
    return "\n".join(
        f"{index}\n{srt_time(start)} --> {srt_time(end)}\n{text}\n"
        for index, (start, end, text) in enumerate(cues, 1)
    )


root = Path(__file__).resolve().parent
public = root / "public"
public.mkdir(exist_ok=True)
ffmpeg = ("ffmpeg", "-hide_banner", "-loglevel", "error", "-y")
texts = ["打开设置。", "点击保存，", "看到提示就完成了。"]
starts = [500, 4500, 5700]
cues = []

with TemporaryDirectory() as temp:
    inputs = []
    for start, text in zip(starts, texts):
        take = Path(temp) / f"{start}.aiff"
        run("say", "-v", "Tingting", "-r", "195", "-o", str(take), text)
        duration = subprocess.check_output((
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "csv=p=0", str(take),
        ), text=True)
        if duration.strip() == "N/A":
            raise RuntimeError("macOS say produced no audio. Verify the Tingting voice is installed and available.")
        cues.append((start, start + round(float(duration) * 1000), text))
        inputs.extend(("-i", str(take)))

    assert all(cue[1] <= next_cue[0] for cue, next_cue in zip(cues, cues[1:])), cues
    assert cues[-1][1] < 12000, cues
    delays = ";".join(f"[{i}:a]adelay={ms}:all=1[a{i}]" for i, ms in enumerate(starts))
    run(*ffmpeg, *inputs, "-filter_complex",
        delays + ";[a0][a1][a2]amix=inputs=3:normalize=0,apad",
        "-t", "12", "-ar", "48000", str(public / "narration.wav"))

run(*ffmpeg, "-f", "lavfi", "-i", "color=c=0x1e293b:s=320x180:r=30:d=12",
    "-vf", "drawbox=x=80:y=60:w=160:h=60:c=0x2563eb:t=fill,"
    "drawbox=x=80:y=60:w=160:h=60:c=0x22c55e:t=fill:enable='gte(n,90)'",
    "-c:v", "libx264", str(public / "screen.mp4"))
run(*ffmpeg, "-f", "lavfi", "-i", "sine=frequency=1200:sample_rate=48000:duration=0.07",
    str(public / "click.wav"))

wide = [cues[0], (cues[1][0], cues[2][1], texts[1] + texts[2])]
for name, data in (("wide", wide), ("tall", cues)):
    (public / f"{name}.srt").write_text(srt(data), encoding="utf-8")
anchors = [
    {"id": "U01", "start": cues[0][0], "end": cues[0][1]},
    {"id": "U02", "start": cues[1][0], "end": cues[2][1]},
]
(root / "src/fixture.json").write_text(
    json.dumps({"wide": srt(wide), "tall": srt(cues), "anchors": anchors}, ensure_ascii=False),
    encoding="utf-8",
)
