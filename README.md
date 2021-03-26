# Calculate π

The goal of this repository is to present a few algorithms that allow you to calculate π with a high level of precision. 

In order to do this the [Python Decimal](https://docs.python.org/3/library/decimal.html) module is used. The module allows one to define the number decimal spaced used in the calculation. Obviously the greater the number of decimal spaces, the longer the calculation of by will take.

Due to the high level of precision required for the calculation of factorials and square roots, the [Math](https://docs.python.org/3/library/math.html) module is also used in most algorithms.

---
## Logic behind the calculation

All the presented algorithms are interactive processes, that increase the precision and the number of decimal spaces, the more loops the calculation is run. 

The algorithms have been setup in a away that the **while loop** ends once further interactions do not change the final number (for the number of decimal spaces selected).

---
## Algorithms used

* ### [Gregory-Leibniz](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80)
* ### [Ramanujan-Sato](https://en.wikipedia.org/wiki/Borwein%27s_algorithm#Class_number_2_(1989))
* ### [Chudnovsky](https://en.wikipedia.org/wiki/Chudnovsky_algorithm)
* ### [Bailey-Borwein-Plouffe](https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula#BBP_digit-extraction_algorithm_for_%CF%80)
* ### [Gauss-Legendre](https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm)

---

## To dos

* ~~Register the start time and the end time of the calculation, so that the total calculating time can be meassured~~
* ~~Save the final result of π in to a file, toghether with the number of interactions, start time and end time~~
* ~~Request the desiered level of precision (number of decimal spaces) right at the beggining -> done for Chudnovsky~~ 
