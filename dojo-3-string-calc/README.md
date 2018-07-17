String Calculator
First step
Create a function add they take a string and return a string like :

```
String add(String)
```

The method can take 0,1 or 2 numbers separated by comma and return their sum,
an empty string will return “0”
Example of inputs : “”, “1”, “1.1,2.2”
Many numbers
Allow the add method to handle an unknow number of arguments

New separator
Allow the add method to handle new lines as separator

1\n2,3 should return 6.
175.2,\n35 is invalid and return the message Number expected but '\n' found at position 6.