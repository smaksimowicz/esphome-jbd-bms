import esphome.codegen as cg
from esphome.components import text_sensor
import esphome.config_validation as cv
from esphome.const import CONF_ICON, CONF_ID

from . import CONF_JBD_BMS_ID, JbdBms

DEPENDENCIES = ["jbd_bms"]

CODEOWNERS = ["@syssi"]

CONF_ERRORS = "errors"
CONF_ALARM = "alarms"
CONF_OPERATION_STATUS = "operation_status"
CONF_DEVICE_MODEL = "device_model"

ICON_ERRORS = "mdi:alert-circle-outline"
ICON_ALARM = "mdi:alert-circle-outline"
ICON_OPERATION_STATUS = "mdi:heart-pulse"
ICON_DEVICE_MODEL = "mdi:chip"

TEXT_SENSORS = [CONF_ERRORS, CONF_ALARM, CONF_OPERATION_STATUS, CONF_DEVICE_MODEL]

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(CONF_JBD_BMS_ID): cv.use_id(JbdBms),

    cv.Optional(CONF_ERRORS): text_sensor.text_sensor_schema({
        cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
        cv.Optional(CONF_ICON, default=ICON_ERRORS): cv.icon,
    }),

    cv.Optional(CONF_ALARM): text_sensor.text_sensor_schema({
        cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
        cv.Optional(CONF_ICON, default=ICON_ALARM): cv.icon,
    }),

    cv.Optional(CONF_OPERATION_STATUS): text_sensor.text_sensor_schema({
        cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
        cv.Optional(CONF_ICON, default=ICON_OPERATION_STATUS): cv.icon,
    }),

    cv.Optional(CONF_DEVICE_MODEL): text_sensor.text_sensor_schema({
        cv.GenerateID(): cv.declare_id(text_sensor.TextSensor),
        cv.Optional(CONF_ICON, default=ICON_DEVICE_MODEL): cv.icon,
    }),
})


async def to_code(config):
    hub = await cg.get_variable(config[CONF_JBD_BMS_ID])
    for key in TEXT_SENSORS:
        if key in config:
            conf = config[key]
            # zamiast new_Pvariable -> użyj helpera
            sens = await text_sensor.new_text_sensor(conf)
            cg.add(getattr(hub, f"set_{key}_text_sensor")(sens))
