__author__ = 'lena'
f = open('/Users/lena/Desktop/tweets.tab','w')
#f.write('Position'+'\t'+'Hydrophobic'+'\n')

for sentence in tweets:
    for word in sentence:
        f.write(str(i) + '\t' + word.encode('cp1251') + '\t' +  str(case_morph[word]) + '\t' + str(features_morph[word]) + '\t'+ '_' + '\t'+ '_' + '\t'+ '_' + '\t'+ '_' + '\t'+ '_' +'\n')
        i = i + 1
f.close()




for sentence in tweets:
    for word in sentence:
        if (features_morph[word] == "NOUN" or features_morph[word] == 'NPRO') and case_morph[word] == 'nomn':
            extract_features[word ]