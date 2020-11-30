# -*- coding: utf-8 -*-

"""
    mycalculator

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from mycalculator.decorators import lazy_property
from mycalculator.configuration import Configuration
from mycalculator.controllers.simple_calculator_controller import SimpleCalculatorController


class MycalculatorClient(object):

    config = Configuration

    @lazy_property
    def simple_calculator(self):
        return SimpleCalculatorController()

