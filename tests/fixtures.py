import factory
import datetime

from .models import UserTable, RegionTable, Session


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = UserTable
        sqlalchemy_session = Session

    user = factory.Iterator(['user1', 'user1', 'user2', 'user2'])
    date = factory.Iterator([
        datetime.date(2013, 1, 1),
        datetime.date(2013, 2, 1),
        datetime.date(2013, 1, 1),
        datetime.date(2013, 3, 1)
    ])
    indicator_a = factory.Iterator([1, 3, 0, 2])
    indicator_b = factory.Iterator([1, 0, 3, 1])
    indicator_c = factory.Iterator([1, None, 2, None])


class RegionFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = RegionTable
        sqlalchemy_session = Session

    region = factory.Iterator(['region1', 'region1', 'region1', 'region1', 'region2'])
    sub_region = factory.Iterator(['region1_a', 'region1_a', 'region1_b', 'region1_b', 'region2_a'])
    date = factory.Iterator([
        datetime.date(2013, 1, 1),
        datetime.date(2013, 2, 1),
        datetime.date(2013, 1, 1),
        datetime.date(2013, 3, 1),
        datetime.date(2013, 1, 1)
    ])
    indicator_a = factory.Iterator([1, 0, 3, 1, 2])
    indicator_b = factory.Iterator([0, 1, 1, 1, 1])
