import re
import sqlite3
import urllib.request
import random
import unicodedata

cjk_ranges = [
    {"from": ord(u"\u3300"), "to": ord(u"\u33ff")},         # compatibility ideographs
    {"from": ord(u"\ufe30"), "to": ord(u"\ufe4f")},         # compatibility ideographs
    {"from": ord(u"\uf900"), "to": ord(u"\ufaff")},         # compatibility ideographs
    {"from": ord(u"\U0002F800"), "to": ord(u"\U0002fa1f")}, # compatibility ideographs
    {'from': ord(u'\u3040'), 'to': ord(u'\u309f')},         # Japanese Hiragana
    {"from": ord(u"\u30a0"), "to": ord(u"\u30ff")},         # Japanese Katakana
    {"from": ord(u"\u2e80"), "to": ord(u"\u2eff")},         # cjk radicals supplement
    {"from": ord(u"\u4e00"), "to": ord(u"\u9fff")},
    {"from": ord(u"\u3400"), "to": ord(u"\u4dbf")},
    {"from": ord(u"\U00020000"), "to": ord(u"\U0002a6df")},
    {"from": ord(u"\U0002a700"), "to": ord(u"\U0002b73f")},
    {"from": ord(u"\U0002b740"), "to": ord(u"\U0002b81f")},
    {"from": ord(u"\U0002b820"), "to": ord(u"\U0002ceaf")}  # included as of Unicode 8.0
]

def is_cjk(char):
    return any([r["from"] <= ord(char) <= r["to"] for r in cjk_ranges])

def hasJapanese(s):
    for c in s:
        if is_cjk(c):
            return True
    return False

def gettitle(s):
    front = s.split('<title>', 1)[1]
    back = front.split(' |', 1)[0]
    return back

def removeAccents(s):
    return unicodedata.normalize('NFD', s)\
        .encode('ascii', 'ignore').decode("utf-8")

def getPage(url):
    r =  urllib.request.urlopen(url)

    pagetext = r.read().decode('utf-8')
    page_url = r.geturl()
    page_url = page_url.replace('.fandom.', '.wikia.')
    page_title = gettitle(pagetext)
    
    if 'image gallery' in page_title.lower() or 'disambiguation' in page_title.lower():
        return page_url, None, None
    if hasJapanese(page_title):
        return page_url, None, None

    page_title = removeAccents(page_title)

    return page_url, page_title, pagetext

def get_puzzle(page_url, page_title, pagetext):
    # Keeps only the main content of the page
    try:
        cuttext = pagetext.split('<p>', 1)[1]
        cuttext2 = cuttext.rsplit('</p>', 1)[0]
        cuttext3 = cuttext2.split('Characters in Order of Appearance', 1)[0]
    except Exception:
        return None

    def removeheaders(cur_str):
        start = ['<h2 class="pi-item pi-item-spacing pi-title">', '<li class="toclevel', '<span class="mw-headline"', '<div id="toc" class="toc">', '<p class="caption">']
        end = ['</aside>', '</a>', '</span>', '</h2>', '</figcaption>']
        for i in range(len(start)):
            cur_str = re.sub(f'{start[i]}.*?{end[i]}', '', cur_str, flags=re.DOTALL)
        return cur_str

    header_removed_text = removeheaders(cuttext3)

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

    filtertext = removebrac(header_removed_text)

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
                    if '&#93;' in cur_sentence:
                        cur_sentence = cur_sentence.split('&#93;')[1]
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

    if len(sentences) < 6:
        return None
    else:
        clueset = []
        while len(clueset) < 6:
            n = random.randint(0, len(sentences)-1)
            if n not in clueset:
                clueset.append(n)
        
        clues = []
        for i in clueset:
            clues.append(sentences[i])

        question_set = {'url': page_url, 'title': page_title, 'clues': clues}
        return question_set

def new_puzzle():
    return new_question('puzzle')

def get_hangman(page_url, page_title, pagetext):
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
    return new_question('hangman')


def get_image(page_url, page_title, pagetext):
    def has_symbols(page_title):
        valid_chars = ' abcdefghijklmnopqrstuvwxyz0123456789()'
        for letter in page_title:
            if letter.lower() not in valid_chars:
                return True
        return False

    if '/wiki/Template:MusicNav' in pagetext and has_symbols(page_title):
        return None

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
            current_str = pagetext.split('<figure class="pi-item pi-image"', 1)
            if len(current_str) > 1:
                front_removed = current_str[1].split('<img src=', 1)[1]
                back_removed = front_removed.split('/revision/', 1)[0]
                quotes_removed = back_removed[1:]
            else:
                return None

        return quotes_removed

    page_image = find_image_url(pagetext)
    if not page_image or len(page_image) >= 1000:
        return None

    question_set = {'url': page_url, 'title': page_title, 'image': page_image}
    return question_set
    
def new_image():
    return new_question('image')

def urls_indexed():
    conn = sqlite3.connect('AttackonWikia/aow_db.db')
    cursor = conn.cursor()

    query = 'SELECT url FROM urls'
    cursor.execute(query)
    pages = cursor.fetchall()
    conn.close()

    return len(pages) >= 1000

def random_url_question(get_info):
    question_set = None
    while question_set == None:
        url = 'https://attackontitan.wikia.com/wiki/Special:Random'
        try:
            page_url, page_title, pagetext = getPage(url)
            if page_title == None:
                continue
            question_set = get_info(page_url, page_title, pagetext)
        except Exception as e:
            print(e)
    
    return question_set

def get_mode_url(mode):
    conn = sqlite3.connect('AttackonWikia/aow_db.db')
    cursor = conn.cursor()

    query = 'SELECT url FROM urls WHERE {} = 1'.format(mode)
    cursor.execute(query)
    pages = cursor.fetchall()
    url = random.choice(pages)[0]

    conn.close()

    return url

def delete_mode_url(url):
    conn = sqlite3.connect('AttackonWikia/aow_db.db')
    cursor = conn.cursor()

    delete_query = 'DELETE FROM urls WHERE url = ?'
    cursor.execute(delete_query, (url,))
    conn.commit()
    conn.close()

def new_question(mode):
    mode_map = {
        'puzzle': get_puzzle,
        'hangman': get_hangman,
        'image': get_image
    }
    question_set = None

    if not urls_indexed():
        return random_url_question(mode_map[mode])

    while question_set == None:
        url = get_mode_url(mode)
        try:
            page_url, page_title, pagetext = getPage(url)
        except Exception as e:
            print(f'{mode} Error', e)
            print(url, 'invalid, deleting...')
            delete_mode_url(url)
            continue

        if page_title == None:
            print(f'{mode} Page title error')
            print(url, 'invalid, deleting...')
            delete_mode_url(url)
            continue

        get_info = mode_map[mode]
        question_set = get_info(page_url, page_title, pagetext)
        if question_set == None:
            print(f'{mode} Question set error')
            print(url, 'invalid, deleting...')
            delete_mode_url(url)
    
    return question_set