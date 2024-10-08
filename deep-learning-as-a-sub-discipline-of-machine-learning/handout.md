# Deep Learning as a sub  discipline of Machine Learning
AutorInnen: Nils Weyrauch (@nilswey) und Julia Ilchmann (@JuliZ3)

## Definitionen

**Künstliche Intelligenz:** Nachahmung intelligenter Verhaltensweisen von Menschen

**Machine Learning:** 
- Fähigkeit zu „lernen“ ohne speziell dafür programmiert zu sein
- Informationsextrahierung aus Daten, die für Menschen unersichtlich sind
- Basiert auf Mustererkennung
- Unterschiedliche Algorithmen und Methoden nach Aufgabenstellung

**Zwei Bereiche:**
1. Supervised Learning (Decision Trees, Support Vector Machines)
2. Unsupervised Learning (k-means, Principal component analysis)


**Deep Learning:** 
- Subklasse von Machine Learning, Aufbau aus neuronalem Netzwerk mit mind. 3 Layern 
- Deep Learning vereinfach komplexe Aufgaben in mehrere simplere Schritte
- Grundgedanke: Entscheidung auf Basis von Wahrscheinlichkeit

## neuronale Netze

- ähnelt der Funktionseise eines menschlichen Gehirns
- besthen aus Knoten und Verbindungen in Schichten
- jeder Knoten ist mit anderen Knoten verbunden und besitzt eine Gewichtung und Schwellenwert
- Knoten werden aktiviert auf Basis ihrer Inputs
- wenn die Summe der gewichteten Inputs > Grenzwert  = „Aktivierung“ und Informationsweiterleitung


## Gemeinsamkeiten und Unterschiede von Machine Learning und Deep Learning

### Gemeinsamkeiten

-	Machine Learning und Deep Learning sind thematische Gebiete der künstlichen Intelligenzen
-	Deep Learning ist ein Teilgebiet von Machine Learning
-	Beide Ansätze ermöglichen es Computern, intelligente Entscheidungen zu treffen.
-	Beide Technologien sind darauf angewiesen, dass größere Mengen Daten zur Verfügung stehen, an denen die Systeme lernen können. 

### Unterschiede

| **Merkmal**                             | **Machine Learning**                                           | **Deep Learning**                                          |
|-----------------------------------------|--------------------------------------------------------------------|-----------------------------------------------------------------|
| **Funktionsweise**                      | Algorithmus wird durch menschliches Feedback angepasst. Arbeitet mit einfachen Algorithmen.              | Maschine trifft eigene Entscheidungen, erstellt Prognosen und hinterfragt Entscheidungen.  Verwendet mehrschichtige neuronale Netze, die dem menschlichen Gehirn nachempfunden sind. |
| **Datenanforderungen**                  | Benötigt strukturierte Daten auf einer überschaubaren Datenbasis.   | Benötigt unstrukturierte Daten und sehr große Datenmengen (über 100 Millionen Datenpunkte). |
| **Einsatzgebiete**                      | Gut geeignet für einfachere, strukturierte Aufgaben.               | Besonders geeignet für komplexe Aufgaben, bei denen nicht alle Aspekte im Vorfeld kategorisiert werden können. |
| **Eigenschaftserkennung**               | Merkmale und Kategorisierungen müssen durch Menschen vorgegeben werden. | System findet selbst geeignete Unterscheidungsmerkmale ohne menschliche Vorgaben. |
| **Lernprozess**                         | Lernen basiert auf menschlichem Feedback und expliziten Vorgaben.  | Maschine lernt kontinuierlich und verbessert sich ohne menschliches Eingreifen. |
| **Ressourcenanforderungen**             | Weniger IT-Ressourcen nötig, einfacher und kostengünstiger zu implementieren. | Benötigt erheblich mehr IT-Ressourcen und ist kostenintensiver zu realisieren. |
| **Entscheidungsfindung**                | Entscheidungen basieren auf statischen, vorgegebenen Regeln.       | Kontinuierliches Hinterfragen der Entscheidungen verbessert die Gewichtung der Informationsverknüpfungen. |
| **Relevanz für Unternehmen**            | Breiter einsetzbar aufgrund der geringeren Kosten und geringeren Komplexität. | Aufwendiger und kostspieliger, daher momentan vor allem für spezialisierte Aufgaben in größeren Unternehmen relevant. |


