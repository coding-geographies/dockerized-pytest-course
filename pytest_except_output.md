@avinash007ap ➜ /workspaces/dockerized-pytest-course (cmd-output-file) $ pytest -k except
ERROR: usage: pytest [options] [file_or_dir] [file_or_dir] [...]
pytest: error: unrecognized arguments: --pep8 --flakes
  inifile: /workspaces/dockerized-pytest-course/pytest.ini
  rootdir: /workspaces/dockerized-pytest-course

@avinash007ap ➜ /workspaces/dockerized-pytest-course (master) $ docker-compose run test sh
WARN[0000] /workspaces/dockerized-pytest-course/docker-compose.yaml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
WARN[0000] Found orphan containers ([dockerized-pytest-course-test-run-298671421b1c]) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up. 
# pytest -k except
/usr/local/lib/python3.7/site-packages/pep8.py:110: FutureWarning: Possible nested set at position 1
  EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[[({] | []}),;:]')
================================================ test session starts ================================================
platform linux -- Python 3.7.6, pytest-5.2.0, py-1.11.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /pytest_project, inifile: pytest.ini, testpaths: tests
plugins: pep8-1.0.6, cov-2.6.1, pythonpath-0.7.4, flakes-2.0.0
collected 72 items / 68 deselected / 4 selected                                                                     

tests/chp2/video3/test_exceptions_start.py FAILED                                                             [ 25%]
tests/chp2/video3/test_exceptions_start.py FAILED                                                             [ 25%]
tests/chp2/video3/test_exceptions_start.py::test_make_one_point PASSED                                        [ 50%]
tests/chp2/video3/test_exceptions_start.py::test_invalid_point_generation FAILED                              [ 75%]

===================================================== FAILURES ======================================================
__________________________________________________ pyflakes-check ___________________________________________________
/pytest_project/tests/chp2/video3/test_exceptions_start.py:10: UnusedVariable
local variable 'exp' is assigned to but never used
____________________________________________________ PEP8-check _____________________________________________________
/pytest_project/tests/chp2/video3/test_exceptions_start.py:4:1: E302 expected 2 blank lines, found 1
def test_make_one_point():
^
/pytest_project/tests/chp2/video3/test_exceptions_start.py:12:9: E265 block comment should start with '# '
        #raise(Exception)
        ^
/pytest_project/tests/chp2/video3/test_exceptions_start.py:13:1: W391 blank line at end of file

^

___________________________________________ test_invalid_point_generation ___________________________________________

    def test_invalid_point_generation():  # TO DO
        with pytest.raises(Exception) as exp:
>           Point("Buenes Aires", 12.11, -555.34)
E           Failed: DID NOT RAISE <class 'Exception'>

tests/chp2/video3/test_exceptions_start.py:11: Failed
============================================= slowest 10 test durations =============================================

(0.00 durations hidden.  Use -vv to show these durations.)
==================================== 3 failed, 1 passed, 68 deselected in 0.17s =====================================
# pytest -k except
/usr/local/lib/python3.7/site-packages/pep8.py:110: FutureWarning: Possible nested set at position 1
  EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[[({] | []}),;:]')
================================================ test session starts ================================================
platform linux -- Python 3.7.6, pytest-5.2.0, py-1.11.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /pytest_project, inifile: pytest.ini, testpaths: tests
plugins: pep8-1.0.6, cov-2.6.1, pythonpath-0.7.4, flakes-2.0.0
collected 72 items / 68 deselected / 4 selected                                                                     

tests/chp2/video3/test_exceptions_start.py FAILED                                                             [ 25%]
tests/chp2/video3/test_exceptions_start.py FAILED                                                             [ 25%]
tests/chp2/video3/test_exceptions_start.py::test_make_one_point FAILED                                        [ 50%]
tests/chp2/video3/test_exceptions_start.py::test_invalid_point_generation FAILED                              [ 75%]

