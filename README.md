
# Ordo

Pre-Vatican II Roman Catholic Ordo with proper readings indicated for the Divine Office and the Mass.

## Python Specifications

Python 3.x.x 64-bit

### Modules:

dateutil

## Overview

The temporal cycle is generated by a funtion as a dictionary. The sanctoral cycle is made up of several files for country, region and diocese, and each file is a pre-built dictionary. These are combined with the temporal cycle after the latter is generated.

The result is a dictionary containing:

1. A liturgical calendar proper to an specified diocese (or several dioceses);
2. Indications of the peculiarities of the office of that day;
3. An ordo for the Mass of that day, or multiple Masses, if applicable.

Easter is the first feast (every 'event' is treated as a feast) to be determined, since most of the liturgical year depends upon the date of Easter. Christmas, being static with regard to its date, requires that we only find the day of the week on which it falls. We begin building the temporal calendar with 01-01.

## Progress

- [x] Temporal Calendar
- [ ] Combined Temporal and Sanctoral Calendar
- [ ] Masses
- [ ] Vespers
- [ ] Colors of Mass and Office
- [ ] Lessons for Laudes
- [ ] Prime
- [ ] Little Hours
- [ ] Solemnities
- [ ] Australian Calendar
- [ ] Canadian Calendar
                

## Calendar for 2022

| Day | Date | Rank | Feast |
|---|---|---|---|
| Sat | 01/01 | d II cl | Circumcisio DNJC et Oct. Nativitatis | 
| Sun | 01/02 | d II cl | Ssmi Nominis Jesu | 
 | | | | *Com:* Octava S. Stephani Protomartyris | 
| Mon | 01/03 | s | Octava S. Joannis Ap Ev | 
| Tue | 01/04 | s | Octava Ss Innocentium Mm. | 
| Wed | 01/05 | sd Vig privil 2 cl | Vigilia Epiphaniæ | 
| Thu | 01/06 | d I cl cum Oct privil 2 ord | Epiphania DNJC | 
| Fri | 01/07 | feria | De II die infra Oct. Epiphaniæ | 
| Sat | 01/08 | feria | De III die infra Oct. Epiphaniæ | 
| Sun | 01/09 | dm | S. Familiæ Jesu, Mariæ, Joseph; Dominica I infra Oct. Epiphaniæ | 
| Mon | 01/10 | feria | De V die infra Oct. Epiphaniæ | 
| Tue | 01/11 | feria | De VI die infra Oct. Epiphaniæ | 
| Wed | 01/12 | feria | De VII die infra Oct. Epiphaniæ | 
| Thu | 01/13 | dm | Octava Epiphaniæ | 
| Fri | 01/14 | d | S Hilarii Episcopi ECD | 
 | | | | *Com:* S Felix SM | 
| Sat | 01/15 | d | S Pauli Primi Eremitæ C | 
 | | | | *Com:* S Mauri Abb | 
| Sun | 01/16 | sd | Dominica II post Epiphaniam | 
 | | | | *Com:* S Marcelli PM | 
| Mon | 01/17 | d | S Antonii Abb | 
| Tue | 01/18 | dm | Cathedræ S Petri Ap Romæ | 
 | | | | *Com:* S Pauli Apostoli | 
 | | | | *Com:* S Priscæ VM | 
| Wed | 01/19 | s | Ss Marii, Marthæ, Audifacis et Abachum Mm | 
 | | | | *Com:* S Canuti RM | 
| Thu | 01/20 | d | Ss Fabiani P \& Sebastiani Mm | 
| Fri | 01/21 | d | S Agnetis VM | 
| Sat | 01/22 | sd | Ss Vincentii \& Anastasii Mm | 
| Sun | 01/23 | sd | Dominica III post Epiphaniam | 
 | | | | *Com:* S Raymundi de Peñafort C mtv | 
| Mon | 01/24 | d | S Timothei EM | 
| Tue | 01/25 | dm | Conversio S Pauli Ap | 
| Wed | 01/26 | d | S Polycarpi EM | 
| Thu | 01/27 | d | S Joannis Chrysostomi | 
| Fri | 01/28 | d | S Petri Nolasci C mtv | 
 | | | | *Com:* S Agnetis VM secundo | 
| Sat | 01/29 | d | S Francisci Salesii ECD | 
| Sun | 01/30 | sd | Dominica IV post Epiphaniam | 
 | | | | *Com:* S Martinæ VM | 
