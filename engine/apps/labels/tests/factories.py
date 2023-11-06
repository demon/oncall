import factory

from apps.labels.models import (
    AlertGroupAssociatedLabel,
    AlertReceiveChannelAssociatedLabel,
    LabelKeyCache,
    LabelValueCache,
)
from common.utils import UniqueFaker


class LabelKeyFactory(factory.DjangoModelFactory):
    id = UniqueFaker("word")
    name = UniqueFaker("word")

    class Meta:
        model = LabelKeyCache


class LabelValueFactory(factory.DjangoModelFactory):
    id = UniqueFaker("word")
    name = UniqueFaker("word")

    class Meta:
        model = LabelValueCache


class AlertReceiveChannelAssociatedLabelFactory(factory.DjangoModelFactory):
    class Meta:
        model = AlertReceiveChannelAssociatedLabel


class AlertGroupAssociatedLabelFactory(factory.DjangoModelFactory):
    class Meta:
        model = AlertGroupAssociatedLabel