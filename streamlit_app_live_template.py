import dataclasses

import streamlit as st
import logging
import coloredlogs
import sys


@dataclasses.dataclass
class Inputs:
    some_value: str = 'hello world!'


def get_class_from_url(class_type: type[dataclasses.dataclass()] = None):
    query_params = st.query_params
    dummy = class_type()
    data_dict = {**dummy.__dict__}
    data_dict.update({k: v for k, v in query_params.items() if k in data_dict})
    instance = class_type(**data_dict)
    return instance


def set_url_from_class(instance):
    instance_dict = dataclasses.asdict(instance)
    valid_keys = {}
    for key, value in instance_dict.items():
        if key.startswith('_'):
            continue
        try:
            bool(value)  # Check if value can be converted to a boolean
            valid_keys[key] = value
        except ValueError:
            continue
    d = {k: v for k, v in valid_keys.items() if v not in (0, None, '')}
    st.query_params.update(d)


def get_inputs():
    inputs = get_class_from_url(Inputs)

    set_url_from_class(inputs)
    return inputs


def app(inputs: Inputs):
    st.subheader(inputs)


def main():
    logger = logging.getLogger(__name__)

    st.set_page_config(page_title="My app",
                       page_icon="🧪",
                       layout="wide",
                       initial_sidebar_state="expanded",
                       )

    l_format = '%(asctime)s [%(name)s] %(module)s::%(funcName)s %(levelname)s - %(message)s'
    coloredlogs.install(level='CRITICAL', fmt=l_format)
    logger_levels = {
        'DEBUG': [logger.name],
        'WARNING': [],
        'INFO': [],
        'ERROR': ['watchdog'],
    }
    
    for level, loggers in logger_levels.items():
        for lg in loggers:
            coloredlogs.install(level=level, fmt=l_format, logger=logging.getLogger(lg), stream=sys.stdout, isatty=True)

    with st.sidebar:
        inputs = get_inputs()

    app(inputs)


if __name__ == '__main__':
    main()
