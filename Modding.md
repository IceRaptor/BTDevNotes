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