import re

class Roman:

 roman_dict = {
 "IIII": "IV",
 "IIIIII": "VI"
 }

 def add(self, A, B):
      if self.rank_string(A) > self.rank_string(B):
          result = A + B
      else:
          result = B + A 

      if result in self.roman_dict:
           result = self.roman_dict[result]
      elif result[0] == "I" and result[1] == "V":
           result = "VI"
      return result

 def rank_string(self,num):
     if re.match(num,r'I'):
         return 1
     elif re.match(num,r'V'):
         return 2     
