# Dialogue Inverse Kinematics

>[!warning]
> This system generates single-turn NPC utterances for bounded game situations.
> It does not do free conversation.
> It does not invent facts.
> It operates on dialogue acts, not raw language.

This is a POC for a dynamic dialogue generation system I am trying to build in hopes of making game dialogues more interesting.
The aim is to create parts of dialogues based on "intent", similarly to Inverse Kinematics, where the position of joins is calculated based on where the end joint is supposed to be.

## Axes
The first step is to define axes, which is my take on conceptualizing "intent" as data. As this is a **bounded** system, we must strictly define what each utterance can do. It's important that you are able to simply explain each axis in a single sentence, otherwise it might easily get complicated.

e.g.
```
inform      (0-1) How much factual info is conveyed
reassure    (0-1) Reassure the player
refuse      (0-1) Deny a request / block progress
authority   (0-1) Assert power or rules
```

## Dialogue Structures
This is the core of the idea, the concept is to define a modular structure/template on which an intent can be mapped.
each structure must be mapped to an intent vector, the more structures the merrier.

e.g. 
```
<S> Informative Statement -> Conveys Info, neutral
<S> Soft refusal -> Denies request, Reassuring
<S> Warning -> Highlight danger or rule, Authoritative
```

Example implementation in pseudo code for one of them:
```
Soft refusal:
    required:
        - refusal
    optional:
        - apology
        - reassurance

intent vector:
    inform: 0
    refuse: 1
    reassure: 0.5
    authority: 0.2
```

## Slots
This is where the language appears, but locally. For each slot, create and define short phrases, each also mapping to an intent vectore to give it a score. I think you see where this is going now.

e.g.
```
apology:
 - "I'm sorry"
 - "I apologize"

refusal:
- "I can't do that"
- "That's not possible"
- "I can't allow that"

reassurance:
- "but it's not a problem"
- "we'll find another way"
- "it should be fine"
```
