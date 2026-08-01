def iframe_gen(file_path: str) -> str:
    iframe_code = f"""
    <iframe id="contentFrame"
            src="{file_path}"
            width="100%"
            style="border:none; display:block; background:transparent; min-height:100vh;"
            onload="
              this.contentWindow.focus();
              const frame = this;
              const syncColorMode = () => {{
                try {{
                  const isDark = document.documentElement.classList.contains('dark');
                  const body = frame.contentDocument.body;
                  const toggle = frame.contentWindow.quartoToggleColorScheme;
                  if (body && typeof toggle === 'function' && body.classList.contains('quarto-dark') !== isDark) {{
                    toggle();
                  }}
                }} catch (error) {{}}
              }};
              syncColorMode();
              if (frame.colorModeObserver) frame.colorModeObserver.disconnect();
              frame.colorModeObserver = new MutationObserver(syncColorMode);
              frame.colorModeObserver.observe(document.documentElement, {{ attributes: true, attributeFilter: ['class'] }});
            ">
    </iframe>
    """

    return iframe_code