| Mon | 01/31 | d | S Joannis Bosco C | 
| Tue | 02/01 | d | S Ignatii EM | 
| Wed | 02/02 | d II cl | In Purificatione BMV | 
| Thu | 02/03 | s | S Blasii EM | 
| Fri | 02/04 | d | S Andreæ Corsini EC | 
| Sat | 02/05 | d | S Agathæ VM | 
| Sun | 02/06 | sd | Dominica V post Epiphaniam | 
 | | | | *Com:* S Titi EC | 
| Mon | 02/07 | d | S Romualdi Abb | 
| Tue | 02/08 | d | S Joannis de Matha C | 
| Wed | 02/09 | d | S Cyrilli ECD | 
 | | | | *Com:* S Apollonia VM | 
| Thu | 02/10 | d | S Scholasticæ V | 
| Fri | 02/11 | dm | In Apparitione BMV Immaculatæ | 
| Sat | 02/12 | d | Ss Septem Fundatorum Ordinis Servorum BMV C | 
| Sun | 02/13 | sd II cl | Dominica in Septuagesima | 
| Mon | 02/14 | s | S Valentini PM | 
| Tue | 02/15 | s | Ss Faustini \& Jovitæ | 
| Fri | 02/18 | s | S Simeonis EM | 
| Sun | 02/20 | sd II cl | Dominica in Sexagesima | 
| Tue | 02/22 | dm | In Cathedra S Petri Ap | 
| Wed | 02/23 | d | S Petri Damiani ECD | 
| Thu | 02/24 | d II cl | S Matthiæ Ap | 
| Sun | 02/27 | sd II cl | Dominica in Quinquagesima | 
 | | | | *Com:* S Gabrirlis a Virgine Perdolente | 
| Wed | 03/02 | feria | Dies Cinerum | 
| Thu | 03/03 | feria | Feria V post Diem Cinerum | 
| Fri | 03/04 | sd | S Casimiri C | 
 | | | | *Com:* Feria VI post Diem Cinerum | 
 | | | | *Com:* S Lucii I PM | 
| Sat | 03/05 | feria | Sabbatum post Diem Cinerum | 
| Sun | 03/06 | sd I cl | Dominica I in Quadragesima | 
| Mon | 03/07 | d | S Thomas De Aquino C | 
 | | | | *Com:* Feria II infra Hebd I in Quadragesima | 
| Tue | 03/08 | d | S Ioannis a Deo C | 
 | | | | *Com:* Feria III infra Hebd I in Quadragesima | 
| Wed | 03/09 | feria | Feria IV Quatuor Temporum Quadragesimæ | 
| Thu | 03/10 | sd | Ss Quadraginta Mm | 
 | | | | *Com:* Feria V infra Hebd I in Quadragesima | 
| Fri | 03/11 | feria | Feria VI Quatuor Temporum Quadragesimæ | 
| Sat | 03/12 | feria | Sabbatum Quatuor Temporum Quadragesimæ | 
| Sun | 03/13 | sd I cl | Dominica II in Quadragesima | 
| Mon | 03/14 | feria | Feria II infra Hebd II in Quadragesima | 
| Tue | 03/15 | feria | Feria III infra Hebd II in Quadragesima | 
| Wed | 03/16 | feria | Feria IV infra Hebd II in Quadragesima | 
| Thu | 03/17 | d | S Patricii Ep C | 
 | | | | *Com:* Feria V infra Hebd II in Quadragesima | 
| Fri | 03/18 | d | S Cyrilli Ep CD | 
 | | | | *Com:* Feria VI infra Hebd II in Quadragesima | 
| Sat | 03/19 | d I cl | S Joseph Sponsi BMV C | 
| Sun | 03/20 | sd I cl | Dominica III in Quadragesima | 
| Mon | 03/21 | dm | S Benedicti Abb | 
 | | | | *Com:* Feria II infra Hebd III in Quadragesima | 
| Tue | 03/22 | feria | Feria III infra Hebd III in Quadragesima | 
| Wed | 03/23 | feria | Feria IV infra Hebd III in Quadragesima | 
| Thu | 03/24 | dm | S Gabrielis Arch | 
 | | | | *Com:* Feria V infra Hebd III in Quadragesima | 
