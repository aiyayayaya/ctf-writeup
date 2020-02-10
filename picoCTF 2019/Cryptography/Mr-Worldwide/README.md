# Mr-Worldwide

## Question
A musician left us a message. What's it mean?

## Solution
The given file:
```
picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}
```

As the title hints, the numbers look like lattitudes and longitudes. 
```
(35.028309, 135.753082)                     2QH3+86 Kyoto, Japan
(46.469391, 30.740883)                      FP9R+Q9 Odesa, Odessa Oblast, Ukraine
(39.758949, -84.191605)                     QR55+H9 Dayton, Ohio, USA
(41.015137, 28.979530)                      2X8H+3R European Side, İstanbul, Turkey
(24.466667, 54.366669)                      F988+MM Abu Dhabi - United Arab Emirates
(3.140853, 101.693207)                      4MRV+87 Kuala Lumpur, Federal Territory of Kuala Lumpur, Malaysia
(9.005401, 38.763611)                       2Q47+5C Addis Ababa, Ethiopia
(-3.989038, -79.203560)                     2Q6W+9H Loja, Ecuador
(52.377956, 4.897070)                       9VHW+5R Amsterdam, Netherlands
(41.085651, -73.858467)                     34PR+7J Sleepy Hollow, New York, USA
(57.790001, -152.407227)                    QHRV+24 Kodiak, Alaska, USA
(31.205753, 29.924526)                      6W4F+8R Alexandria, Egypt
```

After that, we try to look out for the geocode of the city names.
```
(35.028309, 135.753082)                     Kyoto, Japan
(46.469391, 30.740883)                      Odesa, Odessa Oblast, Ukraine, 65000
(39.758949, -84.191605)                     Dayton, OH 45402, United States
(41.015137, 28.979530)                      İstanbul, Turkey
(24.466667, 54.366669)                      Abu Dhabi - United Arab Emirates
(3.140853, 101.693207)                      Kuala Lumpur, Federal Territory of Kuala Lumpur, Malaysia
(9.005401, 38.763611)                       Addis Ababa, Ethiopia
(-3.989038, -79.203560)                     Loja, Ecuador
(52.377956, 4.897070)                       Amsterdam, Netherlands
(41.085651, -73.858467)                     Sleepy Hollow, NY 10591, United States
(57.790001, -152.407227)                    Kodiak, AK 99615, United States
(31.205753, 29.924526)                      Alexandria Governorate, Egypt
```

flag: `picoCTF{KODIAK_ALASKA}`