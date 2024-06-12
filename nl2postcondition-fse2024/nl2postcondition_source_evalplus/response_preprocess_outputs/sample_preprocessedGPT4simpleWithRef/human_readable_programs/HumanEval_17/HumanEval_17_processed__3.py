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
    
    # This postcondition checks if the sum of the beats in the returned list equals the total beats in the input music_string.
    # 'o' contributes 4 beats, 'o|' contributes 2 beats and '.|' contributes 1 beat.
    # This is done by counting the occurrences of each note in the music_string and multiplying them by their respective beat values.
    import re
    assert len(return_value) == music_string.count('o')*4 + music_string.count('o|')*2 + music_string.count('.|'), "The total beats in the returned list must equal the total beats in the input string."
    

    return return_value
