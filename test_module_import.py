def test_module_import():
    # Should print "Importing foo"
    import foo

    # Should print "Importing spam"
    import foo.bar

    # Should print "Importing spam"
    import spam

    # Should not fail
    assert foo.bar is spam

    # Should print "Importing spam.eggs"
    import spam.eggs

    # Should print "Importing spam.eggs"
    import foo.bar.eggs

    # Should not fail
    assert foo.bar.eggs is spam.eggs
    assert spam.eggs.hello is foo.bar.eggs.hello
    assert spam.eggs.Eggs is foo.bar.eggs.Eggs
