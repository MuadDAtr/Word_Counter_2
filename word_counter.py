import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit

# ===============================
# Funkcje przetwarzania tekstu
# ===============================
def char_replace(te_xt):
    """
    Zamienia przecinki, kropki, średniki, znaki zapytania i wykrzykniki na spacje.
    """
    return te_xt.replace(",", " ") \
                .replace(".", " ") \
                .replace(";", " ") \
                .replace("?", " ") \
                .replace("!", " ")

def count_freq(wordlist):
    """
    Dla zadanej listy słów zwraca listę wystąpień dla każdego słowa.
    """
    wordfreq = []
    for word in wordlist:
        wordfreq.append(wordlist.count(word))
    return wordfreq

def freq_dict(wordlist):
    """
    Tworzy słownik, gdzie kluczami są słowa, a wartościami – liczba ich wystąpień.
    """
    wordfreq = [wordlist.count(word) for word in wordlist]
    return dict(list(zip(wordlist, wordfreq)))

def sort_dict(freqdict):
    """
    Zamienia słownik na listę krotek (częstotliwość, słowo), sortuje malejąco i zwraca wynik.
    """
    dict_s = [(freqdict[key], key) for key in freqdict]
    dict_s.sort()      # sortowanie rosnąco
    dict_s.reverse()   # odwrócenie kolejności: od największej do najmniejszej
    return dict_s

# ===============================
# Tryb konsolowy
# ===============================
def main_cli():
    text_init = input('Please insert the text: ')
    print("\nOto wprowadzony tekst:\n")
    print(text_init)
    
    # Przetwarzanie tekstu
    text_l = text_init.lower()
    text = char_replace(text_l)
    wordlist = text.split()
    
    # Wywołanie count_freq 
    count_freq(wordlist)
    
    print("...............\n")
    print("This is the frequency of words in the text:\n")
    
    freqdict = freq_dict(wordlist)
    sorted_freq = sort_dict(freqdict)
    
    # Wypisanie wyników – słowo oraz liczba wystąpień
    for count, word in sorted_freq:
        print(f"{word}: {count}")

# ===============================
# Tryb graficzny z PySide6
# ===============================
class FrequencyCounterGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Word Frequency Counter")
        
        # Układ pionowy
        layout = QVBoxLayout()
        
        # Etykieta tytułowa
        self.label = QLabel("Word Frequency Counter")
        self.label.setStyleSheet("font-size: 18pt; font-family: 'Times New Roman';")
        layout.addWidget(self.label)
        
        # Pole tekstowe
        self.textedit = QTextEdit()
        self.textedit.setStyleSheet("font-size: 12pt; font-family: Arial;")
        layout.addWidget(self.textedit)
        
        # Przycisk wywołania liczenia
        self.button = QPushButton("Count")
        self.button.setStyleSheet("font-size: 14pt; font-family: Arial;")
        layout.addWidget(self.button)
        self.button.clicked.connect(self.count_frequency)
        
        # Etykieta z wynikiem
        self.result_label = QLabel("")
        self.result_label.setStyleSheet("font-size: 12pt; font-family: Arial;")
        self.result_label.setWordWrap(True)
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)
        
    def count_frequency(self):
        # Pobranie tekstu z pola tekstowego
        text = self.textedit.toPlainText().strip()
        if not text:
            self.result_label.setText("Wprowadź tekst.")
            return
        
        # Przetwarzanie tekstu – zamiana na małe litery i usunięcie interpunkcji
        clean_text = char_replace(text.lower())
        wordlist = clean_text.split()
        
        freqdict = freq_dict(wordlist)
        sorted_freq = sort_dict(freqdict)
        
        # Budowa łańcucha wynikowego
        result = "Częstotliwość wystąpień słów (od najczęściej do najmniej):\n"
        for count, word in sorted_freq:
            result += f"{word}: {count}\n"
            
        self.result_label.setText(result)

# ===============================
# Punkt wejścia
# ===============================
def main():
    """
    Jeżeli podczas uruchomienia skryptu podano argument '--cli', wykonana zostanie wersja konsolowa.
    W przeciwnym razie uruchomiona zostanie aplikacja graficzna (PySide6).
    """
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        main_cli()
    else:
        app = QApplication(sys.argv)
        gui = FrequencyCounterGUI()
        gui.show()
        sys.exit(app.exec())

if __name__ == "__main__":
    main()
