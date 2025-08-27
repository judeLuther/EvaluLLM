from __future__ import annotations
from dataclasses import dataclass
import gradio as gr

@dataclass
class Benchmark:
    name: str
    display_name: str | None = None
    icon: str | None = None

@dataclass
class MenuEntry:
    name: str | None
    benchmarks: list[Benchmark | MenuEntry]
    description: str | None = None
    open: bool = False

DEFAULT_BENCHMARK_NAME = "Kenya"

benchmarks_simple = [
    Benchmark(
        name="Kenya",
        display_name="Kenya",
        icon="https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/ke.svg"
    ),
    Benchmark(
        name="Senegal",
        display_name="Senegal",
        icon="https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/sn.svg"
    ),
    Benchmark(
        name="Nigeria",
        display_name="Nigeria",
        icon="https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/ng.svg"
    ),
    Benchmark(
        name="Gabon",
        display_name="Gabon",
        icon="https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/ga.svg"
    ),
    Benchmark(
        name="Morocco",
        display_name="Morocco",
        icon="https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/ma.svg"
    ),
    
    Benchmark(
        name="Haiti",
        display_name="Haiti",
        icon="https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/ht.svg"
    ),
    Benchmark(
        name="Madagascar",
        display_name="Madagascar",
        icon="https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/mg.svg"
    ),
    Benchmark(
        name="Turkey",
        display_name="Turkey",
        icon="https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/tr.svg"
    ),
    Benchmark(
        name="Ukraine",
        display_name="Ukraine",
        icon="https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/ua.svg"
    ),
    Benchmark(
        name="Jordan",
        display_name="Jordan",
        icon="https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/jo.svg"
    ),
    Benchmark(
        name="Bangladesh",
        display_name="Bangladesh",
        icon="https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/bd.svg"
    ),
    Benchmark(
        name="Kazakhstan",
        display_name="MaKazakhstanli",
        icon="https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/kz.svg"
    ),
    Benchmark(
        name="Philippines",
        display_name="Philippines",
        icon="https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/ph.svg"
    ),
    
    Benchmark(
        name="Brazil",
        display_name="Brazil",
        icon="https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/br.svg"
    ),
    Benchmark(
        name="Colombia",
        display_name="Colombia",
        icon="https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/co.svg"
    ),
    Benchmark(
        name="Bolivia",
        display_name="Bolivia",
        icon="https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/bo.svg"
    )
    
    
]

def get_benchmarks(names: list[str], icon_map: dict[str, str]) -> list[Benchmark]:
    return [
        Benchmark(
            name=name,
            display_name=name, 
            icon=icon_map.get(
                name.lower(),
                "https://github.com/DennisSuitters/LibreICONS/raw/main/svg-color/libre-gui-globe.svg"  # Icône par défaut
            )
        )
        for name in names
    ]

icon_map = {
    "multilingual": "https://github.com/DennisSuitters/LibreICONS/raw/2d2172d15e3c6ca03c018629d60050e4b99e5c55/svg-color/libre-gui-globe.svg",
    "eng": "https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/us.svg",

    "text": "https://github.com/DennisSuitters/LibreICONS/blob/master/svg-color/libre-brand-summernote.svg",
    "speech": "https://github.com/DennisSuitters/LibreICONS/raw/2d2172d15e3c6ca03c018629d60050e4b99e5c55/svg-color/libre-gui-picture.svg",


    "code": "https://github.com/DennisSuitters/LibreICONS/raw/2d2172d15e3c6ca03c018629d60050e4b99e5c55/svg-color/libre-tech-electronics.svg",
    "law": "https://github.com/DennisSuitters/LibreICONS/raw/2d2172d15e3c6ca03c018629d60050e4b99e5c55/svg-color/libre-map-library.svg",
    "medical": "https://github.com/DennisSuitters/LibreICONS/raw/2d2172d15e3c6ca03c018629d60050e4b99e5c55/svg-color/libre-map-hospital.svg",
    "chemTEB": "https://github.com/DennisSuitters/LibreICONS/raw/2d2172d15e3c6ca03c018629d60050e4b99e5c55/svg-color/libre-gui-purge.svg",

    "kenya": "https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/ke.svg",
    "senegal": "https://raw.githubusercontent.com/lipis/flag-icons/refs/heads/main/flags/4x3/sn.svg",
    "nigeria" : "https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/ng.svg",
    "gabon" : "https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/ga.svg",
    "morocco": "https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/ma.svg",
    
    "haiti" : "https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/ht.svg",
    "madagascar" : "https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/mg.svg",
    
    "turkey" : "https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/tr.svg",
    "ukraine" : "https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/ua.svg",
    "jordan" : "https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/jo.svg",
    "bangladesh" : "https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/bd.svg",
    "kazakhstan" : "https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/kz.svg",
    "philippines" : "https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/ph.svg",
    
    "brazil" : "https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/br.svg",
    "colombia" : "https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/co.svg",
    "bolivia" : "https://github.com/lipis/flag-icons/raw/refs/heads/main/flags/4x3/bo.svg",
}

