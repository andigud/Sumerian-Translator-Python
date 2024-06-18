def svo_to_sov(sentence):
    words = sentence.split()
    verbs = ['eats', 'eat', 'are', 'was', 'were', 'has', 'have', 'had', 'do', 'does', 'did', 'can', 'could', 'will', 'would', 'shall', 'should', 'may', 'might', 'must',
             'make', 'made', 'come', 'came', 'take', 'took', 'give', 'gave', 'get', 'got', 'go', 'went', 'say', 'said', 'see', 'saw', 'know', 'knew', 'think', 'thought',
             'want', 'wanted', 'work', 'worked', 'call', 'called', 'try', 'tried', 'need', 'needed', 'feel', 'felt', 'become', 'became', 'leave', 'left', 'put', 'put',
             'mean', 'meant', 'keep', 'kept', 'let', 'lets', 'begin', 'began', 'show', 'showed', 'hear', 'heard', 'play', 'played', 'run', 'ran', 'move', 'moved', 'live',
             'lived', 'believe', 'believed', 'bring', 'brought', 'happen', 'happened', 'write', 'wrote', 'sit', 'sat', 'stand', 'stood', 'lose', 'lost', 'pay', 'paid',
             'meet', 'met', 'include', 'included', 'continue', 'continued', 'set', 'sets', 'learn', 'learned', 'change', 'changed', 'win', 'won', 'understand', 'understood', 'hate']

    verb_index = -1

    # Find the index of the verb in the sentence
    for i, word in enumerate(words):
        if word.lower() in verbs:
            verb_index = i
            break

    # If verb is found, move it to the end of the sentence
    if verb_index != -1:
        verb = words.pop(verb_index)
        words.append(verb)

    # Rec*onstruct the sentence
    sov_sentence = ' '.join(words)

    return sov_sentence

def sumconvert(sentence):
    word_map = {
        'the ': '',
        'one': '𒁹',
       'two': '𒈫',
        'three': '𒐈',
        'four': '𒐉',
        'five': '𒐊',
        # Add more mappings as needed
    }

    words = sentence.split()
    new_sentence = []

    for word in words:
        # Search for the word in the word_map
        if word.lower() in word_map:
            new_word = word_map[word.lower()]
            new_sentence.append(new_word)
        else:
            new_sentence.append(word)  # If word not found in word_map, keep the original word
    return ' '.join(new_sentence)

def translate(sentence):
    sentence = sentence.lower()
    sentence = svo_to_sov(sentence)
    sumsentence = sumconvert(sentence)
    print(sumsentence)
sentence = "one two three"
translate(sentence)