| Fri | 03/25 | d I cl | In Annuntiatione BMV | 
| Sat | 03/26 | feria | Sabbatum infra Hebd III in Quadragesima | 
| Sun | 03/27 | sd I cl | Dominica IV in Quadragesima (Lætare) | 
| Mon | 03/28 | sd | S Ioannis a Capistrano C | 
 | | | | *Com:* Feria II infra Hebd IV in Quadragesima  | 
| Tue | 03/29 | feria | Feria III infra Hebd IV in Quadragesima  | 
| Wed | 03/30 | feria | Feria IV infra Hebd IV in Quadragesima  | 
| Thu | 03/31 | feria | Feria V infra Hebd IV in Quadragesima  | 
| Fri | 04/01 | feria | Feria VI infra Hebd IV in Quadragesima  | 
| Sat | 04/02 | d | S Francisco de Paula C | 
 | | | | *Com:* Sabbatum infra Hebd IV in Quadragesima  | 
| Sun | 04/03 | sd I cl | Dominica de Passione | 
| Mon | 04/04 | d | S Isidori CD | 
 | | | | *Com:* Feria II infra Hebd de Passione | 
| Tue | 04/05 | d | S Vincentii Ferrerii C | 
 | | | | *Com:* Feria III infra Hebd de Passione | 
| Wed | 04/06 | feria | Feria IV infra Hebd de Passione | 
| Thu | 04/07 | feria | Feria V infra Hebd de Passione | 
| Fri | 04/08 | dm | Septem Dolorum BMV | 
| Sat | 04/09 | feria | Sabbatum infra Hebd de Passione | 
| Sun | 04/10 | sd I cl | Dominica in Palmis | 
| Mon | 04/11 | feria | Feria II Majoris Hebd | 
| Tue | 04/12 | feria | Feria III Majoris Hebd | 
| Wed | 04/13 | feria | Feria IV Majoris Hebd | 
| Thu | 04/14 | d I cl | Feria V in Cœna Domini | 
| Fri | 04/15 | d I cl | Feria VI in Parasceve | 
| Sat | 04/16 | d I cl | Sabbatum Sanctum | 
| Sun | 04/17 | d I cl cum Oct privil I ord | Dominica Resurrectionis | 
| Mon | 04/18 | d I cl | Feria II infra Oct. Paschæ | 
| Tue | 04/19 | d I cl | Feria III infra Oct. Paschæ | 
| Wed | 04/20 | sd | Feria IV infra Oct. Paschæ | 
| Thu | 04/21 | sd | Feria V infra Oct. Paschæ | 
| Fri | 04/22 | sd | Feria VI infra Oct. Paschæ | 
| Sat | 04/23 | sd | Sabbatum in Albis | 
| Sun | 04/24 | dm | Dominica in Albis | 
| Mon | 04/25 | d II cl | S Marci Ev | 
| Tue | 04/26 | sd | Ss Cleti et Marcellini PP Mm | 
| Wed | 04/27 | d | S Petri Canisii CD | 
| Sun | 05/01 | d II cl | Ss Philippi et Iacobi APp | 
 | | | | *Com:* Dominica II post Pascha | 
| Mon | 05/02 | d | S Athanasii Ep CD | 
| Tue | 05/03 | d II cl | In Inventione S Crucis | 
 | | | | *Com:* Ss Alexandro I Pp, Event et Theodulo Mm ac Juvenile Ep C | 
| Wed | 05/04 | d I cl cum Oct Communi | Solemnitas S. Joseph, Sponsi BMV C. et Ecclesiæ Universalis Patroni | 
| Thu | 05/05 | d | S Pii V Pp C | 
| Fri | 05/06 | dm | S Ioannis Ap et Ev Ante Portam Latinam | 
| Sat | 05/07 | d | S Stanislai Ep M | 
| Sun | 05/08 | sd | Dominica III post Pascha | 
 | | | | *Com:* In Apparitione S Michaelis Archangelis | 
| Mon | 05/09 | d | S Gregorii Nanzanzeni Ep CD | 
| Tue | 05/10 | d | S Antonini Ep C | 
 | | | | *Com:* Ss Gordiani et Epimachi Mm | 
| Wed | 05/11 | dm | Octava Solemnitatis S. Joseph | 
| Thu | 05/12 | sd | Ss Nerei, Achillei at Domitillae V atq Pancratii Mm | 
| Fri | 05/13 | d | S Roberti Bellarmini Ep CD | 
| Sat | 05/14 | s | S Bonifatii M | 
| Sun | 05/15 | sd | Dominica IV post Pascha | 
 | | | | *Com:* S Ioannis Baptistae de la Salle C | 
