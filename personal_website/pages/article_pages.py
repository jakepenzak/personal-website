import reflex as rx

from personal_website.structural import template
from personal_website.components.utilities.html_helpers import iframe_gen
from personal_website.components.giscus import giscus
from personal_website.components.website_bar import website_bar
from assets import asset_data


def generate_article_page(abbreviation: str, article_name: str):
    @template(route=f"/articles/{abbreviation}", title=article_name)
    def article_page() -> rx.Component:
        return rx.vstack(
            rx.box(
                rx.html(iframe_gen(f"/articles/{abbreviation}/{abbreviation}.html")),
                width="100%",
            ),
            rx.center(
                rx.box(
                    giscus(
                        repo="jakepenzak/personal-website",
                        repo_id="R_kgDOKoIM0Q",
                        category="Article Comments",
                        category_id="DIC_kwDOKoIM0c4CoM0P",
                        mapping="specific",
                        term=article_name,
                        strict="0",
                        reactions_enabled="1",
                        emit_metadata="0",
                        input_position="top",
                        theme=rx.color_mode_cond("fro", "dark"),
                        lang="en",
                        loading="lazy",
                    ),
                    width="50%",
                ),
                width="100%",
            ),
            website_bar(),
            min_height="80vh",
            width="100%",
        )

    globals()[abbreviation] = article_page


for abbreviation, article_meta in asset_data.ARTICLES_META_DICT.items():
    generate_article_page(abbreviation, article_meta.title_str)
