# The Altar Hearth, 3rd Movement: Pawns court

## About
In this repository you will find the "operating system" of *constempllation no. 2* by [Altar Hearth](https://www.instagram.com/altar.hearth/) / [Harel Wahnich](https://www.wahnich.studio/): **The Altar Hearth, 3rd Movement: Pawns court**.


*Pawns Court* is presented as part of the [Bezalel MFA thesis exhibition](https://www.instagram.com/bezalel.mfa/).

*Pawns Court* has two operating [pis](https://www.raspberrypi.com/): One for "sound"/audio, named *altar-voices*, and the other for "video"/image-stream named *altar*.

**altar** is responsiblle of video live mapping to two 50x50 cm / 96x96 pxls / 5pp LED modules installed one over the other. It uses [processing](https://processing.org/download) to achive this task.

**altar-voices** is responsiblle of audio, sent to a DAC connected to an apmlfier which has it's outputs connected to [25mm-exciter](https://www.daytonaudio.com/product/1177/daex25fhe-4-framed-high-efficiency-25mm-exciter) which are insalled on foam boards.

[ tbd ] palying audio and video in sync on the two `pis` is done with `python`.

"system control" = `pi` up / down // do this do that is done with commands sent over `ssh`.

[go-task](https://taskfile.dev/installation/) is used as the project swiss task runner.

## LED Diary

### Modules

- LED matrix Graphic Card Resolution = 800 X 600
- Each led Module Resolution = 96 X 96

**Modules Map**:

| Nos. | Nos. | Nos. |
|------|------|------|
| 1 6 4 `(1,1)` | 0 1 5 `(1,2)` | Nos. |
| Nos. | 1 8 3 `(2,2)` | Nos. |
| Nos. | 1 3 4 `(3,2)` | Nos. |

matrix index = (i, j)

### Play Video

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

### Codec errors from hell

```bash
** (Processing core video:5621): WARNING **: 14:58:58.704: v4l2h264dec0: 1 frames 191-191 left undrained after CMD_STOP, eos sent too early: bug in decoder -- please file a bug
```

### CUTTING VIDEOS

```bash
ffmpeg -i /home/altar/pawns.court/altar.aleph/exports/D01.HAND.w.LAMP__HAND.and.WHITE.mp4 -ss 00:00:26 -t 00:00:15 -c copy D01.HAND.w.LAMP__HAND.and.WHITE_short.mp4
```

### Processing "Time to first image"

 --- start up time (ms) = *1688*

**note**: this is not necessarily accurate. as "time for first line of code is setup() is not considered"