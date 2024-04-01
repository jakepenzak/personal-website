from typing import NamedTuple

## COMMON
# Website Footer Image
WEBSITE_FOOTER_IMAGE = "/shared/website_bar.png"

# Logo Paths
FOOTER_LOGO = "/shared/icon-inverted.png"
LINKEDIN_LOGO = "/shared/social_icons/linkedin.png"
MEDIUM_LOGO = "/shared/social_icons/medium.png"
GITHUB_LOGO = "/shared/social_icons/github.png"
EMAIL_LOGO = "/shared/social_icons/email.png"
NAVBAR_LOGO = "/shared/icon.png"

# Social Media Links
GITHUB_URL = "https://github.com/jakepenzak"
CONTACT_URL = "mailto:jakepzak@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/japieniazek/"
MEDIUM_URL = "https://medium.com/@jakepenzak"

## Index Page
INDEX_INTRO = "assets/index/index_intro.md"
INDEX_PHOTO = "/index/self.jpg"

SKILLS_DATA = [
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
        "rating": 65,
    },
    {
        "subject": "Web Development",
        "rating": 46,
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


TECH_INTRO_TXT = """Similarly, below is a selection of some of the tech
                stack & tools that I use or have used in my personal & professional work."""

TECH_LOGOS_META_DICT = {
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
    "Delta Lake": LogoMeta(
        asset_path="/index/skills/tech_logos/delta.png",
        link="https://delta.io/",
    ),
}

LIBRARY_INTRO_TXT = """Below is a selection of some of the python libraries 
                I use or have used in my personal & professional work. This list is by no means exhaustive,
                but it does cover a subset of the core libraries I consider myself to be moderately to highly proficient in."""

LIBRARY_LOGOS_META_DICT = {
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

## Article Page
ARTICLES_INTRO = "assets/articles/intro.md"


class ArticleMeta(NamedTuple):
    img_src: str
    href: str
    title_src: str
    descr_src: str


ARTICLES_META_DICT = {
    "DML2": ArticleMeta(
        img_src="/articles/dml2/cover.png",
        href="https://towardsdatascience.com/double-machine-learning-simplified-part-2-extensions-the-cate-99926151cac",
        title_src="assets/articles/dml2/title.md",
        descr_src="assets/articles/dml2/description.md",
    ),
    "DML1": ArticleMeta(
        img_src="/articles/dml1/cover.png",
        href="https://towardsdatascience.com/double-machine-learning-simplified-part-1-basic-causal-inference-applications-3f7afc9852ee",
        title_src="assets/articles/dml1/title.md",
        descr_src="assets/articles/dml1/description.md",
    ),
    "TSNE": ArticleMeta(
        img_src="/articles/tsne/cover.png",
        href="https://towardsdatascience.com/t-sne-from-scratch-ft-numpy-172ee2a61df7",
        title_src="assets/articles/tsne/title.md",
        descr_src="assets/articles/tsne/description.md",
    ),
    "NM3": ArticleMeta(
        img_src="/articles/nm3/cover.jpeg",
        href="https://towardsdatascience.com/optimization-newtons-method-profit-maximization-part-3-applied-profit-maximization-23a8c16167cd",
        title_src="assets/articles/nm3/title.md",
        descr_src="assets/articles/nm3/description.md",
    ),
    "NM2": ArticleMeta(
        img_src="/articles/nm2/cover.jpeg",
        href="https://towardsdatascience.com/optimization-newtons-method-profit-maximization-part-2-constrained-optimization-theory-dc18613c5770",
        title_src="assets/articles/nm2/title.md",
        descr_src="assets/articles/nm2/description.md",
    ),
    "NM1": ArticleMeta(
        img_src="/articles/nm1/cover.gif",
        href="https://towardsdatascience.com/optimization-newtons-method-profit-maximization-part-1-basic-optimization-theory-ff7c5f966565",
        title_src="assets/articles/nm1/title.md",
        descr_src="assets/articles/nm1/description.md",
    ),
    "Logistic": ArticleMeta(
        img_src="/articles/logistic/cover.png",
        href="https://towardsdatascience.com/predictive-parameters-in-a-logistic-regression-making-sense-of-it-all-476bde9825f3",
        title_src="assets/articles/logistic/title.md",
        descr_src="assets/articles/logistic/description.md",
    ),
    "FWL": ArticleMeta(
        img_src="/articles/fwl/cover.png",
        href="https://towardsdatascience.com/controlling-for-x-9cb51652f7ad",
        title_src="assets/articles/fwl/title.md",
        descr_src="assets/articles/fwl/description.md",
    ),
}

## Research Page
THESIS_TITLE = "assets/research/thesis.md"
CAPSTONE_TITLE = "assets/research/capstone.md"

THESIS_LINK = "/research/thesis.pdf"

## Resume Page
RESUME_IMAGE = "/resume/resume.jpg"
RESUME_LINK = "/resume/resume.pdf"
