<?xml version="1.0" encoding="UTF-8" ?>
<Package name="DibiActivities" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="ask_for_game" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="opponent_to_play" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="hey_hey_you" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="squid_game" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="hello_world" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="wave_detection" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="psst_psst" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="rockpaperscissor" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="face_detection" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="dibi_dance" xar="behavior.xar" />
        <BehaviorDescription name="behavior" src="unlearn_faces" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="ExampleDialog" src="ask_for_game/ExampleDialog/ExampleDialog.dlg" />
        <Dialog name="ask_for_game_topic" src="ask_for_game_topic/ask_for_game_topic.dlg" />
    </Dialogs>
    <Resources>
        <File name="choice_sentences" src="hey_hey_you/Aldebaran/choice_sentences.xml" />
    </Resources>
    <Topics>
        <Topic name="ExampleDialog_enu" src="ask_for_game/ExampleDialog/ExampleDialog_enu.top" topicName="ExampleDialog" language="en_US" />
        <Topic name="ask_for_game_topic_enu" src="ask_for_game_topic/ask_for_game_topic_enu.top" topicName="ask_for_game_topic" language="en_US" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