| Mon | 05/16 | sd | S Ubaldi EC | 
| Wed | 05/18 | d | S Venantii M | 
| Thu | 05/19 | d | S Petri Celestini PC | 
 | | | | *Com:* S Pudentianae V | 
| Fri | 05/20 | sd | S Bernardini Senensis C | 
| Sun | 05/22 | sd | Dominica V post Pascha | 
| Mon | 05/23 | feria | Feria II in Rogationibus | 
| Tue | 05/24 | feria | Feria III in Rogationibus | 
| Wed | 05/25 | d | S Gregorii VII PC | 
 | | | | *Com:* Feria IV in Rogationibus in Vigilia Ascensionis  | 
 | | | | *Com:* S Urbano I PM | 
| Thu | 05/26 | d I cl cum Oct privil 3 ord | Ascensio DNJC | 
| Fri | 05/27 | d | S Bedæ Venerabilis CD | 
 | | | | *Com:* S Joanne I PM | 
| Sat | 05/28 | d | S Augustini EC | 
 | | | | *Com:* Sabbatum infra Oct. Ascensionis | 
| Sun | 05/29 | sd | Dominica infra Octavam Ascensionis | 
 | | | | *Com:* S Mariæ Magdalenæ de Pazzis V | 
| Mon | 05/30 | sd | De IV die infra Oct. Ascensionis | 
| Tue | 05/31 | d | S Angelæ Mericiæ V | 
 | | | | *Com:* De V die infra Oct. Ascensionis | 
 | | | | *Com:* S Petronilla V | 
| Wed | 06/01 | sd | De VI die infra Oct. Ascensionis | 
 | | | | *Com:* Feria IV Quatuor Temporum infra Oct. Pentecostes | 
| Thu | 06/02 | dm | Oct. Ascensionis DNJC | 
 | | | | *Com:* Ss Marcellini, Petri \& Erasmi E Mm | 
| Fri | 06/03 | feria | Feria VI Quatuor Temporum infra Oct. Pentecostes | 
| Sat | 06/04 | d I cl Vig privil I cl | Vigilia Pentecostes | 
| Sun | 06/05 | d I cl cum Oct privil I ord | Dominica Pentecostes | 
| Mon | 06/06 | d I cl | Feria II infra Oct. Pentecostes | 
| Tue | 06/07 | d I cl | Feria III infra Oct. Pentecostes | 
| Wed | 06/08 | sd | Feria IV infra Oct. Pentecostes | 
| Thu | 06/09 | sd | Feria V infra Oct. Pentecostes | 
| Fri | 06/10 | sd | Feria VI infra Oct. Pentecostes | 
| Sat | 06/11 | sd | Sabbatum infra Oct. Pentecostes | 
| Sun | 06/12 | d I cl | Festum Sanctissimæ Trinitatis | 
| Mon | 06/13 | d | S Antonii de Padua C | 
| Tue | 06/14 | d | S Basilii Magni ECD | 
| Wed | 06/15 | s | Ss Vili, Modesti \& Crescentiæ Mm | 
| Thu | 06/16 | d I cl cum Oct privil 2 ord | Sanctissimi Corporis Christi | 
| Fri | 06/17 | sd | Feria VI infra Oct. Ssmi Corporis Christi | 
| Sat | 06/18 | sd | Sabbatum infra Oct. Ssmi Corporis Christi | 
 | | | | *Com:* S Ephræm Syri Diaconi CD | 
| Sun | 06/19 | sd | Dominica infra Oct. Ssmi Corporis Christi (Dominica II post Pentecosten) | 
 | | | | *Com:* S Julianæde Falconeriis V | 
| Mon | 06/20 | sd | Feria II infra Oct. Ssmi Corporis Christi | 
| Tue | 06/21 | sd | Feria III infra Oct. Ssmi Corporis Christi | 
 | | | | *Com:* S Aloisii Gonzagæ C | 
| Wed | 06/22 | sd | Feria IV infra Oct. Ssmi Corporis Christi | 
 | | | | *Com:* S Paulini EC | 
| Thu | 06/23 | dm | Octava Ssmi Corporis Christi | 
| Fri | 06/24 | d I cl cum Oct communi | In Nativitate S Joannis Baptistæ | 
| Fri | 06/24 tranlsated | d I cl cum Oct communi | In Nativitate S Joannis Baptistæ | 
| Sat | 06/25 | d | S Gulielmi Abb | 
 | | | | *Com:* Sabbatum infra Oct. Ssmi Cordis DNJC | 
