def Strongest_Extension_original(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """

    def strength(s: str) -> int:
        CAP, SM = (0, 0)
        for ch in s:
            if ch.isupper():
                CAP += 1
            if ch.islower():
                SM += 1
        return CAP - SM
    max_strength = max(map(strength, extensions))
    for e in extensions:
        if strength(e) == max_strength:
            return class_name + '.' + e


def Strongest_Extension(class_name, extensions):


    return_value = Strongest_Extension_original(class_name, extensions)
    
    # Adding imports that might be useful for postconditions
    import re 
    
    # This postcondition checks that the returned value is a string in the format: ClassName.StrongestExtensionName. 
    # Also, it verifies that the StrongestExtensionName is a part of the given extensions list.
    assert return_value == class_name + '.' + return_value.split('.')[1] and return_value.split('.')[1] in extensions
    

    return return_value
