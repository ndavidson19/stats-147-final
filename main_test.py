from main import coin_toss, weighted_coin_toss

def test_coin_toss():
    # Test that the coin toss function returns a tuple
    assert isinstance(coin_toss(1000), tuple)

def test_coin_toss_length():
    # Test that the coin toss function returns a tuple of length 2
    assert len(coin_toss(1000)) == 2

def test_coin_toss_values():
    # Test that the coin toss function returns a tuple of integers
    assert isinstance(coin_toss(1000)[0], int)
    assert isinstance(coin_toss(1000)[1], int)

def test_weighted_coin_toss():
    # Test that the weighted coin toss function returns a tuple
    assert isinstance(weighted_coin_toss(1000), tuple)

def test_weighted_coin_toss_length():
    # Test that the weighted coin toss function returns a tuple of length 2
    assert len(weighted_coin_toss(1000)) == 2

def test_weighted_coin_toss_values():
    # Test that the weighted coin toss function returns a tuple of integers
    assert isinstance(weighted_coin_toss(1000)[0], int)
    assert isinstance(weighted_coin_toss(1000)[1], int)



