import paho.mqtt.client as mqtt

# MQTT 初始化連線設定
client = mqtt.Client()

# 發送訊息到指定主題
def send_message(server_address, server_port, topic, message):
    # 連線到 MQTT 伺服器
    client.connect(server_address, server_port, 60)
    client.loop_start()
    client.publish(topic, message)
    print(f"Sent message to {topic}: {message}")
    # 斷開 MQTT 伺服器連線
    client.loop_stop()
    client.disconnect()