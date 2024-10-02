import os
import tempfile
from linkml_runtime.dumpers import JSONDumper
from adlib import collect_provider, pointer_file_provider
from builder.item_builder import ItemBuilder
from builder.manifestation_builder import ManifestationBuilder
from builder.work_builder import WorkBuilder


class RecordCategory:
    """
    A class to manage records of a specific type (e.g., works, manifestations, items).

    Attributes:
        priref (int): The identifier used to fetch initial XML data via pointer file.
        builder (class): The builder class used to process the XML data into structured records.
        initial_prirefs (list): A list of prirefs retrieved from the pointer file.
        final_prirefs (list): A list of processed record prirefs after record building.
        records (list): A list to store the processed records.
    """

    def __init__(self, priref, builder):
        xml = pointer_file_provider.get_by_priref(priref)
        self.initial_prirefs = xml.xpath("hit/text()")

        self.builder = builder
        self.final_prirefs = []
        self.records = []


def main():
    """
    Main entry point to process works, manifestations, and items into records,
    and then write them to a JSON file.
    """
    works = RecordCategory(priref=462, builder=WorkBuilder)
    manifestations = RecordCategory(priref=468, builder=ManifestationBuilder)
    items = RecordCategory(priref=469, builder=ItemBuilder)

    print(
        f"Retrieved {len(works.initial_prirefs + manifestations.initial_prirefs + items.initial_prirefs)} prirefs:",
        f"\n1. {len(works.initial_prirefs)} (works)",
        f"\n2. {len(manifestations.initial_prirefs)} (manifestations)",
        f"\n3. {len(items.initial_prirefs)} (items)",
    )

    # Process each record category and its allowed parent records.
    for i, (record_category, allowed_parents) in enumerate(
        [
            (works, works.initial_prirefs),
            (manifestations, works.final_prirefs),
            (items, manifestations.final_prirefs),
        ]
    ):
        print("Handling category", i + 1)
        process_records(
            record_category=record_category,
            allowed_parents=allowed_parents,
        )

    records = works.records + manifestations.records + items.records

    print(f"Built {len(records)} records")

    # Create a temporary file for the JSON output.
    file_obj, json_file = tempfile.mkstemp(suffix=".json")
    os.close(file_obj)

    # Write the records to a JSON file using the JSONDumper.
    dumper = JSONDumper()
    dumper.dump(records, json_file, inject_type=False)

    print(f"Wrote data to file://{json_file}")


def process_records(record_category, allowed_parents):
    """
    Process each priref in a given RecordCategory, build records, and store them.

    Args:
        record_category (RecordCategory): The category of records to process.
        allowed_parents (list): The list of allowed parent prirefs for handling unresolved references to non-existent records.
    """
    # Loop over each priref in the current record category.
    for i, priref in enumerate(record_category.initial_prirefs):
        print(
            "Handling record",
            f"{i+1}/{len(record_category.initial_prirefs)}",
            "of this category with priref",
            priref,
        )
        try:
            # Fetch the XML data from the collect_provider using the priref.
            xml = collect_provider.get_by_priref(priref)
            # Build the record using the associated builder.
            record = record_category.builder(xml, allowed_parents).build()

            # Store the built record and its priref.
            record_category.records.append(record)
            record_category.final_prirefs.append(record.has_identifier[0].id)
        except Exception as e:
            # Silently handle any errors during the record-building process.
            # To debug, comment/uncomment the line below:
            print(f"Error during mapping of {priref}:", e)
            pass


if __name__ == "__main__":
    main()
