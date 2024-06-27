from speechbrain.inference.separation import SepformerSeparation as separator
import torchaudio

torchaudio.set_audio_backend("ffmpeg")

model = separator.from_hparams(source="speechbrain/sepformer-wsj02mix", savedir='pretrained_models/sepformer-wsj02mix')

fp = "/Users/harelwahnich/Documents/works.and.docs/2024.amot/pawns.court/mofaim.audio/exsports/THE.VOICES__NIGHT__no2.wav"
fp = str(fp)
# for custom file, change path
est_sources = model.separate_file(path=fp)

torchaudio.save("source1hat.wav", est_sources[:, :, 0].detach().cpu(), 8000)
torchaudio.save("source2hat.wav", est_sources[:, :, 1].detach().cpu(), 8000)
