##  Vaatimuksiin sidotut testit ja tulokset
| Testi-ID | Liittyvä vaatimus | Testin kuvaus ja toimenpiteet | Odotettu tulos | Toteutunut tulos | Tila |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **T01** | Sensoridatan simulointi | Ajetaan `PlantSimulator.py` komentokehotteessa kansiossa `AT3_Projecti\src`. | Luodaan `raw_sensor_data.csv` (504 riviä) ilman virheitä. | Skripti suoritettiin ja `raw_sensor_data.csv`-tiedostoon syntyi 504 riviä. | Läpäisty |
| **T02** | Datan esikäsittely | Ladataan `raw_sensor_data.csv` sovelluksen dataputkeen (`processor.py`). | Raakadata luetaan ja häiriöarvot suodatetaan ennen analyysiä. | Sovellus lukee raakadatan ja näyttää *Raw Readings* -lukemaksi 504. | Läpäisty |
| **T03** | Käyttöliittymän käynnistys ja tilanäyttö | Käynnistetään Streamlit-sovellus (`app.py`) ja avataan `localhost:8501` selaimessa. | Sivu latautuu ja näyttää kasvien tilat (*OK* / *ALERT*), kosteuden, valoisuuden ja edellisen kasteluajan. | Sovellus avautui selaimeen ja näytti *Basil*, *Cactus* ja *Monstera* -kasvien tilatiedot. | Läpäisty |
| **T04** | Säädettävät hälytysrajat | Säädetään sivupalkin liukusäätimiä (*Moisture Alert Thresholds*). | Kasvien raja-arvot ja kasteluhälytykset päivittyvät näkymään. | Liukusäätimet muuttavat raja-arvoja sivupalkissa ja korttien minimiarvoissa. | Läpäisty |
| **T05** | Uuden datan generointi ja trendit | Painetaan *Regenerate Sensor Data* -painiketta ja tarkastellaan *7-Day Sensor Trends* -osiota. | Data luodaan uudelleen ja 7 päivän trendinäkymä on näkyvissä. | Painike ja *7-Day Sensor Trends* -osio ovat näkyvissä käyttöliittymässä. | Läpäisty |
## Validointi käyttäjätarpeeseen nähden
Käyttäjän tarve on nähdä huonekasvien kosteus, valaistus ja kastelutarve ilman että sensoridataa tarvitsee tulkita itse.

* **Selkeys ja nopea tilannekuva:** "Current plant status" kohdassa näkyy selkeästi joko hälytystila (ALERT) tai normaalitila (OK). Esimerkiksi jos kasvin kosteus on matala, bäkymä tuo esiin "Needs water" -ilmokituksen.
* **Joustavuus eri kasveille ja tilanteille**: Eri kasveilla on eri kosteusrajat joita käyttäjä voi itse säätää.

## Tunnetut puutteet

1. Ei ilmoituksia kuivuvista kasveista, tilanne pitää manuaalisesti tarkistaa.
2. Pidemmän ajan tai useamman kasvin CSV tiedosto voi alkaa hidastamaan prosessia.

