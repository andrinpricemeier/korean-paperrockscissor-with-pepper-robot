from actuators.corpus import Corpus
from utils.static_random_source import StaticRandomSource

def test_lookup_works():
    corpus = Corpus({ "my_id": ["anything"]}, StaticRandomSource())
    assert corpus.lookup("my_id") == "anything"

def test_lookup_not_found_doesnt_crash():
    corpus = Corpus({ "my_id": ["anything"]}, StaticRandomSource())
    assert corpus.lookup("no_id") == "no_id"

def test_lookup_with_args_works():
    corpus = Corpus({ "my_id": ["anything {0}"]}, StaticRandomSource())
    assert corpus.lookup_with_args("my_id", "value") == "anything value"