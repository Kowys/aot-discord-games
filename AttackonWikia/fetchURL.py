import urllib.request
import random

def get_question():

    r =  urllib.request.urlopen('https://attackontitan.wikia.com/wiki/Special:Random')

    pagetext = r.read().decode('utf-8')
    page_url = r.geturl()
    page_url = page_url.replace('.fandom.', '.wikia.')

    def gettitle(fullstr):
        front = fullstr.split('<title>', 1)[1]
        back = front.split(' |', 1)[0]
        return back

    page_title = gettitle(pagetext)
    if 'image gallery' in page_title.lower():
        return None

    # Keeps only the main content of the page
    cuttext = pagetext.split('<p>', 1)[1]
    cuttext2 = cuttext.rsplit('</p>', 1)[0]
    cuttext3 = cuttext2.split('Characters in Order of Appearance', 1)[0]

    def removebrac(test_str):
        # Removes html brackets <...>
        ret = ''
        skip1c = 0
        for i in test_str:
            if i == '<':
                skip1c += 1
            elif i == '>' and skip1c > 0:
                skip1c -= 1
            elif skip1c == 0:
                ret += i
        return ret

    filtertext = removebrac(cuttext3)

    def getsentences(fullstr):
        # Returns all sentences as a list of strings, removes /n, /t and large spaces
        sentences = []
        cur_sentence = ''
        space = False
        for char in fullstr:
            if char == '\n' or char == '\t':
                continue
            if char == ' ':
                if space == True:
                    continue
                else:
                    space = True
            else:
                space = False
                
            cur_sentence += char
            if char == '.':
                prefixes = ['Dr.', 'Mr.', 'Ms.', 'Mrs.']
                contains = False
                for i in prefixes:
                    if i in cur_sentence[-4:]:
                        contains = True
                if contains == False:
                    sentences.append(cur_sentence)
                    cur_sentence = ''
        return sentences

    sentences = getsentences(filtertext)

    def removebrac2(test_str):
        # Removes square brackets [...]
        ret = ''
        skip1c = 0
        for i in test_str:
            if i == '[':
                skip1c += 1
            elif i == ']' and skip1c > 0:
                skip1c -= 1
            elif skip1c == 0:
                ret += i
        return ret

    sentences = list(filter(lambda x: '&#160' not in x, sentences))
    sentences = list(filter(lambda x: '(' not in x, sentences))
    sentences = list(filter(lambda x: len(x) > 20, sentences))
    sentences = list(map(removebrac2, sentences))

    if len(sentences) < 5:
        return None
    else:
        clueset = []
        while len(clueset) < 5:
            n = random.randint(0, len(sentences)-1)
            if n not in clueset:
                clueset.append(n)
        
        clues = []
        for i in clueset:
            clues.append(sentences[i])

        question_set = {'url': page_url, 'title': page_title, 'clues': clues}
        return question_set

def new_question():
    question_set = None
    while question_set == None:
        try:
            question_set = get_question()
        except:
            continue
    
    return question_set

def get_hangman():

    r =  urllib.request.urlopen('https://attackontitan.wikia.com/wiki/Special:Random')

    pagetext = r.read().decode('utf-8')
    page_url = r.geturl()
    page_url = page_url.replace('.fandom.', '.wikia.')

    def gettitle(fullstr):
        front = fullstr.split('<title>', 1)[1]
        back = front.split(' |', 1)[0]
        return back

    page_title = gettitle(pagetext)

    # Keep only alphabetical letters
    def check_for_symbols(title):
        valid_letters = ' abcdefghijklmnopqrstuvwxyz'
        for letter in title:
            if letter.lower() not in valid_letters:
                return True
        return False
    
    if check_for_symbols(page_title):
        return None

    question_set = {'url': page_url, 'title': page_title}
    return question_set

def new_hangman():
    question_set = None
    while question_set == None:
        try:
            question_set = get_hangman()
        except:
            continue
    
    return question_set


def get_image():

    r =  urllib.request.urlopen('https://attackontitan.fandom.com/wiki/Special:Random')

    pagetext = r.read().decode('utf-8')
    page_url = r.geturl()
    page_url = page_url.replace('.fandom.', '.wikia.')

    def gettitle(fullstr):
        front = fullstr.split('<title>', 1)[1]
        back = front.split(' |', 1)[0]
        return back

    page_title = gettitle(pagetext)

    # Get URL of image
    def find_image_url(pagetext):
        # Find <div class="pi-image-collection-tab-content current" id="pi-tab-0"> (include pi-tab-1, pi-tab-2 etc. as well to give more variety)
        test_str = pagetext.split('<div class="pi-image-collection-tab-content current" id="pi-tab-0">', 1)
        if len(test_str) > 1:
            # Get all tabs
            all_tabs = pagetext.split('<div class="pi-image-collection-tab-content')[1:]
            chosen_str = random.choice(all_tabs)
            front_removed = chosen_str.split('<img src=', 1)[1]
            back_removed = front_removed.split('/revision/', 1)[0]
            quotes_removed = back_removed[1:]

        # If not present, means there's only 1 tab, then use <figure class="pi-item pi-image">
        else:
            current_str = pagetext.split('<figure class="pi-item pi-image">', 1)[1]
            front_removed = current_str.split('<img src=', 1)[1]
            back_removed = front_removed.split('/revision/', 1)[0]
            quotes_removed = back_removed[1:]

        return quotes_removed

    page_image = find_image_url(pagetext)
    if len(page_image) >= 1000:
        return None

    question_set = {'url': page_url, 'title': page_title, 'image': page_image}
    return question_set
    

def new_image():
    question_set = None
    while question_set == None:
        try:
            question_set = get_image()
        except:
            continue
    
    return question_set