| Sun | 06/26 | sd | Dominica infra Oct. Ssmi Cordis DNJC (Dominica III post Pentecosten) | 
 | | | | *Com:* S joannis \& Pauli Mm | 
| Mon | 06/27 | sd | Feria II infra Oct. Ssmi Cordis DNJC | 
| Tue | 06/28 | d | Irinæi EM | 
 | | | | *Com:* Feria III infra Oct. Ssmi Cordis DNJC | 
 | | | | *Com:* In Vigilia Ss Petri \& Pauli App | 
| Wed | 06/29 | d I cl cum Oct communi | Ss Petri \& Pauli App | 
| Thu | 06/30 | dm | In Commemoratione S Pauli Apostoli | 
 | | | | *Com:* Feria V infra Oct. Ssmi Cordis DNJC | 
 | | | | *Com:* S Petri Ap | 
| Fri | 07/01 | d I cl | In Festo Pretiosissimi Sanguis DNJC | 
| Sat | 07/02 | d II cl | In Visitatione BMV | 
 | | | | *Com:* Ss Processo \& Martiniano Mm | 
| Sun | 07/03 | sd | Dominica IV post Pentecosten | 
 | | | | *Com:* S Leonis II PC | 
| Mon | 07/04 | s | De ea | 
| Tue | 07/05 | d | S Antonii Mariæ Zaccaria C | 
| Wed | 07/06 | dm | In Octava Ss Petri \& Pauli App | 
| Thu | 07/07 | d | Ss Cyrilli \& Methodii EppCc | 
| Fri | 07/08 | sd | S Elisabeth Reginæ Vid | 
| Sat | 07/09 | s | De ea | 
| Sun | 07/10 | sd | Dominica V post Pentecosten | 
 | | | | *Com:* Ss Septem Fratrum Mm ac Rufinæ \& Secundæ VvMm | 
| Mon | 07/11 | s | S Pii I PM | 
| Tue | 07/12 | d | S Joannis Gualberti Abb | 
 | | | | *Com:* Ss Nabore \& Felice Mm | 
| Wed | 07/13 | sd | S Anacleti PM | 
| Thu | 07/14 | d | S Bonaventuræ ECD | 
| Fri | 07/15 | sd | S Henrici Imperatoris, C | 
| Sat | 07/16 | dm | In Commemoratione BMV de Monte Carmelo | 
| Sun | 07/17 | sd | Dominica VI post Pentecosten | 
 | | | | *Com:* S Alexii C | 
| Mon | 07/18 | d | S Camilli de Lellis C | 
 | | | | *Com:* Ss Symphorosa \& septem Filiis ejus Mm | 
| Tue | 07/19 | d | S Vincent a Paulo C | 
| Wed | 07/20 | d | S Hieronymi Æmiliani C | 
 | | | | *Com:* S Margarita VM | 
| Thu | 07/21 | s | S Praxedis V | 
| Fri | 07/22 | d | S Mariæ Magdalenæ Pænitentis | 
| Sat | 07/23 | d | S Apollinaris EM | 
 | | | | *Com:* S Liborio EC | 
| Sun | 07/24 | sd | Dominica VII post Pentecosten | 
 | | | | *Com:* In Vigilia S Jacobi Ap | 
| Mon | 07/25 | d II cl | S Jacobi Ap | 
 | | | | *Com:* S Christophori M | 
| Tue | 07/26 | d II cl | S Annæ Matris BMV | 
| Wed | 07/27 | s | S Pantaleonis M | 
| Thu | 07/28 | sd | Ss Nazarii \& Celsi Mm, Victoris I PM, ac Innocentii I PC | 
| Fri | 07/29 | sd | S Marthæ V | 
 | | | | *Com:* Ss Felice I P, Simplicis, Faustino \& Beatrice Mm | 
| Sat | 07/30 | s | Ss Abdon \& Sennen Mm | 
| Sun | 07/31 | sd | Dominica VIII post Pentecosten | 
 | | | | *Com:* S Ignatii C | 
| Mon | 08/01 | dm | S Petri Ap, ad Vincula | 
 | | | | *Com:* S Pauli Ap | 
 | | | | *Com:* Ss Machabæis Mm | 
