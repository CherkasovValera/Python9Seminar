import view
import model
import logger

def button_click():
    type = view.get_type()
    value_a = view.get_value(type)
    action = view.get_action()
    value_b = view.get_value(type)
    model.init(value_a, value_b)
    result = model.do_it(action)
    view.view_data(result, "result = ")
    logger.log(f'{value_a}{action}{value_b}={result}')