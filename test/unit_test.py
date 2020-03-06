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

def test_option_merge(logic, disable_set, enable_set):
    print("options : \n{}".format("\n".join(["\t{}: {}".format(opt.id(), opt.name()) for opt in logic._options.values()])))
    print("disable case")
    try:
        disable = Untitled.CompositeOption(id=len(logic._options), name="disable_case",
                                           parents=[logic.get_option(disable_set[0]),logic.get_option(disable_set[1])])
        print("{} is created.".format(disable.name()))
    except Untitled.OptionMergeError as e:
        print(e)

    print("enable case")
    enable = Untitled.CompositeOption(id=len(logic._options), name="enable_case",
                                      parents=[logic.get_option(enable_set[0]),logic.get_option(enable_set[1])])
    print("{} is created.".format(enable.name()))

if __name__ == "__main__":

    logic = Untitled.Logic()
    logic.load_option_data(test_option_data)

    #Test to add option into logic.
    test_select_and_print(logic)
    test_select_and_print(logic, [1])
    test_select_and_print(logic, [5])

    #Test to merge options.
    test_option_merge(logic, disable_set=(0,1), enable_set=(1,3))