| Tue | 08/02 | d | s Alphonso Mariæ de Ligourio ECD | 
 | | | | *Com:* S Stephano PM | 
| Wed | 08/03 | sd | In Inventione S Stephani Protomartyris | 
| Thu | 08/04 | dm | S Dominici C | 
| Fri | 08/05 | dm | In Dedicatione Mariæ ad Nives | 
| Sat | 08/06 | dm | In Transfiguratione DNJC | 
 | | | | *Com:* Ss Xysto P, Felicissimo \& Agapito Mm | 
| Sun | 08/07 | sd | Dominica IX post Pentecosten | 
 | | | | *Com:* S Cajetani C | 
| Mon | 08/08 | sd | Ss Cyriaci, Largi \& Smaragdi Mm | 
| Tue | 08/09 | d | S Joannis Mariæ Vianney C | 
 | | | | *Com:* Vigilia S Laurentii M | 
 | | | | *Com:* S Romano M | 
| Wed | 08/10 | d II cl | S Laurentii M | 
| Thu | 08/11 | s | Ss Tiburtii \& Susannæ VM | 
| Fri | 08/12 | d | S Claræ V | 
| Sat | 08/13 | s | Ss Hippolyti \& Cassiani Mm | 
| Sun | 08/14 | sd | Dominica X post Pentecosten | 
 | | | | *Com:* In Vigilia Assumptionis BMV | 
| Mon | 08/15 | d I cl cum Oct communi | In Assumptione BMV | 
| Tue | 08/16 | d II cl | S Joachim Patris BMV | 
| Wed | 08/17 | d | S Hyacinthi C | 
 | | | | *Com:* Octava S Laurentii M | 
| Thu | 08/18 | s | S Agapito M | 
| Fri | 08/19 | d | S Joannis Eudes C | 
| Sat | 08/20 | d | S Bernardi AbbD | 
| Sun | 08/21 | sd | Dominica XI post Pentecosten | 
 | | | | *Com:* S Joannæ Franciscæ Fremiot de Chantal Vid | 
| Mon | 08/22 | d II cl | In Festo Immaculati Cordis BMV | 
 | | | | *Com:* Ss Timotheo, Hippolyto \& Symphoriano Mm | 
| Tue | 08/23 | v | In Vigilia S Bartholomæi Ap | 
| Wed | 08/24 | d II cl | S Bartholomæi Ap | 
| Thu | 08/25 | sd | S Ludovici RC | 
| Fri | 08/26 | sd | S Zephrini PM | 
| Sat | 08/27 | d | S Josephi Calasantii C | 
| Sun | 08/28 | sd | Dominica XII post Pentecosten | 
 | | | | *Com:* S Augustini ECD | 
| Mon | 08/29 | dm | In Decollatione S Joannis Baptistæ | 
 | | | | *Com:* S Sabina M | 
| Tue | 08/30 | d | S Rosæ a S Maria V | 
 | | | | *Com:* Ss Felice \& Adaucto Mm | 
| Wed | 08/31 | d | S Raymundi Nonnati C | 
| Thu | 09/01 | s | S Ægidii Abb | 
| Fri | 09/02 | sd | S Stephani Regis C | 
| Sat | 09/03 | s | De ea | 
| Sun | 09/04 | sd | Dominica XIII post Pentecosten | 
| Mon | 09/05 | sd | S Laurentii Justiniani EC | 
| Tue | 09/06 | s | De ea | 
| Wed | 09/07 | s | De ea | 
| Thu | 09/08 | d II cl | In Nativitate BMV | 
 | | | | *Com:* S Hadriano M | 
| Fri | 09/09 | s | S Gorgonii M | 
| Sat | 09/10 | d | S Nicolai de Tolentino C | 
| Sun | 09/11 | sd | Dominica XIV post Pentecosten | 
| Mon | 09/12 | dm | Ssmi Nominis Mariæ | 
| Tue | 09/13 | s | De ea | 
| Wed | 09/14 | dm | in Exaltatione S Cruce | 
| Thu | 09/15 | d II cl | Septem Dolorum BMV | 
 | | | | *Com:* S Nicomede M | 
| Fri | 09/16 | sd | Ss Cornelii P \& Cypriani E Mm | 
 | | | | *Com:* Ss Euphemia V, Lucia \& Geminiano Mm | 
| Sat | 09/17 | d | In Impressione Ss Stigmatum S Francisci C | 
| Sun | 09/18 | sd | Dominica XV post Pentecosten | 
 | | | | *Com:* S Joseph a Cupertino C | 
