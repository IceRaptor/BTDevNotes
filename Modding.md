Modding Concepts

### New Salvage Model
FrostRaptor — Today at 1:07 PM
@Interactive Rubber Dolphin what did you mean by?
The proper full mech salvage is one of the white whales of modding tbh
Interactive Rubber Dolphin — Today at 1:07 PM
pone always wanted to do it
FrostRaptor — Today at 1:08 PM
I mean the concept
Like 'pick X units to drag off the field, leave the rest, keep what's in them'?
Interactive Rubber Dolphin — Today at 1:08 PM
you get percentage of salvage and mechs in the state they were left on the field
yeah
!pone
RogueBot
BOT
 — Today at 1:09 PM
@De????n
▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓
▒▒▒░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓
▒▒░▐▌░▒░░░░░░▒▒▒▒▒▒▒▒▒
▒▒░░▌░░░░░░░░░░▒▒▒▒▒▒▒
▒▒▒▒░░░░░░░░░░░░▓▓▓▒▒▒
▒▒▒▒▒▒░░▀▀███░░░░▓▒▒▒▓
▒▒▒▒▒▒░▌▄████▌░░░▓▒▒▒▓
▒▒▒▒▒░░███▄█▌░░░▓▓▒▓▓▓
▒▒▒▒▒▒▒░▀▀▀▀░░░░▓▓▒▒▓▓
▒▒▒▒▒▒▒▒░░░░░░░░░▓▓▓▓▓
▒▒▒▒▒▒▒░░░░░░▐▄░▓▓▓▓▓▓
▒▒▒▒▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓
De????n — Today at 1:10 PM
yeap
i always want to implement it
you have contract % of salvage
like 40%
so you can take 40% of droped cost
FrostRaptor — Today at 1:11 PM
Do I recall you get the state of all destroyed units at end of the mission already?
De????n — Today at 1:11 PM
yes
(with small overflow but not more then 1 unit)
FrostRaptor — Today at 1:12 PM
So mostly the UI work to allow selection of the destroyed units?
Is the complex part?
De????n — Today at 1:12 PM
but every time i think of ui work
i pretend ded
yes
basic idea was when unit go to inventory
in contract confirm
it dissasembled as looted
FrostRaptor — Today at 1:13 PM
So would need modstate to capture state of the unit @ onDeath message, keep it separate than the lootable table HBS builds
Is it easy to inject it straight into the mechbay in the state it left combat?
I should probably make sure Jamie doesn't think I'm distracting you from shops :smile:
De????n — Today at 1:17 PM
no
it is exist lootdef
for mech
but no ui part
so you get potencial salvage list with mech
then overvrite loot window to show mechs data
and follow % loot rule
FrostRaptor — Today at 1:18 PM
Loot by tonnage might be interesting.
De????n — Today at 1:18 PM
then when lootdef go to simgame inventory it will dissasemble
by cost
FrostRaptor — Today at 1:19 PM
Instead of % of total field salvage.
De????n — Today at 1:19 PM
or anyway
FrostRaptor — Today at 1:19 PM
Hurm, interesting. Thanks for sharing.
That sounds like that would be a really fun mod
De????n — Today at 1:19 PM
but i think leftover cost (cost of mechparts and alive items)
FrostRaptor — Today at 1:19 PM
I might poke you if I decide to investigate
Assuming you wouldn't mind?
De????n — Today at 1:20 PM
no
Interactive Rubber Dolphin — Today at 1:20 PM
Since it's a frosty mod we should come up with a catchy name
De????n — Today at 1:20 PM
custom salvage have interface to define some steps
Interactive Rubber Dolphin — Today at 1:20 PM
something like "FightingForScraps"
Idget — Today at 1:20 PM
LOL
bloodydoves — Today at 1:20 PM
they all have snappy names
Idget — Today at 1:20 PM
Oh, I like that actually.
De????n — Today at 1:20 PM
it have part calcualtion
bloodydoves — Today at 1:20 PM
ConcreteJungle is still my favorite
De????n — Today at 1:20 PM
and dissasemble mech to items
BlueWinds — Today at 1:21 PM
NotNailedDown
(we took everything...)
De????n — Today at 1:21 PM
you need to provide custom step that turn mechs into lootdefs
(it have api for custom steps)
FrostRaptor — Today at 1:22 PM
Very interesting.

  
## How to build custom UI
Hello again CWolf, I know you're long retired from BT modding but I hope you won't mind a question.
When you were mocking up planetfall, were you creating new UI elements in Unity editor and injecting them into the game via DLL hooks? Or did you have another approach in mind?
I am considering doing a salvage screen that's fairly complex, and doing it all via DLL edits is daunting. I thought I'd ask in case you had other magic I could instead use.
CWolf — 03/18/2021
Hey :slight_smile:
Always happy to answer a question
Yeah, Landfall mod
So I discovered a trick which I don't think many people know about
I tried to share it around but it's fiddly so not many people listened I think
You can build UI in the Unity Editor along with anything that fits into an asset bundle (c# scripts don't go in bundles) - then get it into the game
when it comes to scripts attached to the UI elements - this is where the trick comes in to maintain the link
otherwise the script links get broken
BTDebug did this too
let me show you
so for a mod I created three projects
[1] BTDebug (the BT mod) - https://github.com/CWolfs/BTDebug
GitHub
CWolfs/BTDebug
HBS BattleTech debug mod. Contribute to CWolfs/BTDebug development by creating an account on GitHub.

[2] BTDebug-Library - the pure c# project that contains c# scripts linking against the Unity dlls required in the scripts for the UI prefabs - https://github.com/CWolfs/BTDebug-Library
GitHub
CWolfs/BTDebug-Library
BTDebug companion code library project for the bundled assets - CWolfs/BTDebug-Library

[3] BTDebug-Bundler - the Unity project where I create my asset bundles, including UI prefabs. https://github.com/CWolfs/BTDebug-Bundler
GitHub
CWolfs/BTDebug-Bundler
Unity project for bundling the BTDebug assets. Contribute to CWolfs/BTDebug-Bundler development by creating an account on GitHub.

so...
what you do is... developing it in parallel - you create the prefabs you want to use in UnityEditor and any logic scripts (c#) need to be created in the Library project
you compile that library project out to a dll then add it to the Bundler project any time you want to update your scripts
then in the Unity project - you can use those scripts (being linked to your library dll) on the prefabs
When you're ready, you put your UI prefabs (or any other prefabs) into the asset bundle and export it
in your BT mod - you ensure your library dll is loaded in first, you then load your Unity asset bundle - and the script links are maintained
This is because Unity links the script references by a fully qualified domain
so... while Asset Bundles don't allow scripts to be exported in them
you can effectively side load it through
... I hope that makes sense
took a long time to discover that by trial and error :smile:
so in your BT mod - you then can use (psuedo code) bundle.LoadAsset("myPrefab", typeof<GameObject>) and there it is
you can then init the prefab in game
Landfall mod used the same trick
You can bring in new Scenes, Textures, Models - anything
and the associated scripts
FrostRaptor — 03/18/2021
As always, you're a font of amazing information
Thank you so much for sharing that with me. I'll try to apply it to this new mod I want to take on
CWolf — 03/18/2021
:slight_smile:
shout if you get stuck
FrostRaptor — 03/18/2021
We really couldn't have done 1/2 of what we've done without your help you know
CWolf — 03/18/2021
has been fun to do it with you all
FrostRaptor — 03/18/2021
BtDebug alone is amazing
CWolf — 03/18/2021
you guys are great too
I couldn't have done MC without BTDebug
was a pre-req mod for it
FrostRaptor — 03/18/2021
I can understand why
Impossible to know how things flow in the UI w/o it
It's let me trace-back through so many parts of the code to add new things
It was instrumental in allowing me to add new pilot types
CWolf — 03/18/2021
cool :slight_smile:
how have things been anyway?
how is the mod community and RT?
FrostRaptor — 03/18/2021
Sorry, been bouncing between meetings. Things are going well for me personally. Had a few covid scares in the family but everybody made it.
The community is surprisingly stable. A couple more folks have wound down their interactions with the community. I don't see much of dz or gnivler anymore, though they are semi-active on the BTR discord.
mpstark's in the same boat. They pop up occasionally but largely seem to have moved on to other things.
RT's doing pretty well. KMission has released some really interesting work since you were last around. There are true transforming models now that switch between 2 forms. Mostly that's used for the LAMs. It's pretty impressive to see. Plus he released quad mechs and battle armor. All are warping the Mech and it's gameobjects in strange ways, but it works
I spend most of my time over on BTA anymore. There's a couple of new modders who have popped in over there and have done some good work. t-bone and BlueWinds have released a dozen or so new mods between them. BW just did a contract overhaul ala GaW called WarTechIIC that's pretty snazzy.
For myself I'm working on a Pilot overhaul mod called Human Resources. Adds vehicle pilots, mech and med tech crews, etc to the hiring hall. Adds contract disputes and things like that. But I've also done some modeling and imported 15 or so vehicles to the game.
Overall the community still feels like it's going strong, albeit with slower releases as fewer folks are doing things.
I more than half expected that most of us would have faded away by now, TBH.
CWolf — 03/18/2021
sounds like great stuff!
Glad it's still going on :slight_smile:
CWolf — 03/18/2021
https://github.com/CWolfs/BTDebug/blob/master/src/Main.cs#L28
GitHub
CWolfs/BTDebug
HBS BattleTech debug mod. Contribute to CWolfs/BTDebug development by creating an account on GitHub.

here's how I load the dll and bundle in - at the start of the mod load then
just as a fyi
both the 'LoadAssembly' and 'LoadAssetBundles' methods are called in the mod Init
FrostRaptor — 03/18/2021
Ah, thank you
CWolf — 03/18/2021
I probably don't need to mention it but just in case - the Unity version of your Bundler project should be the same as BT
FrostRaptor — 03/18/2021
That was a really good thing to mention, actually
All the modeling works against a Unity 5.5 project, as apparently upgrading to 2018.4 breaks the export scripts
So I would have blundered into 5.5 and been wondering my none of that stuff worked :smile:
CWolf — 03/18/2021
Luckily you can have multiple Unity installs these days
Asset bundles are pretty sensitive to version upgrades
so best keep to the one BT is on :slight_smile:
FrostRaptor — 03/18/2021
Great warning, thank you
I really should dive into the modeling project and figure out what doesn't work on 2018.4
CWolf — 03/18/2021
I'm always in awe of the modellers
artists in general
so much talent out there
FrostRaptor — 03/18/2021
Yeah. There are some really talented folks
I'm still amateur / hack quality.
