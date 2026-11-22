# Smart plant monitor
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
| **V1: Sensoridatan simulointi** | Järjestelmä generoi 7 päivän tuntikohtaisen datan (3 kasvia × 168 h = 504 riviä) CSV-tiedostoon sisältäen hallitun virheprosentin[cite: 4, 5]. |
| **V2: Datan esikäsittely** | Järjestelmä lataa raakadatan ja puhdistaa sensorivirheet ennen analyysiä. |
| **V3: Reaaliaikainen tilanäyttö** | Käyttöliittymä näyttää jokaiselle kasville tilan (*OK* / *ALERT*), kosteuden (%), valoisuuden (lux) ja ajan edellisestä kastelusta[cite: 9]. |
| **V4: Säädettävät hälytysrajat** | Käyttäjä voi säätää kasvien kosteusrajoja (5 % – 50 %) sivupalkin liukusäätimillä, ja tilat päivittyvät dynaamisesti[cite: 6, 9]. |
| **V5: Trendien visualisointi** |
