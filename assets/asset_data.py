from typing import Final, NamedTuple

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
INDEX_SPOTIFY = "assets/index/spotify.md"
INDEX_PHOTO = "/index/self.webp"
INDEX_AVATAR = "/index/avatar.webp"
INDEX_AVATAR_URL = "https://github.com/jakepenzak"

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
        "subject": "Artificial Intelligence",
        "rating": 72,
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


# Capability-first index page blocks (used by the refactored skills section).
CORE_STRENGTHS: Final[list[str]] = [
    "Causal Inference, Causal ML, & Econometrics",
    "Statistical Learning, ML, & AI",
    "MLOps / DevOps & Delivery / Package Development",
    "Data Platforms & Analytics Engineering",
]

FOCUS_AREA_STYLE: Final[dict[str, dict[str, str]]] = {
    "Causal Inference, Causal ML, & Econometrics": {
        "color_scheme": "purple",
        "variant": "soft",
    },
    "Statistical Learning, ML, & AI": {"color_scheme": "blue", "variant": "soft"},
    "MLOps / DevOps & Delivery / Package Development": {
        "color_scheme": "orange",
        "variant": "soft",
    },
    "Data Platforms & Analytics Engineering": {
        "color_scheme": "green",
        "variant": "soft",
    },
}

PROFILE_FOCUS_AREAS: Final[list[dict[str, object]]] = [
    {
        "title": "Causal Inference, Causal ML, & Econometrics",
        "tagline": "I mostly work on program evaluation and modeling heterogeneous treatment effects - getting to who benefits, and by how much, not just a single average.",
        "highlights": [
            "CATE / uplift modeling, treatment targeting, and 'Causal ML'",
            "Traditional econometrics and quasi-experimental design & methods",
            "Identification + robustness checks (sensitivity, diagnostics)",
            "Turning research-y work into reusable pipelines",
        ],
        "tools": ["DoubleML", "EconML", "DoWhy", "CausalML", "Statsmodels", "PyMC"],
    },
    {
        "title": "Statistical Learning, ML, & AI",
        "tagline": "I build predictive models and practical AI workflows, with a strong emphasis on evaluation, maintainability, and making outputs usable for real decisions.",
        "highlights": [
            "Model selection, calibration, and monitoring-ready metrics",
            "Interpretable ML and stakeholder-friendly explanations",
            "Agentic workflows + LLM tooling where it genuinely helps",
        ],
        "tools": [
            "scikit-learn",
            "XGBoost",
            "LightGBM",
            "FLAML",
            "MLFlow",
            "Optuna",
            "PyTorch",
            "Hugging Face",
            "LangChain",
            "LiteLLM",
            "OpenCode",
        ],
    },
    {
        "title": "MLOps / DevOps & Delivery / Package Development",
        "tagline": "I like shipping things that other people can actually run: packages, services, and reproducible environments that don't crumble a week later.",
        "highlights": [
            "Packaging + dependency management (reproducible builds)",
            "Containerization and CI-friendly workflows",
            "Docs, tooling, and small developer experience improvements",
        ],
        "tools": ["Git", "GitHub Actions", "Docker", "Linux", "uv", "ruff", "pytest"],
    },
    {
        "title": "Data Platforms & Analytics Engineering",
        "tagline": "I build data foundations that are reliable, fast, and pleasant to use, so analysis and models don't start from chaos every time.",
        "highlights": [
            "Lakehouse patterns + distributed compute",
            "Query performance, reproducible datasets, and data quality checks",
            "Azure + Databricks for production workflows",
        ],
        "tools": [
            "Databricks",
            "Azure",
            "Spark",
            "Delta Lake",
            "DuckDB",
            "Kedro",
        ],
    },
]


## Article Page
ARTICLES_INTRO = "assets/articles/intro.md"


class ArticleMeta(NamedTuple):
    img_src: str
    href: str
    title_src: str
    title_str: str
    descr_src: str
    category: str
    types: list[str]


article_categories = (
    "Econometrics",
    "Optimization",
    "Machine Learning",
    "General Data Science",
    "Networking",
    "Home Lab",
)

