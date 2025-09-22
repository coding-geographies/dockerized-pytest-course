avinash007ap ➜ /workspaces/dockerized-pytest-course (exceptions) $ git status
On branch exceptions
Your branch is up to date with 'origin/exceptions'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   scripts/chp2/video3/mapmaker_exceptions_start.py
        modified:   tests/chp2/video3/test_exceptions_start.py

no changes added to commit (use "git add" and/or "git commit -a")
@avinash007ap ➜ /workspaces/dockerized-pytest-course (exceptions) $ git add  scripts/chp2/video3/mapmaker_exceptions_start.py  tests/chp2/video3/test_exceptions_start.py
@avinash007ap ➜ /workspaces/dockerized-pytest-course (exceptions) $ git commit -m "Assignment done"
[exceptions b726b64] Assignment done
 2 files changed, 9 insertions(+)
@avinash007ap ➜ /workspaces/dockerized-pytest-course (exceptions) $ git push --set-upstream origin exceptions
Enumerating objects: 17, done.
Counting objects: 100% (17/17), done.
Delta compression using up to 2 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (10/10), 1.18 KiB | 1.18 MiB/s, done.
Total 10 (delta 5), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (5/5), completed with 5 local objects.
To https://github.com/avinash007ap/dockerized-pytest-course
   2abcac5..b726b64  exceptions -> exceptions
branch 'exceptions' set up to track 'origin/exceptions'.
@avinash007ap ➜ /workspaces/dockerized-pytest-course (exceptions) $ git checkout master
Switched to branch 'master'
Your branch is up to date with 'origin/master'.
@avinash007ap ➜ /workspaces/dockerized-pytest-course (master) $ git checkout -b parameter
Switched to a new branch 'parameter'
@avinash007ap ➜ /workspaces/dockerized-pytest-course (parameter) $ 
@avinash007ap ➜ /workspaces/dockerized-pytest-course (parameter) $ git status
On branch parameter
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   tests/chp3/video3/test_parametrize_start.py
        modified:   tests/chp3/video4/test_param_challenge.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        pytest-except-parametrize-output.md
        pytest-git-cmd.md

no changes added to commit (use "git add" and/or "git commit -a")
@avinash007ap ➜ /workspaces/dockerized-pytest-course (parameter) $ git add  tests/chp3/video3/test_parametrize_start.py tests/chp3/video4/test_param_challenge.py pytest-except-parametrize-output.md pytest-git-cmd.md
@avinash007ap ➜ /workspaces/dockerized-pytest-course (parameter) $ git commit -m "Except, param: Assignment completed"
[parameter 698bac3] Except, param: Assignment completed
 4 files changed, 400 insertions(+)
 create mode 100644 pytest-except-parametrize-output.md
 create mode 100644 pytest-git-cmd.md
@avinash007ap ➜ /workspaces/dockerized-pytest-course (parameter) $ git push --set-upstream origin parameter
Enumerating objects: 17, done.
Counting objects: 100% (17/17), done.
Delta compression using up to 2 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (10/10), 5.44 KiB | 5.44 MiB/s, done.
Total 10 (delta 4), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (4/4), completed with 4 local objects.
remote: 
remote: Create a pull request for 'parameter' on GitHub by visiting:
remote:      https://github.com/avinash007ap/dockerized-pytest-course/pull/new/parameter
remote: 
To https://github.com/avinash007ap/dockerized-pytest-course
 * [new branch]      parameter -> parameter
branch 'parameter' set up to track 'origin/parameter'.
@avinash007ap ➜ /workspaces/dockerized-pytest-course (parameter) $ 
