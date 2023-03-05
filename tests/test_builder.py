from python_package_template.builder import Builder


def test_builder_add() -> None:
    builder = Builder("This").add("is").add("a").add("string")

    assert isinstance(builder, Builder)
    assert str(builder) == "This is a string"