article_types = ("Series", "Short", "Theory", "Applied")

article_badge_config = {
    "Econometrics": {"color_scheme": "orange", "variant": "soft"},
    "Optimization": {"color_scheme": "green", "variant": "soft"},
    "Machine Learning": {"color_scheme": "blue", "variant": "soft"},
    "General Data Science": {"color_scheme": "gray", "variant": "soft"},
    "Networking": {"color_scheme": "purple", "variant": "soft"},
    "Home Lab": {"color_scheme": "red", "variant": "soft"},
    "Series": {"color_scheme": "gold", "variant": "soft"},
    "Short": {"color_scheme": "jade", "variant": "soft"},
    "Theory": {"color_scheme": "tomato", "variant": "soft"},
    "Applied": {"color_scheme": "cyan", "variant": "soft"},
}

ARTICLES_META_DICT = {
    "dml2": ArticleMeta(
        img_src="/articles/dml2/cover.webp",
        href="/articles/dml2",
        title_src="assets/articles/dml2/title.md",
        title_str="Double Machine Learning, Simplified: Part 2",
        descr_src="assets/articles/dml2/description.md",
        category="Econometrics",
        types=["Theory", "Series"],
    ),
    "dml1": ArticleMeta(
        img_src="/articles/dml1/cover.webp",
        href="/articles/dml1",
        title_src="assets/articles/dml1/title.md",
        title_str="Double Machine Learning, Simplified: Part 1",
        descr_src="assets/articles/dml1/description.md",
        category="Econometrics",
        types=["Theory", "Series"],
    ),
    "tsne": ArticleMeta(
        img_src="/articles/tsne/cover.webp",
        href="/articles/tsne",
        title_src="assets/articles/tsne/title.md",
        title_str="t-SNE from Scratch (ft. NumPy)",
        descr_src="assets/articles/tsne/description.md",
        category="Machine Learning",
        types=["Theory"],
    ),
    "nm3": ArticleMeta(
        img_src="/articles/nm3/cover.webp",
        href="/articles/nm3",
        title_src="assets/articles/nm3/title.md",
        title_str="Optimization, Newton's Method, & Profit Maximization: Part 3",
        descr_src="assets/articles/nm3/description.md",
        category="Optimization",
        types=["Applied", "Series"],
    ),
    "nm2": ArticleMeta(
        img_src="/articles/nm2/cover.webp",
        href="/articles/nm2",
        title_src="assets/articles/nm2/title.md",
        title_str="Optimization, Newton's Method, & Profit Maximization: Part 2",
        descr_src="assets/articles/nm2/description.md",
        category="Optimization",
        types=["Theory", "Series"],
    ),
    "nm1": ArticleMeta(
        img_src="/articles/nm1/cover.gif",
        href="/articles/nm1",
        title_src="assets/articles/nm1/title.md",
        title_str="Optimization, Newton's Method, & Profit Maximization: Part 1",
        descr_src="assets/articles/nm1/description.md",
        category="Optimization",
        types=["Theory", "Series"],
    ),
    "logistic": ArticleMeta(
        img_src="/articles/logistic/cover.webp",
        href="/articles/logistic",
        title_src="assets/articles/logistic/title.md",
        title_str="Predictive Parameters in a Logistic Regression",
        descr_src="assets/articles/logistic/description.md",
        category="Econometrics",
        types=["Theory", "Applied"],
    ),
    "fwl": ArticleMeta(
        img_src="/articles/fwl/cover.webp",
        href="/articles/fwl",
        title_src="assets/articles/fwl/title.md",
        title_str="Controlling for 'X'?",
        descr_src="assets/articles/fwl/description.md",
        category="Econometrics",
        types=["Theory", "Applied"],
    ),
}

## Research Page
BROWN_BAG_PATH = "/research/causal-ml-brown-bag.pdf"
THESIS_LINK = "/research/thesis.pdf"

## Resume Page
RESUME_IMAGE = "/resume/resume.v0.webp"
RESUME_LINK = "/resume/resume.v0.pdf"
