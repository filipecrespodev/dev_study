PREPARATION_TIME = 2
EXPECTED_BAKE_TIME =  40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return time_remaining

def preparation_time_in_minutes(layers):
    """Calculate the preparation time in minutes.

    :param layers: int of layers you want to add.
    :return: int how many minutes you would spend making them.

    Function that takes the of layers you want to add to the lasagna
    an argument and returns how many minutes you would spend making them
    based on the `PREPARATION_TIME`.
    """
    preparation_time = PREPARATION_TIME * layers
    return preparation_time

def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes.

    :param layers: int of layers you want to add.
    :param elapsed_bake_time: int baking time already elapsed.
    :return: int  time elapsed derived in minutes.

    Function that takes the actual minutes the lasagna has been in the oven as
    and the of layers you want to add to the lasagna an argument and returns
    how many minutes the lasagna still needs to bake based on the
    `PREPARATION_TIME`.
    """
    layers_time = PREPARATION_TIME * layers
    elapsed_time = layers_time + elapsed_bake_time
    return elapsed_time