import Untitled

test_option_data = [
    {
        "name": "NAVI_A",
         "id": 0,
         "children": ["BLUETOOTH", "WIRELESS_CHARGE"],
         "incompatible": ["NAVI_B","AUDIO"],
        "optional": False
    },
    {
        "name": "NAVI_B",
         "id": 1,
         "children": ["BLUETOOTH","HIGHEND_SPEAKER"],
         "incompatible": ["NAVI_A","AUDIO"],
        "optional": False
     },
    {
        "name": "AUDIO",
         "id": 2,
         "children": ["HIGHEND_SPEAKER"],
         "incompatible": ["NAVI_A","NAVI_B"],
        "optional": False
     },
    {
        "name":"BLUETOOTH",
         "id": 3,
        "optional": True
     },
    {
        "name":"WIRELESS_CHARGE",
         "id": 4,
         "incompatible": ["HIGHEND_SPEAKER"],
        "optional": True
     },
    {
        "name":"HIGHEND_SPEAKER",
         "id": 5,
         "incompatible": ["WIRELESS_CHARGE"],
        "optional": True
     }
]

def test_select_and_print(logic, selected_ids=[]):
    logic.calculate(added_selection=selected_ids)
    print("selected_option_ids: {}".format(logic.selected_option_ids))
    print("enable_option_ids: {}".format(list(map(lambda x: x.id(), logic.enabled_option))))
    print("disable_option_ids: {}\n".format(list(map(lambda x: x.id(), logic.disabled_option))))
if __name__ == "__main__":
    #Test to add option into logic.
    logic = Untitled.Logic()
    logic.load_option_data(test_option_data)
    test_select_and_print(logic)
    test_select_and_print(logic, [1])
    test_select_and_print(logic, [5])
