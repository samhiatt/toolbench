import pytest
import toolbench
from toolbench import tools

def test_print_module_versions(capsys):
    tools.print_module_versions(globals())
    captured = capsys.readouterr()
    assert 'pytest' in captured.out, "'pytest' was printed to sys.stdout."

def test_get_module_versions():
    versions = tools.get_module_versions(globals())
    print(versions)
    assert 'pytest' in versions.keys(), "pytest should be in versions dict."
    assert type(versions['pytest']) is set, "Versions dict should contain sets of version strings."
    assert len(versions['pytest'].intersection({pytest.__version__}))>0, \
           "pytest.__version__ should be in versions['pytest'] set."

    assert 'toolbench' in versions.keys(), "toolbench should be in versions dict."
    assert len(versions['toolbench'].intersection({toolbench.__version__}))>0, \
           "toolbench.__version__ should be in versions['toolbench'] set."
