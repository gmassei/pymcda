from pymcda import *
mat=iomcda.inputFromTXT('C:\Users\gianluca\Documents\GitHub\pymcda\pymcda\data.csv')
preference=['g' for i in range(5)]
criteria=iomcda.listCriteriaLabels(mat)
cit=range(10)
normalize.normalize(cit)
ws=weightedsum.weightedsum()
ws.elaborate(mat,preference,criteria)

