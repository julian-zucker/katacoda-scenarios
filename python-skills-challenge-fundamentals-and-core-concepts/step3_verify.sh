python -c "import assets.step2; assert assets.step2.get_table('abcbcb') == {'a': {'b': 1}, 'b': {'c': 2}, 'c': {'b': 2}}"