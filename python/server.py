from __future__ import division
import scrape_from_text
from pythonosc import udp_client

# Audio recording parameters
client = udp_client.SimpleUDPClient("localhost", 7904)

scrape_from_text.run(client=client)
