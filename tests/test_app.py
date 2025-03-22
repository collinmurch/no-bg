import os
import pytest
from app import app as flask_app


@pytest.fixture
def app():
    """Create and configure a Flask app for testing."""
    # Create test folders
    os.makedirs(flask_app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(flask_app.config['PROCESSED_FOLDER'], exist_ok=True)
    
    # Disable debug mode for testing
    flask_app.config['TESTING'] = True
    flask_app.config['DEBUG'] = False
    
    yield flask_app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


def test_index_page(client):
    """Test the index page loads correctly."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Background Remover' in response.data