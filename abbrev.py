#!/bin/python3

# You can perform the following operations on the string, :
# 
# Capitalize zero or more of 's lowercase letters.  Delete all of the remaining
# lowercase letters in .  Given two strings,  and , determine if it's possible
# to make  equal to  as described. If so, print YES on a new line. Otherwise,
# print NO.
# 
# For example, given  and , in  we can convert  and delete  to match . If  and ,
# matching is not possible because letters may only be capitalized or discarded,
# not changed.
# 
# Function Description
# 
# Complete the function  in the editor below. It must return either  or .
# 
# abbreviation has the following parameter(s):
# 
# a: the string to modify b: the string to match Input Format
# 
# The first line contains a single integer , the number of queries.
# 
# Each of the next  pairs of lines is as follows: - The first line of each query
# contains a single string, .  - The second line of each query contains a single
# string, .
# 
# Constraints
# 
# String  consists only of uppercase and lowercase English letters,
# ascii[A-Za-z].  String  consists only of uppercase English letters,
# ascii[A-Z].  Output Format
# 
# For each query, print YES on a new line if it's possible to make string  equal
# to string . Otherwise, print NO.
# 
# Sample Input
# 
# 1 daBcd ABC Sample Output
# 
# YES Explanation
# 
# image
# 
# We have  daBcd and  ABC. We perform the following operation:
# 
# Capitalize the letters a and c in  so that  dABCd.  Delete all the remaining
# lowercase letters in  so that  ABC.  Because we were able to successfully
# convert  to , we print YES on a new line.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#
 
counter = 0

memo = dict()
possible = False

# Change first lowercased letter to an upper-case letter
def upperFirstLower(s):
 
  for i in range(0, len(s)):
    
    if s[i].islower():
      s[i] = s[i].upper()
      break
      
  return s
  
# Delete first lower-cased lettter
def delFirstLower(s):
  
  for i in range(0, len(s)):
 
    if s[i].islower():
      del s[i]
      break
 
  return s
  
def listToString(L):
  return "".join(L)

def _abbrev(frag, target):

    global counter
    global memo
    global possible

    counter += 1
    print("counter = ", counter)

    print("frag = ", frag)
    print("target = ", target)

    print("listToString(frag) = ", listToString(frag))
    print("listToString(target) = ", listToString(target))

    if possible:
      return True

    k = listToString(frag)
    if k in memo:
      return memo[k]
  
    if len(frag) < len(target):
      return False
    
    print("frag[len(target) = ", listToString(frag[len(target)+1:]))

    print('listToString(frag).startswith(listToString(target)) = ', listToString(frag).startswith(listToString(target)))

    # We found a match!
    if listToString(frag) == listToString(target):
      print("Found a memo match")
      memo[k] = True
      possible = True
      return True
    
    # If we start with a match, and the tail is all lower (deletable), it's a match
    elif listToString(frag).startswith(listToString(target)) and listToString(frag[len(target)+1:]).islower():
      print("Drop the tail")
      memo[k] = True
      possible = True
      return True
    
    # If the first letter's an upper and it doesn't match the first letter
    # in the target, then game over.
    elif frag[0].isupper() and (frag[0] != target[0]):
      memo[k] = False
      return False

    # If it's not a match, and it can't be modified (because it's all uppercase),
    # then game over.
    elif "".join(frag).isupper():
      memo[k] = False
      return False

    frag1 = frag.copy()
    frag2 = frag.copy()

    frag1 = upperFirstLower(frag1)
    frag2 = delFirstLower(frag2)
 
    print("frag1 = ", frag1)
    print("frag2 = ", frag2)
    
    # Deleted char recursion (go down the path of shorter strings first)
    r2 = _abbrev(frag2, target)
    k = "".join(frag2)
    memo[k] = r2

    # Uppercased char recursion
    r1 = _abbrev(frag1, target)
    k = "".join(frag1)
    memo[k] = r1

    # The or of frag1 and frag2
    k = "".join(frag)
    memo[k] = r1 or r2

    return r1 or r2

def abbreviation(a, b):
  
    global counter
    global memo
    global possible

    print("a = ", a)
    print("b = ", b)
 
    memo.clear()

    r = _abbrev(list(a), list(b))
    
    if r:
      print("YES")
      return "YES"
    else:
      print("NO")
      return "NO"

# Test case 8

print("starting test case 8\n")

# a =  "AfPZN"
# b =  "APZNC"
# abbreviation(a, b)
# exit()
# 
# a = "abaaA"
# b = "AA"
# abbreviation(a, b)
# exit()

