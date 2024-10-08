@amlusc

# F.A.I.R. Data

## Inhaltsverzeichnis

1. [Einleitung](#einleitung)
2. [Die F.A.I.R.-Prinzipien](#die-fair-prinzipien)
3. [Unterschied zwischen Open Data und F.A.I.R. Data](#unterschied-zwischen-open-data-und-fair-data)
4. [Warum sollte man die Daten F.A.I.R. machen?](#warum-sollte-man-daten-fair-machen)
5. [Bedeutung der F.A.I.R.-Prinzipien allgemein](#bedeutung-der-fair-prinzipien-allgemein)
6. [Bedeutung der F.A.I.R.-Prinzipien in der Wissenschaft](#bedeutung-der-fair-prinzipien-in-der-wissenschaft)
7. [Wie macht man Daten F.A.I.R.?](#wie-macht-man-daten-fair)
8. [FAIRification-Prozess](#fairification-prozess)
9. [Anwendung der F.A.I.R.-Prinzipien auf DL-Modelle für EO-Daten](#anwendung-der-fair-prinzipien-auf-dl-modelle-für-eo-daten)
10. [Schlussfolgerung](#schlussfolgerung)
11. [Quellen](#quellen)


## Einleitung
> “Data that is loved tends to survive.”  
> — *Kurt Bollacker*

Die F.A.I.R.-Prinzipien (Findable, Accessible, Interoperable, Reusable) wurden 2016 entwickelt, um den Umgang mit wissenschaftlichen Daten zu verbessern und deren Nutzung in der Forschung zu erleichtern. In einer Zeit, in der Datenmengen und -komplexität stetig wachsen, sind sie von entscheidender Bedeutung.

## Die F.A.I.R.-Prinzipien
![F.A.I.R. Data](https://github.com/amlusc/geosoft2-2024/raw/main/fair-data/FAIRDATA.jpg)

| Prinzip       | Beschreibung |
|---------------|--------------|
| **Findable (Auffindbar)**  | **F1.** (Meta-)Daten werden mit einer weltweit eindeutigen und dauerhaften Kennung versehen <br>**F2.** Daten werden mit umfangreichen Metadaten beschrieben (definiert durch R1 unten)<br>**F3.** Metadaten enthalten eindeutig und explizit den Identifikator der Daten, die sie beschreiben <br>**F4.** (Meta-)Daten sind in einer durchsuchbaren Ressource registriert oder indexiert|
| **Accessible (Zugänglich)**| **A1.** (Meta-)Daten sind anhand ihrer Kennung über ein standardisiertes Kommunikationsprotokoll abrufbar <br>**A1.1** das Protokoll ist offen, frei und universell implementierbar <br>**A1.2** das Protokoll ermöglicht ein Authentifizierungs- und Autorisierungsverfahren, falls erforderlich <br>**A2.** die Metadaten sind zugänglich, auch wenn die Daten nicht mehr verfügbar sind|
| **Interoperable (Interoperabel)** | **I1.** (Meta-)Daten verwenden eine formale, zugängliche, gemeinsame und breit anwendbare Sprache zur Wissensdarstellung <br>**I2.** (Meta-)Daten verwenden Vokabulare, die den FAIR-Grundsätzen folgen <br>**I3.** (Meta-)Daten enthalten qualifizierte Verweise auf andere (Meta-)Daten|
| **Reusable (Wiederverwendbar)**  | **R1.** (Meta-)Daten sind mit einer Vielzahl von genauen und relevanten Attributen reichhaltig beschrieben <br>**R1.1.** (Meta-)Daten werden mit einer klaren und zugänglichen Datennutzungslizenz freigegeben <br>**R1.2.** (Meta-)Daten sind mit einer detaillierten Dokumentation über Herkunft, Entstehungsprozess und sämtliche Änderungen verbunden<br>**R1.3.** (Meta-)Daten entsprechen den für den Bereich relevanten Gemeinschaftsstandards|

### Unterschied zwischen Open Data und F.A.I.R. Data

- Open Data kann von jedem, überall und für jede Art von Nutzung frei verwendet, weitergegeben und weiterentwickelt werden.
- F.A.I.R.-Prinzipien bieten bewährte Praktiken für das Teilen von Daten unter Berücksichtigung ethischer, rechtlicher oder vertraglicher Beschränkungen. Bei Daten, die persönliche Informationen oder Urheberrechte enthalten, müssen die entsprechenden Vorschriften eingehalten werden. Selbst wenn die Daten nicht offen geteilt werden können, sollte eine Beschreibung veröffentlicht werden, um interessierten Forschenden die Anforderung einer Nutzungserlaubnis zu ermöglichen.

## Warum sollte man Daten F.A.I.R. machen?
- Sicherung von Integrität und Reproduzierbarkeit in der Forschung.
- Gültig als Goldstandard für Forschungsdatenmanagement (RDM).
- Erleichterung des Zugangs, der Auffindbarkeit und der Wiederverwendung von Daten, was deren Wert erhöht.
- Förderung der Datenintegration innerhalb und zwischen Disziplinen zur Unterstützung globaler Herausforderungen.
- Viele Förderer (z. B. UN, WHO) haben die Prinzipien in ihre Richtlinien aufgenommen, was die Verpflichtungen der Forscher erhöht.
- Steigerung des öffentlichen Vertrauens in öffentlich finanzierte Forschung.
- Unterstützung durch ergänzende ethische Richtlinien wie die CARE- und TRUST-Prinzipien.

## Bedeutung der F.A.I.R.-Prinzipien allgemein
- **Öffentliches Vertrauen**: Die F.A.I.R.-Prinzipien erhöhen die Rechenschaftspflicht in öffentlich finanzierter Forschung und stärken das Vertrauen in den Umgang mit Steuergeldern.
- **Ethisches Datenmanagement**: Förderung ethischer Überlegungen im Datenmanagement, insbesondere im Hinblick auf sensible Daten, während die Einhaltung ethischer und rechtlicher Standards gewährleistet wird.
- **Interoperabilität und Integration**: Standardisierte Formate und Vokabulare erleichtern die Datenintegration über verschiedene Fachgebiete hinweg, was entscheidend für die Bewältigung globaler Herausforderungen ist (z. B. Klimawandel, Gesundheitskrisen).
- **Nachhaltige Entwicklung**: Verbesserung des Datenzugangs und der Wiederverwendbarkeit unterstützt die Erreichung nachhaltiger Entwicklungsziele, indem wertvolle Daten für Forschung und politische Entscheidungsfindung verfügbar gemacht werden.
- **Anpassungsfähigkeit an neue Technologien**: Die F.A.I.R.-Prinzipien helfen Organisationen, sich an neue Technologien und Datenumgebungen anzupassen, um sicherzustellen, dass Daten in einer sich schnell verändernden Landschaft nützlich und zugänglich bleiben.

## Bedeutung der F.A.I.R.-Prinzipien in der Wissenschaft
- **Transparenz und Reproduzierbarkeit**: Sicherstellung, dass Forschungsergebnisse überprüft und nachvollzogen werden können.
- **Förderung der Zusammenarbeit**: Verbesserte Datenzugänglichkeit und -nutzung erleichtern den Austausch und die Zusammenarbeit zwischen Forschern.
- **Compliance**: Viele Förderorganisationen und wissenschaftliche Zeitschriften verlangen die Einhaltung der F.A.I.R.-Prinzipien.

## Wie macht man Daten F.A.I.R.?
Das **Drei-Punkte-Rahmenwerk** formuliert die wesentlichen Schritte auf dem Weg zu einem globalen Internet aus F.A.I.R.-Daten und -Diensten. Hierdurch sollen Daten auffindbar, zugänglich, interoperabel und wiederverwendbar gemacht werden.

### Das Drei-Punkte FAIRification Framework
Dieses Framework bietet Stakeholdern praktische Anleitungen, wie sie F.A.I.R. werden können. Das Framework maximiert die Wiederverwendung vorhandener Ressourcen, erhöht die Interoperabilität und fördert die schnelle Annäherung an Standards und Technologien für F.A.I.R.-Daten und -Dienste.

#### Die drei Schritte des Frameworks:
1. **Metadata for Machines (M4M) Workshops**: Diese Workshops unterstützen dabei, domänenspezifische Metadatenanforderungen und Richtlinien in maschinenlesbare Metadaten zu überführen.
2. **FAIR Implementation Profile (FIP)**: Das FIP dient als Leitfaden für die Auswahl und Konfiguration der F.A.I.R.-Infrastruktur, wie z. B. FAIR Data Points (FDP) und FAIR Digital Objects (FDO), die Teil eines globalen Internets für F.A.I.R.-Daten und -Dienste sind.
3. **FAIR Data Points**: Sie unterstützen den Aufbau und die Verteilung von F.A.I.R.-Daten und -Diensten weltweit.

Das Framework bietet Stakeholdern einen klaren Überblick darüber, was „F.A.I.R. werden“ für sie in der Praxis bedeutet, und ermöglicht eine koordinierte, skalierbare und schnelle Integration in die entstehende F.A.I.R.-Landschaft. 

## FAIRification-Prozess

Die F.A.I.R.-Prinzipien gelten für Metadaten, Daten und unterstützende Infrastrukturen (z. B. Suchmaschinen). Während die Anforderungen an Auffindbarkeit und Zugänglichkeit meist auf der Metadatenebene erfüllt werden können, erfordern Interoperabilität und Wiederverwendbarkeit intensivere Arbeit auf der Datenebene. Der unten beschriebene FAIRification-Prozess, wie ihn GO FAIR nutzt, fokussiert sich auf die Daten, beschreibt aber auch die notwendigen Arbeiten an den Metadaten.

### Schritte des FAIRification-Prozesses

![FAIRification Prozess](https://github.com/amlusc/geosoft2-2024/raw/main/fair-data/FAIRIFICATION.jpg)

1. **Nicht-FAIR-Daten abrufen**: Zugang zu den zu FAIRifizierenden Daten erhalten.
2. **Analyse der Daten**: Untersuchung der Inhalte und Struktur der Daten: Welche Konzepte sind enthalten? Wie sind die Daten strukturiert? Unterschiedliche Datenstrukturen erfordern verschiedene Analysemethoden.
3. **Semantisches Modell definieren**: Ein semantisches Modell für das Dataset festlegen, das die Bedeutung der enthaltenen Entitäten und Relationen beschreibt. Es ist hilfreich, vorhandene Modelle und Vokabulare zu recherchieren und zu verwenden.
4. **Daten verlinkbar machen**: Anwendung des semantischen Modells, um die Daten verlinkbar zu gestalten und so die Interoperabilität und Wiederverwendbarkeit zu fördern. Dies geschieht oft mithilfe von Semantic Web- und Linked Data-Technologien.
5. **Lizenz zuweisen**: Lizenzinformationen sind Teil der Metadaten, jedoch wird die Lizenzzuweisung als eigenständiger Schritt betrachtet, da das Fehlen einer expliziten Lizenz die Wiederverwendung verhindern kann.
6. **Metadaten definieren**: Metadaten unterstützen alle Aspekte von F.A.I.R. und sollten umfassend und aussagekräftig sein.
7. **F.A.I.R.-Ressource bereitstellen**: Die F.A.I.R.-Datenressource (einschließlich Metadaten und Lizenz) wird bereitgestellt, damit die Metadaten durch Suchmaschinen indexiert und die Daten abgerufen werden können.

## Anwendung der F.A.I.R.-Prinzipien auf DL-Modelle für EO-Daten

Die F.A.I.R.-Prinzipien für Deep-Learning-Modelle (DL) in der Erdbeobachtung (EO) fördern Open Science und Big Data. Die zunehmende Nutzung von freier und offener Software (FOSS) und die Entwicklung öffentlicher Evaluationsplattformen ermöglichen es, Datenprodukte transparent und effizient zu erstellen. Bibliotheken wie [Open RS](https://openlibraryfoundation.org/newsroom/news/introducing-the-open-resource-sharing-coalition-openrs/) und Plattformen wie die [IEEE GRSS](https://www.grss-ieee.org/) bieten moderne Benchmark-Datensätze, die den Herausforderungen von Big Data gerecht werden.

Die Bereitstellung von Ressourcen wie trainierten Modellen und experimentellen Designs unterstützt die Verbreitung anspruchsvoller Modellierungsansätze, bringt die EO- und KI-Gemeinschaften näher zusammen und fördert die Wiederverwendbarkeit. Durch die Veröffentlichung in öffentlich zugänglichen Formaten wird unnötiger Rechenaufwand reduziert.

Ein standardisiertes Datenmodell für Trainingsdaten in einer webbasierten räumlichen Dateninfrastruktur (SDI) erleichtert die Einhaltung der F.A.I.R.-Prinzipien, verbessert die Dokumentation und Nutzung georäumlicher Trainingsdaten und entspricht den Standards des Open Geospatial Consortiums (OGC).

### Ziele der F.A.I.R.-Prinzipien für DL-Modelle in EO:
- Systematische Dokumentation und Bereitstellung in durchsuchbaren Repositorien
- Einhaltung von Standards für Metadaten, Lizenzen und Provenienz
- Förderung nachhaltiger Nutzung und wissenschaftlicher Zusammenarbeit

## Schlussfolgerung
Die F.A.I.R.-Prinzipien sind ein wesentlicher Bestandteil des wissenschaftlichen Fortschritts, da sie die Nutzung und den Austausch von Daten und Modellen optimieren. Die Implementierung dieser Prinzipien kann zur effizienteren und kollaborativen Nutzung wissenschaftlicher Ressourcen beitragen.

## Quellen
- [Zitat Bollacker](https://www.americanscientist.org/article/beautiful-data)
- [F.A.I.R. Prinzipien](https://www.go-fair.org/fair-principles/)
- [How to go F.A.I.R.](https://www.go-fair.org/how-to-go-fair/)
- [FAIRification Process](https://www.go-fair.org/fair-principles/fairification-process/)
- [YouTube: How to be F.A.I.R. with your Data](https://youtu.be/5OeCrQE3HhE?si=LC3114uYoc94_M8-)
- Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., et al. (2016). The FAIR guiding principles for scientific data management and stewardship. *Scientific Data*, *3*, 160018. https://doi.org/10.1038/sdata.2016.18
- Engelhardt, C. (2022). How to be FAIR with your data. https://doi.org/10.17875/gup2022-1915
- Dimitrovski, I., Kitanovski, I., Kocev, D., & Simidjievski, N. (2023). Current trends in deep learning for Earth Observation: An open-source benchmark arena for image classification. *ISPRS Journal of Photogrammetry and Remote Sensing*, *197*, 18-35. https://doi.org/10.1016/j.isprsjprs.2023.01.014
- Persello, C., Wegner, J. D., Hänsch, R., Tuia, D., Ghamisi, P., & Koeva, M. (2022). Deep learning and Earth observation to support the sustainable development goals: Current approaches, open challenges, and future opportunities. *IEEE Geoscience and Remote Sensing Magazine*, *10(2)*, 172-200. https://doi.org/10.1109/MGRS.2021.3136100
- Yue, P., Shangguan, B., Hu, L., Jiang, L., Zhang, C., Cao, Z., & Pan, Y. (2022). Towards a training data model for artificial intelligence in earth observation. *International Journal of Geographical Information Science*, *36(11)*, 2113–2137. https://doi.org/10.1080/13658816.2022.2087223
