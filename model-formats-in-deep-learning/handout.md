# Handout: Modell Formate im Deep Learning

Autoren: [nicevibesplus](https://github.com/nicevibesplus), [awiechma](https://github.com/awiechma)

## Unterschiede zwischen Machine Learning und Deep Learning

- **Datenmengen**:
  - **Machine Learning**: Funktioniert mit kleinen oder großen strukturierten Datenmengen.
  - **Deep Learning**: Arbeitet mit großen unstrukturierten Datenmengen.

- **Hardware und Laufzeit**:
  - **Machine Learning**: Geringere Laufzeit bei einfacher Hardware.
  - **Deep Learning**: Benötigt leistungsstarke Hardware und hat längere Rechenzeiten.

- **Menschlicher Einfluss**:
  - **Machine Learning**:
    - Braucht eine klare Problemdefinition
    - Merkmalsextraktion muss manuell erfolgen
    - Auswahl geeigneter Algorithmen
  - **Deep Learning**:
    - Benötigt Input des Menschen bei dem Aufbau der Netzarchitektur und Hyperparametern

- **Datenformate**:
  - Die gespeicherten Datenformate sind in beiden Fällen ähnlich.

## Was ist ein Deep Learning Modell?

### Komponenten

- **Eingabedaten**: Daten, die ins Modell eingespeist werden.
- **Architektur**: Struktur des neuronalen Netzes.
  - Neuronen: Grundbausteine eines neuronalen Netzes.
  - Schichten: Anordnung der Neuronen im Netzwerk.
  - Aktivierungsfunktionen: Bestimmen, ob ein Neuron aktiviert wird.
- **Verlustfunktionen**: Messen, wie sehr der berechnete Wert vom tatsächlichen Wert abweicht.
- **Optimierungsalgorithmus**: Passt Gewichte und Bias an, um die Leistung des Modells zu verbessern.
- **Gewichte und Bias**: Parametrische Werte, die Eingaben gewichten und die Aktivierungsfunktion verschieben.

## Speicherung von Deep Learning Modellen

- **Frameworks**: Unterschiedliche Machine Learning Frameworks verwenden verschiedene Datenformate zur Speicherung.
- **Ansätze**:
  - Einige speichern nur die Modellarchitektur und die gelernten Parameter.
  - Andere speichern zusätzlich die Trainingsdaten.
- **Relevanz der Trainingsdaten**: Für die Archivierung wichtig, beeinflusst die Nutzung jedoch nicht.

## Verbreitete Frameworks für Deep Learning

1. [**TensorFlow**](https://www.tensorflow.org/) – Google Brain
2. [**PyTorch**](https://pytorch.org/) – Linux Foundation
3. [**Keras**](https://github.com/keras-team/keras)
4. [**CNTK**](https://github.com/microsoft/CNTK) – Microsoft Cognitive Toolkit

## Datei Formate

### HDF5
- **Typ**: Legacy Format
- **Verwendung**: In TensorFlow und Keras.
- **Funktion**: Speicherung von sehr großen Datenmengen.
- **Speichert**:
  - Trainingsdaten
  - Modellarchitektur
  - Gewichte/Bias
  - Informationen über den Zustand des Optimierungsalgorithmus (Checkpointing)
  - Trainingskonfiguration (Verlustfunktion)
  - Metadaten (z.B. Keras Version)

### TFRecord
- **Typ**: Speichert Trainingsdaten
- **Effizienz**: Optimal für sehr große Datenmengen.
- **Verwendung**: Von TensorFlow.

### ONNX (Open Neural Network Exchange)
- **Funktion**: Austausch von DL-Modellen zwischen verschiedenen Frameworks.
- **Speichert**:
  - Modellarchitektur
  - Gewichte/Bias
  - Ein- und Ausgabeformate des Modells
  - Metadaten

### PKL (Pickle)
- **Verwendung**: In PyTorch.
- **Funktion**: Speichert Python-Objekte.
- **Speichert**:
  - Modellarchitektur
  - Gewichte/Bias
  - Alle Python-Objekte
- **Tool**: Serialisierung und Deserialisierung von Python-Objekten.

### PT (PyTorch Tensors)
- **Verwendung**: In PyTorch.
- **Funktion**: Speichert Modellarchitektur, Gewichte/Bias als Tensor.
- **Effizienz**: Besonders effizient für PyTorch.

## Quellen
