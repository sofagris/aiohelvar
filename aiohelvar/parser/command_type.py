from enum import Enum


class CommandType(Enum):

    # Queries
    QUERY_CLUSTERS = (101, "Query Clusters.")
    QUERY_GROUP_DESCRIPTION = (105, "Query group description.")
    QUERY_DEVICE_DESCRIPTION = (106, "Query device description.")
    QUERY_DEVICE_TYPES_AND_ADDRESSES = (100, "Query Device Types and Addresses")
    QUERY_DEVICE_STATE = (110, "Query Device State")
    QUERY_WORKGROUP_NAME = (107, "Query Workgroup Name")
    QUERY_DEVICE_LOAD_LEVEL = (152, "Query Device Load Level")
    QUERY_SCENE_INFO = (167, "Query device scene levels.")
    QUERY_ROUTER_TIME = (185, "Query Router Time")
    QUERY_LAST_SCENE_IN_GROUP = (109, "Query last scene selected in a group.")
    QUERY_LAST_SCENE_IN_BLOCK = (103, "Query last scene selected in a group block.")
    QUERY_GROUP = (164, "Query devices in group.")
    QUERY_GROUPS = (165, "Query all groups.")
    QUERY_SCENE_NAMES = (166, "Query all scene names in group.")
    QUERY_ROUTER_VERSION = (190, "Query the router software version.")
    QUERY_HELVARNET_VERSION = (191, "Query the HelvarNet software version.")

    # Commands
    RECALL_SCENE_GROUP = (11, "Recall Scene (Group)")
    RECALL_SCENE_DEVICE = (12, "Recall Scene (Device)")
    DIRECT_LEVEL_GROUP = (13, "Direct Level (Group)")
    DIRECT_LEVEL_DEVICE = (14, "Direct Level (Device)")
    DIRECT_PROPORTION_GROUP = (15, "Direct Proportion (Group)") 
    DIRECT_PROPORTION_DEVICE = (16, "Direct Proportion (Device)")
    MODIFY_PROPORTION_GROUP = (17, "Modify Proportion (Group)")
    MODIFY_PROPORTION_DEVICE = (18, "Modify Proportion (Device)")
    EMERGENCY_FUNCTION_TEST_GROUP = (19, "Emergency Function Test (Group)")
    EMERGENCY_FUNCTION_TEST_DEVICE = (20, "Emergency Function Test (Device)")
    EMERGENCY_DURATION_TEST_GROUP = (21, "Emergency Duration Test (Group)")
    EMERGENCY_DURATION_TEST_DEVICE = (22, "Emergency Duration Test (Device)")
    STOP_EMERGENCY_TESTS_GROUP = (23, "Stop Emergency Tests (Group)")
    STOP_EMERGENCY_TESTS_DEVICE = (24, "Stop Emergency Tests (Device)")

    def __init__(self, command_id, description):
        self.command_id = command_id
        self.description = description

    def __str__(self):
        return f"{self.command_id}"

    @classmethod
    def get_by_command_id(cls, command_id):
        for member in cls:
            if member.value[0] == command_id:
                return member
        raise KeyError


COMMAND_TYPES_DONT_LISTEN_FOR_RESPONSE = [
    CommandType.RECALL_SCENE_GROUP,
    CommandType.DIRECT_LEVEL_DEVICE,
]


class MessageType(Enum):

    COMMAND = ">"
    INTERNAL_COMMAND = "<"
    REPLY = "?"
    ERROR = "!"

    def __str__(self):
        return self.value


class CommandParameterType(Enum):
    VERSION = "V"
    COMMAND = "C"
    ADDRESS = "@"
    GROUP = "G"
    SCENE = "S"
    BLOCK = "B"
    FADE_TIME = "F"
    LEVEL = "L"
    PROPORTION = "P"
    DISPLAY_SCREEN = "D"
    SEQUENCE_NUMBER = "Q"
    TIME = "T"
    ACK = "A"
    LATITUDE = "L"
    LONGITUDE = "E"
    TIME_ZONE_DIFFERENCE = "Z"
    DAYLIGHT_SAVING_TIME = "Y"
    CONSTANT_LIGHT_SCENE = "K"
    FORCE_STORE_SCENE = "O"

    def __str__(self):
        return self.value
