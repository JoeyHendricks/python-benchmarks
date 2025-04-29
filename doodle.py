from Benchmarking.profiling.intrusive import collect_measurements
from Benchmarking import benchmark as mb
from Benchmarking.visualizations.flame_graphs import FlameGraph


class FooBar:

    @collect_measurements(test_case_name="joey", enabled=True)
    def test(self, test, xxx):
        num = 6 ** 6 ** 6
        self.tim()
        return len(str(num))

    def tim(self):
        print("xxxx")




# Run your method.
FooBar().test(test="test", xxx="xxx")

# Interact with the micro benchmarking object to extract information.
print(mb.test_id)
print(mb.test_case_name)
#print(mb.regression.letter_rank)


graph = FlameGraph(
    test_case_name="joey",
    database_connection_url=mb.database_connection_url,
    test_id=mb.test_id
)

graph.export("C:\\temp\\x\\")