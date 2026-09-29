# Manual download of UNFCCC files

Русская версия: [manual_unfccc_download.md](manual_unfccc_download.md).

> **Status:** this procedure is retained for reproducibility only. All four listed source files have already been obtained and saved in the project; no further manual download is required.

If the raw files ever need independent verification or replacement, use the original files and save them without unpacking or renaming:

| Required file | Official access point | Project destination |
|---|---|---|
| Kazakhstan 2025 CRT | [UNFCCC reports repository](https://www.unfccc.int/reports?f%5B0%5D=corporate_author%3A222&f%5B1%5D=document_type%3A4593&items_per_page=10&order=name&search2=&search3=&sort=desc) | `data/raw/unfccc_crt_2025/` |
| Kazakhstan 2025 NID | [UNFCCC NID 2025 document page](https://unfccc.int/documents/646542) | `data/raw/unfccc_reports/` |
| Kazakhstan 2023 CRF | [UNFCCC reports repository](https://www.unfccc.int/reports?f%5B0%5D=corporate_author%3A222&f%5B1%5D=document_type%3A4147&items_per_page=10&order=field_document_sb&search2=&search3=&sort=desc) | `data/raw/unfccc_crf_2023/` |
| Kazakhstan 2023 NIR | [UNFCCC 2023 inventory submissions](https://www.unfccc.int/ghg-inventories-annex-i-parties/2023) | `data/raw/unfccc_reports/` |

After a replacement, record the retrieval date, URL and SHA-256 hash in the [acquisition log](data_acquisition_log_en.md). Keep originals unchanged and extract tables only into a separate `extracted/` subfolder.

