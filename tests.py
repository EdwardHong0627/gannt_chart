from gannt_chart.ganntchart import GanntChart
import pytest
import os

svg = GanntChart(2, 25, 50)


def test_create_GanntChart():
    assert svg is not None


def test_job_color():
    svg.add_job('J1', 1, 0, 20, fill='red', stroke='#FFFFFF')

    assert "style=\"fill:red;" in svg.svg
    assert "stroke=\"#FFFFFF" in svg.svg


def test_save():
    svg.save_to_file('uni_test')

    assert os.path.exists('uni_test.svg')