===================================================== FAILURES ======================================================
__________________________________________________ pyflakes-check ___________________________________________________
/pytest_project/tests/chp2/video3/test_exceptions_start.py:10: UnusedVariable
local variable 'exp' is assigned to but never used
____________________________________________________ PEP8-check _____________________________________________________
/pytest_project/tests/chp2/video3/test_exceptions_start.py:4:1: E302 expected 2 blank lines, found 1
def test_make_one_point():
^
/pytest_project/tests/chp2/video3/test_exceptions_start.py:12:9: E265 block comment should start with '# '
        #raise(Exception)
        ^
/pytest_project/tests/chp2/video3/test_exceptions_start.py:13:1: W391 blank line at end of file

^

________________________________________________ test_make_one_point ________________________________________________

    def test_make_one_point():
>       p1 = Point("Dakar", 14.7167, 17.4677)

tests/chp2/video3/test_exceptions_start.py:5: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <scripts.chp2.video3.mapmaker_exceptions_start.Point object at 0x7ea59ca38c90>, name = 'Dakar'
latitude = 14.7167, longitude = 17.4677

    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
    
        if not (-90 <= latitude <= 90) or (-90 <= longitude <= 90):
>           raise ValueError("Invalid latitude or longitude")
E           ValueError: Invalid latitude or longitude

scripts/chp2/video3/mapmaker_exceptions_start.py:9: ValueError
___________________________________________ test_invalid_point_generation ___________________________________________

    def test_invalid_point_generation():  # TO DO
        with pytest.raises(Exception) as exp:
>           Point("Buenes Aires", 12.11, -555.34)
E           Failed: DID NOT RAISE <class 'Exception'>

tests/chp2/video3/test_exceptions_start.py:11: Failed
============================================= slowest 10 test durations =============================================

(0.00 durations hidden.  Use -vv to show these durations.)
========================================= 4 failed, 68 deselected in 0.12s ==========================================
# 
# 
# pytest -k except
/usr/local/lib/python3.7/site-packages/pep8.py:110: FutureWarning: Possible nested set at position 1
  EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[[({] | []}),;:]')
================================================ test session starts ================================================
platform linux -- Python 3.7.6, pytest-5.2.0, py-1.11.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /pytest_project, inifile: pytest.ini, testpaths: tests
plugins: pep8-1.0.6, cov-2.6.1, pythonpath-0.7.4, flakes-2.0.0
collected 72 items / 68 deselected / 4 selected                                                                     

tests/chp2/video3/test_exceptions_start.py FAILED                                                             [ 25%]
tests/chp2/video3/test_exceptions_start.py FAILED                                                             [ 25%]
tests/chp2/video3/test_exceptions_start.py::test_make_one_point FAILED                                        [ 50%]
tests/chp2/video3/test_exceptions_start.py::test_invalid_point_generation FAILED                              [ 75%]

===================================================== FAILURES ======================================================
__________________________________________________ pyflakes-check ___________________________________________________
/pytest_project/tests/chp2/video3/test_exceptions_start.py:10: UnusedVariable
local variable 'exp' is assigned to but never used
____________________________________________________ PEP8-check _____________________________________________________
/pytest_project/tests/chp2/video3/test_exceptions_start.py:4:1: E302 expected 2 blank lines, found 1
def test_make_one_point():
^
/pytest_project/tests/chp2/video3/test_exceptions_start.py:12:9: E265 block comment should start with '# '
        #raise(Exception)
        ^
/pytest_project/tests/chp2/video3/test_exceptions_start.py:14:1: W391 blank line at end of file

^

________________________________________________ test_make_one_point ________________________________________________

    def test_make_one_point():
>       p1 = Point("Dakar", 14.7167, 17.4677)

tests/chp2/video3/test_exceptions_start.py:5: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <scripts.chp2.video3.mapmaker_exceptions_start.Point object at 0x78d1811bb890>, name = 'Dakar'
latitude = 14.7167, longitude = 17.4677

    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
    
        if not (-90 <= latitude <= 90) or (-90 <= longitude <= 90):
>           raise ValueError("Invalid latitude or longitude")
E           ValueError: Invalid latitude or longitude

scripts/chp2/video3/mapmaker_exceptions_start.py:9: ValueError
___________________________________________ test_invalid_point_generation ___________________________________________

    def test_invalid_point_generation():  # TO DO
        with pytest.raises(Exception) as exp:
