import math
from bisect import bisect_left


class ChordUtil:
    def __init__(self, octaves=5):
        self.list_notes = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"]
        self.fundamental_freq = [32.70, 34.65, 36.71, 38.89, 41.20, 43.65, 46.25, 49.00, 51.91, 55.00, 58.27, 61.74]
        # note frequencies in order
        self.list_freq_5_oct = [32.70, 34.65, 36.71, 38.89, 41.20, 43.65, 46.25, 49.00, 51.91, 55.00, 58.27, 61.74,
                                65.41, 69.30, 73.42, 77.78, 82.41, 87.31, 92.50, 98.00, 103.8, 110.0, 116.5, 123.5,
                                130.8, 138.6, 146.8, 155.6, 164.8, 174.6, 185.0, 196.0, 207.7, 220.0, 233.1, 246.9,
                                261.6, 277.2, 293.7, 311.1, 329.6, 349.2, 370.0, 392.0, 415.3, 440.0, 466.2, 493.9,
                                523.3, 554.4, 587.3, 622.3, 659.3, 698.5, 740.0, 784.0, 830.6, 880.0, 932.3, 987.8]
        self.list_freq = list()
        self.list_freq += self.fundamental_freq
        if octaves != 5:
            for o in range(1, octaves):
                self.list_freq += list(map(lambda x: x * math.pow(2, o), self.fundamental_freq))
        else:
            self.list_freq = self.list_freq_5_oct

    def __get_note_5oct_index(self, freq):
        index = self.__binary_search(self.list_freq, freq)
        actual_value = self.list_freq[index]
        actual_value_diff = abs(actual_value - freq)

        # if the index returned isn't start or end
        if 0 < index <= len(self.list_freq) - 1:
            prev_value = self.list_freq[index - 1]
            prev_value_diff = abs(prev_value - freq)
            if prev_value_diff < actual_value_diff:
                # we return the interval for display. the middle value is the closest to our freq.
                return index - 1
        return index

    def __binary_search(self, a, x, lo=0, hi=None):  # can't use a to specify default for hi
        hi = hi if hi is not None else len(a)  # hi defaults to len(a)
        pos = bisect_left(a, x, lo, hi)  # find insertion position
        return pos if pos != hi else -1  # don't walk off the end

    def __get_note_label_from_index(self, idx):
        octave = int(idx / 12)
        note_index = int(idx % 12)
        note_name = self.list_notes[note_index].split("#")
        if len(note_name) > 1:
            return str(note_name[0]) + str(octave) + "#"
        else:
            return str(note_name[0]) + str(octave)

    # max note limit is si5. If you want to increase it,
    # you should fill the list_freq_5_oct table ( note that you should have one element more in order to work
    def get_closest_note_freq_label_and_index(self, freq):
        if freq > self.list_freq[-1]:
            idx = len(self.list_freq) - 1
            return self.list_freq[idx], self.__get_note_label_from_index(idx), idx
        else:
            idx = self.__get_note_5oct_index(freq)
            return self.list_freq[idx], self.__get_note_label_from_index(idx), idx

    def get_interval_from_index(self, index):
        if 0 < index < len(self.list_freq) - 1 :
            return self.list_freq[index - 1], self.list_freq[index+1]
        else:
            if index == 0:
                return 2 * self.list_freq[0] - self.list_freq[1], self.list_freq[1]
            else:
                return self.list_freq[index - 1], 2 * self.list_freq[index] - self.list_freq[index - 1]

