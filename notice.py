import logging
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers import event

_LOGGER = logging.getLogger(__name__)
DOMAIN = 'notice'
CONF_INTERVAL_TIME = "time"
CONF_INFO = "message"
CONF_TITLE = 'title'

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Required(CONF_INTERVAL_TIME): cv.time_period,
                vol.Optional(CONF_INTERVAL_TIME, default=86400): cv.time_period,
                vol.Required(CONF_INFO): cv.string,
                vol.Required(CONF_TITLE): cv.string,
            }),
    },
    extra=vol.ALLOW_EXTRA)


async def async_setup(hass, config):
    conf = config[DOMAIN]
    title = conf[CONF_TITLE]
    content = conf[CONF_INFO]

    def crate_notification(event_time):
        hass.components.persistent_notification.async_create(
            content, title)

    event.async_track_time_interval(
        hass, crate_notification, conf[CONF_INTERVAL_TIME])

    return True
