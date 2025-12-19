def getOrderStatus(order_id: str):
    mock_db = {
        "12345": {
            "order_id": "12345",
            "status": "Shipped",
            "carrier": "DHL",
            "tracking_number": "DHL-88439201",
            "estimated_delivery": "2025-03-18"
        },
        "54321": {
            "order_id": "54321",
            "status": "Processing",
            "carrier": None,
            "tracking_number": None,
            "estimated_delivery": None
        }
    }

    return mock_db.get(order_id, {
        "order_id": order_id,
        "status": "Not Found"
    })
