MenuDict = [
    {"name": "Store", "submenu": [
        {"name": "Vessels", "submenu": [
            {"name": "Boats", "submenu": [
                {"name": "Buy Rib", "type":"action", "action": "/api/store/vessels/boats/go-fast/buy", 
                 "infoTip": "/api/store/vessels/boats/go-fast/infoTip",
                 "hoverTip": "/api/store/vessels/boats/go-fast/hoverTip"
                }
            ]}
        ]}
    ]},
    {"name": "Inventory", "submenu": [
        {"name": "Vessels", "submenu": [
            {"name": "Boats", "submenu": [
                {"name": "Rib #1", "subActions": [
                    {"name": "Sell", "action": "/api/inventory/vessels/1/sell", "hoverTip": "/api/inventory/vessels/1/hoverTip"}
                ], "submenu": [
                    {"name": "Upgrade Speed", "type": "action", "infoTip": "/api/inventory/vessels/1/speed/upgrade"},
                    {"name": "Upgrade Fuel efficiency", "type": "action", "infoTip": "/api/inventory/vessels/1/fuelEfficency/upgrade"},
                    {"name": "Upgrade Detection Rate", "type": "action", "infoTip": "/api/inventory/vessels/1/detectionRate/upgrade"}
                ]}
            ]}
        ]}
    ]},
    {"name": "Deals", "submenu": [
        {}
    ]}
]
