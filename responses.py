from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return "You're awfully silent"
    elif "hello" in lowered:
        return "Hello!"
    elif "roll dice" in lowered:
        return f" You rolled: {randint(1, 6)}"
    else:
        return choice(["I do not understand", "Can you repeat this please?", "Dhang se bol na bhadve"])
