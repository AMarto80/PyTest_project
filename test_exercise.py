import pytest

def admin_command(command, sudo=True):
    """
    Prefix a command with `sudo` unless it is explicitly not needed. Expects
    `command` to be a list.
    """
    if not isinstance(command, list):
        raise TypeError(f"was expecting command to be a list, but got a {type(command)}")

    if sudo:
        return ["sudo"] + command #OR (command = ["sudo"] + command)
    return command

class TestAdminCommand:

    def command(self):
        return ["ps", "aux"]

    def invalid_comand(self): # optional method
        return "some comand"

    def test_no_sudo(self):
        result = admin_command(self.command(), sudo=False)
        assert result == self.command()

    def test_sudo(self):
        result = admin_command(self.command(), sudo=True)
        expected = ["sudo"] + self.command()
        assert result == expected
    '''
    def test_non_list_commands(self):
        with pytest.raises(TypeError) as error:
            admin_command("some command", sudo=True) # Because "some command" is a <str> and not a <list>, 
                                                     # admin_command function throws an exception immediately, standard execution stops,
                                                     # preventing you from inspecting standard return frames. 
        assert error.value.args[0] == "was expecting command to be a list, but got a <class 'str'>"
    '''

    ''' 
   # A generic funtion:
    def test_non_list_commands(self):
        invalid_cmd = "some command" # <str>
        # invalid_cmd = 1 # <int>

        with pytest.raises(TypeError) as error:
            admin_command(invalid_cmd, sudo=True)

        assert error.value.args[0] == f"was expecting command to be a list, but got a {type(invalid_cmd)}"
        #print (error.value.args[0])
        #print(type(invalid_cmd))
    '''

    def test_non_list_commands(self):
        with pytest.raises(TypeError) as error:
            admin_command(self.invalid_comand(), sudo=True)
    
        assert error.value.args[0] == f"was expecting command to be a list, but got a {type(self.invalid_comand())}"
        #print (error.value.args[0])
        #print(type(self.invalid_comand()))
