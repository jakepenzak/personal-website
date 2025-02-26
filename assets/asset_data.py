from typing import NamedTuple

## COMMON
# Website Footer Image
WEBSITE_FOOTER_IMAGE = "/shared/website_bar.webp"

# Logo Paths
FOOTER_LOGO = "/shared/icon-inverted.webp"
LINKEDIN_LOGO = "/shared/social_icons/linkedin.webp"
MEDIUM_LOGO = "/shared/social_icons/medium.webp"
GITHUB_LOGO = "/shared/social_icons/github.webp"
EMAIL_LOGO = "/shared/social_icons/email.webp"
NAVBAR_LOGO = "/shared/icon.webp"

# Social Media Links
GITHUB_URL = "https://github.com/jakepenzak"
CONTACT_URL = "mailto:jacob@pieniazek.me"
LINKEDIN_URL = "https://www.linkedin.com/in/japieniazek/"
MEDIUM_URL = "https://medium.com/@jakepenzak"

## Index Page
INDEX_INTRO = "assets/index/index_intro.md"
INDEX_PHOTO = "/index/self.webp"

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
        asset_path="/index/skills/tech_logos/azure.webp",
        link="https://azure.microsoft.com/en-us",
    ),
    "DataBricks": LogoMeta(
        asset_path="https://user-images.githubusercontent.com/25181517/197845567-86a09ca9-d96f-42c4-9ab1-8bce95ab000d.png",
        link="https://databricks.com/",
    ),
    "Digital Ocean": LogoMeta(
        asset_path="/index/skills/tech_logos/digitalocean.webp",
        link="https://www.digitalocean.com/",
    ),
    "CloudFlare": LogoMeta(
        asset_path="https://github.com/devicons/devicon/raw/master/icons/cloudflare/cloudflare-original-wordmark.svg",
        link="https://www.cloudflare.com/",
    ),
    "NGINX": LogoMeta(
        asset_path="https://github.com/devicons/devicon/raw/master/icons/nginx/nginx-original.svg",
        link="https://nginx.org/",
    ),
    "GitHub": LogoMeta(
        asset_path="/index/skills/tech_logos/github.webp",
        link="https://www.github.com/",
    ),
    "Git": LogoMeta(
        asset_path="https://github.com/devicons/devicon/raw/master/icons/git/git-original-wordmark.svg",
        link="https://git-scm.com/",
    ),
    "Docker": LogoMeta(
        asset_path="/index/skills/tech_logos/docker.webp",
        link="https://www.docker.com/",
    ),
    "Conda": LogoMeta(
        asset_path="/index/skills/tech_logos/conda.webp",
        link="https://docs.conda.io/en/latest/",
    ),
    "Astral UV": LogoMeta(
        asset_path="https://docs.astral.sh/uv/assets/logo-letter.svg",
        link="https://docs.astral.sh/uv/",
    ),
    "Cuda": LogoMeta(
        asset_path="/index/skills/tech_logos/cuda.webp",
        link="https://developer.nvidia.com/cuda-zone",
    ),
    "Jupyter": LogoMeta(
        asset_path="/index/skills/tech_logos/jupyter.webp", link="https://jupyter.org/"
    ),
    "Marimo": LogoMeta(
        asset_path="https://raw.githubusercontent.com/marimo-team/marimo/main/docs/_static/marimo-logotype-thick.svg",
        link="https://marimo.io/",
    ),
    "Quarto": LogoMeta(
        asset_path="https://github.com/quarto-dev/quarto-web/raw/main/quarto-icon.svg",
        link="https://quarto.org/",
    ),
    "Mardown": LogoMeta(
        asset_path="https://github.com/devicons/devicon/raw/master/icons/markdown/markdown-original.svg",
        link="https://www.markdownguide.org/",
    ),
    "Spark": LogoMeta(
        asset_path="/index/skills/tech_logos/spark.webp",
        link="https://spark.apache.org/",
    ),
    "duckDB": LogoMeta(
        asset_path="/index/skills/tech_logos/duckdb.webp", link="https://duckdb.org/"
    ),
    "Delta Lake": LogoMeta(
        asset_path="/index/skills/tech_logos/delta.webp",
        link="https://delta.io/",
    ),
    "Neovim": LogoMeta(
        asset_path="https://github.com/devicons/devicon/raw/master/icons/neovim/neovim-original.svg",
        link="https://neovim.io/",
    ),
    "VS Code": LogoMeta(
        asset_path="/index/skills/tech_logos/vscode.webp",
        link="https://code.visualstudio.com/",
    ),
    "Python": LogoMeta(
        asset_path="/index/skills/tech_logos/python.webp",
        link="https://www.python.org/",
    ),
    "R": LogoMeta(
        asset_path="https://github.com/devicons/devicon/raw/master/icons/r/r-original.svg",
        link="https://www.r-project.org/",
    ),
    "Bash": LogoMeta(
        asset_path="https://github.com/devicons/devicon/raw/master/icons/bash/bash-original.svg",
        link="https://www.gnu.org/software/bash/",
    ),
    "Stata": LogoMeta(
        asset_path="/index/skills/tech_logos/stata.webp", link="https://www.stata.com/"
    ),
    "Linux": LogoMeta(
        asset_path="/index/skills/tech_logos/linux.webp", link="https://www.linux.org/"
    ),
    "Apple": LogoMeta(
        asset_path="https://github.com/devicons/devicon/raw/master/icons/apple/apple-original.svg",
        link="",
    ),
    "PowerBI": LogoMeta(
        asset_path="/index/skills/tech_logos/powerbi.webp",
        link="https://powerbi.microsoft.com/en-us/",
    ),
    "Obsidian": LogoMeta(
        asset_path="/index/skills/tech_logos/obsidian.webp", link="https://obsidian.md/"
    ),
}

