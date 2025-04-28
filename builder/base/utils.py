def get_formatted_date(date_start, date_start_prec, date_end, date_end_prec):
    production_date_start_value = date_start + ("~" if date_start_prec else "")
    production_date_end_value = date_end + ("~" if date_end_prec else "")
    return (
        production_date_start_value
        if production_date_start_value == production_date_end_value
        else f"{production_date_start_value}/{production_date_end_value}"
    )