>           Point("Buenes Aires", 12.11, -555.34)
E           Failed: DID NOT RAISE <class 'Exception'>

tests/chp2/video3/test_exceptions_start.py:11: Failed
============================================= slowest 10 test durations =============================================

(0.00 durations hidden.  Use -vv to show these durations.)
========================================= 4 failed, 68 deselected in 0.12s ==========================================
# 
# 
# 
# breakpoint()
> 
> {k:v for k, v in locals().items() if '__' not in k and 'pdb' not in k}
sh: 11: Syntax error: "(" unexpected
# {k:v for k, v in locals().items() if '__' not in k and 'pdb' not in k}^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^[[D^                                               
sh: 11: Syntax error: "(" unexpected
# {k:v for k,v in locals().items if '__' not in k and 'pdb' not in k}
sh: 11: Syntax error: "(" unexpected
# dir(exp)
sh: 11: Syntax error: word unexpected (expecting ")")
# sh: 11: Syntax error: ")" unexpected
# exit

@avinash007ap ➜ /workspaces/dockerized-pytest-course (master) $ docker-compose run test sh
WARN[0000] /workspaces/dockerized-pytest-course/docker-compose.yaml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
WARN[0000] Found orphan containers ([dockerized-pytest-course-test-run-a9ca0c8a438b dockerized-pytest-course-test-run-298671421b1c]) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up. 
# dir(exp)
sh: 1: Syntax error: word unexpected (expecting ")")
# sh: 1: Syntax error: ")" unexpected
# 
# 
# pytest -k except
/usr/local/lib/python3.7/site-packages/pep8.py:110: FutureWarning: Possible nested set at position 1
  EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[[({] | []}),;:]')
================================================ test session starts ================================================
platform linux -- Python 3.7.6, pytest-5.2.0, py-1.11.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /pytest_project, inifile: pytest.ini, testpaths: tests
plugins: pep8-1.0.6, cov-2.6.1, pythonpath-0.7.4, flakes-2.0.0
collected 72 items / 68 deselected / 4 selected                                                                     

tests/chp2/video3/test_exceptions_start.py PASSED                                                             [ 25%]
tests/chp2/video3/test_exceptions_start.py FAILED                                                             [ 25%]
tests/chp2/video3/test_exceptions_start.py::test_make_one_point FAILED                                        [ 50%]
tests/chp2/video3/test_exceptions_start.py::test_invalid_point_generation FAILED                              [ 75%]

===================================================== FAILURES ======================================================
____________________________________________________ PEP8-check _____________________________________________________
/pytest_project/tests/chp2/video3/test_exceptions_start.py:4:1: E302 expected 2 blank lines, found 1
def test_make_one_point():
^

________________________________________________ test_make_one_point ________________________________________________

    def test_make_one_point():
>       p1 = Point("Dakar", 14.7167, 17.4677)

tests/chp2/video3/test_exceptions_start.py:5: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <scripts.chp2.video3.mapmaker_exceptions_start.Point object at 0x77efb75bb590>, name = 'Dakar'
latitude = 14.7167, longitude = 17.4677

    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
    
        if not (-90 <= latitude <= 90) or (-90 <= longitude <= 90):
>           raise ValueError("Invalid latitude or longitude")
E           ValueError: Invalid latitude or longitude

scripts/chp2/video3/mapmaker_exceptions_start.py:9: ValueError
___________________________________________ test_invalid_point_generation ___________________________________________

    def test_invalid_point_generation():  # TO DO
        # with pytest.raises(Exception) as exp:
        #     Point("Buenes Aires", 12.11, -555.34)
        #     #raise(Exception)
        # breakpoint()
        with pytest.raises(ValueError) as exp:
            Point("Buenes Aires", 12.11, -555.34)
>           assert str(exp.value) == "Invalid latitude or longitude"

tests/chp2/video3/test_exceptions_start.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <ExceptionInfo for raises contextmanager>

    @property
    def value(self) -> _E:
        """the exception value"""
        assert (
            self._excinfo is not None
>       ), ".value can only be used after the context manager exits"
E       AssertionError: .value can only be used after the context manager exits

/usr/local/lib/python3.7/site-packages/_pytest/_code/code.py:477: AssertionError
============================================= slowest 10 test durations =============================================

