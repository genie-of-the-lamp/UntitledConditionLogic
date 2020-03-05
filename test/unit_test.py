import Untitled

test_option_data = [
    {
        "name": "NAVI_A",
         "id": 0,
         "children": [3,4],
         "incompatible": [1,2],
        "optional": False
    },
    {
        "name": "NAVI_B",
         "id": 1,
         "children": [3,5],
         "incompatible": [0,2],
        "optional": False
     },
    {
        "name": "AUDIO",
         "id": 2,
         "children": [5],
         "incompatible": [0,1],
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
         "incompatible": [5],
        "optional": True
     },
    {
        "name":"HIGHEND_SPEAKER",
         "id": 5,
         "incompatible": [4],
        "optional": True
     }
]

def test_select_and_print(logic, selected_ids=[]):
    logic.calculate(added_selection=selected_ids)
    print("selected_option_ids: {}".format(logic.selected_options))
    print("enable_option_ids: {}".format(logic.enabled))
    print("disable_option_ids: {}\n".format(logic.disabled))


if __name__ == "__main__":
    logic = Untitled.Logic()
    logic.load_option_data(test_option_data)
    test_select_and_print(logic)
    test_select_and_print(logic, [1])
    test_select_and_print(logic, [5])
