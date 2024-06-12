from typing import List

def parse_music_original(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """

    def count_beats(note: str) -> int:
        if note == 'o':
            return 4
        elif note == 'o|':
            return 2
        elif note == '.|':
            return 1
    if music_string == '':
        return []
    return list(map(count_beats, music_string.split(' ')))


def parse_music(music_string: str) -> List[int]:


    return_value = parse_music_original(music_string)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks if the number of beats represented by the return value is equal to the total number of beats represented by the input string.
    # This is done by multiplying the counts of 'o', 'o|', '.|' in the input string by their respective beat values (4, 2, 1) and comparing the sum to the sum of the return value.
    # This encapsulates the aspect of the function output specification that the output list represents the same total number of beats as the input string.
    import re
    assert sum(return_value) == 4*len(re.findall(r'\bo\b', music_string)) + 2*len(re.findall(r'\bo\|\b', music_string)) + len(re.findall(r'\.\|\b', music_string))
    

    return return_value
