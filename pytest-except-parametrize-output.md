@avinash007ap ➜ /workspaces/dockerized-pytest-course (exceptions) $ docker-compose
Usage:  docker compose [OPTIONS] COMMAND

Define and run multi-container applications with Docker

Options:
      --all-resources              Include all resources, even those not used by services
      --ansi string                Control when to print ANSI control characters ("never"|"always"|"auto") (default "auto")
      --compatibility              Run compose in backward compatibility mode
      --dry-run                    Execute command in dry run mode
      --env-file stringArray       Specify an alternate environment file
  -f, --file stringArray           Compose configuration files
      --parallel int               Control max parallelism, -1 for unlimited (default -1)
      --profile stringArray        Specify a profile to enable
      --progress string            Set type of progress output (auto, tty, plain, json, quiet)
      --project-directory string   Specify an alternate working directory
                                   (default: the path of the, first specified, Compose file)
  -p, --project-name string        Project name

Management Commands:
  bridge      Convert compose files into another model

Commands:
  attach      Attach local standard input, output, and error streams to a service's running container
  build       Build or rebuild services
  commit      Create a new image from a service container's changes
  config      Parse, resolve and render compose file in canonical format
  cp          Copy files/folders between a service container and the local filesystem
  create      Creates containers for a service
  down        Stop and remove containers, networks
  events      Receive real time events from containers
  exec        Execute a command in a running container
  export      Export a service container's filesystem as a tar archive
  images      List images used by the created containers
  kill        Force stop service containers
  logs        View output from containers
  ls          List running compose projects
  pause       Pause services
  port        Print the public port for a port binding
  ps          List containers
  publish     Publish compose application
  pull        Pull service images
  push        Push service images
  restart     Restart service containers
  rm          Removes stopped service containers
  run         Run a one-off command on a service
  scale       Scale services 
  start       Start services
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop services
  top         Display the running processes
  unpause     Unpause services
  up          Create and start containers
  version     Show the Docker Compose version information
  volumes     List volumes
  wait        Block until containers of all (or specified) services stop.
  watch       Watch build context for service and rebuild/refresh containers when files are updated

Run 'docker compose COMMAND --help' for more information on a command.
@avinash007ap ➜ /workspaces/dockerized-pytest-course (exceptions) $ 
@avinash007ap ➜ /workspaces/dockerized-pytest-course (exceptions) $ docker-compose build
WARN[0000] /workspaces/dockerized-pytest-course/docker-compose.yaml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Building 2.6s (16/16) FINISHED                                                                                                                             
 => [internal] load local bake definitions                                                                                                                0.0s
 => => reading from stdin 386B                                                                                                                            0.0s
 => [internal] load build definition from Dockerfile                                                                                                      0.0s
 => => transferring dockerfile: 348B                                                                                                                      0.0s
 => [internal] load metadata for docker.io/library/python:3.7.6-buster                                                                                    2.4s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                             0.0s
 => [internal] load .dockerignore                                                                                                                         0.0s
 => => transferring context: 2B                                                                                                                           0.0s
 => [1/8] FROM docker.io/library/python:3.7.6-buster@sha256:10eacbe8c336fbd0343661c2f831f6a1a6164770dcc95116c1328246673c8947                              0.0s
 => [internal] load build context                                                                                                                         0.0s
 => => transferring context: 70B                                                                                                                          0.0s
 => CACHED [2/8] RUN mkdir /pytest_project/                                                                                                               0.0s
 => CACHED [3/8] COPY ./test-requirements.txt /pytest_project/                                                                                            0.0s
 => CACHED [4/8] COPY ./setup.py ./setup.py                                                                                                               0.0s
 => CACHED [5/8] RUN pip install --upgrade pip                                                                                                            0.0s
 => CACHED [6/8] RUN pip install -e .                                                                                                                     0.0s
 => CACHED [7/8] RUN pip3 install -r /pytest_project/test-requirements.txt                                                                                0.0s
 => CACHED [8/8] WORKDIR /pytest_project/                                                                                                                 0.0s
 => exporting to image                                                                                                                                    0.0s
 => => exporting layers                                                                                                                                   0.0s
 => => writing image sha256:7f1daf29c600435a2ddba2302e4126bf080b6b2dfaa2258090692e8f987ac5cc                                                              0.0s
 => => naming to docker.io/library/dockerized-pytest-course-test                                                                                          0.0s
 => resolving provenance for metadata file                                                                                                                0.0s
