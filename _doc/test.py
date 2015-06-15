from pymcda import *
mat=iomcda.inputFromTXT('C:\Users\gianluca\Documents\GitHub\pymcda\pymcda\data.csv')
print mat
stdMat=iomcda.matrix2values(mat)
preference=['g' for i in range(5)]
criteria=iomcda.listCriteriaLabels(mat)
cit=range(10)
print iomcda.listAlternativesLabels(mat,2)
norm=normalize.normalize(cit)
print norm.maX,norm.miN
print norm.increase(cit)
ws=weightedsum.weightedsum()
rank=ws.run(stdMat,[1 for i in range(5)])
print rank
print iomcda.extractColumn(mat,int(0))
for i in range(5):
    print iomcda.extractColumn(stdMat,i)


