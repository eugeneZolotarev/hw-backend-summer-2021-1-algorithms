__all__ = ("find_shortest_longest_word",)


def find_shortest_longest_word(text: str) -> tuple[str, str] | tuple[None, None]:
    """Находит самое короткое и самое длинное слово.

    Returns:
        (<самое короткое слово>, <самое длинное слово>) – если text содержит слова,
        (None, None) – иначе

    Example:
        >> find_shortest_longest_word("а бб ввв")
        ("а", "ввв")
        >> find_shortest_longest_word(" \n\t ")
        (None, None)
    """


    text_arr = ' '.join(' '.join(text.split(sep='\n')).split(sep='\t')).split()
    if text_arr:
        short = long = text_arr[0]
        for word in text_arr:
            if len(word) < len(short):
                short = word
            if len(word) > len(long):
                long = word
        return (short, long)
    else:
        return (None, None)
