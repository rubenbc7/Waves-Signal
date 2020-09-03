import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate

from thinkdsp import read_wave
from thinkdsp import play_wave

import matplotlib.pyplot as plt

seno = SinSignal(freq=329, amp=1, offset=0)
segundo_seno = SinSignal(freq=659, amp=1, offset=0)
tercer_seno= SinSignal(freq=165, amp=1, offset= 0)
seno2 = SinSignal(freq=391, amp=1, offset=0)
segundo_seno2 = SinSignal(freq=783, amp=1, offset=0)
tercer_seno2= SinSignal(freq=196, amp=1, offset= 0)
seno3 = SinSignal(freq=493, amp=1, offset=0)
segundo_seno3 = SinSignal(freq=987, amp=1, offset=0)
tercer_seno3= SinSignal(freq=246, amp=1, offset= 0)

wave_seno = seno.make_wave(duration=1.0,start=1,framerate=44100)
wave_segundo_seno = segundo_seno.make_wave(duration=1.0,start=1,framerate=44100)
wave_tercer_seno = tercer_seno.make_wave(duration=1.0,start=1,framerate=44100)

wave_seno2 = seno2.make_wave(duration=1.0,start=0,framerate=44100)
wave_segundo_seno2 = segundo_seno2.make_wave(duration=1.0,start=0,framerate=44100)
wave_tercer_seno2 = tercer_seno2.make_wave(duration=1.0,start=0,framerate=44100)

wave_seno3 = seno3.make_wave(duration=1.0,start=2,framerate=44100)
wave_segundo_seno3 = segundo_seno3.make_wave(duration=1.0,start=2,framerate=44100)
wave_tercer_seno3 = tercer_seno3.make_wave(duration=1.0,start=2,framerate=44100)

wave_seno4 = seno2.make_wave(duration=1.0,start=3,framerate=44100)
wave_segundo_seno4 = segundo_seno2.make_wave(duration=1.0,start=3,framerate=44100)
wave_tercer_seno4 = tercer_seno2.make_wave(duration=1.0,start=3,framerate=44100)

resultante = wave_seno + wave_segundo_seno + wave_tercer_seno
resultante2 = wave_seno2 + wave_segundo_seno2 + wave_tercer_seno2
resultante3 = wave_seno3 + wave_segundo_seno3 + wave_tercer_seno3
resultante4 = wave_seno4 + wave_segundo_seno4 + wave_tercer_seno4
resres= resultante + resultante2 + resultante3 + resultante4

decorate(xlabel="Tiempo (s)")
decorate(ylabel="amplitud")

resres.plot()
resres.write("ac4.wav")

plt.show()