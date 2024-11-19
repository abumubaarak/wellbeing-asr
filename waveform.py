import numpy as np
import wave
from scipy.io import wavfile


output = wavfile.read('jfk.wav')
print(output[0])

# # Start opening the file with wave
# with wave.open('jfk.mp3') as f:
#     # Read the whole file into a buffer. If you are dealing with a large file
#     # then you should read it in blocks and process them separately.
#     buffer = f.readframes(f.getnframes())
#     # Convert the buffer to a numpy array by checking the size of the sample
#     # width in bytes. The output will be a 1D array with interleaved channels.
#     interleaved = np.frombuffer(buffer, dtype=f'int{f.getsampwidth()*8}')
#     # Reshape it into a 2D array separating the channels in columns.
#     data = np.reshape(interleaved, (-1, f.getnchannels()))
#     print(data)