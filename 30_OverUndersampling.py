from pcdr import makeRealWave_time
import matplotlib.pyplot as plt

## 1.
## What figure in the Harvey Mudd page demonstrates what is happening in this video? 


## 2. 
## Try this.
## Notice that the wave degrades the closer the frequency gets to the sample rate.
# from pcdr import makeRealWave_time
# import matplotlib.pyplot as plt
# 
# plt.figure(figsize=(8,6))  # since we have multiple subplots this makes it large enough so nothing gets cropped off
# 
# samp_rate = 20
# seconds = 2
# 
# freq = 1
# timestamps, wave = makeRealWave_time(seconds, samp_rate, freq)
# plt.subplot(2, 2, 1, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
# plt.plot(timestamps, wave, "o-")
# 
# freq = 3
# timestamps, wave = makeRealWave_time(seconds, samp_rate, freq)
# plt.subplot(2, 2, 2, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
# plt.plot(timestamps, wave, "o-")
# 
# freq = 6
# timestamps, wave = makeRealWave_time(seconds, samp_rate, freq)
# plt.subplot(2, 2, 3, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
# plt.plot(timestamps, wave, "o-")
# 
# freq = 9
# timestamps, wave = makeRealWave_time(seconds, samp_rate, freq)
# plt.subplot(2, 2, 4, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
# plt.plot(timestamps, wave, "o-")
# 
# plt.tight_layout()
# plt.show()


## 3
## Copy and modify the previous example (including the code for all
## of the subplots). Set the samp_rate to 40.
# ## Do the waves appear to be higher or lower quality?
# 
# from pcdr import makeRealWave_time
# import matplotlib.pyplot as plt
# 
# plt.figure(figsize=(8,6))  # since we have multiple subplots this makes it large enough so nothing gets cropped off
# 
# samp_rate = 40
# seconds = 2
# 
# freq = 1
# timestamps, wave = makeRealWave_time(seconds, samp_rate, freq)
# plt.subplot(2, 2, 1, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
# plt.plot(timestamps, wave, "o-")
# 
# freq = 3
# timestamps, wave = makeRealWave_time(seconds, samp_rate, freq)
# plt.subplot(2, 2, 2, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
# plt.plot(timestamps, wave, "o-")
# 
# freq = 6
# timestamps, wave = makeRealWave_time(seconds, samp_rate, freq)
# plt.subplot(2, 2, 3, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
# plt.plot(timestamps, wave, "o-")
# 
# freq = 9
# timestamps, wave = makeRealWave_time(seconds, samp_rate, freq)
# plt.subplot(2, 2, 4, title=f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
# plt.plot(timestamps, wave, "o-")
# 
# plt.tight_layout()
# plt.show()

## 4a
## Try this. Notice that the frequency is 9,
## but when you plot it, it (surprisingly) has a frequency of 1.
## What is the name for this phenomenon? 
# from pcdr import makeRealWave_time
# 
# samp_rate = 10
# seconds = 1
# freq = 9
# timestamps, wave = makeRealWave_time(seconds, samp_rate, freq, allowAliasing=True)
# plt.title(f"samp_rate: {samp_rate} samp/sec, freq: {freq} Hz")
# plt.plot(timestamps, wave, "o-")
# plt.show()


## 4b
## Let's view that with an adequate sample rate at the same time to see the difference.
# from pcdr import makeRealWave_time
# 
# seconds = 1
# samp_rate_too_low = 10
# samp_rate_adequate = 400
# freq = 9
# timestamps, wave = makeRealWave_time(seconds, samp_rate_too_low, freq, allowAliasing=True)
# timestamps2, wave2 = makeRealWave_time(seconds, samp_rate_adequate, freq)
# 
# plt.xlabel("Time")
# plt.ylabel("Amplitude")
# plt.plot(timestamps, wave, "o-", label=f"{freq} Hz with {samp_rate_too_low} Sps")
# plt.plot(timestamps2, wave2, "x-", label=f"{freq} Hz with {samp_rate_adequate} Sps")
# plt.legend(loc="upper right")
# plt.show()

## 5
## Copy and modify the above example.
## Set the freq to 37 and the sample_rate_too_low variable to 40.
## Due to aliasing, what frequency is displayed by the blue line?
## What is the relationship between the displayed frequency and the sample rate?
# 
# from pcdr import makeRealWave_time
# 
# seconds = 1
# samp_rate_too_low = 40
# samp_rate_adequate = 400
# freq = 37
# timestamps, wave = makeRealWave_time(seconds, samp_rate_too_low, freq, allowAliasing=True)
# timestamps2, wave2 = makeRealWave_time(seconds, samp_rate_adequate, freq)
# 
# plt.xlabel("Time")
# plt.ylabel("Amplitude")
# plt.plot(timestamps, wave, "o-", label=f"{freq} Hz with {samp_rate_too_low} Sps")
# plt.plot(timestamps2, wave2, "x-", label=f"{freq} Hz with {samp_rate_adequate} Sps")
# plt.legend(loc="upper right")
# plt.show()