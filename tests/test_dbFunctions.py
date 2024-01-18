import unittest
from unittest.mock import Mock, patch, MagicMock
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
        # Mock the execute method of the session object
        mock_session = MagicMock()
        mock_startSession.return_value = mock_session

        # Mock the fetchall to return a list of MagicMock objects
        mock_row1, mock_row2 = MagicMock(), MagicMock()
        mock_row1._asdict.return_value = {'id': 1, 'value': 10}
        mock_row2._asdict.return_value = {'id': 2, 'value': 20}
        mock_session.execute().fetchall.return_value = [mock_row1, mock_row2]

        # Perform the test
        statement = 'SELECT * FROM test_table'
        result = runSelectStatement(statement)

        # Assert the expected result
        expected_result = [{'id': 1, 'value': 10}, {'id': 2, 'value': 20}]
        assert result == expected_result

        # Assert that startSession and closeSession were called
        mock_startSession.assert_called_once()
        mock_closeSession.assert_called_once()
        mock_row1._asdict.assert_called_once()
        mock_row2._asdict.assert_called_once()
    
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