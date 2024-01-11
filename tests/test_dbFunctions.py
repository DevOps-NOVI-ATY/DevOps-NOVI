from .test_main import client
import unittest
from unittest.mock import Mock, patch
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from app.models.models import Uitgever, Serie, Stripboek, Karakter, Cover_soort, Serie_strip, Strip_kar, Strip_cover
from app.models.dbFunctions import (
    startSession,
    commitAndCloseSession,
    closeSession,
    runSelectStatement,
    runInsertStatement,
)

class TestYourCode(unittest.TestCase):

    @patch('app.models.dbFunctions.SQLAlchemyError', autospec=True)
    def test_commitAndCloseSession(self, mock_SQLAlchemyError):
        mock_session = Mock()
        commitAndCloseSession(mock_session)
        mock_session.commit.assert_called_once()
        mock_session.close.assert_called_once() 

    @patch('app.models.dbFunctions.SQLAlchemyError', autospec=True)
    def test_closeSession(self, mock_SQLAlchemyError):
        mock_session = Mock()
        closeSession(mock_session)
        mock_session.close.assert_called_once()

    @patch('app.models.dbFunctions.startSession', autospec=True)
    @patch('app.models.dbFunctions.closeSession', autospec=True)
    def test_runSelectStatement(self, mock_closeSession, mock_startSession):
        mock_session = Mock()
        mock_session.scalars.return_value = [1, 2, 3]
        mock_startSession.return_value = mock_session

        result = runSelectStatement('SELECT * FROM table')
        self.assertEqual(result, [1, 2, 3])
        mock_session.scalars.assert_called_once_with('SELECT * FROM table')
        mock_closeSession.assert_called_once_with(mock_session)

    @patch('app.models.dbFunctions.startSession', autospec=True)
    @patch('app.models.dbFunctions.commitAndCloseSession', autospec=True)
    def test_runInsertStatement(self, mock_commitAndCloseSession, mock_startSession):
        mock_session = Mock()
        mock_insertableObject = Mock()
        mock_startSession.return_value = mock_session

        runInsertStatement(mock_insertableObject)
        mock_session.add.assert_called_once_with(mock_insertableObject)
        mock_commitAndCloseSession.assert_called_once_with(mock_session)

if __name__ == '__main__':
    unittest.main()