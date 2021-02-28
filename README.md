<!-- LOGO -->
<p align="center">
  <img src="https://github.com/JoeyHendricks/python-unit-level-performance-testing/blob/master/images/banner-with-text.png?raw=true"/>
</p>

<!-- TAG LINE -->
<h3 align="center">Profile and test to gain insights into the performance of your beautiful Python code</h3>
<p align="center">
    <a href="https://github.com/JoeyHendricks/QuickPotato">View Demo</a> -
    <a href="https://github.com/JoeyHendricks/QuickPotato/issues">Report Bug</a> -
    <a href="https://github.com/JoeyHendricks/QuickPotato/issues">Request Feature</a>
</p>

<!-- BADGES -->
<div align="center">
<a href="https://github.com/JoeyHendricks/QuickPotato/graphs/contributors"><img src="https://img.shields.io/github/contributors/JoeyHendricks/QuickPotato?style=for-the-badge"></a>
<a href="https://github.com/JoeyHendricks/QuickPotato/network/members"><img src="https://img.shields.io/github/forks/JoeyHendricks/QuickPotato?style=for-the-badge"></a>
<a href="https://github.com/JoeyHendricks/QuickPotato/stargazers"><img src="https://img.shields.io/github/stars/JoeyHendricks/QuickPotato?style=for-the-badge"></a>
<a href="https://github.com/JoeyHendricks/QuickPotato/issues"><img src="https://img.shields.io/github/issues/JoeyHendricks/QuickPotato?style=for-the-badge"></a>
<a href="https://github.com/JoeyHendricks/QuickPotato/blob/master/LICENSE.md"><img src="https://img.shields.io/github/license/JoeyHendricks/QuickPotato?style=for-the-badge"></a>
<a href="https://www.linkedin.com/in/joey-hendricks/"><img src="https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555"></a>
</div>
<br>

<!-- TABLE OF CONTENTS -->
<details open="open" >
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#CouchPotato-in-a-nutshell">CouchPotato in a nutshell</a>
    </li>
    <li>
        <a>Getting Started</a>
        <ul>
            <li><a href="#Installation">Installation</a></li>
            <li><a href="#Options-you-can-configure">Options</a></li>
        </ul>
    </li>
    <li>
        <a>Generating visualizations</a>
        <ul>
            <li><a href="#Generating-Flame-Graphs">Flame Graphs</a></li>
        </ul>
    </li>
    <li>
      <a>Test-driven performance testing</a>
      <ul>
        <li><a href="#Boundary-testing">Boundary testing</a></li>
        <li><a href="#Regression-testing">Regression testing</a></li>
      </ul>
    </li>
    <li><a href="#Learn-more-about-CouchPotato">Learn more about CouchPotato</a></li>
  </ol>
</details>

<!-- CONTENT -->
## CouchPotato in a nutshell

CouchPotato is a Python library that aims to make it easier to rapidly profile your software and produce powerful 
code visualizations that enables you to quickly investigate where potential performance bottlenecks are hidden.

Also, CouchPotato is trying to provide you with a path to add an automated performance testing angle to 
your regular unit tests or test-driven development test cases allowing you to test your code early in the 
development life cycle in a simple, reliable, and fast way.

## Installation

Install using [pip](https://pip.pypa.io/en/stable/) or download the source code from GitHub.
```bash
pip install CouchPotato
```
> Do note that CouchPotato hasn't released (yet) on the Python Package Index
> Please just grab the source code or the latest release from GitHub for now :).

## Generating Flame Graphs

