import queue
import sys

from ChordUtil import ChordUtil
from chordeDetectorV2 import Ui_MainWindow
import sounddevice as sd
import scipy as sp
import numpy as np
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSlot


class ChordDetectorController(QMainWindow, Ui_MainWindow):
    # Méthode appelée lorsque l’on crée l’objet
    def __init__(self, parent=None):
        self.chord_util = ChordUtil(10)
        self.q = queue.Queue()
        # Appel la méthode __init__ de QMainWindow
        super(ChordDetectorController, self).__init__(parent)
        # Appelle la méthode setupUi de Ui_grapheur pour remplir la fenêtre
        self.setupUi(self)

    # Appellé au lancement le l’application
    @pyqtSlot()  # Définit un slot pour recevoir un signal
    def on_Simulation_clicked(self):  # signal clicked associé à l’élément btValider
        # freq=self.txtFreq.text() # Range le contenu de la zone de texte txtFreq dans freq
        # message="Sin à "+freq+" Hz" # Crée un message (ici freq est un texte)
        # self.pushButton.setText(message) # Ce message devient le texte associé au bouton valider
        f1 = float(self.lineEdit_2.text())
        a = float(self.lineEdit_3.text())
        t = np.arange(1000) / 200000
        x = np.sin(2 * np.pi * t * f1) + a * np.random.randn(len(t))

        self.Visualisation.canvas.ax.cla()
        self.Visualisation.canvas.ax.plot(t, x)
        self.Visualisation.canvas.draw()


    def audio_callback(self, indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        self.q.put(indata)

    def on_Microphone_clicked(self):
        # Constantes:

        fech = 44100
        N = fech * 1

        ## Enregistre le son du microphone et l'affiche

        microphone = sd.rec(frames=N, samplerate=fech, channels=1, blocking=True)
        t = np.arange(0, N / fech, 1 / fech)
        tf = sp.fft(microphone)
        # freqs, psd = sp.signal.welch(microphone, fs=fech, window='hamming')
        f_max = np.argmax(abs(tf))
        f_req = (f_max * fech) / N
        print(f_req)  # Affichage de la fréquence
        (closest_freq, note_label, idx) = self.chord_util.get_closest_note_freq_label_and_index(f_req)
        (from_freq, to_freq) = self.chord_util.get_interval_from_index(idx)
        self.progressBar.setRange(from_freq, to_freq)
        self.progressBar.setValue(f_req)
        self.VFrequence.setText(str(f_req))
        self.Vnote.setText(str(note_label) + ": " + str(closest_freq))
        self.Visualisation.canvas.ax.cla()
        self.Visualisation.canvas.ax.plot(t, abs(
            tf))  # Fonction à utiliser à la place de plt.plot pour dessiner sur le graphe
        self.Visualisation.canvas.draw()

if __name__ == '__main__':
    # Initialise le gestionnaire Qt si cela n’a pas encore été fait
    if 'app' not in locals():
        app = QApplication(sys.argv)
    # Crée un objet associé à la fenêtre
    graphWin = ChordDetectorController()
    # Affiche la fenêtre
    graphWin.show()
    rc = app.exec_()
    sys.exit(rc)