def generate_response_list(items):
    return {
        "total": len(items),
        "items": items,
    }