[+] Building 1/1
 ✔ test  Built                                                                                                                                            0.0s 
@avinash007ap ➜ /workspaces/dockerized-pytest-course (exceptions) $ docker-compose run test sh
WARN[0000] /workspaces/dockerized-pytest-course/docker-compose.yaml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
WARN[0000] Found orphan containers ([dockerized-pytest-course-test-run-3d82d1846649 dockerized-pytest-course-test-run-a9ca0c8a438b dockerized-pytest-course-test-run-298671421b1c]) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up. 
# 
# pytest -k "invalid_city_name"
/usr/local/lib/python3.7/site-packages/pep8.py:110: FutureWarning: Possible nested set at position 1
  EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[[({] | []}),;:]')
===================================================================== test session starts =====================================================================
platform linux -- Python 3.7.6, pytest-5.2.0, py-1.11.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /pytest_project, inifile: pytest.ini, testpaths: tests
plugins: pep8-1.0.6, cov-2.6.1, pythonpath-0.7.4, flakes-2.0.0
collected 73 items / 72 deselected / 1 selected                                                                                                               

tests/chp2/video3/test_exceptions_start.py::test_invalid_city_name PASSED                                                                               [100%]

================================================================== slowest 10 test durations ==================================================================

(0.00 durations hidden.  Use -vv to show these durations.)
============================================================== 1 passed, 72 deselected in 0.16s ===============================================================
# pytest -vv -k "invalid_city_name"
/usr/local/lib/python3.7/site-packages/pep8.py:110: FutureWarning: Possible nested set at position 1
  EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[[({] | []}),;:]')
===================================================================== test session starts =====================================================================
platform linux -- Python 3.7.6, pytest-5.2.0, py-1.11.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /pytest_project, inifile: pytest.ini, testpaths: tests
plugins: pep8-1.0.6, cov-2.6.1, pythonpath-0.7.4, flakes-2.0.0
collected 73 items / 72 deselected / 1 selected                                                                                                               

tests/chp2/video3/test_exceptions_start.py::test_invalid_city_name PASSED                                                                               [100%]

================================================================== slowest 10 test durations ==================================================================
0.00s setup    tests/chp2/video3/test_exceptions_start.py::test_invalid_city_name
0.00s teardown tests/chp2/video3/test_exceptions_start.py::test_invalid_city_name
0.00s call     tests/chp2/video3/test_exceptions_start.py::test_invalid_city_name
============================================================== 1 passed, 72 deselected in 0.09s ===============================================================
# ^[[A : not found
# pytest -vv -k "invalid_city_name"
/usr/local/lib/python3.7/site-packages/pep8.py:110: FutureWarning: Possible nested set at position 1
  EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[[({] | []}),;:]')
===================================================================== test session starts =====================================================================
platform linux -- Python 3.7.6, pytest-5.2.0, py-1.11.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /pytest_project, inifile: pytest.ini, testpaths: tests
plugins: pep8-1.0.6, cov-2.6.1, pythonpath-0.7.4, flakes-2.0.0
collected 73 items / 72 deselected / 1 selected                                                                                                               

tests/chp2/video3/test_exceptions_start.py::test_invalid_city_name 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> PDB set_trace (IO-capturing turned off) >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
--Return--
> /pytest_project/tests/chp2/video3/test_exceptions_start.py(22)test_invalid_city_name()->None
-> breakpoint()
(Pdb) 
(Pdb) --KeyboardInterrupt--
(Pdb) exit()


================================================================== slowest 10 test durations ==================================================================
0.00s setup    tests/chp2/video3/test_exceptions_start.py::test_invalid_city_name
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! _pytest.outcomes.Exit: Quitting debugger !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
=================================================================== 72 deselected in 32.70s ===================================================================
# pytest -vv -k "invalid_city_name"
/usr/local/lib/python3.7/site-packages/pep8.py:110: FutureWarning: Possible nested set at position 1
  EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[[({] | []}),;:]')
===================================================================== test session starts =====================================================================
platform linux -- Python 3.7.6, pytest-5.2.0, py-1.11.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /pytest_project, inifile: pytest.ini, testpaths: tests
plugins: pep8-1.0.6, cov-2.6.1, pythonpath-0.7.4, flakes-2.0.0
collected 73 items / 72 deselected / 1 selected                                                                                                               

