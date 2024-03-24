import reflex as rx

data = [
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
        "rating": 70,
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

skills_list = rx.unordered_list(
    rx.list_item("Econometrics/Causal Inference"),
    rx.list_item("Statistics/Statistical Learning"),
    rx.list_item("Mathematical Optimization"),
    rx.list_item("Time Series Analysis"),
    rx.list_item("Deep Learning/AI"),
    rx.list_item("Web Development"),
    rx.list_item("DevOps + MLOps"),
    rx.list_item("Data Pipelining/Engineering"),
    rx.list_item("Package Development"),
)
