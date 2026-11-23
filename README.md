# Smart Plant Monitor
Leo Cousins, Misto Pantzar
## Tarkoitus
Smart Plant Monitor on Pythonilla ja Streamlitillä toteutettu sovellus huonekasvien (*Monstera*, *Cactus*, *Basil*) kosteus- ja valoisuustietojen simulointiin, puhdistamiseen, analysointiin ja visualisointiin.
## Käynnistys
Vaatii Pyhton 3.9 tai uudemman. 
Kun projetkikansio on auki esim. Visual Studiossa, asenna tarvittavat paketit (pandas, pytest ja streamlit). Seuraavaksi, generoi sensoridata komennolla "python src/PlantSimulator.py". Ennen dashboardin käynnistystä, voi testata datan oikeuden ja siivota selvästi virheelliset arvot komennolla "python -m pytest -v". Lopuksi käynnistetään dashboard komennolla "python -m streamlit run src/app.py".

## Käyttö
Kun sovellus on käynnistetty ja avattu, sitä voidaan käyttää seuraavasti.
1. Kasvien tilan tarkastelu: "Current plant status" osiossa näet jokaisen kasvin ajantasaisen tilan, mullan kosteuden, valoisuuden, ja tiedon siitä mkilloin kasvi on viimeksi kasteltu.
2. Hälytysrajojen säätäminen: Vasemman sivupalkin liukusäätimillä voi muuttaa kasvien minimikosteusrajoja
3. Sensoridatan uudelleenluonti: Sivupalkin "Controls" osiossa olevalla "regenerate sensor data" painikkeella voit generoida uuden 7 vuorokauden simulaatioaineiston ja päivittää näkymän.
4. Trendien seuranta: "7 day sensor trends" osiosta voit tarkastella sensoridatan kehitystä seitsämän päivän ajalta.

## Testaus
1. **Datan simulointi ja CSV-tuloste:** Ajettu `PlantSimulator.py` komentokehotteessa ja varmistettu, että se luo onnistuneesti 504 riviä dataa `data/raw_sensor_data.csv`-tiedostoon.
2. **Käyttöliittymän ja palvelimen käynnistys:** Käynnistetty Streamlit-sovellus (`app.py`) ja varmistettu, että se avautuu selaimeen ja näyttää kasvien tilat, sivupalkin säätimet sekä *Raw Readings* -lukeman (504).
3. **Toiminnallinen testaus selaimessa:** Testattu kosteusrajojen liukusäätimiä sekä *Regenerate Sensor Data* -toimintoa.
