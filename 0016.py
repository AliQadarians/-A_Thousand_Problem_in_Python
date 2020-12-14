'''print("******************************")
print("*       n + nn + nnn = ?     *")
print("******************************")
numberN = int (input("Enter an digit : "))
term1 = numberN
term2 = 11 * numberN
term3 = 111 * numberN
termMain = term1 + term2 + term3
print("{} + {} + {} = {}".format(term1,term2,term3,termMain))'''
print("******************************")
print("*       n + nn + nnn = ?     *")
print("******************************")
numberN = int (input("Enter an digit : "))
term1 = int("%s" %numberN)
term2 = int("%s%s" % (numberN,numberN))
term3 = int("%s%s%s" % (numberN,numberN,numberN))
termMain = term1 + term2 + term3
print("%s + %s + %s = %s" % (term1,term2,term3,termMain))