(0.00 durations hidden.  Use -vv to show these durations.)
==================================== 3 failed, 1 passed, 68 deselected in 0.14s =====================================
# pytest -k except
/usr/local/lib/python3.7/site-packages/pep8.py:110: FutureWarning: Possible nested set at position 1
  EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[[({] | []}),;:]')
================================================ test session starts ================================================
platform linux -- Python 3.7.6, pytest-5.2.0, py-1.11.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /pytest_project, inifile: pytest.ini, testpaths: tests
plugins: pep8-1.0.6, cov-2.6.1, pythonpath-0.7.4, flakes-2.0.0
collected 72 items / 68 deselected / 4 selected                                                                     

tests/chp2/video3/test_exceptions_start.py PASSED                                                             [ 25%]
tests/chp2/video3/test_exceptions_start.py FAILED                                                             [ 25%]
tests/chp2/video3/test_exceptions_start.py::test_make_one_point FAILED                                        [ 50%]
tests/chp2/video3/test_exceptions_start.py::test_invalid_point_generation FAILED                              [ 75%]

===================================================== FAILURES ======================================================
____________________________________________________ PEP8-check _____________________________________________________
/pytest_project/tests/chp2/video3/test_exceptions_start.py:4:1: E302 expected 2 blank lines, found 1
def test_make_one_point():
^

________________________________________________ test_make_one_point ________________________________________________

    def test_make_one_point():
>       p1 = Point("Dakar", 14.7167, 17.4677)

tests/chp2/video3/test_exceptions_start.py:5: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <scripts.chp2.video3.mapmaker_exceptions_start.Point object at 0x7e4c7388f550>, name = 'Dakar'
latitude = 14.7167, longitude = 17.4677

    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
    
        if not (-90 <= latitude <= 90) or (-90 <= longitude <= 90):
>           raise ValueError("Invalid latitude or longitude")
E           ValueError: Invalid latitude or longitude

scripts/chp2/video3/mapmaker_exceptions_start.py:9: ValueError
___________________________________________ test_invalid_point_generation ___________________________________________

    def test_invalid_point_generation():  # TO DO
        # with pytest.raises(Exception) as exp:
        #     Point("Buenes Aires", 12.11, -555.34)
        #     #raise(Exception)
        # breakpoint()
        with pytest.raises(ValueError) as exp:
>           Point("Buenes Aires", 12.11, -555.34)
E           Failed: DID NOT RAISE <class 'ValueError'>

tests/chp2/video3/test_exceptions_start.py:15: Failed
============================================= slowest 10 test durations =============================================

(0.00 durations hidden.  Use -vv to show these durations.)
==================================== 3 failed, 1 passed, 68 deselected in 0.16s =====================================
# pytest -k except
/usr/local/lib/python3.7/site-packages/pep8.py:110: FutureWarning: Possible nested set at position 1
  EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[[({] | []}),;:]')
================================================ test session starts ================================================
platform linux -- Python 3.7.6, pytest-5.2.0, py-1.11.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /pytest_project, inifile: pytest.ini, testpaths: tests
plugins: pep8-1.0.6, cov-2.6.1, pythonpath-0.7.4, flakes-2.0.0
collected 72 items / 68 deselected / 4 selected                                                                     

tests/chp2/video3/test_exceptions_start.py SKIPPED                                                            [ 25%]
tests/chp2/video3/test_exceptions_start.py FAILED                                                             [ 25%]
tests/chp2/video3/test_exceptions_start.py::test_make_one_point PASSED                                        [ 50%]
tests/chp2/video3/test_exceptions_start.py::test_invalid_point_generation PASSED                              [ 75%]

===================================================== FAILURES ======================================================
____________________________________________________ PEP8-check _____________________________________________________
/pytest_project/tests/chp2/video3/test_exceptions_start.py:4:1: E302 expected 2 blank lines, found 1
def test_make_one_point():
^

============================================= slowest 10 test durations =============================================

(0.00 durations hidden.  Use -vv to show these durations.)
=============================== 1 failed, 2 passed, 1 skipped, 68 deselected in 0.09s ===============================
# 