| Mon | 09/19 | s | De ea | 
| Tue | 09/20 | d | Ss Eustachii \& Soc Mm | 
 | | | | *Com:* In Vigilia S Matthæi ApEv | 
| Wed | 09/21 | feria | Feria IV Quatuor Temporum Septembris | 
| Thu | 09/22 | d | S Thomæ de Villanova EC | 
 | | | | *Com:* Ss Mauritio \& Soc Mm | 
| Fri | 09/23 | sd | S Lini | 
 | | | | *Com:* Feria VI Quatuor Temporum Septembris | 
 | | | | *Com:* S Thecla VM | 
| Sat | 09/24 | dm | BMV de Merdece | 
 | | | | *Com:* Sabbatum Quatuor Temporum Septembris | 
| Sun | 09/25 | sd | Dominica XVI post Pentecosten | 
| Mon | 09/26 | s | Ss Cypriani \& Justinæ Mm | 
| Tue | 09/27 | s | Ss Cosmæ \& Damiani Mm | 
| Wed | 09/28 | sd | S Wenceslau Ducis M | 
| Thu | 09/29 | d I cl | In Dedicatione S Michaelis Arch | 
| Fri | 09/30 | d | S Hieronymi SCD | 
| Sat | 10/01 | s | S Remigii EC | 
| Sun | 10/02 | sd | Dominica XVII post Pentecosten | 
 | | | | *Com:* Ss Angelorum Custodum | 
| Mon | 10/03 | d | S Teresiæ a Jesu Infante V | 
| Tue | 10/04 | dm | S Francisci C | 
| Wed | 10/05 | s | Ss Placidi \& Sociorum Mm | 
| Thu | 10/06 | d | S Brunonis C | 
| Fri | 10/07 | d II cl | Sacratissimi Rosarii BMV | 
 | | | | *Com:* S Marco PC | 
 | | | | *Com:* Ss Sergio, Baccho, Marcello \& Apulejo MM | 
| Sat | 10/08 | d | S Birgittæ Vid | 
| Sun | 10/09 | sd | Dominica XVIII post Pentecosten | 
 | | | | *Com:* S Joannis Leonardi C | 
| Mon | 10/10 | sd | S Francisci Borgiæ C | 
| Tue | 10/11 | d II cl | In Maternitate BMV | 
| Wed | 10/12 | s | De ea | 
| Thu | 10/13 | sd | S Eduardi Regis C | 
| Fri | 10/14 | d | S Callisti I PM | 
| Sat | 10/15 | d | S Teresiæ V | 
| Sun | 10/16 | sd | Dominica XIX post Pentecosten | 
 | | | | *Com:* S Hedwigis Vid | 
| Mon | 10/17 | d | S Margaritæ Mariæ Alacoque V | 
| Tue | 10/18 | d II cl | S Lucæ Ev | 
| Wed | 10/19 | d | S Petri Alcantara C | 
| Thu | 10/20 | d | S Joannis Cantii C | 
| Fri | 10/21 | s | S Hilarionis Abb | 
 | | | | *Com:* Ss Ursula \& Sociabus VM | 
| Sat | 10/22 | s | De ea | 
| Sun | 10/23 | sd | Dominica XX post Pentecosten | 
| Mon | 10/24 | dm | S Raphaelis Arch | 
| Tue | 10/25 | s | Ss Chrysanthi \& Dariæ Mm | 
| Wed | 10/26 | s | S Evaristi PM | 
| Thu | 10/27 | v | In Vigilia Ss Simonis \& Judæ App | 
| Fri | 10/28 | d II cl | Ss Simonis \& Judæ App | 
| Sat | 10/29 | s | De ea | 
| Sun | 10/30 | sd | Dominica XXI post Pentecosten | 
| Mon | 10/31 | v | In Vigilia Omnium Sanctorum | 
| Tue | 11/01 | d I cl cum Oct communi | In Festo Omnium Sanctorum | 
| Wed | 11/02 | d | In Commemoratione Omnium Fidelium Defunctorum | 
| Thu | 11/03 | s | De ea | 
| Fri | 11/04 | d | S Caroli EC | 
 | | | | *Com:* Ss Vitale \& Agricola Mm | 
