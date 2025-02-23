def iframe_gen(file_path: str) -> str:
    iframe_code = f"""
    <iframe id="contentFrame"
            src="{file_path}"
            width="100%"
            style="border:none; display:block; background:white; min-height:80vh;"
            onload="setTimeout(()=>{{ this.style.height = this.contentDocument.documentElement.scrollHeight + 'px'; }}, 300)">
    </iframe>
    """

    return iframe_code