# Expected output:
#   YES
#   YES
#   YES
#   YES
#   NO
#   YES
#   YES
#   NO
#   NO
#   YES

a = "OPZFFVQLADBQFBXLOSUMZZWQUKASCUVQZZVWfPIRTytlvpijddqegbwitkhhsbuehtnpndvcandzjzyepvlnkayfkwzegvbratvwezddjqxrxocqgcghuohlmsondvicocltqhvqfqjpctxfomjoukrheijhhndcbipiobvpbskemgykepokluwqhhejdaimvdvlegfyrrwckgojsbsxmsvhhrlnvcrxfaxinjzsjgvvrlcczqlkvgtftsvktvhtfpaklumhkovphilrappbvkarfhvwxxtrugypracozyqyvaqjityoiyemyavpbchaoagrvujocpueczsgcqdjvkjckxhmnaseshjgecusrxozuxgeieleewwskmiprlqnshvmcp"
b = "OPZFFVQLADBQFBXLOSUMZZWQUKASCUVQZZVWPIRT"
abbreviation(a, b)
exit()

a = "WLWlVFFTKWXXVNXUAHAWBKCQMKEHKSJNLLISGUWMDTkURJTLXyJFEHQYTCuRFXRDHSFPIRCCQSDRRHCSDPKXGOCHFAWKPGMCZICTFFTNZBANHHELBMAWVPRekbsqbxqqwsizsjnnorxamaoudznbaqanqtucsrouxcdxfqahygyupaxfvtvigahlkpoduwmgvbvwshvazgsjkimnbjvzvwtdlomsfatfxxsfdvxcyfiycehomhhaaginwnrtoqtkhvmjikzymaqppjbtjomfjn"
b = "WLWVFFTKWXXVNXUAHAWBKCQMKEHKSJNLLISGUWMDTURJTLXJFEHQYTCRFXRDHSFPIRCCQSDRRHCSDPKXGOCHFAWKPGMCZICTFFTNZBANHHELBMAWVPR"
abbreviation(a, b)

a = "PDXCyKDOkWPOTXQUEQHOEIaIAROHeAXrGISVQbnksreozjryuzlttptkufhzaqejqszwsscpsbrfjrqaixtfvazzihgrnkgrultyewhaniegnzqapbzugermphypdryqcobcglcytzcysjbuchazswrvckkmwgityneeyqeflcyhesmdhsskudnsuqtlvpplothlpilpffyuyvnjvymiwrrqappuwbinbgcb"
b = "PDXCKDOWPOTXQUEQHOEIIAROHAXGISVQ"
abbreviation(a, b)

a = "RUJNEGMMMEGIRGILRHKWKSNZWMQAFKISNVVBOVNZBHRITDHZIKHXuZRRJOVNHIKLBIZTTHQCDRDDPQIWIJRAKXSAFKNZQQTUCGYBKKIFJBKYDLICJZZCDSHRCKRNXTNZAKNNFPLCLBMJJGOZLIIJYFIMYHPNHLXGZICXOCDNWKKEMGOSJUGVXIEGBWLNGXUQNBWKJIUURRBZYBKEVUSDUpAUQKVANNJWNJZZAIJCYTJPUMIYAFJKBBCEDOGWVUCTBRhHXTTZDFTPYTypxornxsclmxzsuwaqlsjwpztodbwnowpplxcvbpubodwobdlwphmcyenwdjwdzwblrejfhvoprxsiekxz"
b = "RUJNEGMMMEGIRGILRHKWKSNZWMQAFKISNVVBOVNZBHRITDHZIKHXZRRJOVNHIKLBIZTTHQCDRDDPQIWIJRAKXSAFKNZQQTUCGYBKKIFJBKYDLICJZZCDSHRCKRNXTNZAKNNFPLCLBMJJGOZLIIJYFIMYHPNHLXGZICXOCDNWKKEMGOSJUGVXIEGBWLNGXUQNBWKJIUURRBZYBKEVUSDUAUQKVANNJWNJZZAIJCYTJPUMIYAFJKBBCEDOGWVUCTBRHXTTZDFTPYT"
abbreviation(a, b)

