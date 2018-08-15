from pydub import AudioSegment
from pydub.silence import split_on_silence
import sys

filename = sys.argv[1]

sound = AudioSegment.from_mp3(filename)

chunks = split_on_silence(sound, 
    # must be silent for at least half a second
    min_silence_len=500,

    # consider it silent if quieter than x dBFS
    silence_thresh=-30,
    
    # keep silence at the beginning and at the end
    keep_silence=100
 )

for i, chunk in enumerate(chunks):
    chunk.export("chunks/chunk{0}-{1}.mp3".format(i,filename.split(".")[0]), format="mp3")

print(len(chunks))
