"""
|----------------------------------------------|
| CS488 -  Senior Capstone Project             |
| Porter Libby                                 |
| Spring 2020                                  |
|----------------------------------------------|
"""
import os

# import custom code
from dataglob import DataGlob # Data structure


# testing
glob1 = DataGlob(os.getcwd() + "/training/plant-id",os.getcwd() +"/out")
glob1.print_configuration()
glob1.set_configuration("caney_auto", True)
#glob1.set_configuration("caney_wide", True)
glob1.set_configuration("original", True)
glob1.print_configuration()
glob1.prepare_database()