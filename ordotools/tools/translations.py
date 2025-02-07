from ordotools.tools.liturgical_dates import integer_to_roman
from ordotools.tools.liturgical_dates import nth

"""
When adding translations, use the ISO 639-1 codes
that can be found in this article:

https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

We will have latin here and in the feast database,
but eventually we will port everything over.

Feasts are given two digits of padding at the end
so that we can take care of duplicate feasts with
different variations.

All of the feasts are 100 digits apart. Of these 100
digits, we will use the odds for the octaves of the
preceeding feast. This should be plenty.
"""

class Translations:

    def __init__(self):

        self.easy_data = {

            100: {
                "la": "S Hilarii Episcopi ECD",
                "en": "St. Hilary, Bp.CD",
                "fr": "",
            },

            200: {
                "la": "S Pauli Primi Eremitæ C",
                "en": "St. Paul the First Hermit, C",
                "fr": "",
            },

            300: {
                "la": "S Marcelli PM",
                "en": "St. Marcellus, PM",
                "fr": "",
            },

            400: {
                "la": "S Antonii Abb",
                "en": "St. Anthony, Abbot",
                "fr": "",
            },

            500: {
                "la": "Cathedræ S Petri Ap Romæ",
                "en": "St. Peter's Chair in Rome",
                "fr": "",
            },

            600: {
                "la": "Ss Marii, Marthæ, Audifacis & Abachum Mm",
                "en": "",
                "fr": "",
            },

            700: {
                "la": "Ss Fabiani P et Sebastiani Mm",
                "en": "St.s Fabian, Priest, and Sebastian, Mm",
                "fr": "",
            },

            800: {
                "la": "S Agnetis VM",
                "en": "St. Agnes, VM",
                "fr": "",
            },

            900: {
                "la": "Ss Vincentii & Anastasii Mm",
                "en": "",
                "fr": "",
            },

            1000: {
                "la": "S Raymundi de Peñafort C",
                "en": "St. Raymond of Penafort, C",
                "fr": "",
            },

            1100: {
                "la": "S Timothei EM",
                "en": "St. Timothy, BpM",
                "fr": "",
            },

            1200: {
                "la": "Conversio S Pauli Ap",
                "en": "Conversion of St. Paul, Ap",
                "fr": "",
            },

            1300: {
                "la": "S Polycarpi EM",
                "en": "St. Polycarp, BpM",
                "fr": "",
            },

            1400: {
                "la": "S Joannis Chrysostomi ECD",
                "en": "St. John Chrysostom, BpCD",
                "fr": "",
            },

            1500: {
                "la": "S Petri Nolasci C",
                "en": "St. Peter Nolasco, C",
                "fr": "",
            },

            1600: {
                "la": "S Francisci Salesii ECD",
                "en": "St. Francis de Sales, BpCD",
                "fr": "",
            },

            1700: {
                "la": "S Martinæ VM",
                "en": "St. Martina, VM",
                "fr": "",
            },

            1800: {
                "la": "S Joannis Bosco C",
                "en": "St. John Bosco, C",
                "fr": "",
            },

            1900: {
                "la": "S Ignatii EM",
                "en": "St. Ignatius, BpM",
                "fr": "",
            },

            2000: {
                "la": "In Purificatione BMV",
                "en": "Purification of the Blessed Virgin Mary",
                "fr": "",
            },

            2100: {
                "la": "S Blasii EM",
                "en": "St. Blaise, BpM",
                "fr": "",
            },

            2200: {
                "la": "S Andreæ Corsini EC",
                "en": "St. Andrew Corsini, BpC",
                "fr": "",
            },

            2300: {
                "la": "S Agathæ VM",
                "en": "St. Agatha, VM",
                "fr": "",
            },

            2400: {
                "la": "S Titi EC",
                "en": "St. Titus, BpC",
                "fr": "",
            },

            2500: {
                "la": "S Romualdi Abb",
                "en": "St. Romuald, Abbot",
                "fr": "",
            },

            2600: {
                "la": "S Joannis de Matha C",
                "en": "St. John of Matha, C",
                "fr": "",
            },

            2700: {
                "la": "S Cyrilli Alexandrini ECD",
                "en": "St. Cyril of Alexandria, BpCD",
                "fr": "",
            },

            2800: {
                "la": "S Scholasticæ V",
                "en": "St. Scholastica, V",
                "fr": "",
            },

            2900: {
                "la": "In Apparitione BVM Immaculatæ",
                "en": "Apparation of Our Lady at Lourdes",
                "fr": "",
            },

            3000: {
                "la": "Ss Septem Fundatores Ordinis Servorum BMV C",
                "en": "Seven Holy Founders",
                "fr": "",
            },

            3100: {
                "la": "S Valentini PM",
                "en": "St. Valentine, PM",
                "fr": "",
            },

            3200: {
                "la": "",
                "en": "",
                "fr": "",
            },

            3300: {
                "la": "S Simeonis EM",
                "en": "St. Simeon, BpM",
                "fr": "",
            },

            3400: {
                "la": "In Cathedra S Petri Ap",
                "en": "St. Peter's Chair in Rome",
                "fr": "",
            },

            3500: {
                "la": "S Petri Damiani ECD",
                "en": "St. Peter Damian, BpCD",
                "fr": "",
            },

            3600: {
                "la": "S Matthiæ Ap",
                "en": "St. Matthew, Ap",
                "fr": "",
            },

            3700: {
                "la": "S Gabrielis a Virgine Perdolente C",
                "en": "",
                "fr": "",
            },

            3800: {
                "la": "S Casimiri C",
                "en": "St. Casmir, C",
                "fr": "",
            },

            3900: {
                "la": "Ss Perpetuæ et Felicitatiis Mm",
                "en": "Sts. Perpetua and Felicity, Mm",
                "fr": "",
            },

            4000: {
                "la": "S Thomæ de Aquino CD",
                "en": "St. Thomas Aquinas, CD",
                "fr": "",
            },

            4100: {
                "la": "S Joannis a Deo C",
                "en": "St. John of God, C",
                "fr": "",
            },

            4200: {
                "la": "S Franciscæ Romanæ V",
                "en": "St. Frances of Rome, V",
                "fr": "",
            },

            4300: {
                "la": "Ss Quadragintarum Mm",
                "en": "Forty Holy Martyrs",
                "fr": "",
            },

            4400: {
                "la": "S Gregorii I PCD",
                "en": "St. Gregory I, PCD",
                "fr": "",
            },

            4500: {
                "la": "S Patricii EC",
                "en": "St. Patrick, BpC",
                "fr": "",
            },

            4600: {
                "la": "S Cyrilii Hierosolymitani ECD",
                "en": "St. Cyril of Jerusalem, BCD",
                "fr": "",
            },

            4700: {
                "la": "S Josephi Sponsi BMV C",
                "en": "St. Joseph, Spouse of the BVM, C",
                "fr": "",
            },

            4800: {
                "la": "S Benedicti Abb",
                "en": "St. Benedict, Abb",
                "fr": "",
            },

            4900: {
                "la": "S Gabrielis Arch",
                "en": "St. Gabriel, Archangel",
                "fr": "",
            },

            5000: {
                "la": "In Annuntiatione BMV",
                "en": "Annuntiation of the BVM",
                "fr": "",
            },

            5100: {
                "la": "S Joannis Damasceni CD",
                "en": "St. John Damascene, CD",
                "fr": "",
            },

            5200: {
                "la": "S Joannis a Capistrano C",
                "en": "",
                "fr": "",
            },

            5300: {
                "la": "S Francisci de Paula C",
                "en": "",
                "fr": "",
            },

            5400: {
                "la": "S Isidori ECD",
                "en": "St. Isidore, ECD",
                "fr": "",
            },

            5500: {
                "la": "S Vincentii Ferrerii C",
                "en": "St. Vincent Ferrier, C",
                "fr": "",
            },

            5600: {
                "la": "S Leonis PCD",
                "en": "St. Leo, PCD",
                "fr": "",
            },

            5700: {
                "la": "S Hermenegildi M",
                "en": "St. Hermenegild, M",
                "fr": "",
            },

            5800: {
                "la": "S Justini M",
                "en": "St. Justin, M",
                "fr": "",
            },

            5900: {
                "la": "S Aniceti PM",
                "en": "",
                "fr": "",
            },

            6000: {
                "la": "S Anselmi ECD",
                "en": "St. Anselm, ECD",
                "fr": "",
            },

            6100: {
                "la": "Ss Soteris et Caii PpMm",
                "en": "",
                "fr": "",
            },

            6200: {
                "la": "S Georgii M",
                "en": "St. George, M",
                "fr": "",
            },

            6300: {
                "la": "S Fidelis a Sigmaringa M",
                "en": "",
                "fr": "",
            },

            6400: {
                "la": "S Marci Ev",
                "en": "St. Mark, Ev",
                "fr": "",
            },

            6500: {
                "la": "Ss Cleti et Marcellini PpMm",
                "en": "",
                "fr": "",
            },

            6600: {
                "la": "S Petri Canisii CD",
                "en": "",
                "fr": "",
            },

            6700: {
                "la": "S Pauli a Cruce C",
                "en": "St. Paul of the Cross, C",
                "fr": "",
            },

            6800: {
                "la": "S Petri M",
                "en": "St. Peter M",
                "fr": "",
            },

            6900: {
                "la": "S Catharinæ Senensis V",
                "en": "St. Catherine of Siena, V",
                "fr": "",
            },

            7000: {
                "la": "Ss Philippi et Jacobi App",
                "en": "Sts. Philip and Jacob, App",
                "fr": "",
            },

            7100: {
                "la": "S Athanasii ECD",
                "en": "St. Athanasius, ECD",
                "fr": "",
            },

            7200: {
                "la": "In Inventione S Crucis",
                "en": "Finding of the Holy Cross",
                "fr": "",
            },

            7300: {
                "la": "S Monicæ V",
                "en": "St. Monica, V",
                "fr": "",
            },

            7400: {
                "la": "S Pii V PC",
                "en": "St. Pius V, PC",
                "fr": "",
            },

            7500: {
                "la": "S Joannis ApEv ante Portam Latinam",
                "en": "St. John ApEv before the Latin Gate",
                "fr": "",
            },

            7600: {
                "la": "S Stanislai EM",
                "en": "St. Stanislaus, EM",
                "fr": "",
            },

            7700: {
                "la": "In Apparitione S Michaelis Arch",
                "en": "Apparition of St. Michael Archangel",
                "fr": "",
            },

            7800: {
                "la": "S Gregorii Nanzanzeni ECD",
                "en": "",
                "fr": "",
            },

            7900: {
                "la": "S Antonini EC",
                "en": "St. Anthony, EC",
                "fr": "",
            },

            8000: {
                "la": "Ss Nerei, Achillei at Domitialæ V atque Pancratii Mm",
                "en": "",
                "fr": "",
            },

            8100: {
                "la": "S Roberti Bellarmino ECD",
                "en": "St. Robert Ballarmine, ECD",
                "fr": "",
            },

            8200: {
                "la": "S Bonifatii M",
                "en": "St. Boniface, M",
                "fr": "",
            },

            8300: {
                "la": "S Joannis Baptistæ de la Salle C",
                "en": "St. John Baptist de la Salle, C",
                "fr": "",
            },

            8400: {
                "la": "S Ubaldi EC",
                "en": "St. Ubald, EC",
                "fr": "",
            },

            8500: {
                "la": "S Paschalis Baylon C",
                "en": "St. Paschal Baylon, C",
                "fr": "",
            },

            8600: {
                "la": "S Venantii M",
                "en": "",
                "fr": "",
            },

            8700: {
                "la": "S Petri Cælestini PC",
                "en": "",
                "fr": "",
            },

            8800: {
                "la": "S Bernardini Senensis C",
                "en": "",
                "fr": "",
            },

            8900: {
                "la": "S Gregorii VII PC",
                "en": "St. Gregory VII, PC",
                "fr": "",
            },

            9000: {
                "la": "S Philippi Nerii C",
                "en": "St. Philip Neri, C",
                "fr": "",
            },

            9100: {
                "la": "S Bedæ Venerabilis CD",
                "en": "St. Bede the Venerable, CD",
                "fr": "",
            },

            9200: {
                "la": "S Augustini EC",
                "en": "St. Augustine, EC",
                "fr": "",
            },

            9300: {
                "la": "S Mariæ Magdalenæ de Pazzis V",
                "en": "St. Mary Madgalene de Pazzi, V",
                "fr": "",
            },

            9400: {
                "la": "S Felix I PM",
                "en": "St. Felix I, PM",
                "fr": "",
            },

            9500: {
                "la": "B Mariæ Virginis Reginæ",
                "en": "Queenship of the Blessed Virgin Mary",
                "fr": "",
            },

            9600: {
                "la": "S Angelæ Mariciæ V",
                "en": "",
                "fr": "",
            },

            9700: {
                "la": "Ss Marcellini, Petri atque Erasmi E Mm",
                "en": "",
                "fr": "",
            },

            9800: {
                "la": "S Francisci Caracciolo C",
                "en": "",
                "fr": "",
            },

            9900: {
                "la": "S Bonifatii EM",
                "en": "St. Boniface, EM",
                "fr": "",
            },

            10000: {
                "la": "S Norberti EC",
                "en": "St. Norbert, BpC",
                "fr": "",
            },

            10100: {
                "la": "Ss Primi et Feliciani Mm",
                "en": "",
                "fr": "",
            },

            10200: {
                "la": "S Margaritæ R V",
                "en": "St. Margaret, Queen V",
                "fr": "",
            },

            10300: {
                "la": "S Barnabæ Ap",
                "en": "St. Barnabas, Ap",
                "fr": "",
            },

            10400: {
                "la": "S Joannis a S Facundo C",
                "en": "",
                "fr": "",
            },

            10500: {
                "la": "S Antonii de Padua CD",
                "en": "St. Anthony of Padua, CD",
                "fr": "",
            },

            10600: {
                "la": "S Basilii Magni ECD",
                "en": "St. Basil the Great, ECD",
                "fr": "",
            },

            10700: {
                "la": "Ss Viti, Modesti atque Crescentiæ Mm",
                "en": "",
                "fr": "",
            },

            10800: {
                "la": "S Ephræm Syri Diaconi CD",
                "en": "",
                "fr": "",
            },

            10900: {
                "la": "S Julianæ de Falconeriis V",
                "en": "",
                "fr": "",
            },

            11000: {
                "la": "S Silverii PM",
                "en": "",
                "fr": "",
            },

            11100: {
                "la": "S Aloisii Gonzagæ C",
                "en": "St. Aloysius Gonzaga, C",
                "fr": "",
            },

            11200: {
                "la": "S Paulini EC",
                "en": "St. Paulinus, EC",
                "fr": "",
            },

            11300: {
                "la": "In Vigilia Nativitatis S Joannis Baptistæ",
                "en": "Vigil of the Nativity of St. John the Baptist",
                "fr": "",
            },

            11400: {
                "la": "In Nativitate S Joannis Baptistæ",
                "en": "Nativity of St. John the Baptist",
                "fr": "",
            },

            11401: {
                "la": "Oct S Joannis Baptistæ",
                "en": "of St. John the Baptist",
                "fr": "",
            },

            11500: {
                "la": "S Gulielmi Abb",
                "en": "",
                "fr": "",
            },

            11600: {
                "la": "Ss Joannis et Pauli Mm",
                "en": "Sts. John and Paul, Mm",
                "fr": "",
            },

            11800: {
                "la": "S Irinæi EM",
                "en": "",
                "fr": "",
            },

            11900: {
                "la": "Ss Petri et Pauli App",
                "en": "Sts. Peter and Paul, App.",
                "fr": "",
            },

            11901: {
                "la": "Oct Ss Petri et Pauli App",
                "en": "of Sts. Peter and Paul, App.",
                "fr": "",
            },

            12000: {
                "la": "In Commemoratione S Pauli Apostoli",
                "en": "Commemoration of St. Paul, Ap",
                "fr": "",
            },

            12100: {
                "la": "In Festo Pretiosissimi Sanguinis DNJC",
                "en": "Feast of the Most Precious Blood",
                "fr": "",
            },

            12200: {
                "la": "In Visitatione BMV",
                "en": "Visitation of the Blessed Virgin Mary",
                "fr": "",
            },

            12300: {
                "la": "S Leonis II PC",
                "en": "St. Leo II, PC",
                "fr": "",
            },

            12500: {
                "la": "S Antonii Mariæ Zaccaria C",
                "en": "",
                "fr": "",
            },

            12700: {
                "la": "Ss Cyrilli et Methodii EeCc",
                "en": "Sts. Cyril and Methodius, BppCc",
                "fr": "",
            },

            12800: {
                "la": "S Elisabeth R Vid",
                "en": "St. Elizabeth, Queen W",
                "fr": "",
            },

            12900: {
                "la": "Ss Septem Fratrum Mm ac Rufinæ et Secundæ VvMm",
                "en": "",
                "fr": "",
            },

            13000: {
                "la": "S Pii I PM",
                "en": "St. Pius I, PM",
                "fr": "",
            },

            13100: {
                "la": "S Joannis Gualberti Abb",
                "en": "St. John Gualbert, Abb",
                "fr": "",
            },

            13200: {
                "la": "S Anacleti PM",
                "en": "",
                "fr": "",
            },

            13300: {
                "la": "S Bonaventuræ ECD",
                "en": "St. Bonaventure, BpCD",
                "fr": "",
            },

            13400: {
                "la": "S Henrici Imp C",
                "en": "St. Henry, Emperor C",
                "fr": "",
            },

            13500: {
                "la": "In Commemoratione BMV de Monte Carmelo",
                "en": "Our Lady of Mount Carmel",
                "fr": "",
            },

            13600: {
                "la": "S Alexii C",
                "en": "",
                "fr": "",
            },

            13700: {
                "la": "S Camilli de Lellis C",
                "en": "St. Camillus of Lellis, C",
                "fr": "",
            },

            13800: {
                "la": "S Vincentii a Paulo C",
                "en": "St. Vincent de Paul, C",
                "fr": "",
            },

            13900: {
                "la": "S Hieronymi Æmiliani C",
                "en": "",
                "fr": "",
            },

            14000: {
                "la": "S Praxedis V",
                "en": "",
                "fr": "",
            },

            14100: {
                "la": "S Mariæ Magdalenæ Pænitentis",
                "en": "",
                "fr": "",
            },

            14200: {
                "la": "S Apollinaris EM",
                "en": "",
                "fr": "",
            },

            14300: {
                "la": "In Vigilia S Jacobi Ap",
                "en": "",
                "fr": "",
            },

            14400: {
                "la": "S Jacobi Ap",
                "en": "",
                "fr": "",
            },

            14500: {
                "la": "S Annæ Matris BMV",
                "en": "",
                "fr": "",
            },

            14600: {
                "la": "S Pantaleonis M",
                "en": "",
                "fr": "",
            },

            14700: {
                "la": "Ss Nazarii et Celsi Mm, Victoris I PM, ac Innocentii I PC",
                "en": "",
                "fr": "",
            },

            14800: {
                "la": "S Marthæ V",
                "en": "",
                "fr": "",
            },

            14900: {
                "la": "Ss Abdon et Sennen Mm",
                "en": "",
                "fr": "",
            },

            15000: {
                "la": "S Ignatii C",
                "en": "",
                "fr": "",
            },

            15100: {
                "la": "S Petri Ap ad Vincula",
                "en": "",
                "fr": "",
            },

            15200: {
                "la": "S Alphonsi Mariæ de Ligorio ECD",
                "en": "",
                "fr": "",
            },

            15300: {
                "la": "In Inventione S Stephani Protomartyris",
                "en": "",
                "fr": "",
            },

            15400: {
                "la": "S Dominici C",
                "en": "",
                "fr": "",
            },

            15500: {
                "la": "In Dedicatione S Mariæ ad Nives",
                "en": "",
                "fr": "",
            },

            15600: {
                "la": "In Transfiguratione DNJC",
                "en": "",
                "fr": "",
            },

            15700: {
                "la": "S Cajetani C",
                "en": "",
                "fr": "",
            },

            15800: {
                "la": "Ss Cyriaci, Largi atque Smaragdi Mm",
                "en": "",
                "fr": "",
            },

            15900: {
                "la": "S Joannis Mariæ Vianney C",
                "en": "",
                "fr": "",
            },

            16000: {
                "la": "S Laurentii M",
                "en": "",
                "fr": "",
            },

            16100: {
                "la": "Ss Tiburtii et Susannæ V, Mm",
                "en": "",
                "fr": "",
            },

            16200: {
                "la": "S Claræ V",
                "en": "",
                "fr": "",
            },

            16300: {
                "la": "Ss Hippolyti et Cassiani Mm",
                "en": "",
                "fr": "",
            },

            16400: {
                "la": "In Vigilia Assumptionis BMV",
                "en": "",
                "fr": "",
            },

            16500: {
                "la": "In Assumptione BMV",
                "en": "Assumption of the BVM",
                "fr": "",
            },

            16501: {
                "la": "Oct Assumptionis BMV",
                "en": "of the Assumption of the BVM",
                "fr": "",
            },

            16600: {
                "la": "S Joachim C, Patris BMV",
                "en": "",
                "fr": "",
            },

            16700: {
                "la": "S Hyacinthi C",
                "en": "",
                "fr": "",
            },

            16800: {
                "la": "S Agapiti M",
                "en": "",
                "fr": "",
            },

            16900: {
                "la": "S Joannis Eudes C",
                "en": "",
                "fr": "",
            },

            17000: {
                "la": "S Bernardi AbbD",
                "en": "",
                "fr": "",
            },

            17100: {
                "la": "S Joannæ Franciscæ Fremiot de Chantal V",
                "en": "",
                "fr": "",
            },

            17200: {
                "la": "In Festo Immaculati Cordis BMV",
                "en": "",
                "fr": "",
            },

            17300: {
                "la": "S Philippi Benitii C",
                "en": "",
                "fr": "",
            },

            17400: {
                "la": "S Bartholomæi Ap",
                "en": "",
                "fr": "",
            },

            17500: {
                "la": "S Ludovici RC",
                "en": "",
                "fr": "",
            },

            17600: {
                "la": "S Zephrini PM",
                "en": "",
                "fr": "",
            },

            17700: {
                "la": "S Josephi Calasanctii C",
                "en": "",
                "fr": "",
            },

            17800: {
                "la": "S Augustini ECD",
                "en": "",
                "fr": "",
            },

            17900: {
                "la": "In Decollatione S Joannis Baptistæ",
                "en": "",
                "fr": "",
            },

            18000: {
                "la": "S Rosæ a S Maria Limanæ V",
                "en": "",
                "fr": "",
            },

            18100: {
                "la": "S Raymundi Nonnati C",
                "en": "",
                "fr": "",
            },

            18200: {
                "la": "S Ægidii Abb",
                "en": "",
                "fr": "",
            },

            18300: {
                "la": "S Stephani R C",
                "en": "",
                "fr": "",
            },

            18400: {
                "la": "S Pii X PC",
                "en": "",
                "fr": "",
            },

            18500: {
                "la": "S Laurentii Justiniani EC",
                "en": "",
                "fr": "",
            },

            18600: {
                "la": "In Nativitate BMV",
                "en": "",
                "fr": "",
            },

            18700: {
                "la": "S Gorgonii M",
                "en": "",
                "fr": "",
            },

            18800: {
                "la": "S Nicolai de Tolentino C",
                "en": "",
                "fr": "",
            },

            18900: {
                "la": "Ss Proti et Hycinthi Mm",
                "en": "",
                "fr": "",
            },

            19000: {
                "la": "Ssmi Nominis BMV",
                "en": "",
                "fr": "",
            },

            19100: {
                "la": "In Exaltatione S Crucis",
                "en": "",
                "fr": "",
            },

            19200: {
                "la": "Septem Dolorum BMV",
                "en": "",
                "fr": "",
            },

            19300: {
                "la": "Ss Cornelii P et Cypriani E Mm",
                "en": "",
                "fr": "",
            },

            19400: {
                "la": "In Impressione Ss Stigmatum S Francisci C",
                "en": "",
                "fr": "",
            },

            19500: {
                "la": "S Josephi a Cupertino C",
                "en": "",
                "fr": "",
            },

            19600: {
                "la": "Ss Januarii E et Sociorum Mm",
                "en": "",
                "fr": "",
            },

            19700: {
                "la": "Ss Eustachii et Sociorum Mm",
                "en": "",
                "fr": "",
            },

            19800: {
                "la": "S Matthæi ApEv",
                "en": "",
                "fr": "",
            },

            19900: {
                "la": "S Thomæ de Villanova EC",
                "en": "",
                "fr": "",
            },

            20000: {
                "la": "S Lini PM",
                "en": "",
                "fr": "",
            },

            20100: {
                "la": "BMV de Merdece",
                "en": "",
                "fr": "",
            },

            20200: {
                "la": "Ss Cypriani et Justinæ Mm",
                "en": "",
                "fr": "",
            },

            20300: {
                "la": "Ss Cosmæ et Damiani Mm",
                "en": "",
                "fr": "",
            },

            20400: {
                "la": "S Wenceslai Ducis M",
                "en": "",
                "fr": "",
            },

            20500: {
                "la": "In Dedicatione S Michælis Arch",
                "en": "",
                "fr": "",
            },

            20600: {
                "la": "S Hieronymi SCD",
                "en": "",
                "fr": "",
            },

            20700: {
                "la": "S Remigii EC",
                "en": "",
                "fr": "",
            },

            20800: {
                "la": "Ss Angelorum Custodum",
                "en": "",
                "fr": "",
            },

            20900: {
                "la": "S Teresiæ a Jesu Infante V",
                "en": "",
                "fr": "",
            },

            21000: {
                "la": "S Francisci C",
                "en": "",
                "fr": "",
            },

            21100: {
                "la": "Ss Placidi et Sociorum Mm",
                "en": "",
                "fr": "",
            },

            21200: {
                "la": "S Brunonis C",
                "en": "",
                "fr": "",
            },

            21300: {
                "la": "Sacratissimi Rosarii BMV",
                "en": "",
                "fr": "",
            },

            21400: {
                "la": "S Birgittæ V",
                "en": "",
                "fr": "",
            },

            21500: {
                "la": "S Joannis Leonardi C",
                "en": "",
                "fr": "",
            },

            21600: {
                "la": "S Francisci Borgiæ C",
                "en": "",
                "fr": "",
            },

            21700: {
                "la": "In Maternitate BMV",
                "en": "",
                "fr": "",
            },

            21800: {
                "la": "S Eduardi R C",
                "en": "",
                "fr": "",
            },

            21900: {
                "la": "S Callisti I PM",
                "en": "",
                "fr": "",
            },

            22000: {
                "la": "S Teresiæ V",
                "en": "",
                "fr": "",
            },

            22100: {
                "la": "S Hedwigis V",
                "en": "",
                "fr": "",
            },

            22200: {
                "la": "S Margaritæ Mariæ Alacoque V",
                "en": "",
                "fr": "",
            },

            22300: {
                "la": "S Lucæ Ev",
                "en": "",
                "fr": "",
            },

            22400: {
                "la": "S Petri de Alacantara C",
                "en": "",
                "fr": "",
            },

            22500: {
                "la": "S Joannis Cantii C",
                "en": "",
                "fr": "",
            },

            22600: {
                "la": "S Hilarionis Abb",
                "en": "",
                "fr": "",
            },

            22700: {
                "la": "S Raphaelis Arch",
                "en": "",
                "fr": "",
            },

            22800: {
                "la": "Ss Chrysanthi et Dariæ Mm",
                "en": "",
                "fr": "",
            },

            22900: {
                "la": "S Evaristi PM",
                "en": "",
                "fr": "",
            },

            23000: {
                "la": "In Vigilia Ss Simonis et Judæ App",
                "en": "",
                "fr": "",
            },

            23100: {
                "la": "Ss Simonis et Judæ App",
                "en": "",
                "fr": "",
            },

            23200: {
                "la": "In Vigilia Omnium Sanctorum",
                "en": "",
                "fr": "",
            },

            23300: {
                "la": "In Festo Omnium Sanctorum",
                "en": "Feast of All Saints",
                "fr": "",
            },

            23301: {
                "la": "Oct Omnium Sanctorum",
                "en": "of All Saints",
                "fr": "",
            },

            23400: {
                "la": "In Commemoratione Omnium Fidelium Defunctorum",
                "en": "",
                "fr": "",
            },

            23500: {
                "la": "S Caroli EC",
                "en": "",
                "fr": "",
            },

            23700: {
                "la": "In Dedicatione Archibasilicæ Ssmi Salvatoris",
                "en": "",
                "fr": "",
            },

            23800: {
                "la": "S Andreæ Avellini C",
                "en": "",
                "fr": "",
            },

            23900: {
                "la": "S Martini EC",
                "en": "",
                "fr": "",
            },

            24000: {
                "la": "S Martini I PM",
                "en": "",
                "fr": "",
            },

            24100: {
                "la": "S Didaci C",
                "en": "",
                "fr": "",
            },

            24200: {
                "la": "S Josaphat EM",
                "en": "",
                "fr": "",
            },

            24300: {
                "la": "S Alberti Magni ECD",
                "en": "",
                "fr": "",
            },

            24400: {
                "la": "S Gertrudis V",
                "en": "",
                "fr": "",
            },

            24500: {
                "la": "S Gregorii Thaumaturgi EC",
                "en": "",
                "fr": "",
            },

            24600: {
                "la": "In Dedicatione Basilicarum Ss Petri et Pauli App",
                "en": "",
                "fr": "",
            },

            24700: {
                "la": "S Elisabeth V",
                "en": "",
                "fr": "",
            },

            24800: {
                "la": "S Felicis de Valois C",
                "en": "",
                "fr": "",
            },

            24900: {
                "la": "In Præsentatione BMV",
                "en": "",
                "fr": "",
            },

            25000: {
                "la": "S Cæciliæ VM",
                "en": "",
                "fr": "",
            },

            25100: {
                "la": "S Clementis I PM",
                "en": "",
                "fr": "",
            },

            25200: {
                "la": "S Joannis a Cruce CD",
                "en": "",
                "fr": "",
            },

            25300: {
                "la": "S Catharinæ VM",
                "en": "",
                "fr": "",
            },

            25400: {
                "la": "S Sylvestri Abb",
                "en": "",
                "fr": "",
            },

            25500: {
                "la": "In Vigilia S Andreæ Ap",
                "en": "",
                "fr": "",
            },

            25600: {
                "la": "S Andreæ Ap",
                "en": "",
                "fr": "",
            },

            25800: {
                "la": "S Bibianæ VM",
                "en": "",
                "fr": "",
            },

            25900: {
                "la": "S Francisci Xaverii C",
                "en": "",
                "fr": "",
            },

            26000: {
                "la": "S Petri Chrysologi ECD",
                "en": "",
                "fr": "",
            },

            26100: {
                "la": "S Sabbæ Abb",
                "en": "",
                "fr": "",
            },

            26200: {
                "la": "S Nicolai EC",
                "en": "",
                "fr": "",
            },

            26300: {
                "la": "S Ambrosii ECD",
                "en": "",
                "fr": "",
            },

            26400: {
                "la": "In Conceptione Immaculata BMV",
                "en": "Feast of the Immaculate Conception",
                "fr": "",
            },

            26401: {
                "la": "Oct Concept Immac BMV",
                "en": "of the Immaculate Conception",
                "fr": "",
            },

            26600: {
                "la": "S Melchidi PM",
                "en": "",
                "fr": "",
            },

            26700: {
                "la": "S Damasi I PC",
                "en": "",
                "fr": "",
            },

            26900: {
                "la": "S Luciæ VM",
                "en": "",
                "fr": "",
            },

            27000: {
                "la": "S Eusebii EM",
                "en": "",
                "fr": "",
            },

            27100: {
                "la": "In Vigilia S Thomæ Ap",
                "en": "",
                "fr": "",
            },

            27200: {
                "la": "S Thomæ Ap",
                "en": "",
                "fr": "",
            },

            27300: {
                "la": "In Vigilia S Matthiæ",
                "en": "Vigil of St. Matthew, Ap",
                "fr": "",
            },

            27400: {
                "la": "S Felicis SM",
                "en": "",
                "fr": "",
            },

            27500: {
                "la": "S Mauri Abb",
                "en": "",
                "fr": "",
            },

            27600: {
                "la": "S Pauli Apostoli",
                "en": "",
                "fr": "",
            },

            27700: {
                "la": "S Priscæ VM",
                "en": "",
                "fr": "",
            },

            27800: {
                "la": "S Canuti RM",
                "en": "",
                "fr": "",
            },

            27900: {
                "la": "S Emerentianæ VM",
                "en": "",
                "fr": "",
            },

            28000: {
                "la": "S Petri Apostoli",
                "en": "",
                "fr": "",
            },

            28100: {
                "la": "S Agnetis VM secundo",
                "en": "",
                "fr": "",
            },

            28200: {
                "la": "S Dorotheæ VM",
                "en": "",
                "fr": "",
            },

            28300: {
                "la": "S Apollonia VM",
                "en": "",
                "fr": "",
            },

            28400: {
                "la": "S Lucii I PM",
                "en": "",
                "fr": "",
            },

            28500: {
                "la": "Ss Tiburtii, Valeriani et Maximi Mm",
                "en": "",
                "fr": "",
            },

            28600: {
                "la": "S Vitali M",
                "en": "",
                "fr": "",
            },

            28700: {
                "la": "Ss Alexandro I Pp, Eventii et Theoduli Mm ac Juvenale Ep C",
                "en": "",
                "fr": "",
            },

            28800: {
                "la": "Ss Gordiani et Epimachi Mm",
                "en": "",
                "fr": "",
            },

            28900: {
                "la": "S Pudentianæ V",
                "en": "",
                "fr": "",
            },

            29000: {
                "la": "S Urbani I PM",
                "en": "St. Urban I, PM",
                "fr": "",
            },

            29100: {
                "la": "S Eleutherii PM",
                "en": "",
                "fr": "",
            },

            29200: {
                "la": "S Joannis I PM",
                "en": "St. John I, PM",
                "fr": "",
            },

            29300: {
                "la": "S Petronillæ V",
                "en": "",
                "fr": "",
            },

            29400: {
                "la": "Ss Basilidi, Cyrini, Nabori atq Nazarii Mm",
                "en": "",
                "fr": "",
            },

            29500: {
                "la": "Ss Marci et Marcelliani Mm",
                "en": "",
                "fr": "",
            },

            29600: {
                "la": "In Vigilia Ss Petri et Pauli App",
                "en": "",
                "fr": "",
            },

            29700: {
                "la": "S Petri Ap",
                "en": "St. Peter Ap",
                "fr": "",
            },

            29800: {
                "la": "Ss Processi et Martiniani Mm",
                "en": "",
                "fr": "",
            },

            29900: {
                "la": "Ss Noboris et Felicis Mm",
                "en": "",
                "fr": "",
            },

            30000: {
                "la": "Ss Symphorosæ et Septem Filiis ejus Mm",
                "en": "",
                "fr": "",
            },

            30100: {
                "la": "S Margaritæ VM",
                "en": "",
                "fr": "",
            },

            30200: {
                "la": "S Liborii EC",
                "en": "",
                "fr": "",
            },

            30300: {
                "la": "S Christinæ VM",
                "en": "St. Christina VM",
                "fr": "",
            },

            30400: {
                "la": "S Christophori M",
                "en": "St. Christopher M",
                "fr": "",
            },

            30500: {
                "la": "Ss Felicis II P, Simplicis, Faustinis atq Beatricae Mm",
                "en": "",
                "fr": "",
            },

            30600: {
                "la": "S Pauli Ap",
                "en": "",
                "fr": "",
            },

            30700: {
                "la": "S Stephani PM",
                "en": "",
                "fr": "",
            },

            30800: {
                "la": "Ss Xysti P, Felicissimi atq Agapiti Mm",
                "en": "",
                "fr": "",
            },

            30900: {
                "la": "S Donati EM",
                "en": "",
                "fr": "",
            },

            31000: {
                "la": "Vigilia S Laurentii M",
                "en": "",
                "fr": "",
            },

            31100: {
                "la": "S Eusebii C",
                "en": "",
                "fr": "",
            },

            31200: {
                "la": "Octava S Laurentii M",
                "en": "",
                "fr": "",
            },

            31300: {
                "la": "Ss Timothei, Hippolyti atq Symphoriani Mm",
                "en": "",
                "fr": "",
            },

            31400: {
                "la": "In Vigilia S Bartholomæi Ap",
                "en": "",
                "fr": "",
            },

            31500: {
                "la": "S Hermetis M",
                "en": "",
                "fr": "",
            },

            31600: {
                "la": "S Sabinae M",
                "en": "",
                "fr": "",
            },

            31700: {
                "la": "Ss Felicis et Adaucti Mm",
                "en": "",
                "fr": "",
            },

            31800: {
                "la": "Ss Duodecim Fratribus",
                "en": "",
                "fr": "",
            },

            31900: {
                "la": "S Hadriani M",
                "en": "",
                "fr": "",
            },

            32000: {
                "la": "S Nicomedis M",
                "en": "",
                "fr": "",
            },

            32100: {
                "la": "Ss Euphemiae V, Luciae atq Geminiani Mm",
                "en": "",
                "fr": "",
            },

            32200: {
                "la": "In Vigilia S Matthæi ApEv",
                "en": "",
                "fr": "",
            },

            32300: {
                "la": "Ss Mauritii et Sociorum Mm",
                "en": "",
                "fr": "",
            },

            32400: {
                "la": "S Theclae VM",
                "en": "",
                "fr": "",
            },

            32500: {
                "la": "S Marci PC",
                "en": "",
                "fr": "",
            },

            32600: {
                "la": "Ss Dionysii E, Rustici atq Eleutherii Mm",
                "en": "",
                "fr": "",
            },

            32700: {
                "la": "Ss Ursulae et Sociarum VM",
                "en": "",
                "fr": "",
            },

            32800: {
                "la": "Octavae Omnium Sanctorum",
                "en": "",
                "fr": "",
            },

            32900: {
                "la": "S Theodori M",
                "en": "",
                "fr": "",
            },

            33000: {
                "la": "Ss Tryphonis, Respicii atq Nymphae V Mm",
                "en": "",
                "fr": "",
            },

            33100: {
                "la": "S Mennae M",
                "en": "",
                "fr": "",
            },

            33200: {
                "la": "S Pontiani PM",
                "en": "",
                "fr": "",
            },

            33300: {
                "la": "S Felicitatis M",
                "en": "",
                "fr": "",
            },

            33400: {
                "la": "S Chrysogoni M",
                "en": "",
                "fr": "",
            },

            33500: {
                "la": "S Petri Alexandrini EM",
                "en": "",
                "fr": "",
            },

            33600: {
                "la": "S Saturnini M",
                "en": "",
                "fr": "",
            },

            33700: {
                "la": "S Barbarae VM",
                "en": "",
                "fr": "",
            },

            33800: {
                "la": "In Vigilia Conceptionis Immaculatæ BMV",
                "en": "",
                "fr": "",
            },


            34500: {
                "la": "Ss Naboris et Felicis Mm",
                "en": "",
                "fr": "",
            },

            34700: {
                "la": "Ss Machabæis Mm",
                "en": "",
                "fr": "",
            },

            34800: {
                "la": "S Romani M",
                "en": "",
                "fr": "",
            },

            34900: {
                "la": "Ss Sergii, Bacchi, Marcelli atq Apuleji Mm",
                "en": "",
                "fr": "",
            },



            ##########################
            #     COMMEMORATIONS     #
            ##########################

            99901: {
                # first week of advent
                "la": "Excita, quæsumus",
                "en": "",
                "fr": "",
            },

            99902: {
                # second week of advent
                "la": "Excita, Domine",
                "en": "",
                "fr": "",
            },

            99903: {
                # third week of advent
                "la": "Aurem tuam",
                "en": "",
                "fr": "",
            },

            99904: {
                # fourth week of advent
                "la": "Excita, quæsumus",
                "en": "",
                "fr": "",
            },

            99905: {
                # De Spiritu Sancto
                "la": "Deus, qui corda",
                "en": "",
                "fr": "",
            },

            99906: {
                # BVM in advent
                "la": "de BMV (Deus, qui de beátæ)",
                "en": "",
                "fr": "",
            },

            99907: {
                # BVM from Dec 29 - Feb 2 inclusive
                "la": "de BMV (Deus, qui salútis)",
                "en": "",
                "fr": "",
            },

            99908: {
                # BVM for the rest of the year
                "la": "Concéde",
                "en": "",
                "fr": "",
            },

            99909: {
                # Against the Persecutors
                "la": "Ecclésiæ",
                "en": "",
                "fr": "",
            },

            99910: {
                # For the Pope
                "la": "Deus, ómnium",
                "en": "",
                "fr": "",
            },

            99911: {
                # Suffrage
                "la": "A cunctis",
                "en": "",
                "fr": "",
            },

            99912: {
                # All the faithful departed
                "la": "Fidélium",
                "en": "",
                "fr": "",
            },

            99913: {
                # priest's choice
                "la": "ad lib",
                "en": "",
                "fr": "",
            },

            99914: {
                # of the feria
                "la": "de feria",
                "en": "",
                "fr": "",
            },

            99915: {
                # for the living and the dead
                "la": "Omnípotens",
                "en": "",
                "fr": "",
            },

            ##########################
            #    TEMPORAL "FEASTS"   #
            ##########################

            100000: {
                "la": "S Telesphori PM",
                "en": "",
                "fr": "",
            },

            "lady_saturday": {
                "la": "De Sancta Maria in Sabbato",
                "en": "Our Lady's Saturday",
                "fr": "",
            },

            "Circumcision": {
                "la": "Circumcisio DNJC et Oct. Nativitatis",
                "en": "Circumcision",
                "fr": "",
            },

            "8_Stephen": {
                "la": "Octava S Stephani Protomartyris",
                "en": "Octave day of St. Stephen, Protomartyr",
                "fr": "",
            },

            "8_John": {
                "la": "Octava S Joannis Ap Ev",
                "en": "Octave day of St. John, ApEv",
                "fr": "",
            },

            "8_Innocents": {
                "la": "Octava Ss Innocentium Mm.",
                "en": "Octave day of the Holy Innocents, Mm",
                "fr": "",
            },

            "SNameJesus": {
                "la": "Ssmi Nominis Jesu",
                "en": "Feast of the Holy Name",
                "fr": "",
            },

            "SNameJesu_8_Ste": {
                "la": "Ssmi Nominis Jesu",
                "en": "",
                "fr": "",
            },

            "V_Epiphany": {
                "la": "Vigilia Epiphaniæ",
                "en": "Vigil of the Epiphany",
                "fr": "",
            },

            "Epiphany": {
                "la": "Epiphania DNJC",
                "en": "The Epiphany",
                "fr": "",
            },

            "8_Epiphany": {
                "la": "Octava Epiphaniæ",
                "en": "Octave day of the Epiphany",
                "fr": "",
            },

            "D_Epiphany": {
                "la": "In Octava Epiphaniæ",
                "en": "Sunday within the Octave of the Epiphany",
                "fr": "",
            },

            "HolyFamily": {
                "la": "S Familiæ Jesu, Mariæ, Joseph",
                "en": "Feast of the Holy Family",
                "fr": "",
            },
            "D_HolyFamily": {
                "la": "S Familiæ Jesu, Mariæ, Joseph; Dominica I infra Oct. Epiphaniæ",
                "en": "",
                "fr": "",
            },
            "de_AshWed": {
                "la": "Dies Cinerum",
                "en": "Ash Wednesday",
                "fr": "",
            },
            "AshWed_f5": {
                "la": "Feria V post Diem Cinerum",
                "en": "Thursday after Ash Wednesday",
                "fr": "",
            },
            "AshWed_f6": {
                "la": "Feria VI post Diem Cinerum",
                "en": "Friday after Ash Wednesday",
                "fr": "",
            },
            "AshWed_fs": {
                "la": "Sabbatum post Diem Cinerum",
                "en": "Saturday after Ash Wednesday",
                "fr": "",
            },
            "D_Lent_1": {
                "la": "Dominica I in Quadragesima",
                "en": "First Sunday of Lent",
                "fr": "",
            },
            "Ember_Lent_4": {
                "la": "Feria IV Quatuor Temporum Quadragesimæ",
                "en": "Ember Wednesday in Lent",
                "fr": "",
            },
            "Ember_Lent_6": {
                "la": "Feria VI Quatuor Temporum Quadragesimæ",
                "en": "Ember Friday in Lent",
                "fr": "",
            },
            "Ember_Lent_s": {
                "la": "Sabbatum Quatuor Temporum Quadragesimæ",
                "en": "Ember Saturday in Lent",
                "fr": "",
            },

            "SevenSorrows": {
                "la": "Septem Dolorum BMV",
                "en": "Feast of the Seven Sorrows of the BVM",
                "fr": "",
            },

            "de_Palm_f2": {
                "la": "Feria II Majoris Hebd",
                "en": "Monday in Holy Week",
                "fr": "",
            },

            "de_Palm_f3": {
                "la": "Feria III Majoris Hebd",
                "en": "Tuesday in Holy Week",
                "fr": "",
            },

            "de_Palm_f4": {
                "la": "Feria IV Majoris Hebd",
                "en": "Spy Wednesday",
                "fr": "",
            },

            "de_Palm_f5": {
                "la": "Feria V in Cœna Domini",
                "en": "Maundy Thursday",
                "fr": "",
            },

            "de_Palm_f6": {
                "la": "Feria VI in Parasceve",
                "en": "Good Friday",
                "fr": "",
            },

            "de_Palm_fs": {
                "la": "Sabbatum Sanctum",
                "en": "Holy Saturday",
                "fr": "",
            },

            "Easter": {
                "la": "Dominica Resurrectionis",
                "en": "",
                "fr": "",
            },

            "8Easter_f2": {
                "la": "Feria II infra Oct. Paschæ",
                "en": "",
                "fr": "",
            },

            "8Easter_f3": {
                "la": "Feria III infra Oct. Paschæ",
                "en": "",
                "fr": "",
            },

            "8Easter_f4": {
                "la": "Feria IV infra Oct. Paschæ",
                "en": "",
                "fr": "",
            },

            "8Easter_f5": {
                "la": "Feria V infra Oct. Paschæ",
                "en": "",
                "fr": "",
            },

            "8Easter_f6": {
                "la": "Feria VI infra Oct. Paschæ",
                "en": "",
                "fr": "",
            },

            "WhitSaturday": {
                "la": "Sabbatum in Albis",
                "en": "",
                "fr": "",
            },

            # C. et Ecclesiæ Universalis Patroni",
            "StJoseph": {
                "la": "Solemnitas S Joseph, Sponsi BMV",
                "en": "Solemnity of St. Joseph, Spouse of the BVM",
                "fr": "",
            },

            "8_StJoseph": {
                "la": "Octava Solemnitatis S Joseph",
                "en": "",
                "fr": "",
            },

            "Rogation_1": {
                "la": "Feria II in Rogationibus",
                "en": "",
                "fr": "",
            },

            "Rogation_2": {
                "la": "Feria III in Rogationibus",
                "en": "",
                "fr": "",
            },

            "Rogation_3": {
                "la": "Feria IV in Rogationibus in Vigilia Ascensionis ",
                "en": "",
                "fr": "",
            },

            "Ascension": {
                "la": "Ascensio DNJC",
                "en": "",
                "fr": "",
            },

            "8_Ascension": {
                "la": "Oct. Ascensionis DNJC",
                "en": "",
                "fr": "",
            },

            # TODO: this day has special rules
            "p_Ascension_f6": {
                "la": "Oct. Ascensionis DNJC",
                "en": "",
                "fr": "",
            },

            "D_Ascension": {
                "la": "Dominica infra Oct. Ascensionis",
                "en": "",
                "fr": "",
            },

            "S_8_Ascension": {
                "la": "Sabbatum infra Oct. Ascensionis",
                "en": "",
                "fr": "",
            },

            "WhitSunday": {
                "la": "Dominica in Albis",
                "en": "",
                "fr": "",
            },

            "V_Pentecost": {
                "la": "Sabbatum Vigilia Pentecostes",
                "en": "",
                "fr": "",
            },

            "Pentecost": {
                "la": "Dominica Pentecostes",
                "en": "",
                "fr": "",
            },

            "8Pent_f2": {
                "la": "Feria II infra Oct. Pentecostes",
                "en": "",
                "fr": "",
            },

            "8Pent_f3": {
                "la": "Feria III infra Oct. Pentecostes",
                "en": "",
                "fr": "",
            },

            "8Pent_f5": {
                "la": "Feria V infra Oct. Pentecostes",
                "en": "",
                "fr": "",
            },

            "Ember_Pent_4": {
                "la": "Feria IV Quatuor Temporum infra Oct. Pentecostes",
                "en": "",
                "fr": "",
            },

            "Ember_Pent_6": {
                "la": "Feria VI Quatuor Temporum infra Oct. Pentecostes",
                "en": "",
                "fr": "",
            },

            "Ember_Pent_s": {
                "la": "Sabbatum Quatuor Temporum infra Oct. Pentecostes",
                "en": "",
                "fr": "",
            },

            "Trinity": {
                "la": "Festum Sanctissimæ Trinitatis",
                "en": "",
                "fr": "",
            },

            "D_Pent_2": {
                "la": "Dominica infra Oct. Ssmi Corporis Christi", #Christi (Dominica II post Pentecosten)",
                "en": "",
                "fr": "",
            },

            "D_Pent_3": {
                "la": "Dominica infra Oct. Ssmi Cordis DNJC",  # (Dominica III post Pentecosten)",
                "en": "",
                "fr": "",
            },

            "CorpusChristi": {
                "la": "Sanctissimi Corporis Christi",
                "en": "",
                "fr": "",
            },

            "8_CorpusChristi": {
                "la": "Octava Ssmi Corporis Christi",
                "en": "",
                "fr": "",
            },

            "SacredHeart": {
                "la": "Sacratissimi Cordis Jesu",
                "en": "",
                "fr": "",
            },

            "8_SacredHeart": {
                "la": "Octava Sacratissimi Cordis Jesu",
                "en": "",
                "fr": "",
            },

            "Ember_Sept_4": {
                "la": "Feria IV Quatuor Temporum Septembris",
                "en": "",
                "fr": "",
            },

            "Ember_Sept_6": {
                "la": "Feria VI Quatuor Temporum Septembris",
                "en": "",
                "fr": "",
            },

            "Ember_Sept_s": {
                "la": "Sabbatum Quatuor Temporum Septembris",
                "en": "",
                "fr": "",
            },

            "ChristKing": {
                "la": "In Festo DNJC Regis",
                "en": "",
                "fr": "",
            },

            "Ember_Advent_4": {
                "la": "Feria IV Quatuor Temporum in Adventus",
                "en": "",
                "fr": "",
            },

            "Ember_Advent_6": {
                "la": "Feria VI Quatuor Temporum in Adventus",
                "en": "",
                "fr": "",
            },

            "Ember_Advent_s": {
                "la": "Sabbatum Quatuor Temporum in Adventus",
                "en": "",
                "fr": "",
            },

            "V_Christmas": {
                "la": "Vigilia Nativitas DNJC",
                "en": "",
                "fr": "",
            },

            "DV_Christmas": {
                "la": "Vigilia Nativitas DNJC",
                "en": "",
                "fr": "",
            },

            "Christmas": {
                "la": "Nativitas DNJC",
                "en": "",
                "fr": "",
            },

            "D_Christmas_r": {
                "la": "Dominica Infra Octavam Nativitatis reposita",
                "en": "",
                "fr": "",
            },

            "D_Christmas": {
                "la": "Dominica Infra Octavam Nativitatis",
                "en": "",
                "fr": "",
            },

            "8_Chritmas_f6": {
                "la": "Feria VI infra Octavam Nativitatis",
                "en": "Firday within the Octave of the Nativity",
                "fr": "",
            },

            "StStephan": {
                "la": "S Stephani Protomartyris",
                "en": "",
                "fr": "",
            },

            "StJohn": {
                "la": "S Joannis Ap Ev",
                "en": "",
                "fr": "",
            },

            "StsInnocents": {
                "la": "Ss Innocentium Mm",
                "en": "",
                "fr": "",
            },

            "StThomas": {
                "la": "S Thomæ EM",
                "en": "",
                "fr": "",
            },

            "StSylvester": {
                "la": "S Silvestri I PC",
                "en": "",
                "fr": "",
            },

            "D_StThomas": {
                "la": "S Thomæ EM",
                "en": "",
                "fr": "",
            },

            "D_StSylvester": {
                "la": "S Silvestri I PC",
                "en": "",
                "fr": "",
            },

        }

        # TODO: to avoid excess computation, all of these have to take
        #       language as a parameter. Perhaps add a subclass?
        self.data = self.easy_data |\
            self.epiphany_time() |\
            self.epiphany_octave() |\
            self.septuagesima_time() |\
            self.lent_sundays() |\
            self.paschaltime() |\
            self.ascension_ferias() |\
            self.corpus_ferias() |\
            self.sacredheart_ferias() |\
            self.solemnity_st_joseph() |\
            self.pentecost_sundays() |\
            self.pentecost_epiphany_sundays() |\
            self.last_pentecost() |\
            self.advents() |\
            self.three_weeks_after_pentecost()

    def lent_sundays(self) -> dict:
        the_days = {}
        normal_lents = [f"D_Lent_{l+1}" for l in range(4)]
        later_lents = ["D_Passion_5", "D_Palm_6"]
        lents = [*normal_lents, *later_lents]
        for x, date in enumerate(lents):
            for feria in range(7):
                if feria == 0:
                    the_days |= {
                        date: {
                            "la": f"""Dominica {f'''infra Hebd {integer_to_roman(x+1)} in Quadragesima{' (Lætare)' if x+1 == 4 else ''}''' if x < 4 else '''Passione''' if x == 4 else '''Palmis''' }""",
                            "en": "",
                            "fr": "",
                        }
                    }
                else:
                    the_days |= {
                        f"de_{'Lent' if x < 4 else 'Passion'}_f{feria+1 if feria != 6 else 's'}": {
                            "la": "De ea",
                            "en": "Feria",
                            "fr": "",
                        }
                    }
        return the_days

    def ascension_ferias(self) -> dict:
        return {  # NOTE: there are duplicates, but does it matter?
            f"in_8_Ascension_{date}": {
                "la": f"De {integer_to_roman(date)} die infra Oct. Ascensionis",
                "en": "",
                "fr": "",
            } for date in range(1,8)
        }

    def corpus_ferias(self) -> dict:
        return {
            f"{date+1}_in_8_CorpusChristi": {
                "la": f"De {integer_to_roman(date+1)} die infra Oct. Ssmi Corporis Christi",
                "en": "",
                "fr": "",
            } for date in range(1,8)
        }

    def sacredheart_ferias(self) -> dict:
        return {
            f"{date+1}_in_8_SacredHeart": {
                "la": f"De {integer_to_roman(date+1)} die infra Oct. Sacratissimi Cordis Jesu",
                "en": "",
                "fr": "",
            } for date in range(1,8)
        }

    def pentecost_sundays(self) -> dict:
        # TODO: add the first 4 Sundays after Pentecost (excluding Trinity)
        pentecost_season = {}
        for date in range(4, 29):
            pentecost_season |= {
                f"D_Pent_{date}": {
                    "la": f"Dominica {integer_to_roman(date)} post Pentecosten",
                    "en": "",
                    "fr": "",
                }
            }
            for feria in range(6):
                pentecost_season |= {
                    f"de_Pent_{date}_f{feria+2 if feria != 5 else 's'}": {
                        "la": "De ea",
                        "en": "",
                        "fr": "",
                    }
                }
        return pentecost_season

