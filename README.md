<!-- LOGO -->
<p align="center">
  <img src="https://github.com/JoeyHendricks/QuickPotato/blob/master/images/banner-wide-with-text.jpg"/>
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

<!-- CONTENT -->
## QuickPotato in a nutshell

QuickPotato is a Python library that aims to make it easier to rapidly profile your software and produce powerful 
code visualizations that enables you to quickly investigate where potential performance bottlenecks are hidden.

Also, QuickPotato is trying to provide you with a path to add an automated performance testing angle to 
your regular unit tests or test-driven development test cases allowing you to test your code early in the 
development life cycle in a simple, reliable, and fast way.

## Installation

Install using [pip](https://pip.pypa.io/en/stable/) or download the source code from GitHub.
```bash
pip install QuickPotato
```
> Do note that QuickPotato hasn't released (yet) on the Python Package Index
> Please just grab the source code or the latest release from GitHub for now :).

## Generating Flame Graphs

[![Example of a Python flame graph](/images/python-code-flame-graph.png "flame graph Python")](
https://github.com/JoeyHendricks/QuickPotato/blob/master/images/python-code-flame-graph.png)

How to interpret the Flame Graphs generated by QuickPotato together with [d3-flame-graph](https://github.com/spiermar/d3-flame-graph):

- Each box is a function in the stack
- The y-axis shows the stack depth the top box shows what was on the CPU.
- The x-axis **does not show time** but spans the population and is ordered alphabetically.
- The width of the box show how long it was on-CPU or was part of an parent function that was on-CPU.

> If you are unfamiliar with Flame Graphs you can best read about them on [Brendan Greg's website](http://www.brendangregg.com/flamegraphs.html).

In the following way you can generate a Python flame graph with QuickPotato:

```python
from QuickPotato.configuration.management import options
from QuickPotato.statistical.visualizations import FlameGraph
from QuickPotato.profiling.intrusive import performance_breakpoint

options.enable_intrusive_profiling = True  # <-- Make sure that when using intrusive profiling 
                                           #     that intrusive profiling is enabled.

@performance_breakpoint  # <-- Make sure you attach the performance critical decorator.
def i_am_a_slow_function():
  num = 6 ** 6 ** 6
  return len(str(num))


# Generate Flame Graph
FlameGraph().export(path="C:\\Temp\\")
```

## Generating Heatmaps (Beta)

[![Example of a Python heatmap](/images/python-code-performance-heatmap.png "heatmap Python")](
https://github.com/JoeyHendricks/QuickPotato/blob/master/images/python-code-performance-heatmap.png)

How does a by QuickPotato generated heatmap work:

- Every box in the heatmap is a function
- The y-axis is made up of functions ordered by its latency.
- The x-axis spans the amount of sample (one sample is on execution of your code) and is separated into 
  columns of test id's (one test id is one completely executed test).
- The color shows the speeds of the function to more red a box is the more time there was spent.
- All boxes are clickable and will give you information about that particular function.

In the following way you can generate a Python heatmap with QuickPotato:

```python
from examples.example_code import FancyCode
from QuickPotato.profiling.intrusive import performance_test as pt
from QuickPotato.configuration.management import options
from QuickPotato.statistical.visualizations import HeatMap

options.enable_intrusive_profiling = True  # <-- Make sure that profiling is enabled

# Turn this setting on when to also include untested or failed test ids into your performance test.
options.allow_the_selection_of_untested_or_failed_test_ids = True

pt.test_case_name = "heatmap"  # <-- For recording multiple sample QuickPotato needs a test case name.

# Run you code an X amount of times.
for _ in range(0, 100):
    FancyCode().say_my_name_and_more(name="joey hendricks")

# Generate a heatmap
heatmap = HeatMap(test_case_name=pt.test_case_name, test_ids=[pt.previous_test_id, pt.current_test_id])
heatmap.export("C:\\temp\\")

```
> This visualization is still being tweaked and improved if you encounter any issue with it please open an issue. 
> (Your feedback is appreciated!)

## Generating a CSV file

[![Example of a csv file](/images/csv-example.jpg "csv file")](
https://github.com/JoeyHendricks/QuickPotato/blob/master/images/csv-example.jpg)

You can generate a CSV export in the following way:

```python
from QuickPotato.configuration.management import options
from QuickPotato.statistical.visualizations import CsvFile
from QuickPotato.profiling.intrusive import performance_breakpoint

options.enable_intrusive_profiling = True  # <-- Make sure that when using intrusive profiling 


#     that intrusive profiling is enabled.


@performance_breakpoint  # <-- Make sure you attach the performance critical decorator.
def i_am_a_slow_function():
  num = 6 ** 6 ** 6
  return len(str(num))


# export measurements to csv
CsvFile().export(path="C:\\Temp\\")
```

## Boundary testing

Within QuickPotato, it is possible to create a performance test that validates if your code breaches any 
defined boundary or not. An example of this sort of test can be found in the snippet below:

```python
from QuickPotato.profiling.intrusive import performance_test as pt
from examples.example_code import fast_method

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
from QuickPotato.profiling.intrusive import performance_test as pt
from examples.example_code import fast_method

# Define test case name
pt.test_case_name = "test_performance"

# Execute method under test
for _ in range(0, 10):
    fast_method()

# Analyse results for change True if there is no change otherwise False
results = pt.verify_benchmark_against_previous_baseline
```

## Options you can configure

QuickPotato comes equipped with some options you can configure to make sure QuickPotato fits your needs.
Below you can find a list of all basic options:

```python
from QuickPotato.configuration.management import options

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

## Coming soon

Some features which I am planning to add to QuickPotato soon:

- Improving the heatmap
- Scatter plot
- Creating a virtual map of your code
- Time Line (Showing from left to right the time spent per action in your code.)
- non-intrusive profiling by means of setting a start and stop point

## Learn more about QuickPotato

If you want to learn more about test driven performance testing and want to 
see how this project reached its current state? 
Then I would encourage you to check out the following resources:

- 11/07/2020: [Don’t lose your mind over slow code check your performance sanity.(English)](https://www.linkedin.com/pulse/dont-lose-your-mind-over-slow-code-check-performance-sanity-joey/) 
- 08/10/2020: [My recording about QuickPotato @NeotysPAC 2020. (English)](https://www.youtube.com/watch?v=AWlhalEywEw) 
- 15/12/2020: [Interview about QuickPotato @TestGuild 2020. (English)](https://testguild.com/podcast/performance/p56-joey/)
- 12/01/2020: [An article I wrote for Neotys about my @NeotysPAC 2020 presentation. (English)](https://www.neotys.com/blog/neotyspac-performance-testing-unit-level-joey-hendricks/)
