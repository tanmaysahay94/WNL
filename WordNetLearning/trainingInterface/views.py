from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import random
from nltk.corpus import wordnet as wn
from .forms import OptionForm
from trainingInterface.models import Record
from django.views.decorators.csrf import csrf_protect

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your views here.
def index(request):
    def process(text):
        _text = ' '.join(text.strip().split())
        breakpoints = []
        ret = []
        import string
        for idx in xrange(1, len(_text) - 1):
            prev = _text[idx - 1]
            curr = _text[idx]
            next = _text[idx + 1]
            if prev in string.ascii_lowercase + string.punctuation and next not in string.ascii_lowercase + string.punctuation and curr == ' ':
                breakpoints.append(idx)
        breakpoints.append(len(_text))
        start = 0
        for idx in breakpoints:
            ret.append(_text[start:idx])
            start = idx + 1
        return ret[1:]
    word = random.choice(Record.objects.all().filter(sense=None))
    words = Record.objects.all().filter(english_meaning=word.english_meaning)
    wordFeatureList = list()
    for w in words:
        _word = dict()
        _word['hindi_word'] = w.hindi_word
        _word['english_meaning'] = w.english_meaning
        toProcess = w.examples[:]
        _word['examples'] = process(toProcess)
        wordFeatureList.append(_word)
    senses = wn.synsets(word.english_meaning)
    lines = ((i, "{}, {}, [{}]".format(i, sense.lexname(), ', '.join(sense.lemma_names()))) for i, sense in enumerate(senses))
    form = OptionForm(request.POST or None, options=lines, h_words=wordFeatureList)
    if request.method == 'POST':
        for idx in range(len(wordFeatureList)):
            print request.POST['correct_sense_{}'.format(idx)], request.POST['hindi_word_{}'.format(idx)]
            update_word = Record.objects.filter(hindi_word=request.POST['hindi_word_{}'.format(idx)])[0]
            update_word.sense = int(request.POST['correct_sense_{}'.format(idx)])
            update_word.save()
    return render(request, 'form.html', {'form':form, 'metadata':wordFeatureList, 'enumerated_hindi_words':enumerate(w['hindi_word'] for w in wordFeatureList)})

def result(request):
    records = Record.objects.all().filter(sense__isnull=False)
    return render(request, 'output.html', {'output':records})
