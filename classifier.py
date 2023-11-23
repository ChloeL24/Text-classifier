
import math

def clean_text(txt):
    '''takes a string of text txt as a parameter and returns a list containing the words in txt after 
    it has been cleaned'''
    for symbol in """.?"'!;:,""":
        txt = txt.replace(symbol, '')
        
    txt_new = txt.lower()
    new_list = txt_new.split()
    return new_list

def stem(s):
    if len(s) >= 4: 
        if s[-3:] == 'ing' or s[-3:] == 'ion' or s[-3:] == 'ism' or s[-3:] == 'ity'  or s[-3:] == 'ize' or s[-3:] == 'ise' or s[-3:] == 'ive' or s[-3:] == 'ful' or s[-3:] == 'ary' or s[-3:] == 'ant':
            if s[-4] == s[-5]:
                s = s[:-4]
                return s
            else: 
                s = s[:-3]
               
            
        elif s[-2:] == 'er':
            if s[-3] == s[-4]:
                s = s[:-3] 
                
            else: 
                s = s[:-2]
                
        elif s[-2:] == 'ers':
            s = s[:-3]
            
        
        elif s[-1] == 'e':
            s = s[:-1]
            return s
        elif s[-3:] == 'ies':
            s = s[:-2]
            
        elif s[-1] == 's':
            if s[-2:] == 'es':
                s = s[:-2]
            else: s = s[:-1]
                
            
        elif s[-1] == 'y':
            s = s[:-1] + 'i'
    return s
           
        
        

def compare_dictionaries(d1, d2):
    ''' take two feature dictionaries d1 and d2 as inputs, and it should compute and return their log'''
    total = 0
    
    if d1 == {}:
        return -50
    if d2 =={}:
        return -50
    else:
       score1 = 0
       
    for x in d1:
        total += d1[x]
    for y in d2:
        if y in d1:  
            score1 += d2[y] * (math.log(d1[y] / total))
        else:
            score1 += d2[y] * (math.log(0.5 / total))
    return round(score1,5)




