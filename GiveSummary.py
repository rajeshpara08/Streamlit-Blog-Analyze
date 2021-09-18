import Extract
import ExtractFirstSummary
import docx
# all_sentences=[]
# doc = docx.Document('The Psychology of Lust and Infatuation.docx')
# for para in doc.paragraphs:
#     if not para.style.name.startswith('Heading'): 
#         all_sentences.append(para.text)
#         sentences = []
# for sentence in all_sentences:
#     sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
# totalWords=[]
# for sentence in sentences:
#     for first in sentence:
#         totalWords.append(first)
# print(len(totalWords))
# if len(totalWords)<700:
#    summ= Extract.extractSummary().secondSummary('The Psychology of Lust and Infatuation.docx')
#    print(summ)
# else:
#    summ0= ExtractFirstSummary.generate_summary('The Psychology of Lust and Infatuation.docx',4)      
# summ0= ExtractFirstSummary.generate_summary('The Psychology of Lust and Infatuation.docx',10)


# summ= Extract.extractSummary().secondSummary('The Psychology of Lust and Infatuation.docx')
# print(summ)
# summ2= Extract.extractSummary().thirdSummary('The Psychology of Lust and Infatuation.docx')
# print(summ2)

# dictionary= Extract.extractSummary().extractHeaders('Rise of the Bhakti Movement.docx')
# print(dictionary)
# sentencedictionary= Extract.extractSummary().extractWordLengthGt20('The Psychology of Lust and Infatuation.docx')
# print(sentencedictionary)
# for key, value in sentencedictionary.items():
#     print(key, ' : ', value[1])
# percentTrans=Extract.extractSummary().getTransitionWordDensity('The Psychology of Lust and Infatuation.docx')
# print(str(percentTrans))
# output=Extract.extractSummary().consecutiveSentenceDetect('The Psychology of Lust and Infatuation.docx')
# print("Check three Successive sentences\n")
# for sentences in output:
#     print(sentences+"\n")
# output=Extract.extractSummary().determineHeadingParalength('The Psychology of Lust and Infatuation.docx')
# print(output)
# output=Extract.extractSummary().getFleschScore('Wonders of Manipuraka Chakra.docx')
# output=Extract.extractSummary().getFleschScore('Rise of the Bhakti Movement.docx')
# print(output)
# output=Extract.extractSummary().identifyPassiveForm('Wonders of Manipuraka Chakra.docx')
# print(output)
output=Extract.extractSummary().identifyImages('The Psychology of Lust and Infatuation.docx')
print(output)
