# CS3110_GroupProject1
An FA that has preset FAs and after asks for an user inputed FA

Input/Output Testing:
(1) An FA (M1) which recognizes the set of strings over {0,1} that ends with 0.
Test strings: , 100, 011, 10abc1, 0, 1, 0101011, 11010, 0001, 1110

(2) An FA (M2) which recognizes the set of strings over {0,1} that do not have two consecutive 1's.
Test strings: , 1, 000, 101, 111, 01001, 1011011, 1011000, 01010, 1010101110

(3) An FA (M3) which recognizes all identifiers that begin with a letter (both upper and lower) and followed by
any number of letters and digits.
Test strings: , HelloWorld, abc, 1st_Ex, Java, the_num, code, X3Y7, X=90, X*Y

(4) An FA (M4) which recognizes the set of all decimal unsigned integer numbers without leading zeros except
the number 0 (i.e. number 0 should be accepted while number 01 should be rejected.)
Test strings: 7, -7, 007, 3.14, 103, 24930000, 0, 01, 100, 0101
