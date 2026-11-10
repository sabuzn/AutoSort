from autosort.app.app import App

import sys

def main() -> None:
    try:
        app: App = App()
        app.Start()

    except Exception as Error:
        sys.exit(
            f"\x1b[31merror:\x1b[0m {Error}"
        )

    except KeyboardInterrupt:
        sys.exit(
            0
        )

if __name__ == "__main__":
    sys.stdout.write(
        "\x1b[2J\x1b[H"
    )

    sys.exit(
        main()
    )
