from actuators.name_reaction import NameReaction
from actuators.speaker import Speaker

def test_react_works(mocker):
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say")
    reaction = NameReaction(speaker)
    reaction.add("ok", "ok_id")
    reaction.react("ok")
    speaker_spy.assert_called_with("ok_id")

def test_react_doesnt_crash_with_unknown_name(mocker):
    speaker = Speaker()
    speaker_spy = mocker.spy(speaker, "say")
    reaction = NameReaction(speaker)
    reaction.react("ok")
    speaker_spy.assert_not_called()