## Anwendungsgebiete von Deep Learning


  - Deep Learning kann alle Aufgaben lösen, die auch mit Machine Learning möglich sind.
  - **ABER:** Deep Learning erfordert hohe Rechenleistung, insbesondere für das Training großer Modelle, sowie große Datenmengen, um die Netzwerke effektiv zu trainieren. Dadurch sind die Kosten und der Ressourcenaufwand in der Regel deutlich höher im Vergleich zu traditionellen Machine-Learning-Modellen, die einfacher und ressourcenschonender sind. 
  Deswegen sind Anwendungsgebiete von Machine Learning und Deep Learning klar getrennt. Was mit Machine Learning gelöst werden kann, wird damit gelöst.

### Beipiele:

  - **Bildverarbeitung:** 
    - Deep Learning ermöglicht es Computern, Bilder auf ähnliche Weise wie Menschen zu erfassen und zu verstehen. 
    - Anwendungsbeispiele sind Gesichtserkennung (wie bei Face ID), Bildklassifizierung (wie die Kategorisierung von Objekten in Bildern) und automatisierte Inhaltsmoderation, die in sozialen Medien oder Foren eingesetzt wird, um problematische Inhalte zu erkennen und zu entfernen.

  - **Spracherkennung:** 
    - Deep-Learning-Modelle analysieren Audioaufnahmen, um die Sprachmuster zu erkennen, z.B. Tonhöhe, Tonfall und Akzent. 
    - Dies wird in Anwendungen wie Sprachsteuerung, Echtzeit-Transkription und in personalisierten Kundenerlebnissen eingesetzt. Eine bedeutende Anwendung ist die automatische Untertitelung, die die Barrierefreiheit erhöht.

- **Sprachassistenten:**
     - Sprachassistenten wie Siri, Alexa oder Google Assistant basieren auf fortgeschrittenen DL-Techniken, die Spracherkennung, NLP und Sprachsynthese integrieren. Diese Assistenten nutzen große Datensätze und kontinuierliches Training, um Nutzeranfragen zu verstehen und angemessen zu reagieren. 
     - Die Assistenten können vielfältige Aufgaben übernehmen, von der Steuerung von Smart-Home-Geräten über das Versenden von Nachrichten bis hin zu komplexeren Aufgaben wie dem Erstellen von Berichten und dem Durchführen von Recherchen.
    
- **Wettervorhersagen:**
  - Deep-Learning-Modelle verarbeiten riesige Mengen an Daten aus Satellitenbildern, Wetterstationen und historischen Wetterdaten und lernen dabei Muster und Zusammenhänge in den atmosphärischen Bedingungen.
  - Durch die Analyse dieser Daten mit DL-Methoden können präzisere Wettervorhersagen getroffen werden, die sowohl kurzfristige als auch langfristige Wettertrends vorhersagen können. Dies wird besonders wichtig in Bereichen wie Katastrophenmanagement (z.B. Vorhersage von Hurrikanen) und Landwirtschaft, wo genaue Wettervorhersagen für die Planung und Sicherheit entscheidend sind.


# Literaturquellen

- Bengio, Y., Goodfellow, I., & Courville, A. (2017). Deep learning (Vol. 1). Cambridge, MA, USA: MIT press.
- Bitkom e. V. und Deutsches Forschungszentrum für künstliche Intelligenz. Künstliche Intelligenz Wirtschaftliche Bedeutung, gesellschaftliche Herausforderungen, menschliche Verantwortung (2017)
- IBM: Was sind neuronale Netzwerke?, https://www.ibm.com/de-de/topics/neural-networks (07.10.2024)
- Ionos: Deep Learning vs. Machine Learning - was sind die Unterschiede, https://www.ionos.de/digitalguide/online-marketing/suchmaschinenmarketing/deep-learning-vs-machine-learning/ (07.10.2024)
- Mahesh, B. (2020). Machine learning algorithms-a review. International Journal of Science and Research (IJSR).[Internet], 9(1), 381-386.
- Nielsen, M. A. (2015). Neural networks and deep learning (Vol. 25, pp. 15-24). San Francisco, CA, USA: Determination press.
- RedHat: Was ist Deep Learning?, https://www.redhat.com/de/topics/ai/what-is-deep-learning (07.10.2024)
- The MathWorks, Inc.: Deep Learning, https://de.mathworks.com/discovery/deep-learning.html (08.10.2024)
- Weissenberg: Was ist Deep Learning?, https://weissenberg-group.de/was-ist-deep-learning/ (07.10.2024)
