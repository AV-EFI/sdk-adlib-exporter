from avefi_schema import model as efi

agent_type_enum = {
    "Institution": efi.AgentTypeEnum.CorporateBody,
    "Person": efi.AgentTypeEnum.Person,
    # Covered keys without mapping! Please provide mapping! #
    "Körperschaft": None,
}