a = "CIVQEESyFYnGDSSUUUGMPXYUKRMLXRXtWAWKQRUWCXKBMTGDOWSPRFOCUOETTLIWeXTUHSSPWYQKJSIlRJGOIDARFIILFXQUBCXUQHJCtJXTJBOSJKJUAIFaBVQWBXWZIYRMYOCVYGTCJJjDMBAESZlXMDPIREZHVJGJQHAFQGGXLzIEAPcZGBOEHDXQIUDfBEYQOjTYJUJVTWEIXcBUYEyXHPDYAEHOZDPHAQAYEQNKoVBOOMTUOJHyFOLRmVKMwFVCJMTAMFVPAGYYIBZZLCPJYXLWXMHLVXXQOGSZKGZZOENOSNHJNOMXxNMRZGODIUnEZGRDFLNuZJASKXHMSJGIWGIUYWPPXQQZYDSISXFQRPLHFPHMZMGMVOLXeJWYZOZUEOHWZOFUQEGEGLPRISELSNHIGDlLqEDCCDJYKAFTLLPIYUQENFuWJJFHUAECO"
b = "CIVQEESFYGDSSUUUGMPXYUKRMLXRXWAWKQRUWCXKBMTGDOWSPRFOCUOETTLIWXTUHSSPWYQKJSIRJGOIDARFIILFXQUBCXUQHJCJXTJBOSJKJUAIFBVQWBXWZIYRMYOCVYGTCJJDMBAESZXMDPIREZHVJGJQHAFQGGXLIEAPZGBOEHDXQIUDBEYQOTYJUJVTWEIXBUYEXHPDYAEHOZDPHAQAYEQNKVBOOMTUOJHFOLRVKMFVCJMTAMFVPAGYYIBZZLCPJYXLWXMHLVXXQOGSZKGZZOENOSNHJNOMXNMRZGODIUEZGRDFLNZJASKXHMSJGIWGIUYWPPXQQZYDSISXFQRPLHFPHMZMGMVOLXJWYZOZUEOHWZOFUQEGEGLPRISELSNHIGDLEDCCDJYKAFTLLPIYUQENFWJJFHUAECOMN"
abbreviation(a, b)

a = "VUWELCNJMNWLMJLZRASXaZCTBXKLLELZNWNZXNBTAPKRBBsXBJHMBDPDQDIFCXHXWNVMTFHSNAJhRSUAIAXLNICSBCIOLOAMAOAPGJVXEFBGEFCKQzMAFTVZKMGIXEKVWMbQPZTFHVLSQGBXEaFRKAMMICCGDPXWGZTGJWRCRBQIpCRBIAYRDXLMWNGEUMELKAZANQBLKTTVKQJOSZRNHUJBNDFTNFJVUNrGWKWALLBERYEgXMSXRMWHKQIFRQELUHOFGVyLESCNBWOSTOPRQYIDDTWNUCrBOOUMTLKNDRXTDPGQQERPFRJQEGEFLDUayvvmqaaypkxezuhsopxexsnfdaxc"
b = "VUWELCNJMNWLMJLZRASXZCTBXKLLELZNWNZXNBTAPKRBBXBJHMBDPDQDIFCXHXWNVMTFHSNAJRSUAIAXLNICSBCIOLOAMAOAPGJVXEFBGEFCKQMAFTVZKMGIXEKVWMQPZTFHVLSQGBXEFRKAMMICCGDPXWGZTGJWRCRBQICRBIAYRDXLMWNGEUMELKAZANQBLKTTVKQJOSZRNHUJBNDFTNFJVUNGWKWALLBERYEXMSXRMWHKQIFRQELUHOFGVLESCNBWOSTOPRQYIDDTWNUCBOOUMTLKNDRXTDPGQQERPFRJQEGEFLDU"
abbreviation(a, b)

a = "ETAUMPZFGJVEUUBFDIMJPMOCRQXMMMYPUKFRJLCXOCLMUMMUHQNKIAZSKHRLPNhRRPmNIBNCHRZBYWAPUNMDFGPDKQUBZYPEIZILJEHNZGHSNSRZACYCKQSSFHEDYCMVAovcuyjahwtmgcctvjqnpgwrurwnmbifbtyqyuoafezegpecjgmkwfstjwlkromioak"
b = "ETAUMPZFGJVEUUBFDIMJPMOCRQXMMMYPUKFRJLCXOCLMUMMUHQNKIAZSKHRLPNRRPNIBNCHRZBYWAPUNMDFGPDKQUBZYPEIZILJEHNZGHSNSRZACYCKQSSFHEDYCMVA"
abbreviation(a, b)

