from faster_whisper import WhisperModel,BatchedInferencePipeline
import logging
from datetime import datetime

model_size = "distil-small.en"
 

# Run on GPU with FP16
model = WhisperModel(model_size,device="cpu", compute_type="float32")
#batched_model = BatchedInferencePipeline(model=model)

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# model = WhisperModel(model_size, device="cpu", compute_type="int8")

#segments, info = batched_model.transcribe("here.wav", beam_size=1,batch_size=32)

segments, info = model.transcribe("mil.wav", beam_size=1,temperature=0)


# print("Detected language '%s' with probability %f" % (info.language,info.duration))
# logging.b1asicConfig()
# logging.getLogger("faster_whisper")


for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))


#create new file
#write to the file
#add the file name to array
#process each array