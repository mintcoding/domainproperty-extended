def parse_query_data(form):

    querydata = {
        "listingType": "Sale",
        "minPrice": "",
        "maxPrice": "",
        "locations": [
            {
                "state": "WA",
                "postCode": "",
            }
        ]
    }
    form_dict = {
        "locations": [
            {
                "state": "WA",
                "postCode": "",
            }
        ]
    }

    for i in form.visible_fields():
        field_name = i.name
        field_value = i.value()
        if i.name == "postCode":
            try:
                form_dict['locations'][0].update({'postCode': field_value})
            except (ValueError, Exception) as e:
                raise e
        else:
            try:
                form_dict.update({field_name: field_value})
            except (ValueError, Exception) as e:
                raise e
    try:
        querydata.update(form_dict)
    except (ValueError, Exception) as e:
        raise e

    print(querydata)
    return querydata
