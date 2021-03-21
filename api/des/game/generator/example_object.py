from des.user.db_actions import user_exists


def get_menu_dict(jwt_identity):
    user = user_exists(username=jwt_identity)
    return [
        {"name": jwt_identity, "folded": True, "submenu": [
            {"name": "Vessels", "folded": True, "submenu": [
                {"name": "Boats", "folded": True, "submenu": [
                    {"name": "Buy Rib", "type":"action", "action": "game/store/vessels/boats/go-fast/buy/", 
                     "infoTip": "game/store/vessels/boats/go-fast/infoTip/",
                     "hoverTip": "game/store/vessels/boats/go-fast/hoverTip/"
                    }
                ]}
            ]}
        ]},
        {"name": "Inventory", "folded": True, "submenu": [
            {"name": "Vessels", "folded": True, "submenu": [
                {"name": "Boats", "folded": True, "submenu": [
                    {"name": "Rib #1", "subActions": [
                        {"name": "Sell", "action": "game/inventory/vessels/1/sell/", "hoverTip": "game/inventory/vessels/1/hoverTip/"}
                    ], "folded": True, "submenu": [
                        {"name": "Upgrade Speed", "type": "action", "infoTip": "game/inventory/vessels/1/speed/upgrade/"},
                        {"name": "Upgrade Fuel efficiency", "type": "action", "infoTip": "game/inventory/vessels/1/fuelEfficency/upgrade/"},
                        {"name": "Upgrade Detection Rate", "type": "action", "infoTip": "game/inventory/vessels/1/detectionRate/upgrade/"}
                    ]}
                ]}
            ]}
        ]},
        {"name": "Deals", "folded": True, "submenu": [
            {}
        ]},
        {"name": user['matching_user'].role, "type": "label", "folded": True, "submenu": [
            {}
        ]}
    ]