tests/chp2/video3/test_exceptions_start.py::test_invalid_city_name PASSED                                                                               [100%]

================================================================== slowest 10 test durations ==================================================================
0.00s call     tests/chp2/video3/test_exceptions_start.py::test_invalid_city_name
0.00s teardown tests/chp2/video3/test_exceptions_start.py::test_invalid_city_name
0.00s setup    tests/chp2/video3/test_exceptions_start.py::test_invalid_city_name
============================================================== 1 passed, 72 deselected in 0.08s ===============================================================
# 
# 
# pytest -k "with_param"
/usr/local/lib/python3.7/site-packages/pep8.py:110: FutureWarning: Possible nested set at position 1
  EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[[({] | []}),;:]')
============================================================ test session starts =============================================================
platform linux -- Python 3.7.6, pytest-5.2.0, py-1.11.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /pytest_project, inifile: pytest.ini, testpaths: tests
plugins: pep8-1.0.6, cov-2.6.1, pythonpath-0.7.4, flakes-2.0.0
collected 71 items / 1 errors / 71 deselected                                                                                                

=================================================================== ERRORS ===================================================================
_________________________________________ ERROR collecting tests/chp3/video4/test_param_challenge.py _________________________________________
In test_csv_writer_with_param: function uses no argument 'country'
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 errors during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
====================================================== 71 deselected, 1 error in 0.16s =======================================================
# pytest -k "with_param" -vv                                                                
/usr/local/lib/python3.7/site-packages/pep8.py:110: FutureWarning: Possible nested set at position 1
  EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[[({] | []}),;:]')
============================================================ test session starts =============================================================
platform linux -- Python 3.7.6, pytest-5.2.0, py-1.11.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /pytest_project, inifile: pytest.ini, testpaths: tests
plugins: pep8-1.0.6, cov-2.6.1, pythonpath-0.7.4, flakes-2.0.0
collected 71 items / 1 errors / 71 deselected                                                                                                

=================================================================== ERRORS ===================================================================
_________________________________________ ERROR collecting tests/chp3/video4/test_param_challenge.py _________________________________________
In test_csv_writer_with_param: function uses no argument 'country'
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 errors during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
====================================================== 71 deselected, 1 error in 0.13s =======================================================
# pytest -k "with_param" -vv
/usr/local/lib/python3.7/site-packages/pep8.py:110: FutureWarning: Possible nested set at position 1
  EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[[({] | []}),;:]')
============================================================ test session starts =============================================================
platform linux -- Python 3.7.6, pytest-5.2.0, py-1.11.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /pytest_project, inifile: pytest.ini, testpaths: tests
plugins: pep8-1.0.6, cov-2.6.1, pythonpath-0.7.4, flakes-2.0.0
collected 75 items / 72 deselected / 3 selected                                                                                              

tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Andorra-Mean-1641.42] FAILED                                     [ 33%]
tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Andorra-Median-1538.01] FAILED                                   [ 66%]
tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Argentina-Median-125.0] PASSED                                   [100%]

================================================================== FAILURES ==================================================================
______________________________________________ test_csv_writer_with_param[Andorra-Mean-1641.42] ______________________________________________

process_data = <function process_data.<locals>._specify_type at 0x7ad6e5c0e950>, country = 'Andorra', stat = 'Mean', expected = 1641.42

    @pytest.mark.parametrize("country,stat,expected",
    [
        ('Andorra', 'Mean', 1641.42),
        ('Andorra', 'Median', 1538.01),
        ('Argentina', 'Median', 125.0)
    ])
    def test_csv_writer_with_param(process_data, country, stat, expected):
        """
         TO DO: Update the function to be parametrized with 3 scenarios:
         ('Andorra', 'Mean', 1641.42),
         ('Andorra', 'Median', 1538.02),
         ('Argentina', 'Median', 125.0),
    
        Hint:
        - In the final assertion, you will need to use an f-string to inject the
          arguments into the final string.
    
        - For example: f'{stat} would inject the string statistic that we use for
          the csv writer.
        """
        data = process_data(file_name_or_type="clean_map.csv")
        andorran_median_res = data_aggregator.atitude_stat_per_country(data, country, stat)
        output_location = StringIO()
        data_aggregator.csv_writer(andorran_median_res, output_location)
    
        res = output_location.getvalue().strip('\r\n')
