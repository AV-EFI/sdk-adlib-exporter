import logging
import os
import tempfile
from datetime import datetime

from linkml_runtime.dumpers import JSONDumper

from adlib import collect_provider, pointer_file_provider
from records.base.custom_errors import UnresolvableReferenceError
from records.item.item_record import ItemRecord
from records.manifestation.manifestation_record import ManifestationRecord
from records.work.work_record import WorkRecord

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
    def __init__(self, priref, builder, name):
        xml = pointer_file_provider.get_by_priref(priref)
        self.initial_prirefs = xml.xpath("hit/text()")
        self.builder = builder
        self.final_prirefs = []
        self.records = []
        self.name = name


def main():
    works = RecordCategory(
        priref=3,
        builder=WorkRecord,
        name="work",
    )
    manifestations = RecordCategory(
        priref=4,
        builder=ManifestationRecord,
        name="manifestation",
    )
    items = RecordCategory(
        priref=5,
        builder=ItemRecord,
        name="item",
    )

    logging.info(
        f"# Retrieved {len(works.initial_prirefs + manifestations.initial_prirefs + items.initial_prirefs)} prirefs:"
    )

    for i, record_category in enumerate([works, manifestations, items]):
        logging.info(
            f"{i+1}. {len(record_category.initial_prirefs)} ({record_category.name}s)"
        )

    # Process each record category and its allowed parent records.
    for i, (record_category, allowed_parents) in enumerate(
        [
            (works, works.initial_prirefs),
            (manifestations, works.final_prirefs),
            (items, manifestations.final_prirefs),
        ]
    ):
        logging.info(f"# Handling {record_category.name}s")
        process_records(
            record_category=record_category,
            allowed_parents=allowed_parents,
        )

    records = works.records + manifestations.records + items.records

    logging.info(f"# Built {len(records)} records")

    # Create a temporary file for the JSON output.
    file_obj, json_file = tempfile.mkstemp(
        prefix=datetime.now().strftime("%Y%m%d-%H%M%S-"),
        suffix=".json",
    )
    os.close(file_obj)

    # Write the records to a JSON file using the JSONDumper.
    dumper = JSONDumper()
    dumper.dump(records, json_file, inject_type=False)

    print(f"Wrote data to file://{json_file}")


def process_records(record_category, allowed_parents):
    # Loop over each priref in the current record category.
    for i, priref in enumerate(record_category.initial_prirefs):
        logging.info(
            f"Handling {record_category.name} {i+1}/{len(record_category.initial_prirefs)} with priref {priref}"
        )
        try:
            # Fetch the XML data from the collect_provider using the priref.
            xml = collect_provider.get_by_priref(priref)

            # print(type(xml))
            # Build the record using the associated records.
            record = record_category.builder(xml, allowed_parents, priref).build()

            # record_json = JSONDumper().dumps(record)
            #
            # print(record_json)
            #
            # pid = get_pid(json.loads(record_json))
            # print(pid)

            # Store the built record and its priref.
            record_category.records.append(record)
            record_category.final_prirefs.append(record.has_identifier[0].id)
        except UnresolvableReferenceError as e:
            logging.error(f"Error during mapping of {priref}: {type(e).__name__}, {e}")
        except Exception as e:
            logging.error(f"Error during mapping of {priref}: {e}", exc_info=True)
            pass


if __name__ == "__main__":
    main()
