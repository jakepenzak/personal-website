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
        "rating": 60,
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
        asset_path="/index/skills/tech_logos/github.png", link="https://www.github.com/"
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
    "duckDB": LogoMeta(
        asset_path="/index/skills/tech_logos/duckdb.png", link="https://duckdb.org/"
    ),
    "VS Code": LogoMeta(
        asset_path="/index/skills/tech_logos/vscode.png",
        link="https://code.visualstudio.com/",
    ),
    "Python": LogoMeta(
        asset_path="/index/skills/tech_logos/python.png", link="https://www.python.org/"
    ),
    "Stata": LogoMeta(
        asset_path="/index/skills/tech_logos/stata.jpg", link="https://www.stata.com/"
    ),
    "Linux": LogoMeta(
        asset_path="/index/skills/tech_logos/linux.png", link="https://www.linux.org/"
    ),
    "PowerBI": LogoMeta(
        asset_path="/index/skills/tech_logos/powerbi.png",
        link="https://powerbi.microsoft.com/en-us/",
    ),
}


library_logos_dict = {
    "EconML": LogoMeta(
        asset_path="/index/skills/library_logos/econml.jpg",
        link="https://www.microsoft.com/en-us/research/project/econml/",
    ),
    "DoubleML": LogoMeta(
        asset_path="/index/skills/library_logos/doubleml.png",
        link="https://docs.doubleml.org/stable/index.html",
    ),
    "DoWhy": LogoMeta(
        asset_path="/index/skills/library_logos/dowhy.png",
        link="https://www.pywhy.org/dowhy/v0.11.1/",
    ),
    "CausalML": LogoMeta(
        asset_path="/index/skills/library_logos/causalml.png",
        link="https://causalml.readthedocs.io/en/latest/",
    ),
    "SciKit-Learn": LogoMeta(
        asset_path="/index/skills/library_logos/sklearn.png",
        link="https://scikit-learn.org/stable/",
    ),
    "XGBoost": LogoMeta(
        asset_path="/index/skills/library_logos/xgboost.png",
        link="https://xgboost.readthedocs.io/en/latest/",
    ),
    "LightGBM": LogoMeta(
        asset_path="/index/skills/library_logos/lightgbm.svg",
        link="https://lightgbm.readthedocs.io/en/latest/",
    ),
    "PyTorch": LogoMeta(
        asset_path="/index/skills/library_logos/pytorch.png",
        link="https://pytorch.org/",
    ),
    "InterpretML": LogoMeta(
        asset_path="/index/skills/library_logos/interpretml.png",
        link="https://interpret.ml/",
    ),
    "SHAP": LogoMeta(
        asset_path="/index/skills/library_logos/shap.png",
        link="https://shap.readthedocs.io/en/latest/",
    ),
    "StatsModels": LogoMeta(
        asset_path="/index/skills/library_logos/statsmodels.svg",
        link="https://www.statsmodels.org/stable/index.html",
    ),
    "Nixtla": LogoMeta(
        asset_path="/index/skills/library_logos/nixtla.png",
        link="https://nixtlaverse.nixtla.io/",
    ),
    "PyMC": LogoMeta(
        asset_path="/index/skills/library_logos/pymc.svg", link="https://docs.pymc.io/"
    ),
    "Scipy": LogoMeta(
        asset_path="/index/skills/library_logos/scipy.png",
        link="https://www.scipy.org/",
    ),
    "Pyomo": LogoMeta(
        asset_path="/index/skills/library_logos/pyomo.png", link="http://www.pyomo.org/"
    ),
    "Pandas": LogoMeta(
        asset_path="/index/skills/library_logos/pandas.svg",
        link="https://pandas.pydata.org/",
    ),
    "Ibis": LogoMeta(
        asset_path="/index/skills/library_logos/ibis.png",
        link="https://ibis-project.org/",
    ),
    "Numpy": LogoMeta(
        asset_path="/index/skills/library_logos/numpy.svg", link="https://numpy.org/"
    ),
    "Cupy": LogoMeta(
        asset_path="/index/skills/library_logos/cupy.png", link="https://cupy.dev/"
    ),
    "Rapids": LogoMeta(
        asset_path="/index/skills/library_logos/rapids.png", link="https://rapids.ai/"
    ),
    "NBDev": LogoMeta(
        asset_path="/index/skills/library_logos/nbdev.png",
        link="https://nbdev.fast.ai/",
    ),
    "Kedro": LogoMeta(
        asset_path="/index/skills/library_logos/kedro.png",
        link="https://kedro.readthedocs.io/en/stable/",
    ),
    "Reflex": LogoMeta(
        asset_path="/index/skills/library_logos/reflex.svg", link="https://reflex.dev/"
    ),
    "Matplotlib": LogoMeta(
        asset_path="/index/skills/library_logos/matplotlib.svg",
        link="https://matplotlib.org/",
    ),
    "Seaborn": LogoMeta(
        asset_path="/index/skills/library_logos/seaborn.svg",
        link="https://seaborn.pydata.org/",
    ),
    "Plotly": LogoMeta(
        asset_path="/index/skills/library_logos/plotly.png", link="https://plotly.com/"
    ),
}
