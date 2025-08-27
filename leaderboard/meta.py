from typing import Literal
from leaderboard.load_data import ALL_BENCHMARKS_DATA

MIN_MODEL_SIZE = 0
MAX_MODEL_SIZE = 100 

class ModelMeta:
    def __init__(self, name, n_parameters, open_weights, use_instructions, frameworks, zero_shot_status):
        self.name = name
        self.n_parameters = n_parameters
        self.open_weights = open_weights
        self.use_instructions = use_instructions
        self.frameworks = frameworks
        self.zero_shot_status = zero_shot_status  # dict: task_name -> bool | None

    def is_zero_shot_on(self, tasks: list[str]):
        result = []
        for task in tasks:
            status = self.zero_shot_status.get(task)
            result.append(status)
        if all(s is True for s in result):
            return True
        elif any(s is False for s in result):
            return False
        else:
            return None

def get_model_metas(model_names, n_parameters_range):
    lower, upper = n_parameters_range

    benchmarks_data = ALL_BENCHMARKS_DATA

    model_names_set = set(model_names) if model_names else None

    models = []
    for benchmark in benchmarks_data.benchmarks:
        for result in benchmark.results:
            language = result.language
            for m in result.models:
                full_name = f"{m.model_name}_{language}"
                if model_names_set and full_name not in model_names_set:
                    continue

                #zero_shot_status = {task.name: None for task in m.task_type}
                
                zero_shot_status = {
                    task.name: (m.zero_shot_percentage == 100) 
                    for task in m.task_type
                }


                model = ModelMeta(
                    name=full_name,
                    n_parameters=None,
                    open_weights=None,
                    use_instructions=None,
                    frameworks=None,
                    zero_shot_status=zero_shot_status
                )
                models.append(model)

    filtered = []
    for m in models:
        if model_names and m.name not in model_names:
            continue
        # if open_weights is not None and m.open_weights != open_weights:
        #     continue
        # if use_instructions is not None and m.use_instructions != use_instructions:
        #     continue
        # if frameworks and not any(f in m.frameworks for f in frameworks):
        #     continue
        # if lower is not None and m.n_parameters < lower:
        #     continue
        # if upper is not None and m.n_parameters > upper:
        #     continue
        if lower is not None and m.n_parameters is not None and m.n_parameters < lower:
            continue
        if upper is not None and m.n_parameters is not None and m.n_parameters > upper:
            continue
        filtered.append(m)

    return filtered