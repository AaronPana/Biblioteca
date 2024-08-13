""" This clase will be used to keep and get the components reference """


class ControlReferences:
    """ControlReference class to store the reference of all components"""

    _controls_reference: dict = {}

    @classmethod
    def add_reference(cls, key: str, value: object) -> None:
        """
        Add a new control reference to the dictionary

        :param key: Key to reference the control
        :type key: str
        :param value: Value to reference the control
        :type value: object
        """
        if not isinstance(key, str):
            raise ValueError("Invalid key")
            # print(f"it was not possible add {value} whit key {key} to the dictionary")
            # return
        cls._controls_reference[key] = value

    @classmethod
    def get_reference(cls, key: str) -> object:
        """
        Get a control reference from the dictionary

        :param key: Key to get the reference
        :type key: str
        :return: Control reference if found
        :rtype: object
        """
        control = cls._controls_reference.get(key, None)
        if not control:
            raise NameError("Control not found")
            # print(f"{key} doesn't reference a control")
            # return
        return control


# Test
if __name__ == "__main__":
    controls1: ControlReferences = ControlReferences()
    my_component: object = object()
    controls1.add_reference("my_component", my_component)

    controls2: ControlReferences = ControlReferences()
    print(controls2.get_reference("my_component"))
# end main
