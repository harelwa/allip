# The Altar Hearth Code

**note** this code is holy

- video processing [py]
- video live mapping [pde]

## TASKS

- [ ] Imp Calibration Routine
- [ ] Calibrate Screen
- [ ] Create Video in desired resolution
- [ ] Map Video
- [ ] Manipulate Videos
  - how to crop ? ( maybe de vinci, as you are already editing there )


WHEN YOU DONT KNOW WHAT TO DO, REST.

## INFO

- Graphic Card Resolution = 800 X 600
- Each led Module Resolution = 96 X 96

## Modules Map

| Nos. | Nos. | Nos. |
|------|------|------|
| 1 6 4 `(1,1)` | 0 1 5 `(1,2)` | Nos. |
| Nos. | 1 8 3 `(2,2)` | Nos. |
| Nos. | 1 3 4 `(3,2)` | Nos. |

matrix index = (i, j)

## Altar ALEPH

play audio in a loop, to selected device, controling volume

using `ffplay`:

```bash
SDL_AUDIODRIVER="alsa" AUDIODEV="hw:3,0" ffplay -nodisp -autoexit -loop 0 -volume 50 ~/data/altar.voices/MOFAIM.KFAR-BLUM.JUNE-01-2024.13PM.wav
```

using `vlc`:

```bash
cvlc --aout alsa --alsa-audio-device hw:3,0 --volume 200 --loop $(realpath ~/data/altar.voices/MOFAIM.KFAR-BLUM.JUNE-01-2024.13PM.wav)
```

to list devices:

```bash
aplay -l
```

codec error from hell:

```bash
** (Processing core video:5621): WARNING **: 14:58:58.704: v4l2h264dec0: 1 frames 191-191 left undrained after CMD_STOP, eos sent too early: bug in decoder -- please file a bug
```

## CUTTING VIDEOS

```bash
ffmpeg -i /home/altar/pawns.court/altar.aleph/exports/D01.HAND.w.LAMP__HAND.and.WHITE.mp4 -ss 00:00:26 -t 00:00:15 -c copy D01.HAND.w.LAMP__HAND.and.WHITE_short.mp4
```

## Processing "Time to first image"

 --- start up time (ms) = *1688*

note: this is not necessarily accurate. as "time for first line of code is setup() is not considered"