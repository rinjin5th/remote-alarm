from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

class MQTTClient:

    def __init__(self, client_id, host, root_ca, cert, key):
        self._client = AWSIoTMQTTClient(client_id)
        self._client.configureEndpoint(host, 8883)
        self._client.configureCredentials(root_ca, key, cert)
        self._client.configureAutoReconnectBackoffTime(1, 32, 20)
        self._client.configureOfflinePublishQueueing(-1)
        self._client.configureDrainingFrequency(2)
        self._client.configureConnectDisconnectTimeout(10)
        self._client.configureMQTTOperationTimeout(5)

    def subscribe(self, topic, callback):
        self._client.connect()
        self._client.subscribe(topic, 1, callback)
