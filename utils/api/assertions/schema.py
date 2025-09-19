from typing import Any

import allure
from jsonschema import validate
from jsonschema.validators import Draft202012Validator
from utils.logger import get_logger

logger = get_logger("SCHEMA_ASSERTIONS")


@allure.step("Validation of JSON schema")
def validate_json_schema(instance: Any, schema: dict) -> None:
    logger.info('Validation of JSON schema')

    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )
