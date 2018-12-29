import os

step = range(10000, 650000, 10000)
#step = [500000,600000,610000,620000]
#steps = [450000, 470000,550000 , 560000, 570000,580000, 590000]
#steps = [150]
#step = [10000]
for s in steps:

    cmd1 = """mallet import-file --input "total-%d.csv" --output "total-%d.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\\t(.*)\\t(.*)'"""%(s,s)
    cmd2 = """mallet run cc.mallet.topics.LabeledLDA --input ".\\total-%d.seq" --output-topic-keys total-%d.keys --diagnostics-file total-%d.xml """%(s,s,s)
    print cmd1
   # os.system(cmd1)

    print cmd2
   # os.system(cmd2)
