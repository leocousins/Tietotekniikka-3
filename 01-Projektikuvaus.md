Sovellus esittää 7 päivän sensoritrendit visuaalisessa muodossa# Smart plant monitor
## Tarve ja arvolupas
Oikea aikainen kastelu aiheuttaa haasteita huonekasvien hoidossa, etenkin kun eri kasveilla on eri kosteusvaatimukset. Liian harva tai liian tiheä kastelu heikentää kasvien hyvinvointia, ja raa'asta sensoridatasta voi olla vaikea havaita poikkeamia tai virhelukemia.

Smart Plant Monitor tarjoaa selkeän selaimessa toimivan hallintanäkymän, joka muuntaa raa'an sensoridatan ymmärrettäväksi tilannekuvaksi. Sovellus suodattaa datan häiriöt, visualisoi 7 päivän kehitystrendit ja hälyttää automaattisesti, kun kasvin mullan kosteus laskee lajikohtaisen raja-arvon alapuolelle.
## 2. Käyttäjäskenaariot
* Skenaario 1 - Kasvien tilan tarkistus: Avaamalla sovelluksen, käyttäjä näkee kaikkien kasvien kosteuden, valaistuksen sekä niiden viimeisen kastelukerran.
* Skenaario 2 - Hälytykseen reagointi: Käyttäjä huomaa hälytyksen että kasvin kosteus on tippunut alle raja-arvon yli kolmen tunnin ajaksi. Käyttäjä kastelee kasvin huomattuaan hälytyksen.
* Skenaario 3 - Raja-arvojen säätö: Käyttäjä muttaa liukusäätimillä kasvien minimikosteusrajoja. Käyttäjä näkee heti kuinka hälytystilat päivittyvät.
* Skenaario 4 - Uuden testidatan generointi: Kehittäjä tai testaaja painaa sivupalkin *Regenerate Sensor Data* -painiketta luodakseen uuden 7 vuorokauden simulaatioaineiston (504 mittauspistettä) ja tarkastaakseen sovelluksen toiminnan eri tilanteissa.

## 3. Vaatimukset ja hyväksymiskriteerit
| Vaatimus | Hyväksymiskriteeri |
| :--- | :--- |
| **V1: Sensoridatan simulointi** | Järjestelmä generoi 7 päivän tuntikohtaisen datan (3 kasvia × 168 h = 504 riviä) CSV-tiedostoon sisältäen hallitun virheprosentin. |
| **V2: Datan esikäsittely** | Järjestelmä lataa raakadatan ja puhdistaa sensorivirheet ennen analyysiä. |
| **V3: Reaaliaikainen tilanäyttö** | Käyttöliittymä näyttää jokaiselle kasville tilan (*OK* / *ALERT*), kosteuden (%), valoisuuden (lux) ja ajan edellisestä kastelusta. |
| **V4: Säädettävät hälytysrajat** | Käyttäjä voi säätää kasvien kosteusrajoja (5 % – 50 %) sivupalkin liukusäätimillä, ja tilat päivittyvät dynaamisesti. |
| **V5: Trendien visualisointi** | Sovellus esittää 7 päivän sensoritrendit visuaalisessa muodossa

## 4. Rajaus
* Sisältyy projektiin: Ohjelmallinen sensoridatan simulointi, datan puhdistus, sääntöpohjainen tila-analyysi sekä paikallisesti selaimessa ajettava Streamlit-käyttöliittymä.
* Ei sisälly projektiin: Fyysinen antureiden kytkentä, automaattinen kastelulaitteisto.

## 5. Keskeinen rakenne
1. `PlantSimulator.py` (Datan tuotto):** Luo synteettisen 7 päivän aikasarjadatan (`data/raw_sensor_data.csv`) kolmelle kasville mallintaen kuivumisnopeutta, kastelua ja satunnaisia sensorihäiriöitä.
2. `processor.py` (Esikäsittely):** Lukee raakadatan CSV-tiedostosta ja suodattaa virheelliset mittausarvot.
3. `analyzer.py` (Analyysi):** Määrittelee oletusraja-arvot (`THRESHOLDS`) ja arvioi kasvien kastelutarpeen kosteushistorian perusteella.
4. `app.py` (Käyttöliittymä):** Streamlit-sovellus, joka yhdistää dataputken, tarjoaa interaktiiviset kontrollit sivupalkkiin ja piirtää tilakortit sekä trendikuvaajat.

 ## 6. Oletukset
* Sovellusta ajetaan paikallisesti Python-ympäristössä, johon on asennettu `streamlit` sekä tarvittavat datankäsittelykirjastot.
* Simuloitu data edustaa realistisesti kolmen erityyppisen kasvin (*Basilika*, *Cactus*, *Peikonlehti*) kosteuskäyttäytymistä yhden viikon jaksolla.
* Käyttäjä ymmärtää prosentuaalisen kosteusarvon ja lux-yksikön merkityksen kasvien hoidossa.
