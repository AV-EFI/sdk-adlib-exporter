from avefi_schema import model as efi

format_video_type_enum = {
    "Betacam SP": efi.FormatVideoTypeEnum.BetacamSP,
    "D1": efi.FormatVideoTypeEnum.D1,
    "DVCPRO": efi.FormatVideoTypeEnum.DVCPROHD,
    "DigiBeta": efi.FormatVideoTypeEnum.DigitalBetacam,
    "HDCam SR": efi.FormatVideoTypeEnum.HDCAMSR,
    # Covered keys without mapping! Please provide mapping! #
    "VHS": None,
    "U-Matic": None,
    "DIGI BETA SP": None,
    "MPEG IMX": None,
    "Betamax": None,
    "DVD": None,
    "Blu-ray": None,
    "HDCam": None,
}
