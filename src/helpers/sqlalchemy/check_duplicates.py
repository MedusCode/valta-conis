def check_entity_exists(model, field, value):
    entity = model.query.filter(getattr(model, field) == value).one_or_none()

    return True if entity else False
