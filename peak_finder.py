from pydub import AudioSegment
import sys

syncfile = AudioSegment.from_file(sys.argv[1])

voldb = [(x.dBFS, index) for (index, x) in enumerate(syncfile) if x.dBFS > -1000]
top10 = sorted([x[0] for x in voldb])[-10:]

# Print peak times (in seconds) of top 10 dB peaks
for item in voldb:
    if item[0] in top10:
        print(item[1] * 0.001)