| Sat | 11/05 | s | De ea | 
| Sun | 11/06 | sd | Dominica XXII post Pentecosten | 
| Mon | 11/07 | s | De ea | 
| Tue | 11/08 | sd | Ss Quatuor Coronatis Mm | 
| Wed | 11/09 | d II cl | In Dedicatione Archibasilicæ Ssmi Salvatoris | 
 | | | | *Com:* S Theodoro M | 
| Thu | 11/10 | d | S Andreæ Avellini C | 
 | | | | *Com:* Ss Tryphone, Respicio \& Nympha VM | 
| Fri | 11/11 | d | S Martini  EC | 
 | | | | *Com:* S Menna M | 
| Sat | 11/12 | sd | S Martini I PM | 
| Sun | 11/13 | sd | Dominica XXIII post Pentecosten | 
 | | | | *Com:* S Didaci C | 
| Mon | 11/14 | d | Josaphat EM | 
| Tue | 11/15 | d | S Alberti Magni ECD | 
| Wed | 11/16 | d | S Gertrudis V | 
| Thu | 11/17 | sd | S Gregorii Thaumaturgi EC | 
| Fri | 11/18 | dm | In Dedicatione Basilicarum Ss Petri \& Pauli App | 
| Sat | 11/19 | d | S Elisabeth Vid | 
 | | | | *Com:* S Pontiano PM | 
| Sun | 11/20 | sd | Dominica XXIV et ultima post Pentecosten | 
 | | | | *Com:* S Felicis de Valois C | 
| Mon | 11/21 | dm | In Præsentatione BMV | 
| Tue | 11/22 | d | S Cæciliæ VM | 
| Wed | 11/23 | d | S Clementis I PM | 
 | | | | *Com:* S Felicitate M | 
| Thu | 11/24 | d | S Joannis de Cruce CD | 
 | | | | *Com:* S Chrysogono M | 
| Fri | 11/25 | d | S Catharinæ VM | 
| Sat | 11/26 | d | S Sylvestri Abb | 
 | | | | *Com:* S Petro Alexandrino EM | 
| Sun | 11/27 | sd | Dominica I Adventus | 
| Tue | 11/29 | v | In Vigilia S Andreæ Ap | 
 | | | | *Com:* S Saturnino M | 
| Wed | 11/30 | d II cl | S Andreæ Ap | 
| Fri | 12/02 | sd | S Bibianæ VM | 
| Sat | 12/03 | dm | S Francisci Xaverii C | 
| Sun | 12/04 | sd II cl | Dominica II Adventus | 
 | | | | *Com:* S Petri Chrysologi ECD | 
| Mon | 12/05 | s | S Sabba Abb | 
| Tue | 12/06 | d | S Nicolai EC | 
| Wed | 12/07 | d | S Ambrosii ECD | 
 | | | | *Com:* In Vigilia Conceptionis Immaculatæ BMV | 
| Thu | 12/08 | d I cl cum Oct communi | In Conceptione Immaculata BMV | 
| Sat | 12/10 | s | S Melchide PM | 
| Sun | 12/11 | sd II cl | Dominica III Adventus | 
 | | | | *Com:* S Damasi I PC | 
| Tue | 12/13 | d | S Luciæ VM | 
| Wed | 12/14 | feria | Feria IV Quatuor Temporum in Adventus | 
| Fri | 12/16 | sd | S Eusebii EM | 
 | | | | *Com:* Feria VI Quatuor Temporum in Adventus | 
| Sat | 12/17 | feria | Sabbatum Quatuor Temporum in Adventus | 
| Sun | 12/18 | sd II cl | Dominica IV Adventus | 
| Tue | 12/20 | v | In Vigilia S Thomæ Ap | 
| Wed | 12/21 | d II cl | S Thomæ Ap | 
| Sat | 12/24 | d I cl Vig privil I cl | Vigilia Nativitas DNJC | 
| Sun | 12/25 | d I cl cum Oct privil 3 ord | Nativitas DNJC | 
| Mon | 12/26 | d II cl cum Oct simplici | S. Stephani Protomartyris | 
| Tue | 12/27 | d II cl cum Oct simplici | S. Joannis Ap. Ev. | 
| Wed | 12/28 | d II cl cum Oct simplici | Ss Innocentium Mm. | 
| Thu | 12/29 | d | S. Thomæ E.M. | 
| Fri | 12/30 | sd | Dominica Infra Octavam Nativitatis reposita | 
| Sat | 12/31 | d | S. Silvestri I P.C. | 
