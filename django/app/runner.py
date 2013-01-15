import os

from django.conf import settings
from django.test import TestCase
from django.test.simple import DjangoTestSuiteRunner, reorder_suite
from django.utils.unittest.loader import defaultTestLoader


class DiscoveryRunner(DjangoTestSuiteRunner):

    def build_suite(self, test_labels, extra_tests=None, **kwargs):
        suite = None

        if test_labels:
            suite = defaultTestLoader.loadTestsFromNames(test_labels)

        if suite is None:
            path = os.path.abspath(os.path.join(settings.BASE_PATH, ".."))
            suite = defaultTestLoader.discover(start_dir=path)

        if extra_tests:
            for test in extra_tests:
                suite.addTest(test)

        return reorder_suite(suite, (TestCase,))
