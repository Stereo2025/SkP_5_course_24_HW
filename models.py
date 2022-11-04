from marshmallow import Schema, fields, validates_schema, ValidationError

VALID_CMD = ('filter', 'map', 'unique', 'sort', 'limit', 'regex')


class RequestParams(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)

    @validates_schema
    def valid_cdm_params(self, values, *args, **kwargs):
        if values['cmd'] not in VALID_CMD:
            raise ValidationError('"cmd: invalid value"')


class BatchRequestParams(Schema):
    queries = fields.Nested(RequestParams, many=True)
