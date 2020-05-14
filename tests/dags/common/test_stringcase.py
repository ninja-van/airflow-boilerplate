from common.stringcase import snake_case, kebab_case


def test_snake_case():
    test_cases = [
        (None, None),
        ("", ""),
        ("Foo Bar Baz", "foo_bar_baz"),
        ("FOO BAR BAZ", "foo_bar_baz"),
        ("FooBarBaz", "foo_bar_baz"),
        ("Foo_BAR_Baz", "foo_bar_baz"),
        ("Foo   Bar__Baz", "foo_bar_baz"),
        ("foo_bar_baz", "foo_bar_baz"),
        ("_foo.bar-baz", "foo_bar_baz"),
        ("__foo.bar-baz--", "foo_bar_baz"),
        ("foo-bar-baz", "foo_bar_baz"),
        ("foo.bar.baz", "foo_bar_baz"),
        ("   You shallNot_Pass ", "you_shall_not_pass"),
    ]
    for tc in test_cases:
        assert snake_case(tc[0]) == tc[1], f"snake_case('{tc[0]}') != '{tc[1]}'"


def test_kebab_case():
    test_cases = [
        (None, None),
        ("", ""),
        ("Foo Bar Baz", "foo-bar-baz"),
        ("FOO BAR BAZ", "foo-bar-baz"),
        ("FooBarBaz", "foo-bar-baz"),
        ("Foo_BAR_Baz", "foo-bar-baz"),
        ("Foo   Bar__Baz", "foo-bar-baz"),
        ("foo-bar-baz", "foo-bar-baz"),
        ("-foo.bar_baz", "foo-bar-baz"),
        ("__foo.bar-baz--", "foo-bar-baz"),
        ("foo_bar_baz", "foo-bar-baz"),
        ("foo.bar.baz", "foo-bar-baz"),
        ("foobarbaz", "foobarbaz"),
        ("   You shallNot_Pass ", "you-shall-not-pass"),
    ]
    for tc in test_cases:
        assert kebab_case(tc[0]) == tc[1], f"snake_case('{tc[0]}') != '{tc[1]}'"
