import datetime

from avefi_schema import model as efi

from records.base.base_record import XMLAccessor


def compute_described_by(xml: XMLAccessor):
    return efi.DescriptionResource(
        has_issuer_id="https://w3id.org/isil/DE-MUS-407010",
        has_issuer_name="Deutsche Kinemathek - Museum für Film und Fernsehen",
        last_modified=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    )
