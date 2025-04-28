from app import change


def test_change():
    assert [{"ten_rupee_coins": 4}, {"five_rupee_coins": 1}] == change(45)
