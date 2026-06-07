import sys
import os

# Ensure project root is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.utils import clean_text

def test_clean_text_basic():
    assert clean_text("Hello World!") == "hello world"

def test_clean_text_urls():
    assert clean_text("Go to http://example.com or www.google.com") == "go to url or url"
    assert clean_text("Check https://test.org/path") == "check url"

def test_clean_text_emails():
    assert clean_text("Contact me at test@example.com.") == "contact me at email"

def test_clean_text_contractions():
    assert clean_text("what's up") == "what is up"
    assert clean_text("it's cool") == "it cool"
    assert clean_text("I've been there") == "i have been there"
    assert clean_text("I can't do it") == "i cannot do it"
    assert clean_text("don't run") == "do not run"
    assert clean_text("I'm fine") == "i am fine"
    assert clean_text("we're testing") == "we are testing"
    assert clean_text("I'd go") == "i would go"
    assert clean_text("they'll win") == "they will win"
    assert clean_text("'scuse me") == "excuse me"

def test_clean_text_numbers_and_special_chars():
    assert clean_text("Room 101 has 3 apples.") == "room has apples"
    assert clean_text("This / is # a @ test!") == "this is a test"

def test_clean_text_spacing():
    assert clean_text("   lots  of    spaces   ") == "lots of spaces"
