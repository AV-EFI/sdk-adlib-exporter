from avefi_schema import model as efi

frame_rate_enum = {
    "16": efi.FrameRateEnum["16fps"],
    "23,98": efi.FrameRateEnum["23.98fps"],
    "24": efi.FrameRateEnum["24fps"],
    "25": efi.FrameRateEnum["25fps"],
    "30": efi.FrameRateEnum["30fps"],
    "48": efi.FrameRateEnum["48fps"],
    # Covered keys without mapping! Please provide mapping! #
    "18": None,
    "19": None,
    "20": None,
    "21": None,
    "22": None,
    "24fps": None,
    "29": None,
    "32": None,
    "42": None,
}