[![Example of a Python flame graph](/images/python-code-flame-graph.png "flame graph Python")](
https://raw.githubusercontent.com/JoeyHendricks/QuickPotato/Trying-d3-flame-graphs/example/example_basic_flame_graph.html)

How to interpret the Flame Graphs generated by CouchPotato together with [d3-flame-graph](https://github.com/spiermar/d3-flame-graph):

- Each box is a function in the stack
- The y-axis shows the stack depth the top box shows what was on the CPU.
- The x-axis **does not show time** but spans the population and is ordered alphabetically.
- The width of the box show how long it was on-CPU or was part of an parent function that was on-CPU.

> If you are unfamiliar with Flame Graphs you can best read about them on [Brendan Greg's website](http://www.brendangregg.com/flamegraphs.html).

In the following way you can generate a Python flame graph with CouchPotato:

```python
from CouchPotato.configuration.management import options
from CouchPotato.statistical.visualizations import FlameGraph
from CouchPotato.profiling.intrusive import performance_critical

options.enable_intrusive_profiling = True  # <-- Make sure that when using intrusive profiling 
                                           #     that intrusive profiling is enabled.


@performance_critical  # <-- Make sure you attach the performance critical decorator.
def i_am_a_slow_function():
    num = 6 ** 6 ** 6
    return len(str(num))


# Generate Flame Graph
FlameGraph().export(path="C:\\Temp\\")
```

## Generating a CSV file

|id  |test_id     |test_case_name|sample_id                           |name_of_method_under_test|epoch_timestamp|human_timestamp           |child_path                                                                                      |child_line_number|child_function_name                   |parent_path                                                                                     |parent_line_number|parent_function_name                |number_of_calls|total_time|cumulative_time|total_response_time|
|:--:|:----------:|:------------:|:----------------------------------:|:-----------------------:|:-------------:|:------------------------:|:----------------------------------------------------------------------------------------------:|:---------------:|:------------------------------------:|:----------------------------------------------------------------------------------------------:|:----------------:|:----------------------------------:|:-------------:|:--------:|:-------------:|:-----------------:|
|2160|UMFN1LIHA8J8|QuickProfiling|3fa1314f-79ee-11eb-88ef-14dda977a447|  say_my_name_and_more   |  1614534988   |2021-02-28 18:56:28.415248|C:\Users\joeyh\Documents\Python Projects\python-unit-performance-testing\example\example_code.py|       23        |         say_my_name_and_more         |                                               ~                                                |        0         |3fa1314f-79ee-11eb-88ef-14dda977a447|       1       | 2.35e-05 |    14.0049    |      14.0048      |
|2168|UMFN1LIHA8J8|QuickProfiling|3fa1314f-79ee-11eb-88ef-14dda977a447|  say_my_name_and_more   |  1614534988   |2021-02-28 18:56:28.415248|C:\Users\joeyh\Documents\Python Projects\python-unit-performance-testing\example\example_code.py|       68        |      sleep_based_on_name_length      |C:\Users\joeyh\Documents\Python Projects\python-unit-performance-testing\example\example_code.py|        23        |        say_my_name_and_more        |       1       | 6.8e-06  |    14.0048    |      14.0048      |
|2171|UMFN1LIHA8J8|QuickProfiling|3fa1314f-79ee-11eb-88ef-14dda977a447|  say_my_name_and_more   |  1614534988   |2021-02-28 18:56:28.415248|                                               ~                                                |        0        |     <built-in method time.sleep>     |C:\Users\joeyh\Documents\Python Projects\python-unit-performance-testing\example\example_code.py|        68        |     sleep_based_on_name_length     |       1       | 14.0048  |    14.0048    |      14.0048      |
|2176|UMFN1LIHA8J8|QuickProfiling|3fa1314f-79ee-11eb-88ef-14dda977a447|  say_my_name_and_more   |  1614534988   |2021-02-28 18:56:28.415248|                                               ~                                                |        0        |   <built-in method builtins.print>   |C:\Users\joeyh\Documents\Python Projects\python-unit-performance-testing\example\example_code.py|        23        |        say_my_name_and_more        |       8       | 3.77e-05 |   3.77e-05    |      14.0048      |
|2177|UMFN1LIHA8J8|QuickProfiling|3fa1314f-79ee-11eb-88ef-14dda977a447|  say_my_name_and_more   |  1614534988   |2021-02-28 18:56:28.415248|                                               ~                                                |        0        |   <built-in method builtins.print>   |C:\Users\joeyh\Documents\Python Projects\python-unit-performance-testing\example\example_code.py|        51        |  show_message_when_name_very_long  |       8       | 3.77e-05 |   3.77e-05    |      14.0048      |
|2178|UMFN1LIHA8J8|QuickProfiling|3fa1314f-79ee-11eb-88ef-14dda977a447|  say_my_name_and_more   |  1614534988   |2021-02-28 18:56:28.415248|                                               ~                                                |        0        |   <built-in method builtins.print>   |C:\Users\joeyh\Documents\Python Projects\python-unit-performance-testing\example\example_code.py|        59        |                 y                  |       8       | 3.77e-05 |   3.77e-05    |      14.0048      |

> The complete file can be found [here](https://github.com/JoeyHendricks/QuickPotato/blob/Trying-d3-flame-graphs/example/example_csv_file.csv).

## Boundary testing

Within CouchPotato, it is possible to create a performance test that validates if your code breaches any 
defined boundary or not. An example of this sort of test can be found in the snippet below:

```python
from CouchPotato.profiling.intrusive import performance_test as pt
from example.example_code import fast_method

# Define test case name
pt.test_case_name = "test_performance"

# Establish performance boundaries
pt.max_and_min_boundary_for_average = {"max": 1, "min": 0.001}

# Execute method under test
for _ in range(0, 10):
    fast_method()

# Analyse profiled results will output True if boundaries are not breached otherwise False
results = pt.verify_benchmark_against_set_boundaries
```

## Regression testing

It is also possible to verify that there is no regression between the current benchmark and a previous baseline.
The method for creating such a test can also be found in the snippet below:

```python
from CouchPotato.profiling.intrusive import performance_test as pt
from example.example_code import fast_method

# Define test case name
pt.test_case_name = "test_performance"

# Execute method under test
for _ in range(0, 10):
    fast_method()

# Analyse results for change True if there is no change otherwise False
results = pt.verify_benchmark_against_previous_baseline
```

## Options you can configure

CouchPotato comes equipped with some options you can configure to make sure CouchPotato fits your needs.
Below you can find a list of all basic options:

```python
from CouchPotato.configuration.management import options

# Profiling Settings
options.enable_intrusive_profiling = True 
options.enable_system_resource_collection = True

# Results Storage
options.connection_url = None  # <-- None will use SQlite and store results in Temp directory
options.enable_database_echo = False

# Storage Maintenance 
options.enable_auto_clean_up_old_test_results = True
options.maximum_number_saved_test_results = 10

```
> States of options are saved in a static yaml options file.  
> That is why settings can be defined just once or changed on the fly.

## Learn more about CouchPotato

If you want to learn more about test driven performance testing and want to 
see how this project reached its current state? 
Then I would encourage you to check out the following resources:

- 11/07/2020: [Don’t lose your mind over slow code check your performance sanity.(English)](https://www.linkedin.com/pulse/dont-lose-your-mind-over-slow-code-check-performance-sanity-joey/) 
- 08/10/2020: [My recording about QuickPotato @NeotysPAC 2020. (English)](https://www.youtube.com/watch?v=AWlhalEywEw) 
- 15/12/2020: [Interview about CouchPotato @TestGuild 2020. (English)](https://testguild.com/podcast/performance/p56-joey/)
- 12/01/2020: [An article I wrote for Neotys about my @NeotysPAC 2020 presentation. (English)](https://www.neotys.com/blog/neotyspac-performance-testing-unit-level-joey-hendricks/)
