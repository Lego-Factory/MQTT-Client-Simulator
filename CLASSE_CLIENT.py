from CLASSE_MQTT import MQTT_Network
import time

class Client(MQTT_Network):

	def __init__ (self):

		super().__init__()
		self.topics = self.setup["topics"]

		self.time_msg = 3 #in secondi , serve a cambiare i secondi che intercorrono tra un messaggio e l'altro
		self.qty_msg = 20 #numero di messaggi di general e main manda il simulatore

	# Topics subscription method 
	def topics_subscriptions(self):
		self.client.subscribe(self.topics["general_topic"])
		self.client.subscribe(self.topics["setup_topic"])
		self.client.subscribe(self.topics["main_topic"])

	# Send test message (YOU CAN DELETE THIS PART)
	def publish_test_messages(self):
		
		#se vuoi mandare una sola tipologia di messaggi commenta la parte che non vuoi far mandare(ti metto i ## per capire le parti)
		
		for i in range(self.qty_msg):

			word = "TEST"+str(i)

			#
			payload_general = {
				"Station" : "Station-test",
				"State" : word
			}

			self.publish_msg(self.topics["general_topic"], payload_general)
			time.sleep(self.time_msg)
			#

			#
			payload_main = {
				"sender_name" : "PC-test",
				"receiver_name" : "M-test",
				"data" : word
			}

			self.publish_msg(self.topics["main_topic"], payload_main)
			time.sleep(self.time_msg)
			#


	# Messages logic method
	def messages_logic(self, topic, payload):
		print ("Topic :",topic)
		print("Payload :",payload) 
		#Insert logic here :
		#...



if __name__ == "__main__":

	client = Client()
	client.Print_Attributes()

	client.Start()
	time.sleep(3)
	client.publish_test_messages()
	time.sleep(3)
	client.Stop()

