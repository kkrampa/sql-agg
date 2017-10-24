from unittest2.case import TestCase

from .fixtures import Session, UserFactory, RegionFactory


class BaseTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(BaseTest, cls).setUpClass()
        cls.session = Session()
        UserFactory.create_batch(4)
        RegionFactory.create_batch(5)

    @classmethod
    def tearDownClass(cls):
        cls.session.rollback()
        Session.remove()
        super(BaseTest, cls).tearDownClass()
