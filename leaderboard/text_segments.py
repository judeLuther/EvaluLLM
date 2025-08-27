from __future__ import annotations

FAQ = """### How translation validation works

In our dashboard, we only display translations that have been confirmed by two separate LLMs to ensure the output is indeed in the expected language. 
This is because we do not have human evaluators for every translation. 
Using two independent LLM checks helps increase confidence in the correctness of the language.

### What do aggregate measures (Rank(Borda), Mean(Task), etc.) mean?

- **Rank(borda)** is computed based on the [borda count](https://en.wikipedia.org/wiki/Borda_count), where each task is treated as a preference voter, which gives votes on the models per their relative performance on the task. The best model obtains the highest number of votes. The model with the highest number of votes across tasks obtains the highest rank. The Borda rank tends to prefer models that perform well broadly across tasks. However, given that it is a rank it can be unclear if the two models perform similarly.
- **Mean(Task)**: This is a naïve average computed across all the tasks within the benchmark. This score is simple to understand and is continuous as opposed to the Borda rank. However, the mean can overvalue tasks with higher variance in its scores.
- **Mean(TaskType)**: This is a weighted average across different task categories, such as translation or classification. It is computed by first computing the average by task category and then computing the average on each category. Similar to the Mean(Task) this measure is continuous and tends to overvalue tasks with higher variance. This score also prefers models that perform well across all task categories.

### What does zero-shot mean?

A model is considered zero-shot if it has not been trained on any split of the datasets used to define the tasks.
The percentages shown in the table represent the share of the benchmark that is out-of-distribution for a given model.
A value of 100% means the model has not been trained on any dataset from that benchmark, so its score can be taken as a measure of generalization ability.
In contrast, a value of 50% means the model has been fine-tuned on half of the benchmark’s tasks, so the results should be interpreted with caution.
This definition also leads to a few borderline cases.

### What do the other columns mean?

- **Number of Parameters**: This is the total number of parameters in the model including embedding parameters. A higher value means the model requires more CPU/GPU memory to run; thus, less is generally desirable.
- **Embedding Dimension**: This is the vector dimension of the embeddings that the model produces. When saving embeddings to disk, a higher dimension will require more space, thus less is usually desirable.
- **Max tokens**: This refers to how many tokens (=word pieces) the model can process. Generally, a larger value is desirable.
- **Zero-shot**: This indicates if the model is zero-shot on the benchmark. For more information on zero-shot see the info box above.

### Why is a model missing or not showing up?

Possible reasons why a model may not show up in the leaderboard:

- **Filter Setting**: It is being filtered out with your current filter. By default, we do not show models that are not zero-shot on the benchmark.
You can change this setting in the model selection panel.
- **Missing Results**: The model may not have been run on the tasks in the benchmark. We only display models that have been run on at least one task
in the benchmark. For visualizations that require the mean across all tasks, we only display models that have been run on all tasks in the benchmark.
You can see existing results in the [results repository](https://github.com/judeLuther/EvaluLLM/blob/main/README.md).
- **Missing Metadata**
"""


ACKNOWLEDGEMENT = """
<div style="border-top: 1px solid #ddd; margin-top: 30px; padding-top: 10px; font-size: 0.85em; color: #666;">
  <p><strong>Acknowledgment:</strong> We thank <a href="https://www.afd.fr/fr/accueil">AFD - Agence Française de Développement</a> for their generous sponsorship. If you'd like to sponsor us, please get in <a href="mailto:jude.kaisens.data@gmail.com">touch</a>.</p>
  
<div class="sponsor-image-about" style="display: flex; align-items: center; gap: 10px;">
    <a href="https://www.afd.fr/fr/accueil">
        <img src="https://www.afd.fr/sites/default/files/2025-03/logo_AFD.png" width="60" height="55" style="padding: 10px;">
    </a>
</div>
  
</div>
"""

CITATIONS = {
    "translation": """@inproceedings{translation2025,
  title={Benchmarking LLM Models},
  author={Leckomba, Jude and Millerat, Jean},
  booktitle={Benchmark: LLM Performance on Core Low-resource Language Tasks},
  year={2025}
}""",
}