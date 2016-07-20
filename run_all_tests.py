import unittest
import sys
import os
import argparse
from multiprocessing import Pool


def run_all_tests():
    to_run = []
    for solution in find_solutions():
        test = find_test_for_solution(solution)
        if test:
            to_run.append((solution, test))

    pool = Pool()
    failures = pool.map(run_one_testsuite, to_run)
    return [failure for failure in failures if failure]


def print_failures(failures):
    if not failures:
        print("All test cases passed!")

    for solution in failures:
        print("Some test cases failed in {0}".format(solution))


def run_one_testsuite(to_run):
    solution, test = to_run
    sys.path.append(solution)
    results = unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover(test))

    if results.wasSuccessful():
        return None
    else:
        return solution


def find_solutions():
    solutions = set()
    for root, folders, files in os.walk("Solutions"):
        for file_name in files:
            if is_python_file(file_name):
                solutions.add(root)

    return list(solutions)


def find_test_for_solution(solution):
    number = get_solution_number(solution)
    if number:
        return get_course_path(number)


def get_course_path(number):
    path = os.path.join("Course", "Lesson_{0}".format(number))

    if os.path.exists(path) and has_tests(path):
        return path
    else:
        return None


def has_tests(path):
    for file_name in os.listdir(path):
        if is_test_file(file_name):
            return True
    else:
        return False


def get_solution_number(solution):
    try:
        name, number = os.path.basename(solution).split("_")
    except (IndexError, ValueError):
        return None

    return number


def is_test_file(file_name):
    return file_name.lower().startswith("test") and is_python_file(file_name)


def is_python_file(file_name):
    return file_name.lower().endswith(".py")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This tool runs all tests on all solutions. '
                                                 'This is used for continuous integration.')

    parser.parse_args()

    failures = run_all_tests()
    print_failures(failures)

    sys.exit(1 if failures else 0)
