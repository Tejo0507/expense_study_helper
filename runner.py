from streamlit.web.cli import main
import sys

if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "app/main.py"]
    sys.exit(main())
