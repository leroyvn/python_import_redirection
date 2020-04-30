def test_class_import():
    import foo.bar.eggs
    e1 = foo.bar.eggs.Eggs()
    import spam.eggs
    e2 = foo.bar.eggs.Eggs()
    e3 = spam.eggs.Eggs()

    # All three objects should be spam.eggs.Eggs instances
    assert isinstance(e1, spam.eggs.Eggs)
    assert isinstance(e2, spam.eggs.Eggs)
    assert isinstance(e3, spam.eggs.Eggs)

    # Both Eggs classes should be equivalent
    assert foo.bar.eggs.Eggs is spam.eggs.Eggs
