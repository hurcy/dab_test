from path_manager import PathResolver

def test_path_resolver():
    paths = PathResolver()
    assert 'dab_demo/resources' in str(paths.resources)
    assert 'common_framework' in str(paths.common_framework)
    assert 'dab_demo/tests' in str(paths.tests)
