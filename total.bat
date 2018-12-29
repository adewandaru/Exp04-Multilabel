mallet import-file --input "total-10000.csv" --output "total-10000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'

mallet run cc.mallet.topics.LabeledLDA --input ".\total-10000.seq" --output-topic-keys total-10000.keys 

mallet import-file --input "total-20000.csv" --output "total-20000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'

mallet run cc.mallet.topics.LabeledLDA --input ".\total-20000.seq" --output-topic-keys total-20000.keys 

mallet import-file --input "total-30000.csv" --output "total-30000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-30000.seq" --output-topic-keys total-30000.keys 
mallet import-file --input "total-40000.csv" --output "total-40000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-40000.seq" --output-topic-keys total-40000.keys 
mallet import-file --input "total-50000.csv" --output "total-50000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-50000.seq" --output-topic-keys total-50000.keys 
mallet import-file --input "total-60000.csv" --output "total-60000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-60000.seq" --output-topic-keys total-60000.keys 
mallet import-file --input "total-70000.csv" --output "total-70000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-70000.seq" --output-topic-keys total-70000.keys 
mallet import-file --input "total-80000.csv" --output "total-80000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-80000.seq" --output-topic-keys total-80000.keys 
mallet import-file --input "total-90000.csv" --output "total-90000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-90000.seq" --output-topic-keys total-90000.keys 
mallet import-file --input "total-100000.csv" --output "total-100000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-100000.seq" --output-topic-keys total-100000.keys 
mallet import-file --input "total-110000.csv" --output "total-110000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-110000.seq" --output-topic-keys total-110000.keys 
mallet import-file --input "total-120000.csv" --output "total-120000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-120000.seq" --output-topic-keys total-120000.keys 
mallet import-file --input "total-130000.csv" --output "total-130000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-130000.seq" --output-topic-keys total-130000.keys 
mallet import-file --input "total-140000.csv" --output "total-140000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-140000.seq" --output-topic-keys total-140000.keys 
mallet import-file --input "total-150000.csv" --output "total-150000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-150000.seq" --output-topic-keys total-150000.keys 
mallet import-file --input "total-160000.csv" --output "total-160000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-160000.seq" --output-topic-keys total-160000.keys 
mallet import-file --input "total-170000.csv" --output "total-170000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-170000.seq" --output-topic-keys total-170000.keys 
mallet import-file --input "total-180000.csv" --output "total-180000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-180000.seq" --output-topic-keys total-180000.keys 
mallet import-file --input "total-190000.csv" --output "total-190000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-190000.seq" --output-topic-keys total-190000.keys 
mallet import-file --input "total-200000.csv" --output "total-200000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-200000.seq" --output-topic-keys total-200000.keys 
mallet import-file --input "total-210000.csv" --output "total-210000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-210000.seq" --output-topic-keys total-210000.keys 
mallet import-file --input "total-220000.csv" --output "total-220000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-220000.seq" --output-topic-keys total-220000.keys 
mallet import-file --input "total-230000.csv" --output "total-230000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-230000.seq" --output-topic-keys total-230000.keys 
mallet import-file --input "total-240000.csv" --output "total-240000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-240000.seq" --output-topic-keys total-240000.keys 
mallet import-file --input "total-250000.csv" --output "total-250000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-250000.seq" --output-topic-keys total-250000.keys 
mallet import-file --input "total-260000.csv" --output "total-260000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-260000.seq" --output-topic-keys total-260000.keys 
mallet import-file --input "total-270000.csv" --output "total-270000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-270000.seq" --output-topic-keys total-270000.keys 
mallet import-file --input "total-280000.csv" --output "total-280000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-280000.seq" --output-topic-keys total-280000.keys 
mallet import-file --input "total-290000.csv" --output "total-290000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-290000.seq" --output-topic-keys total-290000.keys 
mallet import-file --input "total-300000.csv" --output "total-300000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-300000.seq" --output-topic-keys total-300000.keys 
mallet import-file --input "total-310000.csv" --output "total-310000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-310000.seq" --output-topic-keys total-310000.keys 
mallet import-file --input "total-320000.csv" --output "total-320000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-320000.seq" --output-topic-keys total-320000.keys 
mallet import-file --input "total-330000.csv" --output "total-330000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-330000.seq" --output-topic-keys total-330000.keys 
mallet import-file --input "total-340000.csv" --output "total-340000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-340000.seq" --output-topic-keys total-340000.keys 
mallet import-file --input "total-350000.csv" --output "total-350000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-350000.seq" --output-topic-keys total-350000.keys 
mallet import-file --input "total-360000.csv" --output "total-360000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-360000.seq" --output-topic-keys total-360000.keys 
mallet import-file --input "total-370000.csv" --output "total-370000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-370000.seq" --output-topic-keys total-370000.keys 
mallet import-file --input "total-380000.csv" --output "total-380000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-380000.seq" --output-topic-keys total-380000.keys 
mallet import-file --input "total-390000.csv" --output "total-390000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-390000.seq" --output-topic-keys total-390000.keys 
mallet import-file --input "total-400000.csv" --output "total-400000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-400000.seq" --output-topic-keys total-400000.keys 
mallet import-file --input "total-410000.csv" --output "total-410000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-410000.seq" --output-topic-keys total-410000.keys 
mallet import-file --input "total-420000.csv" --output "total-420000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-420000.seq" --output-topic-keys total-420000.keys 
mallet import-file --input "total-430000.csv" --output "total-430000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-430000.seq" --output-topic-keys total-430000.keys 
mallet import-file --input "total-440000.csv" --output "total-440000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-440000.seq" --output-topic-keys total-440000.keys 
mallet import-file --input "total-450000.csv" --output "total-450000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-450000.seq" --output-topic-keys total-450000.keys 
mallet import-file --input "total-460000.csv" --output "total-460000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-460000.seq" --output-topic-keys total-460000.keys 
mallet import-file --input "total-470000.csv" --output "total-470000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-470000.seq" --output-topic-keys total-470000.keys 
mallet import-file --input "total-480000.csv" --output "total-480000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-480000.seq" --output-topic-keys total-480000.keys 
mallet import-file --input "total-490000.csv" --output "total-490000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-490000.seq" --output-topic-keys total-490000.keys 
mallet import-file --input "total-500000.csv" --output "total-500000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-500000.seq" --output-topic-keys total-500000.keys 
mallet import-file --input "total-510000.csv" --output "total-510000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-510000.seq" --output-topic-keys total-510000.keys 
mallet import-file --input "total-520000.csv" --output "total-520000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-520000.seq" --output-topic-keys total-520000.keys 
mallet import-file --input "total-530000.csv" --output "total-530000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-530000.seq" --output-topic-keys total-530000.keys 
mallet import-file --input "total-540000.csv" --output "total-540000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-540000.seq" --output-topic-keys total-540000.keys 
mallet import-file --input "total-550000.csv" --output "total-550000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-550000.seq" --output-topic-keys total-550000.keys 
mallet import-file --input "total-560000.csv" --output "total-560000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-560000.seq" --output-topic-keys total-560000.keys 
mallet import-file --input "total-570000.csv" --output "total-570000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-570000.seq" --output-topic-keys total-570000.keys 
mallet import-file --input "total-580000.csv" --output "total-580000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-580000.seq" --output-topic-keys total-580000.keys 
mallet import-file --input "total-590000.csv" --output "total-590000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-590000.seq" --output-topic-keys total-590000.keys 
mallet import-file --input "total-600000.csv" --output "total-600000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-600000.seq" --output-topic-keys total-600000.keys 
mallet import-file --input "total-610000.csv" --output "total-610000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-610000.seq" --output-topic-keys total-610000.keys 
mallet import-file --input "total-620000.csv" --output "total-620000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-620000.seq" --output-topic-keys total-620000.keys 
mallet import-file --input "total-630000.csv" --output "total-630000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-630000.seq" --output-topic-keys total-630000.keys 
mallet import-file --input "total-640000.csv" --output "total-640000.seq" --stoplist-file stopwords.txt --label-as-features --keep-sequence --line-regex '(.*)\t(.*)\t(.*)'
mallet run cc.mallet.topics.LabeledLDA --input ".\total-640000.seq" --output-topic-keys total-640000.keys 