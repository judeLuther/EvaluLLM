import os
import json
import pycountry 
from typing import Set
from dacite import from_dict
from benchmark.models import BenchmarksData

def load_benchmark_data(filepath: str) -> BenchmarksData:
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return from_dict(data_class=BenchmarksData, data=data)

def get_model_names(data: BenchmarksData) -> Set[str]:
    return {
        f"{model.model_name}_{result.language}"
        for benchmark in data.benchmarks
        for result in benchmark.results
        for model in result.models
    }
    
def generate_benchmark(root_dir: str) -> BenchmarksData:

    data = {"benchmarks": []}
    benchmark_id = 1

    for country in sorted(os.listdir(root_dir)):
        country_path = os.path.join(root_dir, country)
        if not os.path.isdir(country_path):
            continue

        try:
            country_data = pycountry.countries.lookup(country)
            iso_code = country_data.alpha_2.lower()
        except LookupError:
            iso_code = country[:2].lower()

        results = []
        all_tasks = set()
        all_domains = set()

        for language in sorted(os.listdir(country_path)):
            language_path = os.path.join(country_path, language)
            if not os.path.isdir(language_path):
                continue

            models = []
            for file in os.listdir(language_path):
                if not file.endswith(".json"):
                    continue
                with open(os.path.join(language_path, file), "r", encoding="utf-8") as f:
                    mdata = json.load(f)

                if mdata.get("confidence", 0) != 1:
                    continue
                
                if any(t["score"] < 0 for t in mdata.get("task_type", [])):
                    continue  
                
                task_type = []
                for t in mdata.get("task_type", []):
                    score_percent = (t["score"] / 20)
                    task_type.append({
                        "name": t["name"],
                        "type": t["type"],
                        "score": score_percent,
                        "source_languages": t["source_languages"],
                        "domains": t["domains"],
                        "modalities": t["modalities"]
                    })
                    all_tasks.add(t["type"])
                    all_domains.update(t["domains"])

                models.append({
                    "model_name": mdata.get("model_name", ""),
                    "max_tokens": mdata.get("max_tokens", 0),
                    "embed_dim": mdata.get("embed_dim", 0),
                    "n_parameters": mdata.get("n_parameters", 0),
                    "zero_shot_percentage": mdata.get("zero_shot_percentage", 0),
                    "confidence": mdata.get("confidence", 0),
                    "text_length": mdata.get("max_tokens", 0)//2,
                    "reference": mdata.get("reference", ""),
                    "task_type": task_type
                })

            if models:
                results.append({
                    "language": language,
                    "models": models
                })

        if results:
            country_meta = {
                "country": country,
                "iso_3166_code": iso_code,
                "number_of_languages": len(results),
                "number_of_tasks": len(all_tasks),
                "number_of_domain": len(all_domains),
                "source": f"https://www.ethnologue.com/country/{iso_code.upper()}/",
                "description": f"Benchmark for {country} Indigenous Languages"
            }

            data["benchmarks"].append({
                "id": benchmark_id,
                "country_metadata": country_meta,
                "results": results
            })
            benchmark_id += 1

    from_dict = BenchmarksData.from_dict
    return from_dict(data)