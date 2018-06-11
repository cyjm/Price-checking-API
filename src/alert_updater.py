from src.models.alerts.alert import Alert

alert_needing_update = Alert.find_needing_updates()

for alert in alert_needing_update:
    alert.load_item_price()
    alert.send_email_if_price_reached()