BENCHMARK_ENTRIES = [
    MenuEntry(
        name="Select Benchmark",
        description="",
        open=False,
        benchmarks=get_benchmarks([
            "Kenya",
            "Senegal",
            "Nigeria",
            "Gabon",
            "Morocco",
            
            "Haiti",
            "Madagascar",
            
            "Turkey",
            "Ukraine",
            "Jordan",
            "Bangladesh",
            "Kazakhstan",
            "Philippines",
            
            "Brazil",
            "Colombia",
            "Bolivia",
        ], icon_map) + [
            # MenuEntry(
            #     "Task",
            #     get_benchmarks([
            #         "text",
            #         "speech",
            #                     ], icon_map)
            # ),
            # MenuEntry(
            #     "Domain-Specific",
            #     get_benchmarks([
            #         "Code",
            #         "Law",
            #         "Medical",
            #         "ChemTEB",
            #     ], icon_map)
            # ),
            # MenuEntry(
            #     "Language-specific",
            #     get_benchmarks([
            #         "kenya",
            #         "senegal",
            #         "mali",
            #         "cameroon",
            #     ], icon_map) + [
            #         MenuEntry(
            #             "Other",
            #             get_benchmarks([
            #                 "eng"
            #             ], icon_map)
            #         )
            #     ]
            # ),
            # MenuEntry(
            #     "Miscellaneous",
            #     get_benchmarks([
            #         "AFD",
            #         "AFD-NLP"
            #     ], icon_map)
            # ),
        ]
    )
]

# ============================
# UI Gradio
# ============================

def _create_button(
    i: int,
    benchmark: Benchmark,
    state: gr.State,
    label_to_value: dict[str, str],
    **kwargs,
):
    val = benchmark.name
    label = benchmark.display_name or benchmark.name
    label_to_value[label] = val

    button = gr.Button(
        label,
        variant="secondary" if i != 0 else "primary",
        icon=benchmark.icon,
        key=f"{i}_button_{val}",
        elem_classes="text-white",
        **kwargs,
    )

    def _update_variant(state_val: str, label: str) -> gr.Button:
        return gr.Button(variant="primary" if state_val == label_to_value[label] else "secondary")

    def _update_value(label: str) -> str:
        return label_to_value[label]

    state.change(_update_variant, inputs=[state, button], outputs=[button])
    button.click(_update_value, inputs=[button], outputs=[state])
    return button


def make_selector(entries: list[MenuEntry]) -> tuple[gr.State, gr.Column]:
    label_to_value = {}
    button_counter = 0

    with gr.Column() as column:
        state = gr.State(DEFAULT_BENCHMARK_NAME)

        for category_entry in entries:
            button_counter = _render_category(
                category_entry, state, label_to_value, button_counter
            )

    return state, column


def _render_category(
    entry: MenuEntry,
    state: gr.State,
    label_to_value: dict,
    button_counter: int,
) -> int:
    gr.Markdown(f"## {entry.name}")
    if entry.description:
        gr.Markdown(entry.description)

    for benchmarks_group in entry.benchmarks:
        button_counter = _render_benchmark_item(
            benchmarks_group, state, label_to_value, button_counter, level=0
        )

    return button_counter


def _render_benchmark_item(
    item: Benchmark | MenuEntry,
    state: gr.State,
    label_to_value: dict,
    button_counter: int,
    level: int,
) -> int:
    if isinstance(item, Benchmark):
        size = "md" if level == 0 else "sm"
        _create_button(button_counter, item, state, label_to_value, size=size)
        return button_counter + 1

    with gr.Accordion(item.name, open=item.open):
        for nested_item in item.benchmarks:
            button_counter = _render_benchmark_item(
                nested_item, state, label_to_value, button_counter, level + 1
            )

    return button_counter

if __name__ == "__main__":
    with gr.Blocks() as demo:
        make_selector(BENCHMARK_ENTRIES)
    demo.launch()