LIBRARY_INTRO_TXT = """Below is a non-exhaustive selection of some of the python libraries/frameworks/ecosystems 
                I use or have used in my personal & professional work."""

LIBRARY_LOGOS_META_DICT = {
    "EconML": LogoMeta(
        asset_path="/index/skills/library_logos/econml.webp",
        link="https://www.microsoft.com/en-us/research/project/econml/",
    ),
    "DoubleML": LogoMeta(
        asset_path="/index/skills/library_logos/doubleml.webp",
        link="https://docs.doubleml.org/stable/index.html",
    ),
    "DoWhy": LogoMeta(
        asset_path="/index/skills/library_logos/dowhy.webp",
        link="https://www.pywhy.org/dowhy/v0.11.1/",
    ),
    "CausalML": LogoMeta(
        asset_path="/index/skills/library_logos/causalml.webp",
        link="https://causalml.readthedocs.io/en/latest/",
    ),
    "SciKit-Learn": LogoMeta(
        asset_path="/index/skills/library_logos/sklearn.webp",
        link="https://scikit-learn.org/stable/",
    ),
    "XGBoost": LogoMeta(
        asset_path="/index/skills/library_logos/xgboost.webp",
        link="https://xgboost.readthedocs.io/en/latest/",
    ),
    "LightGBM": LogoMeta(
        asset_path="/index/skills/library_logos/lightgbm.webp",
        link="https://lightgbm.readthedocs.io/en/latest/",
    ),
    "PyTorch": LogoMeta(
        asset_path="/index/skills/library_logos/pytorch.webp",
        link="https://pytorch.org/",
    ),
    "Hugging Face": LogoMeta(
        asset_path="https://huggingface.co/datasets/huggingface/brand-assets/resolve/main/hf-logo.svg",
        link="https://huggingface.co/",
    ),
    "InterpretML": LogoMeta(
        asset_path="/index/skills/library_logos/interpretml.webp",
        link="https://interpret.ml/",
    ),
    "SHAP": LogoMeta(
        asset_path="/index/skills/library_logos/shap.webp",
        link="https://shap.readthedocs.io/en/latest/",
    ),
    "StatsModels": LogoMeta(
        asset_path="/index/skills/library_logos/statsmodels.webp",
        link="https://www.statsmodels.org/stable/index.html",
    ),
    "Nixtla": LogoMeta(
        asset_path="/index/skills/library_logos/nixtla.webp",
        link="https://nixtlaverse.nixtla.io/",
    ),
    "PyMC": LogoMeta(
        asset_path="/index/skills/library_logos/pymc.webp", link="https://docs.pymc.io/"
    ),
    "Scipy": LogoMeta(
        asset_path="/index/skills/library_logos/scipy.webp",
        link="https://www.scipy.org/",
    ),
    "Pyomo": LogoMeta(
        asset_path="/index/skills/library_logos/pyomo.webp",
        link="http://www.pyomo.org/",
    ),
    "Pandas": LogoMeta(
        asset_path="/index/skills/library_logos/pandas.webp",
        link="https://pandas.pydata.org/",
    ),
    "Ibis": LogoMeta(
        asset_path="/index/skills/library_logos/ibis.webp",
        link="https://ibis-project.org/",
    ),
    "Polars": LogoMeta(
        asset_path="https://raw.githubusercontent.com/pola-rs/polars-static/master/banner/polars_github_banner.svg",
        link="https://pola.rs/",
    ),
    "Numpy": LogoMeta(
        asset_path="/index/skills/library_logos/numpy.webp", link="https://numpy.org/"
    ),
    "Jax": LogoMeta(
        asset_path="https://docs.jax.dev/en/latest/_static/jax_logo_250px.png",
        link="https://docs.jax.dev/en/latest/",
    ),
    "Cupy": LogoMeta(
        asset_path="/index/skills/library_logos/cupy.webp", link="https://cupy.dev/"
    ),
    "Rapids": LogoMeta(
        asset_path="/index/skills/library_logos/rapids.webp", link="https://rapids.ai/"
    ),
    "Ray": LogoMeta(
        asset_path="https://cdn.brandfetch.io/idxF9UqF37/theme/dark/logo.svg?c=1dxbfHSJFAPEGdCLU4o5B",
        link="https://docs.ray.io/en/latest/",
    ),
    "Flaml": LogoMeta(
        asset_path="https://github.com/microsoft/FLAML/raw/main/website/static/img/flaml.svg",
        link="https://microsoft.github.io/FLAML/docs/Getting-Started",
    ),
    "NBDev": LogoMeta(
        asset_path="/index/skills/library_logos/nbdev.webp",
        link="https://nbdev.fast.ai/",
    ),
    "Kedro": LogoMeta(
        asset_path="/index/skills/library_logos/kedro.webp",
        link="https://kedro.readthedocs.io/en/stable/",
    ),
    "Reflex": LogoMeta(
        asset_path="/index/skills/library_logos/reflex.webp", link="https://reflex.dev/"
    ),
    "Matplotlib": LogoMeta(
        asset_path="/index/skills/library_logos/matplotlib.webp",
        link="https://matplotlib.org/",
    ),
    "Seaborn": LogoMeta(
        asset_path="/index/skills/library_logos/seaborn.webp",
        link="https://seaborn.pydata.org/",
    ),
    "Plotly": LogoMeta(
        asset_path="/index/skills/library_logos/plotly.webp", link="https://plotly.com/"
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
        img_src="/articles/dml2/cover.webp",
        href="https://towardsdatascience.com/double-machine-learning-simplified-part-2-extensions-the-cate-99926151cac",
        title_src="assets/articles/dml2/title.md",
        descr_src="assets/articles/dml2/description.md",
    ),
    "DML1": ArticleMeta(
        img_src="/articles/dml1/cover.webp",
        href="/articles/dml1",
        title_src="assets/articles/dml1/title.md",
        descr_src="assets/articles/dml1/description.md",
    ),
    "TSNE": ArticleMeta(
        img_src="/articles/tsne/cover.webp",
        href="/articles/tsne",
        title_src="assets/articles/tsne/title.md",
        descr_src="assets/articles/tsne/description.md",
    ),
    "NM3": ArticleMeta(
        img_src="/articles/nm3/cover.webp",
        href="https://towardsdatascience.com/optimization-newtons-method-profit-maximization-part-3-applied-profit-maximization-23a8c16167cd",
        title_src="assets/articles/nm3/title.md",
        descr_src="assets/articles/nm3/description.md",
    ),
    "NM2": ArticleMeta(
        img_src="/articles/nm2/cover.webp",
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
        img_src="/articles/logistic/cover.webp",
        href="/articles/logistic",
        title_src="assets/articles/logistic/title.md",
        descr_src="assets/articles/logistic/description.md",
    ),
    "FWL": ArticleMeta(
        img_src="/articles/fwl/cover.webp",
        href="/articles/fwl",
        title_src="assets/articles/fwl/title.md",
        descr_src="assets/articles/fwl/description.md",
    ),
}

## Research Page
THESIS_TITLE = "assets/research/thesis.md"
CAPSTONE_TITLE = "assets/research/capstone.md"

THESIS_LINK = "/research/thesis.pdf"

## Resume Page
RESUME_IMAGE = "/resume/resume.webp"
RESUME_LINK = "/resume/resume.pdf"
