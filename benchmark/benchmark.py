from benchmark.models import BenchmarksData, TaskType
from leaderboard.load_data import ALL_BENCHMARKS_DATA

class BenchmarkResults:
    def __init__(self, scores=None):
        if scores is not None:
            self.scores = scores
        else:
            benchmarks_data: BenchmarksData = ALL_BENCHMARKS_DATA

            self.scores = []
            for benchmark in benchmarks_data.benchmarks:
                for result in benchmark.results:
                    language = result.language
                    for model in result.models:
                        full_model_name = f"{model.model_name}_{language}"
                        for task in model.task_type:
                            self.scores.append({
                                "model_name": full_model_name,
                                "task_name": task.name,
                                "score": task.score,
                                "reference": None  
                            })

        self.task_names = sorted({score["task_name"] for score in self.scores})

    def get_scores(self, format="long"):
        return self.scores

    def join_revisions(self):
        return self


class Metadata:
    def __init__(self, name, type_, domains, modalities):
        self.name = name
        self.type = type_
        self.domains = domains
        self.modalities = modalities


class Benchmark:
    def __init__(self, name):
        self.name = name
    
        benchmarks_data: BenchmarksData = ALL_BENCHMARKS_DATA
        benchmark = next((b for b in benchmarks_data.benchmarks if b.country_metadata.country.lower() == name.lower()), None)
                
        self.description = benchmark.country_metadata.description
        self.reference = benchmark.country_metadata.source
        self.results = benchmark.results
        
        self.tasks = []
        if benchmark:
            task_seen = set()
            for result in benchmark.results:
                for model in result.models:
                    for task in model.task_type:
                        if task.name not in task_seen:
                            task_seen.add(task.name)
                            self.tasks.append(
                                TaskType(
                                    name=task.name,
                                    type=task.type,
                                    score=task.score,
                                    domains=task.domains,
                                    modalities=task.modalities,
                                    source_languages=model.task_type[0].source_languages
                                )
                            )
        else:
            self.tasks = []
    
    def load_results(self, base_results=None):
        return BenchmarkResults()
    
    
class AggregatedBenchmarkResults:
    def __init__(self, base_results):
        if hasattr(base_results, "benchmarks"):
            benchmarks = base_results.benchmarks
        elif isinstance(base_results, list):
            benchmarks = base_results
        else:
            raise TypeError(f"base_results doit être BenchmarksData ou liste, pas {type(base_results)}")

        self._task_names = set()
        self._languages = set()
        self._task_types = set()
        self._domains = set()
        self._modalities = set()
        self._scores = []

        for benchmark in benchmarks:
            if hasattr(benchmark, "results"):
                results = benchmark.results
            else:
                results = [benchmark]

            for result in results:
                language = result.language
                for model in result.models:
                    full_model_name = f"{model.model_name}_{language}"
                    for task in model.task_type:
                        self._task_names.add(task.name)
                        self._languages.update(task.source_languages or [])
                        self._task_types.add(task.type)
                        self._domains.update(task.domains or [])
                        self._modalities.update(task.modalities or [])

                        if task.score is not None:
                            self._scores.append({
                                "model_name": full_model_name,
                                "task_name": task.name,
                                "score": task.score,
                                "reference": model.reference or "",
                            })

    def join_revisions(self):
        return self

    def get_scores(self, format="long"):
        return self._scores

    @property
    def task_names(self):
        return sorted(self._task_names)

    @property
    def languages(self):
        return sorted(self._languages)

    @property
    def task_types(self):
        return sorted(self._task_types)

    @property
    def domains(self):
        return sorted(self._domains)

    @property
    def modalities(self):
        return sorted(self._modalities)


def get_benchmarks():
    class Benchmark:
        def __init__(self, name, results):
            self.name = name
            self.results = results 

        def load_results(self, base_results=None):
            return AggregatedBenchmarkResults(self.results)

    benchmarks = []
            
    for bench in ALL_BENCHMARKS_DATA.benchmarks:
        name = bench.country_metadata.country.lower()
        results = bench.results 
        benchmarks.append(Benchmark(name, results))

    return benchmarks