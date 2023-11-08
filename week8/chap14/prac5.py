import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import wave


class WavFFT(object):
    def __init__(self, wav_path):
        self.wave_data = None
        self.time_len = None
        self.nframes = None
        self.framerate = None
        self.sampwidth = None
        self.nchannels = None
        self.path = wav_path

    def read_wav(self):
        with wave.open(self.path, "rb") as fp:
            parameters = fp.getparams()
            self.nchannels, self.sampwidth, self.framerate, self.nframes = parameters[:4]
            self.time_len = self.nframes * 1.0 / self.framerate
            str_data = fp.readframes(self.nframes)
            # wave_data = np.fromstring(str_data, dtype=np.short)
            wave_data = np.frombuffer(str_data, dtype=np.short)
            wave_data.shape = -1, self.nchannels
            self.wave_data = wave_data.T

    def FFT(self):
        yf = np.fft.fft(self.wave_data)  # FFT
        bias = (yf[:, 0] / self.nframes).real
        yf_amplitude = np.abs(yf) * (2.0 / self.nframes)
        yf_amplitude[:, 0] = bias  # 直流分量(0 Hz处)修正
        self.yf_amplitude = yf_amplitude[:, 0:self.nframes // 2]  # 有效信息只有一半

    def plot(self):
        # matplotlib.rcParams["font.sans-serif"] = ["SimHei"]
        # matplotlib.rcParams["axes.unicode_minus"] = False
        self.time = np.arange(0, self.nframes // 2) * (1.0 / self.framerate)
        self.freq = np.arange(0, self.nframes // 2) * self.framerate / self.nframes  # 实际频率
        for i in range(self.nchannels):
            plt.subplot(2, self.nchannels, i + 1)
            plt.plot(self.time, self.wave_data[i, :])
            plt.xlabel("time")
            plt.ylabel("signal")
            plt.grid()
            plt.title("channel%d timezone signal" % (i + 1))
            plt.subplot(2, self.nchannels, self.nchannels + i + 1)
            plt.plot(self.freq, self.yf_amplitude[i, :], "r-")
            plt.xlabel("Frequency [Hz]")
            plt.ylabel("Amplitude ")
            plt.grid()
            plt.title("FFT (channel%d freqzone signal)" % (i + 1))
        plt.suptitle("wav FFT", fontsize=14, color="magenta")
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    wav = WavFFT(wav_path='./resource/1.wav')
    wav.read_wav()
    wav.FFT()
    wav.plot()
