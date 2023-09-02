import logging
from pathlib import Path
import arxiv


logger = logging.getLogger(__name__)


PATH_HERE = Path(__file__).resolve()
DATA_DIR = PATH_HERE.parent.parent / "data"
ARXIV_IDS = ["2303.18223"]


def fetch_arxiv_pdfs(arxiv_ids: list[str]=ARXIV_IDS, data_dir: Path=DATA_DIR):
    logger.info(f"using {data_dir=}")
    data_dir.mkdir(parents=True, exist_ok=True)
    papers = list(arxiv.Search(id_list=arxiv_ids).results())
    for paper in papers:
        logger.info(f"fetching {paper}")
        paper.download_pdf(dirpath=data_dir)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fetch_arxiv_pdfs()