# @functools.lru_cache()
    def pentecost_epiphany_sundays(self) -> dict:
        # WARN: This is really rough and might not be too efficient, but
        # it works for now.
        epiphany_pents = {}
        for pent in range(22, 29):
            for epiph in range(1, 7): # start at 1 needed for the year 2156
                epiphany_pents |= {
                    f"D_Epiph_{epiph}_{pent}": {
                        "la": f"Dominica {integer_to_roman(pent)} post Pentecosten, {integer_to_roman(epiph)} Epiphania",
                        "en": f"{nth(pent)} Sunday after Pentecost, {nth(epiph)} after Epiphany",
                    }
                }
                # OPTIM: maybe we can grab this only when we need it.
                for feria in range(6):
                    epiphany_pents |= {
                        f"de_Epiph_{epiph}_{pent}_f{feria+2 if feria != 5 else 's'}": {
                            "la": "De ea",
                            "en": "Feria",
                            "fr": "",
                        }
                    }
        return epiphany_pents

    def last_pentecost(self) -> dict:
        last_pents = {}
        for pent in range(23, 29):
            last_pents |= {
                f"D_UltPent_{pent}": {
                    "la": f"Dominica {integer_to_roman(pent)} et ultima post Pentecosten",
                    "en": "",
                    "fr": "",
                }
            }
            for feria in range(6):
                last_pents |= {
                    f"de_UltPent_{pent}_f{feria+2 if feria != 5 else 's'}": {
                        "la": "De ea",
                        "en": "",
                        "fr": "",
                    }
                }
        return last_pents

    def advents(self) -> dict:
        advent_season = {}
        advent_sundays = [
            "Ad te levavi",
            "Populus Sion",
            "Gaudete",
            "Rorate cæli",
        ]
        for x, introit in enumerate(advent_sundays):
            advent_season |= {
                # TODO: verify that 2-4 advents are minor sundays
                f"D_Advent_{x+1}": {
                    "la": f"Dominica {integer_to_roman(x+1)} Adventus",
                    "en": "",
                    "fr": "",
                }
            }
            for feria in range(6):
                advent_season |= {
                    f"de_Advent_{x+1}_f{feria+2 if feria != 5 else 's'}": {
                        "la": "De ea",
                        "en": "",
                        "fr": "",
                    }
                }
        return advent_season

    def three_weeks_after_pentecost(self) -> dict:
        # NOTE: this is overkill, but it works, and is probably faster than a fix
        weeks = {}
        introits = [
            "Benedicta sit",
            "Factus est",
            "Respice in me",
        ]
        for x, introit in enumerate(introits):
            for feria in range(6):
                weeks |= {
                    f"de_Pent_{x+1}_f{feria+2 if feria != 5 else 's'}": {
                        "la": "De ea",
                        "en": "",
                        "fr": "",
                    },
                }
        return weeks

    def paschaltime(self) -> dict:
        paschaltime = {}
        for week in range(6):
            paschaltime |= {
                f"D_Easter_{week+1}": {
                    "la": f"Dominica {integer_to_roman(week+1)} post Resurrectionis",
                    "en": "",
                    "fr": "",
                }
            }
            for feria in range(6):
                pass
                paschaltime |= {
                    f"de_Easter_{week+1}_f{feria+2 if feria != 5 else 's'}": {
                        "la": "De ea",
                        "en": "",
                        "fr": "",
                    }
                }
        return paschaltime

    def solemnity_st_joseph(self) -> dict:
        solemnity_ferias = {}
        for feria in range(6):
            solemnity_ferias |= {
                f"{feria+2}_in_8_StJoseph": {
                    "la": f"De {integer_to_roman(feria+2)} die infra Solemnitas S Joseph",
                    "en": "",
                    "fr": "",
                }
            }
        return solemnity_ferias

    def septuagesima_time(self) -> dict:
        septuagesima = {}
        for x, sunday in enumerate(["Septuagesima", "Sexagesima", "Quinquagesima"]):
            septuagesima |= {
                sunday: {
                    "la": f"Dominica in {sunday}",
                    "en": "",
                    "fr": "",
                }
            }
            for feria in range(6):
                septuagesima |= {
                    f"de_{sunday[:4]}_f{feria+2 if feria != 5 else 's'}": {
                        "la": "De ea",
                        "en": "",
                        "fr": "",
                    }
                }
        return septuagesima

    def epiphany_time(self) -> dict:
        epiphany = {}
        for sunday in range(6):
            epiphany |= {
                f"D_Epiph_{sunday+1}": {
                    "la": f"Dominica {integer_to_roman(sunday+1)} post Epiphaniam",
                    "en": "",
                    "fr": "",
                }
            }
            for feria in range(6):
                epiphany |= {
                    f"de_Epiph_{sunday+1}_{feria+2 if feria != 5 else 's'}": {
                        "la": "De ea",
                        "en": "Feria",
                        "fr": "",
                    }
                }
        return epiphany

    def epiphany_octave(self) -> dict:
        octave = {
            "8_Epiph_fs": {
                "la": "Sabbato infra Oct Epiphaniæ",
                "en": "Saturday within the Octave of the Epiphany",
                "fr": "",
            },
        }
        for feria in range(6):
            num = feria + 2
            octave |= {
                f"8_Epiph_f{feria+2}": {
                    "la": f"De {integer_to_roman(num)} die infra Oct. Epiphaniæ",
                    "en": f"{nth(num)} day within the Octave of the Epiphany",
                    "fr": f"{nth(num)}",
                }
        }
        return octave

    def translations(self) -> dict:
        return self.data

    def octave(self, lang: str, num: int, ref: int) -> str:
        """ Rather than doing this too dynamically, we
        have all of the days separated, to avoid as many grammar
        issues as possible """
        octave_days = {
            "la": [
                "De II die infra",
                "De III die infra",
                "De IV die infra",
                "De V die infra",
                "De VI die infra",
                "De VII die infra",
                "",
            ],
            "en": [
                "2nd day within the Octave",
                "3rd day within the Octave",
                "4th day within the Octave",
                "5th day within the Octave",
                "6th day within the Octave",
                "7th day within the Octave",
                "Octave day",
            ],
            "fr": [
                "2nd day within the Octave",
                "3rd day within the Octave",
                "4th day within the Octave",
                "5th day within the Octave",
                "6th day within the Octave",
                "7th day within the Octave",
                "Octave day",
            ],
        }

        return octave_days[lang][num-1] + " " + self.translations()[ref][lang]
