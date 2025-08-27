from dataclasses import dataclass, field
from typing import List


@dataclass
class TaskType:
    name: str
    type: str
    score: float
    source_languages: List[str]
    domains: List[str]
    modalities: List[str]


@dataclass
class Model:
    model_name: str
    max_tokens: int
    embed_dim : int
    n_parameters: float
    zero_shot_percentage: int
    confidence: int  
    text_length: int
    reference: str  
    task_type: List[TaskType]


@dataclass
class LanguageResult:
    language: str
    models: List[Model]


@dataclass
class CountryMetadata:
    country: str
    iso_3166_code: str
    number_of_languages: int
    number_of_tasks: int
    number_of_domain: int
    source: str
    description: str = "Pas de description disponible."


@dataclass
class Benchmark:
    id: int
    country_metadata: CountryMetadata
    results: List[LanguageResult]


@dataclass
class BenchmarksData:
    benchmarks: List[Benchmark] = field(default_factory=list)

    @staticmethod
    def from_dict(data: dict) -> 'BenchmarksData':
        benchmarks = []
        for b in data.get("benchmarks", []):
            country_meta = CountryMetadata(**b["country_metadata"])
            results = []
            for r in b["results"]:
                models = []
                for m in r["models"]:
                    tasks = [TaskType(**t) for t in m["task_type"]]
                    model = Model(
                        model_name=m["model_name"],
                        max_tokens=m["max_tokens"],
                        embed_dim=m["embed_dim"],       # ✅ nouveau champ
                        n_parameters=m["n_parameters"], # ✅ nouveau champ
                        zero_shot_percentage=m["zero_shot_percentage"], # ✅ nouveau champ
                        confidence=m["confidence"],
                        text_length=m["text_length"],
                        reference=m["reference"],
                        task_type=tasks
                    )
                    models.append(model)
                results.append(LanguageResult(language=r["language"], models=models))
            benchmarks.append(
                Benchmark(
                    id=b["id"],
                    country_metadata=country_meta,
                    results=results
                )
            )
        return BenchmarksData(benchmarks=benchmarks)
