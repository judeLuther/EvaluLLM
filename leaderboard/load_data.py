import json
import requests
from benchmark.models import BenchmarksData


#ALL_BENCHMARKS_DATA = load_benchmark_data("../format.json")
#ALL_BENCHMARKS_DATA = generate_benchmark("...")

url = "https://huggingface.co/datasets/lojl/llms_low_resource_benchmark_2025/resolve/main/benchmarks.json"

response = requests.get(url)
if response.status_code == 200:
    data = json.loads(response.text)
else:
    data = {}

ALL_BENCHMARKS_DATA = BenchmarksData.from_dict(data)