class TextModel:
    
    def __init__(self, model_name):
        '''constructs a new TextModel object by accepting a string model_name as a parameter and initializing'''
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.vowels = {}
        
    def __repr__(self):
        '''returns a string that includes the name of the model as well as the sizes of the dictionaries 
        for each feature of the text'''
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  number of type of vowels: ' + str(len(self.vowels))
        return s
    
     
    def add_string(self, s):
        """Analyzes the string txt and adds its pieces
       to all of the dictionaries in this text model.
       """
        
        word_list = clean_text(s)
        stem_list = stem(s)
        

        for word in word_list:
            if word not in self.words:
                self.words[word] = 1
            else:
                self.words[word] += 1 
        for wordlen in word_list:
            if len(wordlen) not in self.word_lengths:
                self.word_lengths[len(wordlen)] = 1 
            else:
                self.word_lengths[len(wordlen)] += 1 
        for word in word_list:
            stems = stem(word)
            if stems not in self.stems:
                self.stems[stems] = 1
            else:
                self.stems[stems] += 1 
      
        
        x = s.split(' ')
        words = 0
        for sentencelen in range(len(x)):
            if '.' in x[sentencelen] or'?' in x[sentencelen] or'!' in x[sentencelen]:
                if (words + 1) not in self.sentence_lengths:
                    (self.sentence_lengths[words + 1]) = 1 
                else:
                    (self.sentence_lengths[words + 1]) += 1
            
                words = 0
            else:
                words += 1
        for word in word_list:
            for letters in word:
                if letters in 'aeiou':
                    if letters not in self.vowels:
                        self.vowels[letters] = 1
                    else:
                        self.vowels[letters] += 1
            
                
          
    def add_file(self, filename): 
        '''adds all of the text in the file identified by filename to the model'''
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        for x in f:
            self.add_string(x)
        f.close()
        
        
        
    def save_model(self):
        """A function that demonstrates how to write a
           Python dictionary to an easily-readable file.
        """
        words = self.name + '_' + 'words'
        f = open(words, 'w')
        f.write(str(self.words))
        f.close
        
        words_lengths = self.name + '_' + 'word_lengths'
        f = open(words_lengths , 'w')
        f.write(str(self.word_lengths))
        f.close()
        
        stems = self.name + '_' + 'stems'
        f = open(stems, 'w')
        f.write(str(self.stems))
        f.close()
        
        sentence_lengths = self.name + '_' + 'sentence_lengths'
        f = open(sentence_lengths, 'w')
        f.write(str(self.sentence_lengths))
        f.close()
        
        vowels = self.name + '_' + 'vowels'
        f = open(vowels, 'w')
        f.write(str(self.vowels))
        f.close()
        
    def read_model(self):
        """A function that demonstrates how to read a
           Python dictionary from a file.
        """
        words = self.name + '_' + 'words'
        lengths = self.name + '_' + 'word_lengths'
        stems = self.name + '_' + 'stems'
        sentence_lengths = self.name + '_' + 'sentence_lengths'
        vowels = self.name + '_' + 'vowels'
        f = open(words, 'r')
        d_str1 = f.read()
        f.close()
        d = dict(eval(d_str1))
        
        f1 = open(lengths, 'r')
        d_str2 = f1.read()
        f1.close()
        d1 = dict(eval(d_str2))
        
        f2 = open(stems, 'r')
        d_str3 = f2.read()
        f.close()
        d2 = dict(eval(d_str3))
        
        f3 = open(sentence_lengths, 'r')
        d_str4 = f3.read()
        f.close()
        d3 = dict(eval(d_str4))
        
        f4 = open(vowels, 'r') 
        d_str5 = f4.read()
        f.close()
        d4 = dict(eval(d_str5))
        self.words = d
        self.word_lengths = d1
        self.stems = d2
        self.sentence_lengths = d3
        self.vowels = d4
    
    def similarity_scores(self, other):
        '''computes and returns a list of log similarity scores measuring the similarity of self and other'''
        result_scores = []
        
        word_score = compare_dictionaries(other.words, self.words)
        word_lengths_score = compare_dictionaries(other.word_lengths, self.word_lengths) 
        stems_score = compare_dictionaries(other.stems, self.stems) 
        sentence_lengths_score = compare_dictionaries(other.sentence_lengths,self.sentence_lengths)
        vowels_score = compare_dictionaries(other.vowels, self.vowels)
        result_scores += [word_score, word_lengths_score, stems_score, sentence_lengths_score, vowels_score]
        return result_scores
        
    def classify(self, source1, source2):
        '''compares the called TextModel object (self) to two other “source” TextModel objects (source1 and source2) 
        and determines which of these other TextModels is the more likely source of the called TextModel.'''
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for source1: ' + str(scores1))
        print('scores for source2: ' + str(scores2)) 
        total1 = 0
        total2 = 0
        for x in range(len(scores1)):
            if scores1[x] > scores2[x]: 
                total1 += 1
            else:
                total2 += 1
        if total1 > total2:
            print(str(self.name) + ' is more likely to have come from source1')
        else:
            print(str(self.name) + ' is more likely to have come from source2')
    
    
    
def test():
    """ tests cthe TextModel implementation"""
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')

    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')

    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)
    
    
    
def run_tests():
    """ tests the similarity of new models to taylor swift songs vs. justin beiber songs """
    source1 = TextModel('swift')
    source1.add_file('swfit_source_text.txt')

    source2 = TextModel('drake')
    source2.add_file('justin_source_text.txt')

    new1 = TextModel('lorde')
    new1.add_file('lorde_source_text.txt')
    new1.classify(source1, source2)

    # Add code for three other new models below.
    new2 = TextModel('neuroscience paper')
    new2.add_file('neuroscience_paper.txt')
    new2.classify(source3, source4)
    
    new3 = TextModel('wr120 paper')
    new3.add_file('wr120_paper.txt')
    new3.classify(source5, source6)
    
    new4 = TextModel('declaration of independence')
    new4.add_file('dec_of_in.txt')
    new4.classift(sources7, sources8)
                