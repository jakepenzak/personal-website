from typing import NamedTuple

skills_data = [
    {
        "subject": "Econometrics/Causal Inference",
        "rating": 100,
    },
    {
        "subject": "Statistics/Statistical Learning",
        "rating": 90,
    },
    {
        "subject": "Mathematical Optimization",
        "rating": 80,
    },
    {
        "subject": "Time Series Analysis",
        "rating": 70,
    },
    {
        "subject": "Deep Learning/AI",
        "rating": 55,
    },
    {
        "subject": "Web Development",
        "rating": 50,
    },
    {
        "subject": "DevOps + MLOps",
        "rating": 75,
    },
    {
        "subject": "Data Pipelining/Engineering",
        "rating": 75,
    },
    {
        "subject": "Package Development",
        "rating": 85,
    },
    {
        "subject": "Python Data Science Ecosystem",
        "rating": 90,
    },
]


class LogoMeta(NamedTuple):
    asset_path: str
    link: str


tech_logos_dict = {
    "Azure": LogoMeta(
        asset_path="/index/skills/tech_logos/azure.png",
        link="https://azure.microsoft.com/en-us",
    ),
    "Conda": LogoMeta(
        asset_path="/index/skills/tech_logos/conda.png",
        link="https://docs.conda.io/en/latest/",
    ),
    "Cuda": LogoMeta(
        asset_path="/index/skills/tech_logos/cuda.png",
        link="https://developer.nvidia.com/cuda-zone",
    ),
    "DataBricks": LogoMeta(
        asset_path="/index/skills/tech_logos/databricks.png",
        link="https://databricks.com/",
    ),
    "Digital Ocean": LogoMeta(
        asset_path="/index/skills/tech_logos/digitalocean.png",
        link="https://www.digitalocean.com/",
    ),
    "Docker": LogoMeta(
        asset_path="/index/skills/tech_logos/docker.png", link="https://www.docker.com/"
    ),
    "GitHub": LogoMeta(
        asset_path="/index/skills/tech_logos/github.png", link="https://ww.github.com/"
    ),
    "Jupyter": LogoMeta(
        asset_path="/index/skills/tech_logos/jupyter.png", link="https://jupyter.org/"
    ),
    "Obsidian": LogoMeta(
        asset_path="/index/skills/tech_logos/obsidian.png", link="https://obsidian.md/"
    ),
    "Quarto": LogoMeta(
        asset_path="/index/skills/tech_logos/quarto.png", link="https://quarto.org/"
    ),
    "Spark": LogoMeta(
        asset_path="/index/skills/tech_logos/spark.png",
        link="https://spark.apache.org/",
    ),
    "VS Code": LogoMeta(
        asset_path="/index/skills/tech_logos/vscode.png",
        link="https://code.visualstudio.com/",
    ),
}

# tech_list = rx.unordered_list(
#     *[rx.link(rx.list_item(tech), href=tech_logos_dict[tech].link, target="_blank") for tech in list(tech_logos_dict.keys())])
