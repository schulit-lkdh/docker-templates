#!/usr/bin/env python
import subprocess as sp
import sys
import time

import git

REGISTRY_URL = 'our.private.registry'


def main():
    changed_dockerfiles = [f.a_path for f in git.Repo('.').index.diff("HEAD~1")
        if f.a_path.startswith("base/")]
    n_files = len(changed_dockerfiles)

    if n_files == 0:
        print("Nothing to do!")
        exit(0)

    print("Processing {} dockerfile{}..."
          .format(n_files, 's' if n_files else ''))
    for idx, fname in enumerate(changed_dockerfiles):
        progress = "({}/{})".format(idx + 1, n_files)

        steps = [("Building",
                    "docker build --pull -t {0}/{1} -f {1} . "
                    .format(REGISTRY_URL, fname)),
                 ("Pushing",
                    "docker push {0}/{1}"
                    .format(REGISTRY_URL, fname))]

        print('-' * 79)

        for step, cmd in steps:
            print("{} {} '{}'".format(progress, step, fname))
            child = sp.Popen(
                cmd, shell=True, stdout=sys.stdout, stderr=sys.stderr)
            child.communicate()


if __name__ == '__main__':
    main()


