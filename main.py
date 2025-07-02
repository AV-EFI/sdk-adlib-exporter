import logging
import os
import tempfile
from datetime import datetime

from linkml_runtime.dumpers import JSONDumper

from axiell_collections import collect_provider, pointer_file_provider
from records.record import Record

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

all_logs_handler = logging.FileHandler("all.log", mode="w")
all_logs_handler.setLevel(logging.INFO)
all_logs_handler.setFormatter(formatter)
logger.addHandler(all_logs_handler)

error_logs_handler = logging.FileHandler("errors.log", mode="w")
error_logs_handler.setLevel(logging.ERROR)
error_logs_handler.setFormatter(formatter)
logger.addHandler(error_logs_handler)


class RecordCategory:
    def __init__(self, priref, record_type):
        xml = pointer_file_provider.get_by_priref(priref)
        self.prirefs = xml.xpath("hit/text()")
        self.record_type = record_type
        self.records = []


def main():
    works = RecordCategory(
        priref=3,
        record_type="work",
    )
    manifestations = RecordCategory(
        priref=4,
        record_type="manifestation",
    )
    items = RecordCategory(
        priref=5,
        record_type="item",
    )

    logging.info(
        f"# Retrieved {len(works.prirefs + manifestations.prirefs + items.prirefs)} prirefs:"
    )

    for i, record_category in enumerate([works, manifestations, items]):
        logging.info(f"{i+1}. {len(record_category.prirefs)} ({record_category.record_type}s)")

    for i, record_category in enumerate([works, manifestations, items]):
        logging.info(f"# Handling {record_category.record_type}s")
        process_records(
            record_category=record_category,
        )

    logging.info(
        f"# Built {len(works.records + manifestations.records + items.records)} records"
    )

    purged_records = purge_records(works.records, manifestations.records, items.records)

    logging.info(f"# After purge: {len(purged_records)} records")

    file_obj, json_file = tempfile.mkstemp(
        prefix=datetime.now().strftime("%Y%m%d-%H%M%S-"),
        suffix=".json",
    )
    os.close(file_obj)

    dumper = JSONDumper()
    dumper.dump(purged_records, json_file, inject_type=False)

    print(f"Wrote data to file://{json_file}")


def process_records(record_category):
    for i, priref in enumerate(record_category.prirefs):
        logging.info(
            f"Handling {record_category.record_type} {i+1}/{len(record_category.prirefs)} with priref {priref}"
        )
        try:
            xml = collect_provider.get_by_priref(priref)
            record = Record(record_category.record_type, xml).build()
            record_category.records.append(record)
        except Exception as e:
            logging.error(f"Error during mapping of {priref}: {e}", exc_info=True)
            pass


def purge_records(works, manifestations, items):
    work_prirefs = {work.has_identifier[0].id for work in works}
    purged_works = [
        work
        for work in works
        if all(parent.id in work_prirefs for parent in work.is_part_of)
    ]

    purged_work_prirefs = {work.has_identifier[0].id for work in purged_works}
    purged_manifestations = [
        manifestation
        for manifestation in manifestations
        if all(
            parent.id in purged_work_prirefs
            for parent in manifestation.is_manifestation_of
        )
    ]

    purged_manifestation_prirefs = {
        manifestation.has_identifier[0].id for manifestation in purged_manifestations
    }
    purged_items = [
        item
        for item in items
        if item.is_item_of and item.is_item_of.id in purged_manifestation_prirefs
    ]

    return purged_works + purged_manifestations + purged_items


if __name__ == "__main__":
    main()
