from path_manager import PathResolver

def test_path_resolver():
    paths = PathResolver()
    assert 'dab_demo/resources' in str(paths.resources)
    assert 'dab_demo/config' in str(paths.config)
    assert 'dab_demo/tests' in str(paths.tests)
