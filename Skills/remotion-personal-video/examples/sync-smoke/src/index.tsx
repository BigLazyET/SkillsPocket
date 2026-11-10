import React from 'react';
import {parseSrt} from '@remotion/captions';
import {
  AbsoluteFill,
  Composition,
  Html5Audio,
  OffthreadVideo,
  Sequence,
  registerRoot,
  staticFile,
  useVideoConfig,
} from 'remotion';
import fixture from './fixture.json';

const fps = 30;
const intro = 60;
const clickFrame = intro + 90;
const totalFrames = 450;

const Smoke: React.FC<{format: 'wide' | 'tall'}> = ({format}) => {
  const {width, height} = useVideoConfig();
  const {captions} = parseSrt({input: fixture[format]});
  const segmenter = new Intl.Segmenter('zh', {granularity: 'grapheme'});
  const cap = format === 'wide' ? 16 : 12;
  const font = '20px "PingFang SC", sans-serif';
  const measurer = document.createElement('canvas').getContext('2d')!;
  measurer.font = font;

  return (
    <AbsoluteFill style={{background: '#0f172a', color: 'white'}}>
      <Sequence from={0} durationInFrames={intro}>
        <AbsoluteFill style={{display: 'grid', placeItems: 'center', fontSize: 26}}>SyncSmoke</AbsoluteFill>
      </Sequence>
      <Sequence from={intro} durationInFrames={12 * fps}>
        <OffthreadVideo
          src={staticFile('screen.mp4')}
          muted
          style={{position: 'absolute', width: width * 0.8, left: width * 0.1, top: height * 0.12}}
        />
        <Html5Audio src={staticFile('narration.wav')} />
      </Sequence>
      <Sequence from={clickFrame} durationInFrames={3}>
        <Html5Audio src={staticFile('click.wav')} />
      </Sequence>
      {captions.map(({text, startMs, endMs}) => {
        const anchor = fixture.anchors.find(({start, end}) => start <= startMs && endMs <= end);
        const length = Array.from(segmenter.segment(text.trim())).reduce(
          (sum, {segment}) => sum + (/^[\x20-\x7e]$/.test(segment) ? 0.5 : 1), 0,
        );
        const start = intro + Math.round(startMs * fps / 1000);
        const end = intro + Math.round(endMs * fps / 1000);
        if (!anchor || length > cap || measurer.measureText(text).width + 24 > width * 0.9 || end <= start) {
          throw new Error(`Caption does not fit its anchor or layout: ${text}`);
        }
        return (
          <Sequence key={start} from={start} durationInFrames={end - start}>
            <AbsoluteFill style={{alignItems: 'center', justifyContent: 'flex-end', paddingBottom: height * 0.1}}>
              <span style={{background: '#111827', padding: '6px 12px', font, whiteSpace: 'nowrap'}}>{text}</span>
            </AbsoluteFill>
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};

registerRoot(() => (
  <>
    <Composition id="SyncWide" component={Smoke} defaultProps={{format: 'wide'}} fps={fps}
      durationInFrames={totalFrames} width={640} height={360} />
    <Composition id="SyncTall" component={Smoke} defaultProps={{format: 'tall'}} fps={fps}
      durationInFrames={totalFrames} width={360} height={640} />
  </>
));
