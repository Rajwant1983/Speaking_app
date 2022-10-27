from unicodedata import name
from flask_testing import LiveServerTestCase
from urllib.request import urlopen
from flask import url_for

#  this is testing 3
from application.app import application, d


class TestBase(LiveServerTestCase):
    TEST_PORT = 5050  # test port, doesn't need to be open

    def create_app(self):
        application.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///",
            LIVESERVER_PORT=self.TEST_PORT,
            DEBUG=True,
            TESTING=True
        )
        return application

    def setUp(self):
        from application.schema import Students
        d.create_all()  # create schema before we try to get the page
        #
        # test_student = Students(name="Test")
        # test1_student = Students(name="Test") need to create a query 2
        # d.session.add(test_student)
        # d.session.commit()

    def tearDown(self):
        d.session.remove()
        d.drop_all()


class TestAdd(TestBase):

    def test_index_route(self):
        response = application.test_client().get('/')

        assert response.status_code == 200
