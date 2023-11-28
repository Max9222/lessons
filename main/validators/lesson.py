import re
from rest_framework.serializers import ValidationError


class YouTubeValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        regex = re.compile(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/')
        tmp_val = dict(value).get(self.field)

        if not bool(regex.match(tmp_val)):
            raise ValidationError('Не тот сайт')
