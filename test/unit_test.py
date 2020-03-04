import Untitled

test_option_data = [
    {
        "name": "NAVI_A",
         "id": 0,
         "children": [3,4],
         "incompatible": [1,2]
    },
    {
        "name": "NAVI_B",
         "id": 1,
         "children": [3,5],
         "incompatible": [0,2]
     },
    {
        "name": "AUDIO",
         "id": 2,
         "children": [5],
         "incompatible": [0,1]
     },
    {
        "name":"BLUETOOTH",
         "id": 3
     },
    {
        "name":"WIRELESS_CHARGE",
         "id": 4,
         "incompatible": [5]
     },
    {
        "name":"HIGHEND_SPEAKER",
         "id": 5,
         "incompatible": [4]
     }
]

def test_data_input(logic):
    for data in test_option_data:
        opt = logic.create_option(data.get("name"))
        if data.get("children"):
            opt._child_options.extend(data.get("children"))
        if data.get("incompatible"):
            opt._incompatible_options.extend(data.get("incompatible"))

def test_select_and_print(logic, selected_ids=[]):
    logic.calculate(added_selection=selected_ids)
    print("selected_option_ids: {}".format(logic.selected_options))
    print("enable_option_ids: {}".format(logic.enabled))
    print("disable_option_ids: {}\n".format(logic.disabled))


if __name__ == "__main__":
    logic = Untitled.Logic()
    test_data_input(logic)
    test_select_and_print(logic, [1])
    test_select_and_print(logic, [5])