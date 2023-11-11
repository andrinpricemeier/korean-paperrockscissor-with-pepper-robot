import time

from sensors.game_region import GameRegion
import logging

class DibiGameRegion(GameRegion):
    def __init__(self, memory, speaker):
        self.memory = memory
        self.speaker = speaker

    def is_in_zone(self, zone):
        zone_people = self.memory.getData("EngagementZones/PeopleInZone" + str(zone))
        return zone_people is not None and len(zone_people) > 0

    def all_zones_empty(self):
        return not self.is_in_zone(1) and not self.is_in_zone(2) and not self.is_in_zone(3)

    def ensure_is_in_zone(self, desired_zone, num_tries=5, time_in_seconds_for_opponent_to_move=2):
        current_tries = num_tries
        while current_tries > 0:
            for zone in range(1, 4):
                if self.all_zones_empty():
                    logging.info("No one around anymore. Stopping region scan.")
                    return
                if self.is_in_zone(desired_zone):
                    logging.info("Is in the desired zone. Stopping scan.")
                    return
                if zone != desired_zone and self.is_in_zone(zone):
                    if zone < desired_zone:
                        logging.info("Person too close.")
                        self.speaker.say("opponent_too_close")
                        time.sleep(time_in_seconds_for_opponent_to_move)
                    else:
                        logging.info("Person too far away.")
                        self.speaker.say("opponent_too_far")
                        time.sleep(time_in_seconds_for_opponent_to_move)
            current_tries -= 1