>       assert res == f'Country,Median\r\n{country},{expected}'
E       AssertionError: assert 'Country,Mean...dorra,1641.42' == 'Country,Medi...dorra,1641.42'
E         - Country,Mean
E         + Country,Median
E         ?           ++
E           Andorra,1641.42

tests/chp3/video4/test_param_challenge.py:77: AssertionError
_____________________________________________ test_csv_writer_with_param[Andorra-Median-1538.01] _____________________________________________

process_data = <function process_data.<locals>._specify_type at 0x7ad6e5c0e950>, country = 'Andorra', stat = 'Median', expected = 1538.01

    @pytest.mark.parametrize("country,stat,expected",
    [
        ('Andorra', 'Mean', 1641.42),
        ('Andorra', 'Median', 1538.01),
        ('Argentina', 'Median', 125.0)
    ])
    def test_csv_writer_with_param(process_data, country, stat, expected):
        """
         TO DO: Update the function to be parametrized with 3 scenarios:
         ('Andorra', 'Mean', 1641.42),
         ('Andorra', 'Median', 1538.02),
         ('Argentina', 'Median', 125.0),
    
        Hint:
        - In the final assertion, you will need to use an f-string to inject the
          arguments into the final string.
    
        - For example: f'{stat} would inject the string statistic that we use for
          the csv writer.
        """
        data = process_data(file_name_or_type="clean_map.csv")
        andorran_median_res = data_aggregator.atitude_stat_per_country(data, country, stat)
        output_location = StringIO()
        data_aggregator.csv_writer(andorran_median_res, output_location)
    
        res = output_location.getvalue().strip('\r\n')
>       assert res == f'Country,Median\r\n{country},{expected}'
E       AssertionError: assert 'Country,Medi...dorra,1538.02' == 'Country,Medi...dorra,1538.01'
E           Country,Median
E         - Andorra,1538.02
E         ?               ^
E         + Andorra,1538.01
E         ?               ^

tests/chp3/video4/test_param_challenge.py:77: AssertionError
========================================================= slowest 10 test durations ==========================================================
0.00s call     tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Andorra-Mean-1641.42]
0.00s call     tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Argentina-Median-125.0]
0.00s call     tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Andorra-Median-1538.01]
0.00s setup    tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Andorra-Mean-1641.42]
0.00s setup    tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Argentina-Median-125.0]
0.00s teardown tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Argentina-Median-125.0]
0.00s setup    tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Andorra-Median-1538.01]
0.00s teardown tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Andorra-Mean-1641.42]
0.00s teardown tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Andorra-Median-1538.01]
================================================= 2 failed, 1 passed, 72 deselected in 0.11s =================================================
# 
# ^[[A  : not found
# : 13: 
# pytest -k "with_param" -vv
/usr/local/lib/python3.7/site-packages/pep8.py:110: FutureWarning: Possible nested set at position 1
  EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[[({] | []}),;:]')
============================================================ test session starts =============================================================
platform linux -- Python 3.7.6, pytest-5.2.0, py-1.11.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /pytest_project, inifile: pytest.ini, testpaths: tests
plugins: pep8-1.0.6, cov-2.6.1, pythonpath-0.7.4, flakes-2.0.0
collected 75 items / 72 deselected / 3 selected                                                                                              

tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Andorra-Mean-1641.42] PASSED                                     [ 33%]
tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Andorra-Median-1538.02] PASSED                                   [ 66%]
tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Argentina-Median-125.0] PASSED                                   [100%]

========================================================= slowest 10 test durations ==========================================================
0.00s call     tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Argentina-Median-125.0]
0.00s call     tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Andorra-Mean-1641.42]
0.00s call     tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Andorra-Median-1538.02]
0.00s setup    tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Andorra-Mean-1641.42]
0.00s setup    tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Argentina-Median-125.0]
0.00s setup    tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Andorra-Median-1538.02]
0.00s teardown tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Argentina-Median-125.0]
0.00s teardown tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Andorra-Median-1538.02]
0.00s teardown tests/chp3/video4/test_param_challenge.py::test_csv_writer_with_param[Andorra-Mean-1641.42]
====================================================== 3 passed, 72 deselected in 0.08s ======================================================
# 