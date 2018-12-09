import wave
import pyaudio

class Alarm:
    playing = False
    
    def __init__(self):
        self._audio = pyaudio.PyAudio()

    def play(self, filename):
        self.playing = True
        while True:
            if not self.playing :
                break
            with wave.open(filename, 'rb') as wf:
                stream = self._audio.open(format=self._audio.get_format_from_width(wf.getsampwidth()),
                                 channels=wf.getnchannels(),
                                 rate=wf.getframerate(),
                                 output=True)
                 
                data = wf.readframes(1024)

                while data != b'':
                    stream.write(data)
                    data = wf.readframes(1024)

                stream.stop_stream()
                stream.close()

    def stop(self, client, userdata, message):
        self.playing = False
        # self._audio.terminate()
