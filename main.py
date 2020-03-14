import sys
""" a simple python script that outputs whether there exists a one-to-one character mapping
from s1 to s2. input should be given throught console. 
Order of string matters, eg. s1="fbb" s2="ccd" will output false
"""
def main():
  #raise missing argument exception
  if len(sys.argv[1:]) < 2:
      raise Exception("missing "+str(3-len(sys.argv))+" arguments for this python script")
  #raise too many arguments exception
  elif len(sys.argv[1:])>2:
      raise Exception("too many arguments for this python script:expect 2")

  try:
    
    s1=sys.argv[1]
    s2=sys.argv[2]
    #this script assumes that if lengths of s1 and s2 are different,
    #then there is no one-to-one mapping from s1 to s2
    if len(s1) != len(s2):
      print("false")
      return
    char_mapping={}
    for c1, c2 in zip(s1,s2):
      if c1 not in char_mapping:
        char_mapping[c1]=c2
      else:
        if char_mapping[c1] != c2:
          print("false")
          return
    print("true")

 #handle other exception when reading the arguments
  except:
      e = sys.exc_info()[0]
      print (e)

if __name__ == "__main__":
  try:
    main()
  except Exception as ex: print(ex)