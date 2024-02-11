"""Test the command line interface."""
from src.pyo_proj_amort42.app import main


def test_main(capsys):
    """
    Test the main function with a valid name.

    Args:
        capsys: pytest fixture to capture stdout and stderr.
    """
    assert main(["--name", "test"]) == 0
    out, err = capsys.readouterr()

    # test is a user which does not have any contributions since 2010.
    # Hopefully this will not change in the future and the test will not break.
    assert out == "Hello test!\nYou have 5 repos.\n"
    assert err == ""


def test_main_empty_name(capsys):
    """
    Test the main function with an empty name.

    Args:
        capsys: pytest fixture to capture stdout and stderr.
    """
    assert main(["--name", ""]) == 1
    out, err = capsys.readouterr()
    assert out == "Username cannot be empty\n"
    assert err == ""


def test_main_unknown_name(capsys):
    """
    Test the main function with an incorrect name.

    Args:
        capsys: pytest fixture to capture stdout and stderr.
    """
    assert main(["--name", "bkljbgnhrk;tnhbrnbs;nbdjynbhy,djn"]) == 1
    out, err = capsys.readouterr()
    assert (
        out
        == "Hello bkljbgnhrk;tnhbrnbs;nbdjynbhy,djn!\nstatus.code is 404\nRunning version 0.1.0\n"
    )
    assert err == ""
