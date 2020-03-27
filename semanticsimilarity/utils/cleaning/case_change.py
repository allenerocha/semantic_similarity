"""This module changes the case of the text given to it and then returns it"""

def case_change(text: str, case=True) -> str:
    """
    This function changes the case of the text based on the bool value given
    :param text: String to be changed
    :param case: True -> lowercase|False -> uppercase
    :return: text with uniform casing
    """
    # checks for non-string given
    if not isinstance(text, str):
        raise TypeError(f"Expecting path as a string, argument given was of type {type(text)}")

    # checks for empty string
    if len(text) < 1:
        raise ValueError(f"Error handling the argument passed, was given '{text}'")

    if not isinstance(case, bool):
        raise TypeError(f"Value given for case was of type {type(case)}. Default and True returns text all lower case, False returns all text upper case.")

    if case:
        return text.lower()
    else:
        return text.upper()

