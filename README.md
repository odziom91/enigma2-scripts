# enigma2-scripts
Skrypty wspomagające dla tunerów DVB-S/S2, DVB-C, DVB-T/T2 opartych o system OpenATV.
## Lista skryptów
### **e2-uniqueiptv**
Podmienia wartości SID w plikach bukietów, aby zapewnić unikalność wpisów na liście TV. Przydatne, podczas przypisywania EPG do programów IPTV.
#### **Jak użyć?**
1. Skopiować do katalogu e2-uniqueiptv plik z bukietem IPTV.
2. Uruchomić skrypt
```
cd e2-uniqueiptv
python e2-uniqueiptv.py
```
3. Wpisać nazwę pliku wejściowego oraz wybrać domyślny odtwarzacz IPTV dostępny w dekoderze.
4. Nowy plik będzie zapisany z przedrostkiem **new_**. Przy kopiowaniu pliku na dekoder nalezy ten przedrostek usunąć.