# Ручная загрузка файлов UNFCCC

English version: [manual_unfccc_download_en.md](manual_unfccc_download_en.md).

> **Статус:** инструкция сохранена для воспроизводимости. Все четыре перечисленных исходника уже получены и сохранены в проекте; вручную скачивать их больше не требуется.

Автоматическая загрузка из текущей рабочей среды возвращает HTML-страницу защиты UNFCCC вместо файлов. Пожалуйста, скачайте оригиналы в браузере и поместите их в указанные папки без распаковки.

| Нужный файл | Официальная ссылка | Что нажать / ожидаемый формат | Куда положить |
|---|---|---|---|
| Kazakhstan 2025 CRT | [репозиторий CRT Казахстана](https://www.unfccc.int/reports?f%5B0%5D=corporate_author%3A222&f%5B1%5D=document_type%3A4593&items_per_page=10&order=name&search2=&search3=&sort=desc) | строка «Kazakhstan. 2025 Common Reporting Table (CRT)», submission 15 Apr 2025, English ZIP | `data/raw/unfccc_crt_2025/` |
| Kazakhstan 2025 NID | [страница документа NID 2025](https://unfccc.int/documents/646542) | скачать PDF «Kazakhstan. 2025 National Inventory Document (NID)» | `data/raw/unfccc_reports/` |
| Kazakhstan 2023 CRF | [репозиторий CRF Казахстана](https://unfccc.int/reports?f%5B0%5D=corporate_author%3A222&f%5B1%5D=document_type%3A4147&items_per_page=10&order=field_document_sb&search2=&search3=&sort=desc) | строка «Kazakhstan. 2023 Common Reporting Format (CRF) Table», submission 15 Apr 2023, English ZIP | `data/raw/unfccc_crf_2023/` |
| Kazakhstan 2023 NIR | [страница инвентарных представлений 2023](https://www.unfccc.int/ghg-inventories-annex-i-parties/2023) | в строке Kazakhstan выбрать `NIR`, дата 15 Apr 2023 | `data/raw/unfccc_reports/` |

После загрузки напишите «файлы загружены». Я проверю типы файлов, внесу контрольные суммы в реестр и начну извлечение IPPU-рядов. Не требуется переименовывать файлы: исходное имя полезно для аудита.