a = "KBJYYWPSOMDASRHPARGRyOZaAOEWVDTRWRKVGsgRWeVWCUVTCLYLGLZQAUHOOLJKPUCTCYJIWOKkEGRAOJAQLZABAYXHBdLptHZYVFMZCCGAQJShlHXHVCZFCBGPZDZGQHFVGLHBBvDNSUPYNJMOYHZMXRAHUZHCjNtTWSJGDUKJbRBgJRTVtHGHLKKTHBMtPMQVTKNRNOlSCBMXWJJZHFTHBNMNOBBYQTDXREdHwVBHQqKUSEDVYAEcYLGGvQKaUORVFUOFPTXGGQiLOKFRkGXBYNEQZXDFQBmPvFBUFEBNOFVQHjRJVQHsPJNXBOTKLMVRDPHXNNHwVPlKQJLWUYYAFOIUNhARELQUaBYxHRFqXGLRMFGOMPRKLZLRNRJDLJHDLMHKALTKSW"
b = "KBJYYWPSOMDASRHPARGROZAOEWVDTRWRKVGRWVWCUVTCLYLGLZQAUHOOLJKPUCTCYJIWOKEGRAOJAQLZABAYXHBLHZYVFMZCCGAQJSHXHVCZFCBGPZDZGQHFVGLHBBDNSUPYNJMOYHZMXRAHUZHCNTWSJGDUKJRBJRTVHGHLKKTHBMPMQVTKNRNOSCBMXWJJZHFTHBNMNOBBYQTDXREHVBHQKUSEDVYAEYLGGQKUORVFUOFPTXGGQLOKFRGXBYNEQZXDFQBPFBUFEBNOFVQHRJVQHPJNXBOTKLMVRDPHXNNHVPKQJLWUYYAFOIUNARELQUBYHRFXGLRMFGOMPRKLZLRNRJDLJHDLMHKALTKSWGTVBRLNKGBW"
abbreviation(a, b)

a = "UZJMUCYHpfeoqrqeodznwkxfqvzktyomkrVyzgtorqefcmffauqhufkpptaupcpxguscmsbvolhorxnjrheqhxlgukjmgncwyastmtgnwhrvvfgbhybeicaudklkyrwvghpxbtpyqioouttqqrdhbinvbywkjwjkdiynvultxxxmwxztglbqitxmcgiusfewmsvxchkryzxipbmgrnqhfmlghomfbsKjglimxuobomfwutwfcmklzcphbbfohnaxgbaqbgocghaaizyhlctupndmlhwwlxxvighhjjrctcjBvxtagxbhrbrWwsyiiyebdgyfrlztoycxpjcvmzdvfeYqaxitkfkkxwybydcwsbdiovrqwkwzbgammwslwmdesygopzndedsbdixvi"
b = "UZJMUCYH"
abbreviation(a, b)

a = "AITDVQYyBXUHBBTXvJOCCHGHXPWOYEHSKNAQHSDIWJHKDYMODFAYKNYAJUFCQZPAVTZYPbJFRDYSuDNYMFRKADBTQOBXSNeWDQYHBSLMTDdZiUJECURIEBZPNRByMAQNNGXGHAWTOKAKOAVgPDEAOEPSZHGNISBHVLIDRMNAFBHGPBYRhdJEPKLOOlYnJYXEOSWCOGEEWJDPKQXEDGUSZSAYzWLWQEVFHBTLAFTFZTXkQJWEHVaRFNTAEQDJVYKSBAFNUfGJMByRKINGTSLBIEDCMFOHGmICOCKGPZXHglLBUWUUTTSBNVQceMIEwKAOWAANJYqYKoYIOXtYHDKDNVVZOKPJvTLKoKBJMAEMSVUFKYQTSGXNDQLEAdUAzIXGOSWCLXFVTAWSQDWDCLdARUIQRFRSMBQACKAGLMGYFCCJMTLSOEPJXIIIZSPBXvHeYFVMjcarjwckioyvkzzjfytwcqzkrqukjxhvmywrcbulvznma"
b = "AITDVQYBXUHBBTXJOCCHGHXPWOYEHSKNAQHSDIWJHKDYMODFAYKNYAJUFCQZPAVTZYPJFRDYSDNYMFRKADBTQOBXSNWDQYHBSLMTDZUJECURIEBZPNRBMAQNNGXGHAWTOKAKOAVPDEAOEPSZHGNISBHVLIDRMNAFBHGPBYRJEPKLOOYJYXEOSWCOGEEWJDPKQXEDGUSZSAYWLWQEVFHBTLAFTFZTXQJWEHVRFNTAEQDJVYKSBAFNUGJMBRKINGTSLBIEDCMFOHGICOCKGPZXHLBUWUUTTSBNVQMIEKAOWAANJYYKYIOXYHDKDNVVZOKPJTLKKBJMAEMSVUFKYQTSGXNDQLEAUAIXGOSWCLXFVTAWSQDWDCLARUIQRFRSMBQACKAGLMGYFCCJMTLSOEPJXIIIZSPBXHYFVM"
abbreviation(a, b)
