# -*- coding: utf-8 -*-

"""Basic functionality tests for proving that ZigZag can publish results to qTest accurately."""

# ======================================================================================================================
# Imports
# ======================================================================================================================
import uuid
import pytest


# ======================================================================================================================
# Test Suites
# ======================================================================================================================
class TestGlobalProperties(object):
    """Test cases for tests with 'Passed' status in qTest."""

    # noinspection PyUnresolvedReferences
    def test_use_cli_to_supply_global_properties(self, single_passing_test_for_asc):
        """Verify ZigZag can publish results from the "asc" CI environment with one passing test in the JUnitXML
        file.
        """
        # use the defaults for MK8s to test we can override
        properties_from_cli = {"BUILD_URL": "BUILD_URL",
                              "BUILD_NUMBER": "BUILD_NUMBER",
                              "BUILD_ID": "BUILD_ID",
                              "JOB_NAME": "JOB_NAME",
                              "BUILD_TAG": "BUILD_TAG",
                              "JENKINS_URL": "JENKINS_URL",
                              "EXECUTOR_NUMBER": "EXECUTOR_NUMBER",
                              "WORKSPACE": "WORKSPACE",
                              "CVS_BRANCH": "CVS_BRANCH",
                              "GIT_COMMIT": "GIT_COMMIT",
                              "GIT_URL": "Unknown",
                              "GIT_BRANCH": "master",
                              "GIT_LOCAL_BRANCH": "GIT_LOCAL_BRANCH",
                              "GIT_AUTHOR_NAME": "GIT_AUTHOR_NAME",
                              "GIT_AUTHOR_EMAIL": "GIT_AUTHOR_EMAIL",
                              "BRANCH_NAME": "BRANCH_NAME",
                              "CHANGE_AUTHOR_DISPLAY_NAME": "CHANGE_AUTHOR_DISPLAY_NAME",
                              "CHANGE_AUTHOR": "CHANGE_AUTHOR",
                              "CHANGE_BRANCH": "CHANGE_BRANCH",
                              "CHANGE_FORK": "CHANGE_FORK",
                              "CHANGE_ID": "CHANGE_ID",
                              "CHANGE_TARGET": "CHANGE_TARGET",
                              "CHANGE_TITLE": "CHANGE_TITLE",
                              "CHANGE_URL": "CHANGE_URL",
                              "JOB_URL": "JOB_URL",
                              "NODE_LABELS": "NODE_LABELS",
                              "NODE_NAME": "NODE_NAME",
                              "PWD": "PWD",
                              "STAGE_NAME": "STAGE_NAME",
                              "ci-environment": "mk8s"}

        # Setup
        single_passing_test_for_asc.global_properties_from_cli = properties_from_cli
        single_passing_test_for_asc.assert_invoke_zigzag()
        test_runs = single_passing_test_for_asc.tests[0].qtest_test_runs

        # Expectations
        test_run_status_exp = 'Passed'

        # Test
        assert len(test_runs) == 1
        pytest.helpers.assert_qtest_property(test_runs[0], 'Status', test_run_status_exp)
