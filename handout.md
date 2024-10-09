#   Microservices

AutorInnen: Jakub Zahwe (@Kubisili) und Maximilian Holtkamp (@MaxiKamp)

## Definition


* Architekturstil, bei dem Anwendungen in kleine, autonome Services unterteilt sind.
* Jeder Microservice hat eine spezifische Funktion und ist unabhängig.
* Kommunikation zwischen Services erfolgt meist über HTTP-APIs (z.B. REST oder GRPC).
* Microservices können unabhängig entwickelt, bereitgestellt und skaliert werden.
* Fördert Flexibilität und Fehler-Isolierung innerhalb der Anwendung.


### Vorteile und Nachteile

* **Vorteile**:
    * übersichtlich und leicht weiterentwickelbar, da sie idealerweise klein sind
    * Skalierbarkeit
        * jeder service kann nach bedarf unabhängig skaliert werden
    * Wiederverwendbar:
        * kann in mehreren Anwendungen benutzt werden
    * Flexibilität: 
        * Jedes Team kann für einen Service die beste Programmiersprache, Datenbank oder Technologie wählen, ohne auf andere Services Rücksicht nehmen zu müssen
    * schnellere Entwicklung:
        * fördern schnelle Entwicklung da Teams unabhängig von einander arbeiten können
    * keine ungewollten Abhängigkeiten, da diese über API eingeführt werden müssen
    * Resilienz

* **Nachteile**:
    * erhöhte Komplexität
        * Management der Servicekommunikation kann eine Herausfordrung sein
        * es muss eventuell zusätzlicher Code geschrieben werden um reibungslose kommunikation zu gewährleisten
    * hoher Ressourcenbedarf
    * aufwendige Fehlersuche
    * Softwareverteilung und Tests komplex
    * Netzwerkabhängigkten
    * Herausforderungen beim Datenmanagement:
        * Datenkonsistenz und Transaktionen über mehrere Services hinweg können komplex sein, deshalb erfordert es eine sorgfältige Datenverwaltung und  -koordination, um die Datenintegrität zu unterstützen.
    * erhöhtes Risiko, dass eine Komponente ausfällt
    * Das Logging und Monitoring wird komplexer, da mehrere Systeme involviert sind, welche ggf. unterschiedliche Logging- und Monitoringtechnologien einsetzen.
    * es muss zwischen Verfügbarkeit und Datenkonsistenz gewählt werden (CAP-Theorem)

### Microservices mit docker compose verwalten
 
* docker installiert haben
* Ein Verzeichnis für da Projekt erstellen, jeder Microservice sollte eigenen Ordner haben und jeder dieser Ordner sollte eine eigene dockerfile für den service enthalten
* Eine docker-compose.yml datei im Hauptverzeichnis anlegen, diese definiert alle Microservices und zeigt wie sie zussammenarbeiten
* über den Befehl "docker-compose up" werden alle Microservices gestartet

Damit erstellt docker automatisch ein Netzwerk für die definerten services über dieses sie mit ihren servicenamen kommunizieren können

Mit Docker Compose kannst du so eine vollständige Microservices-Umgebung auf deinem PC einfach starten, verwalten und skalieren. Das Tool ist vor allem nützlich für Entwicklung und Testing, bevor die Services in produktiven Umgebungen wie Kubernetes bereitgestellt werden.

### Wie kommunizieren Microservices:
* Synchron (direkte Kommunikation):

    * HTTP/REST: Häufig verwendet, da es einfach zu implementieren und weit verbreitet ist. Microservices nutzen RESTful APIs, um Daten über HTTP-Anfragen auszutauschen.

    * gRPC: Ein leistungsstarkes, binäres Protokoll, das von Google entwickelt wurde. Es bietet höhere Effizienz und ist nützlich für schnelle Kommunikation und komplexe Datenstrukturen.

    * GraphQL: Ein flexibles Abfrage-Framework, das es ermöglicht, genau die benötigten Daten abzurufen. Vor allem nützlich, wenn Clients unterschiedliche Datenanforderungen haben.

* Asynchron (Nachrichtenaustausch):

    * Message Broker: Systeme wie Apache Kafka, RabbitMQ oder Amazon SQS ermöglichen es Microservices, Nachrichten an eine Warteschlange zu senden und von dort zu empfangen. Das hilft, Verzögerungen und Lastspitzen abzufedern.

    * Event-Driven Architecture: Microservices reagieren auf Ereignisse (Events), die von anderen Services gesendet werden, und kommunizieren durch das Austauschen dieser Events. Dies erleichtert die Entkopplung und erlaubt reaktive Systeme.

    * Publish/Subscribe (Pub/Sub): Ein Service veröffentlicht Nachrichten (Publish) und andere Services, die daran interessiert sind, abonnieren diese (Subscribe). Dies ermöglicht eine lose Kopplung und vereinfacht die Skalierung.

* Service Discovery:

    * Da Microservices oft dynamische IP-Adressen haben, wird ein Service Discovery Tool wie Consul, Eureka oder Kubernetes Service Discovery verwendet. Dadurch  können Services einander finden und wissen, wie sie miteinander kommunizieren können.

* API Gateway:

    * Ein API Gateway dient als zentraler Einstiegspunkt für Anfragen und koordiniert die Kommunikation zwischen den Microservices. Es hilft bei der Verwaltung von Authentifizierung, Ratenbegrenzung und Sicherheit und stellt eine Vermittlerschicht für die Kommunikation mit Clients dar.


#### Sources
* https://de.wikipedia.org/wiki/Microservices
* https://www.youtube.com/watch?v=lL_j7ilk7rc&ab_channel=5MinutesorLess
* https://www.atlassian.com/de/microservices/cloud-computing/advantages-of-microservices
* 

