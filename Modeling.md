# BT Developer Notes
This is my collection of random notes for use when modding the [HBS BattleTech](http://battletechgame.com/) game. I doubt anybody else would find them interesting.

# Table of Contents
- [Custom Units Process](#import-cu)
 	+ [CU Mech Process](#import-cu-mech)
 	+ [CU Quad Process](#import-cu-quad)
	+ [CU VTOL Process](#import-cu-vtol)
- [UABE Process](#import-uabe)
	- [UABE Mech Process](#import-uabe-mech)
	- [UABE Vehicle Process](#import-uabe-vehicle)
- [BTIRS Process](#btirs)
- [Misc Notes](#misc)
	+ [Misc Modeling](#misc-modeling)
 	+ [Misc Texturing](#misc-texturing)
- [Requests](#requests)


# Custom Units Import Process<a name="import-cu"></a>

KMission has created a custom import workflow that is powered by his [CustomUnits](https://github.com/BattletechModders/CustomBundle/tree/master/CustomUnits) package. 

-- Turret Spec
-- Vehicle
-- Blip
-- Animation (w/ triggers)
-- Hardpoint types (anim vs. non)
-- weapon prefabs
-- transforms
-- collider
-- special conventions
-- headlights

#### Animations

- CU body animator will set 'in_battle', 'charge', 'forward' animator properties
- Animators have to be defined in json, like "Animators": [ "j_Body","LB","LF","RB","RF" ], 
- Animators should be attached to objects with distinct names. Don't use `body`!
- 
in_battle - boolean
charge - trigger
forward - float
- weapon animations gated by in_battle as well. 
- weapon anims also support start_random_idle and idle_param. start_random_idle is a bool indicating the unit is in idle state, idle_param is ranges from (0.6-0.9) with 0.6 being a netural value.
- Layered animators need to be Override with weight 1
- Twist animations need to not loop

#### Twist Animations
TwistAnimators - it is different set of animators which can be triggered independently they are triggering next animator values
StartRandomIdle - bool
TwistR - float (0-1) used with StartRandomIdle = false
TwistL - float (0-1) used with StartRandomIdle = false
IdleTwistR - float (0-1) used with StartRandomIdle = true
IdleTwistL - float (0-1) used with StartRandomIdle = true
you can look at yellowjacket twist animator implementation for inspiration



## CU Mech Import<a name="import-cu-mech"></a>

The CustomUnits mech import process swaps the Meshes and Materials on a target mech with the Meshes and Materials supplied in the CU mech asset bundle. This happens at runtime, and as far as the game is concerned what's spawned and active is the donor mech, not a CU mech. This differs from the legacy process, where you parasitically replace elements of the donor assetbundle, resulting in a completely new asset. Instead, you are spawning a parent, tearing off and replacing its skin, and letting it go from there.

(!) The most important thing to understand is you CAN NOT modify the skeleton (bones) of the parent. This process will let you attach to them, but that's all. 

To start with, you will need:  

 * Unity Editor 2018.4.X (NOT 5.5!)
 * [AssetStudio](https://github.com/Perfare/AssetStudio)
 * A donor mech
 * Your meshes + textures

Download KMiSSioN's custom mechs Unity Project and import it in your editor. You should see the `cugunslinger` and an atlas. Take a look at the `cugunslinger` hierarchy. You'll see there is a `bones` and `mesh` nodes. The `bones` come directly from the donor bundle, plus your additions. Meshes come from you, and generally should follow the same pattern of `mesh_Head`, `mesh_Head/Head_dmg`, `mesh_Head/Head_whole`. Mesh locations have to match the locations defined in the CustomRepresentation JSON file (discussed later). The `_dmg` meshes are shown when the part is destroyed, otherwise `_whole` meshes are shown. Take note of the `mesh/camoholder` object. This is how you add 'unit paint' schemes, up to 6 RGBa maps that allow player color schemes to display.

__Step 1: Setup__
Copy and paste the `chrprfmech_cugunslingerbase-001`, renaming it to the mech name you are importing. I imported the cuelemental, so my new object was `chrprfmech_cuelementalbase-001`. Delete everything under `bones` node, but leave the `bones` node. Go through the `mesh` node, delete everything under a `_dmg` node and rename everything left to your mechname. So `elemental_arm_RLower`, `elemental_centre_torso_pelvis`, etc. Certain names map to mesh names, and while you can change them it's better if you don't. These are:

* XXX_centre_torso
* XXX_centre_torso_pelvis
* XXX_left_leg_calf
* XXX_left_leg_foot
* XXX_left_leg_hip
* XXX_left_leg_thigh
* XXX_left_arm_clavicle
* XXX_left_arm_forearm
* XXX_left_arm_upperarm

(!) I'm lazy. Anywhere you see `_left` mesh or `j_LXXXX` bone, assume there is a corresponding `_right` mesh and `j_RXXXX` bone.

__Step 2: Donor Import__
Fire up AssetStudioGUI, and navigate to `BATTLETECH\BattleTech_Data\StreamingAssets\data\assetbundles`. Load your assetbundle, then choose Export -> All Assets. Choose a directory on disk and let AS do it's thing. Because these are 1.9 exports, I *strongly* encourage you to distinguish these from the 1.6 exports you need for the legacy process. I keep all of mine in a `btg_exports/exported_1.6` and `btg_exports/exported_1.9` directory to be safe.

Once the export is done, in Unity Editor create a new directory under Assets/characters/mechs/models named after your parent. I used the chrPrfMech_battlemasterBase-001, so `Assets/characters/mechs/models/battlemaster` became the path. In this directory, right click and `Import New Asset`, navigating to `btg_exports/exported_1.9/exported_1.9\Battlemaster\Animator\chrPrfMech_battlemasterBase-001` and selecting the FBX present in the directory. This was `chrPrfMech_battlemasterBase-001.fbx` in my case.

When the import finishes, click the arrow next to the imported model to expand the view and see everything it contains. Select all of the animations; they look like a square with a circular play button in them. Once they are selected, click Ctrl + D to extract them from the FBX. They will copy into the models/battlemaster folder. We'll use them later.  
  
Click-drag the imported `chrPrfMech_battlemasterBase-001` model into your viewport. They should appear in the display, as well as on the top-left. Move them where you like, then expand their hierarchy. Delete all the following, you won't need them:

* BlipObjectIdentified
* BlipObjectUnknown
* Foot IK
* Grounder IK
* Heraldry
* VFXCollider_vert
* WindZone
* j_Root/j_camera*
 
Do into the `mesh/` node and disable (unselect the checkbox directly under inspector in the top right) all of the `_dmg` meshes. Expand the `j_Root` node. You can delete the following nodes if you like:

* `j_Root/j_Pelvis/j_Pitch/j_Spine/j_Spine1/j_Spine2/BlipObjectGhostStrong`
* `j_Root/j_Pelvis/j_Pitch/j_Spine/j_Spine1/j_Spine2/BlipObjectGhostWeak`
* `j_Root/j_Pelvis/j_Pitch/j_Spine/j_Spine1/j_Spine2/J_COCKPIT_CAM`

Finally, go back into the `Assets/characters/mechs/models/battlemaster` folder and select all the animations. Drag them onto the `chrPrfMech_battlemasterBase-001` GameObject in the Hierarchy window. This enables the animations for display. Click `chrPrfMech_battlemasterBase-001` in the hierarchy, then the Animation tab on the bottom viewport. Choose one of the animations and hit play to preview what it looks like. This is how you can check your alignment in the editor, without needing to load HBS BTG.

__Step 3: CU Bones__
Next, we need to create CU specific transforms associated with the parent skeleton. These map to specific transforms on the skeleton, that HBS BT's mesh renderer uses to build the skin. These are:  
  
* `j_Root/j_Pelvis/` - bone for the pelvis
* `j_Root/j_Pelvis/j_LHip` - bone for the hip
* `j_Root/j_Pelvis/j_LHip/j_LThigh` - bone for the upper thigh
* `j_Root/j_Pelvis/j_LHip/j_LThigh/j_LCalf/` - bone for lower leg and calf
* `j_Root/j_Pelvis/j_LHip/j_LThigh/j_LCalf/j_LFoot` - bone for the foot
* `j_Root/j_Pelvis/j_Pitch/j_Spine/j_Spine1/j_Spine2/` - bone for the torso and cockpit 
* `j_Root/j_Pelvis/j_Pitch/j_Spine/j_Spine1/j_Spine2/j_LClavicle` - bone for the clavicle
* `j_Root/j_Pelvis/j_Pitch/j_Spine/j_Spine1/j_Spine2/j_LClavicle/j_LUpperArm` - bone for the upper-arm
* `j_Root/j_Pelvis/j_Pitch/j_Spine/j_Spine1/j_Spine2/j_LClavicle/j_LUpperArm/j_LForearm` - bone for the lower-arm
* `j_Root/j_Pelvis/j_Pitch/j_Spine/j_Spine1/j_Spine2/j_LClavicle/j_LUpperArm/j_LForearm/j_LHand` - bone for the hand

There are other bones you can target, like talons and toes, but I don't care about them. You figure it out.

You MUST include meshes for the pelvis, torso, cockpit (more on this below), L/R thigh and calf, L/R upper and lower arms. Everything else you can skip, though the animations may be weird without them. For each mesh you intend to target, go to the relevant bone and create a **new** bone named the same, with a `_cu` suffix. For instance, create a **new** GameObject under `j_Root/j_Pelvis/j_Pitch/j_Spine/j_Spine1/j_Spine2/` named `j_Spine2_cu`. `j_Spine2_cu` MUST BE parented by `j_Spine2`. 

These new `_cu` 'bones' are what we'll target. CustomUnits will add these new transforms into the parent skeleton, allowing them to overlap with the existing skeleton. Because the old mesh will be completely discarded, only new meshes you add to these `_cu` bones will be displayed.

(!) You can name these whatever you like, the name isn't important. I chose this idiom to let me easily understand the parent bone relationship.

__Step 4: Meshes and Materials__

Create the following new folders in the project view, for your mech:

* `Assets/characters/mechs/materials/XXX`
* `Assets/characters/mechs/models/XXX`
* `Assets/characters/mechs/textures/XXX`

Import your meshes into `/models`. Each mech component should have an origin at the center of the mesh geometry. 

Import your textures into `/textures/`. You need an albedo, ambient occlusion, emissive, specular (metallic), and normals as a minimum. You should also have 6 camo masks, RGBa masks (covered in Texturing up in this document). Click the normals texture and mark it as Texture Type: normal map in the top right, and hit save. 

Right click and choose Create -> Material. You MUST use the name of your PREFAB + `base` as the material name. For my `cuelemental` prefab, I used material `cuelementalbase`. Click the new material. Copy the albedo texture into the albedo block, the AO map into the occlusion block, enable emission and copy the emissive mask there. Copy the normals texture to the normal map block, and finally copy the speculars to the metallic block. 

If you have camo masks, create one material for each mask. It should be name prefix + `_camoX` where X is the camo ID (0 through 5). Copy ONLY the camo mask into the albedo block, and leave everything else blank. Example: `cuelemental_camo0`

Go back to your model's mesh/ hierarchy. Click-drag the meshes into the relevant section (i.e. the head into ``meshes/mesh_Head/Head_Whole`). For each part, right-click and choose 'Unpack Prefab Completely'. Once all your parts are imported, select them all. In the Inspector window, remove the `Mesh Filter` component by clicking the gear icon on the far right. Next, click 'Add Component' and add a `Skinned Mesh Renderer` component. Click the i button next to the `Materials/element 0` and choose the material you created above.

Note the 'Mesh' and 'Root Bone' fields. CustomUnits works its magic by finding all Skinned Mesh Render components, and trying to match their `Root Bone` with the same name on the parent skeleton. It will replace the mesh found on the parent with the mesh on the CU mech if the bones match. If the SkinnedMeshRenderer bone doesn't match an existing bone on the parent, it will create it and copy the transform information. By creating the `_cu` transforms you're creating new bones that will additively map to the existing parent skeleton. 

As you are not limited to the bones of the parent, you can import meshes beyond the basic ones referenced above. Keep them in the mesh/ area closest to where they will be mounted. If you add new meshes to the left arm, drop the mesh in `mesh/mesh_LArm/LArm_whole`. 

(!) HBS splits it's models into a left, center, and right torso. This isn't necessary, you can provide a single centre_torso mesh and it will work fine. In this case (which I recommend), just have empty `LTorso_dmg` and `LTorso_whole` paths. 

__Step 4b: Animation Tests__

Once your meshes are mapped to the parent's skeleton, you can preview the animations and see how they should look in game. Disable all of the parent meshes (i.e. chrPrfMech_battlemasterBase-001/mesh/ in the hierarchy), and you should be left with just your model's meshes. Go to the animation tab, choose an animation, and hit play. In particular try the __MoveCoreRunXXX___ and ___MoveCoreWalkXXX___ animations to see how it will look while moving.

Adjust the `_cu` transform positions until you get the animations looking 'good enough'. People will give your models some leeway, so don't try to get it too perfect here. Once you are satisfied, go to the next step.

__Step 4c: Skeleton Copy and Damage Meshes__

Your mech's `bones/` node should still be empty. Click the parent's `j_Root` bone, copy it, and paste it under your mech's `bones/` node. This should transplant the parent structure to your actual copy. Zero out the new j_Root transform values; Unity will try to make it relative to the copied location which is not what we want. 

Unfortunately this only copies the transform information, but all the meshes are still pointing to the parent transforms. Go into each SkinnedMeshRender node, click the I button next to 'Root Bone', and change it from the parent bone to your mech's bone. There *should* be only two of the same type. When you update it, the mesh should jump from the parent's location, to your mech's location.

Once you've mapped everything, you need to update the `_dmg` directories. Copy the objects from the `_whole` directory  and move the copies into the `_dmg` directory. You can keep everything the same if you want, or strip off certain parts. You can use different meshes for `_dmg`, or different materials. This latter approach is what HBS does, with custom damaged meshes and materials used when a part is destroyed.

Once you have all SkinnedMeshRenderer components attached to `_cu` bones, manipulate the `_cu` bones to get the alignment you want in the UnityEditor. Once you're happy with the results, move on to the next step.

__Step 5: Export and CustomRep__

Drag your prefab (i.e. `chrprfmech_cuelementalbase-001`) from the hierarchy window to the project window, at `Assets/character/mech/prefabs`. Click the prefab in the project pane, then under the bottom right window where it says AssetBundle click the dropdown. Choose new, and supply the *exact* name of the prefab again. In my case, that is `chrprfmech_cuelementalbase-001`. Now right-click in the project viewport, and choose 'Build Asset Bundle'. This will take ~ 30s during which time the editor will be unresponsive. When done, the prefab in the hierarchy will be blue; this indicates it's now a packaged prefab. You will need to click it, and choose 'Unpack Prefab Completely', in order to edit it in the future.

Open a File Explorer window, and navigate to your Unity project area. It's probably something like `Users\<USERNAME>\Documents\Unity\BTG Projects\CU Mech Imports\Assets\AssetsBundles`, but your location may vary. Inside that folder you'll see your packaged AssetBundle (i.e. `chrprfmech_cuelementalbase-001`) along with a .manifest, .manifest.meta, and .meta file. Ignore those, and copy only the assetbundle to `BATTLETECH\Mods\CAB-CU\assetbundles` in your BattleTech game install folder.   
  
This is your local copy of the CustomUnits CAB (Community Asset Bundle). The CAB is a collection of the all the units created by folks in the community, and contains the Unity resources (assetbundles) along with resources specific to the HBS game. A model requires 4 edits to the CAB:  
  
  * An assetbundle (in CAB-CU/assetbundles)
  * A hardpointDef (in CAB-CU/hardpoints)
  * A customRepresentation (in CAB-CU/representations)
  * Manifest data (in CAB-CU/mod.json)
  
The mod.json edits are the easiest. Open the file, and you'll see many lines like:  
  
```
		{ "Type": "Prefab", "Path": "assets/character/mech/prefabs/chrprfmech_cugunslingerbase-001.prefab", "AssetBundleName": "chrprfmech_cugunslingerbase-001" },
		
		{ "Type": "Prefab", "Path": "assets/character/mech/prefabs/chrprfweap_cugunslinger_leftarm_ac20_bh1.prefab", "AssetBundleName": "chrprfmech_cugunslingerbase-001" },
		{ "Type": "Prefab", "Path": "assets/character/mech/prefabs/chrprfweap_cugunslinger_leftarm_gauss_bh1.prefab", "AssetBundleName": "chrprfmech_cugunslingerbase-001" },
		{ "Type": "Prefab", "Path": "assets/character/mech/prefabs/chrprfweap_cugunslinger_leftarm_laser_eh1.prefab", "AssetBundleName": "chrprfmech_cugunslingerbase-001" },
		{ "Type": "Prefab", "Path": "assets/character/mech/prefabs/chrprfweap_cugunslinger_leftarm_laser_eh2.prefab", "AssetBundleName": "chrprfmech_cugunslingerbase-001" },
		{ "Type": "Prefab", "Path": "assets/character/mech/prefabs/chrprfweap_cugunslinger_leftarm_laser_eh3.prefab", "AssetBundleName": "chrprfmech_cugunslingerbase-001" },
		{ "Type": "Prefab", "Path": "assets/character/mech/prefabs/chrprfweap_cugunslinger_leftarm_laser_eh4.prefab", "AssetBundleName": "chrprfmech_cugunslingerbase-001" },  
		...
```


The first line imports your assetbundle that we just created. Note that `path` element matches the path in the Unity Editor, NOT the file system. The `AssetBundleName` instead matches the filesystem path, and which is inherently referenced by an AssetBundle type defined elsewhere in the file.  
  
The other lines are _dynamic weapon prefabs_. We'll cover those later, but it's the same idea as your mech model. A weapon prefab is just another package, created the same way in the editor, that we can import via this file. 

The customRepresentation for plain mechs is straightforward; open `chrprfmech_cugunslingerbase-001.json` to see what I mean. The donor mech preab should in the `SourcePrefabIdentifier` element, while the `Destructibles` paths should reflect what you see in the Unity Editor hierarchy. These paths are the linkage between CustomUnits and your Unity prefab, so make sure they are correct. If you followed the guide so far, the only thing you need to change is your `Id` and `PrefabBase` attributes to reflect your design. Maybe `SourcePrefabIdentifier` if you used something other than the Battlemaster as a parent.

Finally, the hardpoint file maps dynamic weapons to locations and many other effects in game. Open `hardpointdatadef_cugunslinger.json` to see the structure. For all files, you shoul have an empty `HardpointData` section. This is the default HBS data structure that KMiSSiON overwrites with custom logic.  
  
`CustomHardpoints` defines how prefabs are mounted for dynamic matching. Because we're ignoring that for the moment, you'll want to update the `ID` value and have an empty CustomHardpoints block like so:

```
  "CustomHardpoints": {
    "prefabs": [
    ],
    "aliases": {
    }
  },
```

You're now ready to try the unit out in game. If you're using KMiSSiON's CBDebugEnvironment, go to `BATTLETECH\Mods\CACDebugContent` and find a chassis that roughly matches what you're building. It's easy enough to use the Gunslinger, so open `BATTLETECH\Mods\CACDebugContent\chassis\chassisdef_gunslinger_GUN-1ERD.json`. You need to change the `HardpointDataDefID`, `PrefabIdentifier`, and `PrefabBase` values to your new mech. For instance, where's what I used for my elemental:  
  
```
    "HardpointDataDefID": "hardpointdatadef_cuelemental",
    "PrefabIdentifier": "chrprfmech_cuelementalbase-001",
    "PrefabBase": "cuelemental",
```

Once the file is saved, load up HBS BT, go into Skirmish and drop with the Gunslinger. It should new be using your custom model.

There may be positioning issues with the model. If so, adjust the `_cu` transform positions and re-package your AssetBundle. I've found it safest to delete the prefab from the Project window (at `Assets\character\mech\prefabs`) first - this will turn the prefab red in the Hierarchy window (if you didn't already unpack it). Drag it back into the project window at `\prefabs`, re-associate it with the assetbundle name, and rebuild the asset bundle. Copy it over, and try again. And again, and again!

__Step 6: Dynamic Hardpoints__

HBS expects models to have different models it can map onto the a weapon slot. This process maps a prefab onto a hardpoint id, using some magic in the name of the prefab. For instance, `chrPrfWeap_cugunslinger_leftarm_gauss_bh1` tells the game engine that it's a ballistic (`_b`) in hardpoint 1 (`h1`), it looks like a gauss (`_gauss`) and it's in the left arm (`_leftarm`).

The different weapon types are:

* `_eh` - energy
* `_bh` - ballistic
* `_mh` - missile
* `_ah` - auxillary (ams, etc)

The model types that are exposed are:

* gauss
* laser
* ppc
* lrmX
* mg
* srmX
* blank
* TODO

Inside the UnityEditor, create a new GameObject in the hierarchy window. It's name must start with `chrprfweap` (case matters!) and reflect the location, type, and hardpoint type. For a left-torso laser hardpoint, we'd use `chrprfweap_cuYOURMECH_lefttorso_laser_eh1`. This GameObject's transform **MUST be zeroed** at all times, and you shouldn't change this.
  
Inside this parent, create a new GameObject called 'body'. Below this create two child GameObjects named 'visuals' and 'fire'. Under 'fire' create an empty GameObject called 'fire1'. This should give you a structure like:

* `chrprfweap_cuYOURMECH_lefttorso_laser_eh` / body / visuals
* `chrprfweap_cuYOURMECH_lefttorso_laser_eh` / body / fire / fire1

Drag your mesh under 'body' to create a new child GameObject. Add the SkinnedMeshRenderer component to the child, but DO NOT associate it with a root bone. 

To adjust the position of the weapon mesh, you will ONLY adjust the transform on the 'body' GO. It's not special, and you can technically go without it and adjust the transform on the GO via the SkinnedMeshRenderer transform values. I prefer to keep all transform changes on 'body' because these will propagate through to the 'fire' children as well. We'll talk about those in a bit.

Copy your chrprfweap GO into the location that will mount the weapon. Here's the breakdown of locations by bind-bone:

* `j_Root/j_Pelvis/j_Pitch/j_Spine/j_Spine1/j_Spine2/j_COCKPIT` - used for left, right, centre torso and head weapons 
* `j_Root/j_Pelvis/j_Pitch/j_Spine/j_Spine1/j_Spine2/j_LClavicle/j_LUpperArm/j_LForearm` - used for arm weapons
* `j_Root/j_Pelvis/j_LHip/j_LThigh/j_LCalf/`- used for leg weapons

**DO NOT** use the `_cu` GameObjects that you created for your parts as the parents for your weapons. Your weapons are always lashed up to the **parent** skeleton, not your derived parts. 

Once you have the new chrprfweap under the appropriate attach point, align the weapon to the mesh using the `body` transform. For arm weapons you may find the donor model as the forearms rotated at random degrees. Do you best to align them now, but it's trivial to correct the alignment with BTDebug later. Once the `body` transform for a weapon what you want it to be, copy the transform component (click the cog icon, then choose Copy Component). Then go back to the original `chrprfweap_cuYOURMECH_lefttorso_laser_eh1` at the top level, and copy those values onto it's `body` element (click the cog icon, then Paste Component Values).   

__Step 6a: Emitter Game Objects__

The 'fireX' Game Objects allow you to specify the emitter point for weapon projectiles. This is where the beam will start for lasers, the bullet will start for autocannons, etc. You typically want one per barrel or slot on the weapon. An SRM6 with 6 barrels would have 'fire1', 'fire2', 'fire3', 'fire4', 'fire5', 'fire6' below 'fire'. A MLAS with 1 barrel would have a single 'fire1' defined. 

It's worth noting it's completely up to you how many emitter points there are. My understanding is that multi-shot weapons will iterate through defined emitter points, and cycle back to the first emitter point when they run out of emitters. If you wanted to model a LRM20 with 5 barrels, you would have 'fire1', 'fire2', 'fire3', 'fire4', 'fire5' GOs. You'd get 4 missiles out of each barrel, following the sequence fire1, fire2, fire3, fire4, fire5, fire1, fire2, ...

If you don't specify a fire GO, the emission will be from the chrprfweap_ transform.

__Step 6b: Bundling Prefabs with Asset Bundle__
  
If you have done this correctly, the transform on `chrprfweap_cuYOURMECH_lefttorso_laser_eh1` should be 0,0,0 for position and rotation, and scale of 1. The `body` child has the same values on the top-level and your embedded chrprfweap GOs. Now, copy your top-level chrprfweap prefab into the project window, under the path assets/character/mech/prefabs/. You have to do this one at a time, and it's extremely annoying.

I prefer to use a directory to hold all my assets for a model, so my path for the Rifleman3 was assets/character/mech/prefabs/rifleman3. You just need to remember this later when the hardpoints are being defined.

Next, associate the chrprfweap prefab with the parent model's assetbundle. Click the prefab and in the bottom right window, choose the mech's assetbundle. For my rifleman3, this meant `chrprfweap_curifleman3_leftarm_ac2_bh1` was embedded in AssetBundle `chrprfmech_curifleman3base-001`. Now, build your assetbundle and wait for Unity to do it's thing.


__Step 6c: Hardpoints and Prefab Loading__

Go into the CAB-CU `mod.json` and add import statements for your weapon prefabs. Under your assetbundle, you'll need to add one line for each chrprfweap that you have built into the assetbundle, like so:

```
		{ "Type": "Prefab", "Path": "assets/character/mech/prefabs/chrprfmech_curifleman3base-001.prefab", "AssetBundleName": "chrprfmech_curifleman3base-001" },

		{ "Type": "Prefab", "Path": "assets/character/mech/prefabs/rifleman3/chrprfweap_curifleman3_leftarm_gauss_bh1.prefab", "AssetBundleName": "chrprfmech_curifleman3base-001" },
		{ "Type": "Prefab", "Path": "assets/character/mech/prefabs/rifleman3/chrprfweap_curifleman3_leftarm_ac20_bh1.prefab", "AssetBundleName": "chrprfmech_curifleman3base-001" },
		{ "Type": "Prefab", "Path": "assets/character/mech/prefabs/rifleman3/chrprfweap_curifleman3_leftarm_ac10_bh1.prefab", "AssetBundleName": "chrprfmech_curifleman3base-001" },
		...
```

The `Path` element is the path in the Unity editor's project view. This tells ModTek to load the prefab and make it available. Next, we have to associate the prefab with the hardpoints. Go to your CU hardpoints file (i.e. `CAB-CU\hardpoints\hardpointdatadef_curifleman3.json`) and open it. There are two sections you need to edit; `CustomHardpoints` and `aliases`.

Under the `CustomHardpoints` block, you need to add (yet again) add every chrprfweap prefab you've created. This associates them with CU directly. A typical block looks like:  
  
```
    "prefabs": [
		{"prefab": "chrprfweap_curifleman3_leftarm_gauss_bh1", "attachType": "Body", "shaderSrc": "chrPrfWeap_atlas_centertorso_laser_eh1", "emitters": [ "fire1" ] },
		{"prefab": "chrprfweap_curifleman3_leftarm_ac20_bh1", "attachType": "Body", "shaderSrc": "chrPrfWeap_atlas_centertorso_laser_eh1", "emitters": [ "fire1" ] },
		{"prefab": "chrprfweap_curifleman3_leftarm_ac10_bh1", "attachType": "Body", "shaderSrc": "chrPrfWeap_atlas_centertorso_laser_eh1", "emitters": [ "fire1" ] },  
```

You can do A LOT with this, but the above is your basic binding. It will load the prefab, attaches to the body of the model, use a generic shader, and has no specific emitters. 

If created multiple emitters above, make sure to include each of the GOs under the 'fire' GO here. So for a lrm5 prefab you'd have:

```
	{ "prefab": "chrprfweap_horskr_center_lrm5_mh4", "shaderSrc": "chrPrfWeap_atlas_centertorso_laser_eh1", "emitters": [ "fire_1", "fire_2", "fire_3", "fire_4", "fire_5" ] }
```

Which associates the GameObjects with the prefab.

Now that the prefabs are available for use, they MUST be aliased to the names that HBS uses. HBS hardpoints have very strict logic about the name, since they rely upon convention for most of it. The pattern is `chrPrfWeap_ASSETBUNDLE_LOCATION_WEAPONCLASS_LOCATIONINDEX`, like `chrPrfWeap_curifleman3_lefttorso_gauss_bh1`. If you've gotten here you know how this works, and I'm not going to break it down for you.

You need to create at least one alias for the prefabs, and associate them with the location of the mech. Here's an example of how that looks:
```
		"chrPrfWeap_curifleman3_leftarm_ac2_bh2": { "location": "leftarm", "prefab": "chrprfweap_curifleman3_leftarm_ac2_bh2" },
		"chrPrfWeap_curifleman3_leftarm_laser_eh1": { "location": "leftarm", "prefab": "chrprfweap_curifleman3_leftarm_laser_eh1" },
		"chrPrfWeap_curifleman3_leftarm_laser_eh2": { "location": "leftarm", "prefab": "chrprfweap_curifleman3_leftarm_laser_eh2" },
		
		"chrPrfWeap_curifleman3_lefttorso_gauss_bh1": { "location": "lefttorso", "prefab": "chrprfweap_curifleman3_lefttorso_gauss_bh1" },
		"chrPrfWeap_curifleman3_lefttorso_ac2_bh1": { "location": "lefttorso", "prefab": "chrprfweap_curifleman3_lefttorso_ac20_bh1" },
		"chrPrfWeap_curifleman3_lefttorso_ac10_bh1": { "location": "lefttorso", "prefab": "chrprfweap_curifleman3_lefttorso_ac10_bh1" },
```

If you duplicate prefab to alias bindings in the same location, CU will throw an error in it's logs. This is a common error case.

** Final Checklist **

Once you have done the following, you should be able to load your model into mechbay or combat and see it largely as you expect:

* Create your chrprfweap prefab
* Linked the prefab to your assetbundle
* Rebuilt and redeployed the updated assetbundle
* Updated the mod.json with the prefab loads
* Added the prefab and its alias to the hardpointdef

Within game, if a weapon is misaligned simply open BTDebug and navigate to the model. In combat you should be able to find it by the assetbundle name; in the mechbay it's hidden under the Mechbay elements fairly deeply. When you find it, you should be able to locate the j_Spine GO and navigate down to the attach points, below which will be your weapon prefabs. If you have the `body` GO as I recommend, you can directly change it's localPosition and localRotation elements to change the weapon alignment. These can be freely copied back to the chrprfweap_XXX/body element transforms as corrections. 


#### Common Mistakes

* Model throwing an NRE that you can't figure out? 
** Did you make sure to add a camoholder object, with 6 patterns? They can all be the same, but it needs to be present.
** When you copied your meshes from _whole to _dmg, did they end up with a (1) in the name? This will cause the NRE. You need to rename them without the parenthesis to work properly.
* Material not loading? Make sure you name it CUMODELNAMEbase and CUMODELNAMEweapons. For the `chrprfmech_curifleman3base-001` assetbundle, that means the names must be `curifleman3base` and `curifleman3weapons`. Camos are just `curifleman3_camo0`.
* Model not loading, but no NRES? Make sure your donor j_Root is under bones/. CU will look to match using the /bones object, so leaving it out will cause subtle weird errors.
* Top level under your assetbundle (i.e. `chrprfmech_curifleman3base-001`) needs to be bones/, mesh/, and camoholder. 
* If a mesh element vanishes in the Mechbay when you zoom in, check the bounding box. It's probably not aligned with the mesh, which will cause the game to hide the mesh close-up.
* If you get mesh tearing, remember you need a 'nomerge' GO under any new meshes you add outside the standard head/torsos/arms/legs
* If you get an array index out of bounds error in your hardpoint, make sure the first items in a location is ordered numerically (i.e. mh1, eh2, etc). If you try to add a hardpoint out of numeric order (i.e. mh4 first in lefttorso, then eh1) it will throw this error.

#### MISC NOTES
Weapon prefabs in simgame may be getting camo patterns / multiple mats? Resetting mat directly fixes the corruption
- Using the same mesh name as a native prefab causes it to go crazy
- Direct import from blender doesn't see to work for legs; complains about missing bones. May be the missing avatar? Whereas Transient's imports has an avatar associated with the meshes...
- Had to import from Transient's import, then MUST use bones & meshes that exactly match
  - You MUST manually reset each bind point (it links back to the copied prefab)
- position body using j_QuadBody orientation; cannot change it during game via BTDebug
- hardpointdatadef MUST include a hardpointdata section for any mounted location; otherwise CU skips it. They should be empty, but must be present
- Need to test blender direct import for quad legs; will just a vertex weight against skele give enough of a link for CU? The standard process links via mesh painting, with FBX importer plugin will blender work?
- DO NOT FUCKING COPY j_root/ and mesh DIRECTLY. CLONE THE IMPORT (chrprfmech_battlemasterBase-001) AND RENAME IT. FUCK.

## CU Quad Import<a name="import-cu-quad"></a>

- each j_FLLeg style node has a 'ScorpionLegSolver' script. This script aligns the j_FLThigh, j_FLCalf, and j_FLFoot nodes with the j_FLFootTarget. 
- You have to disable the script to edit the positions, then re-enable the script
- The most important point - the blue arrow (on the transform) points in the direction of the bone. So thigh points up, calf points down, foot points down into ground
- The j_FLFootTarget has a script 'CustomUnitsGroundLedar' that tries to align the j_FLFoot to the target surface. Disable the leg solver, then move the j_FLFootTarget where you want it. 
- 'Up Leg Vector' values on CustomUnitsGroundLedar controls the transform displacement during the animation cycle. In particular, changing Y allows you to manipulate how far 'up' the legs will move during the walk cycle
- Once you've moved the j_FLFootTarget, you need to update the walk/run anims to reflect the displacement. The scorp used 6/8 for instance, whereas the Tarantula used 12/14
- The values in both scripts are output values, not control values. Only the first four values in the Ledar script are controls (keey distance through over ground height) AFAICT
- j_BodyTerrainAligner seems to keep the main body aligned with the donor animation skeleton. j_Pelvis is the pelvis from the *donor*, and the transform on j_BodyTerrainAligner is a transform from the donor pelvis position. As with other scripts, disable it, edit the transform, then re-enable. This seems to solve the mechbay verticality issue more cleanly than editing j_pelvis directly.
- If you unit pitches during battle and doesn't return, it's because you've disabled the CustomUnitsgroundLedars on the Front or Rear Pos of the j_BodyTerrainAligner. My guess is that it's picking up the pitch from the donor pelvis.
- j_ScorpionBody under j_BodyTerrainAligner determines how far 'up' the unit is in mechbay. 
- j_ScorpionBody is used in most of my imports because the animation overrides are tied to it. IF YOU CHANGE THE ANIMATIONS, YOU DO SO ON EVERY IMPORT because they are all using the same animator. You need to duplicate / change the animator to resolve this.

## CU VTOL Import<a name="import-cu-vtol"></a>

- Download workspace from KMission (add link / fix CU)
- Duplicate model you want to mimic, rename to `chrPrfMech_XXX_vtol`
- bones/ hierarchy is for attach points, particles, etc. 
- mesh/ heirarchy is for all mesh objects
- mesh/XXX_destructable is the 'live' mesh objects
- mesh/XXX_destroyed is for killed object meshes
- (VERIFY) Mesh objects need a nomerge and camoholder GO attached to them. Copy from elsewhere
- When you copy models to mesh/XXX_destructable, need to add `Skinned Mesh Renderer` component. This removes Mesh Renderer
- SMR `Root Bone` needs to reflect the attach heirarchy under bones/
- i.e. mesh/strix_destructable/StrixCutUp has a root bone of bones/j_Root/j_Body/normal_h/normal_v/normal/StrixCutUp
- Rename the bones heirarchy to match new model

- TODO
- Added paint mat 
- Add headlights?
- Add weapon attach points
- ? What are vfxTransforms used for?
- Disable animations on death

## CU Misc Notes
- If a model disappears in the mechlab, make sure the bounding box is set properly. If it's set incorrectly, it will vanish when it goes behind the 'wall'
- Custom hardpoints are at **WeaponsAttachPoints** not **WeaponAttachPoints** as shown in the various CU bundles. Confirmed on Markolab import
- Use NestedPrefabs on customrep to define additional prefabs that should be loaded. Use this when you want to reuse weapon prefabs across multiple models. 

# UABE Import Process<a name="import-uabe"></a>

Imports are a long, complicated process that is error and frustration prone. Basic vehicles are straightforward and can take between 5-10 hours when you understand the steps. Mechs are significantly more complex and typically take 30-60 hours to model, texture, and import. The import process is largely the same for both types of units.

1. You choose a **donor** vehicle or Mech. The donor defines the skeleton, animations, hardpoint, and meshes you can replace during the import process. You will want to choose a donor that approximates your final unit, as this simplifies the process.
2. You uncompress, extract, and export the **donor**'s assetbundle to get access to the meshes, textures, and GameObjects that Unity requires.
	1. You use [UABE](https://github.com/DerPopo/UABE) to uncompress the assetbundle
	2. You use [AssetStudio](https://github.com/Perfare/AssetStudio) to extract the animations and meshes for import 
	3. You use *UABE* to extract the assetbundle contents to a working directory
3. You model your unit using Blender, 3DS Max, or whatever tool you choose
4. You create an assetbundle for your unit using Unity 5.5.6f2
4. You texture your unit using Substance Painter, Quixel Mixer, or Armor Painter
5. You import your model into a new assetbundle that is built upon the *donor* unit's assetbundle
	1. You export your main assetbundle into a working folder to get access to your GameObject
	2. You extract your parts assetbundle into a working folder for meshes
	3. You import the donor's assetbundle contents onto your assetbundle, to pickup all the pieces that are required for your assetbundle
	4. You modify the manifest (i.e. list of items in the asset bundle) to reflect your new parts
	5. You replace the donor's textures with your own in your asset bundle
	6. You replace the donor's meshes with your own in your asset bundle
	7. You compress your asset bundle
8. You define assetbundle imports for one of the Community Asset Bundles (CAB)s that contain the models
9. You define the hardpoints for your unit. This links assetbundle entities to the weapon representations.

:warning: You MUST use donor bundles from BattleTech version 1.6, not BTG 1.7 or higher. UABE can't export textures on current bundles, and will corrupt them when you make assets. The import project is based on Unity 5.6.6f2 and breaks when updated to 2018.4.X.

*Miscellaneous Best Practices*

* Avoid name collisions at all costs. Use your avatar initials if there is a potential for a conflict, like `irscorpion` instead of 'scorpion'
* You should always lowercase the name. Use `chrprfvhcl_irscorpion` not `ChrPrfVhcl_IRScorpion`. 

## UABE Mech Import<a name="import-uabe-mech"></a>

UABE mech imports are heavily constrained by the donor Mech's specifics. Dynamic weapons are limited to the assetbundles defined in a location, both type and quantity. If your donor only has 3 missile mounts in the left torso, you can only support 3 of your own missile bundles. Bundles can be renamed, so those 3 missile bundles can repurposed to laser bundles. But the main theme is you're making due with what the donor has, not adding new functionality like in CU.

Notes:

- UABE imports split between mechs and weapons. Both go into the same assetbundle, as different prefabs.
- Mechs get textures (albedo, ambient occlusion, metallic, normals, emissive). They also have 6 RBG masks representing the paint schemes.
- Weapons only have the base textures, no masks. 
- Any part from the donor you don't want to show, you "blank". Blank means replacing it with a very tiny part that's technically in scene, but invisible to the player.
- hardpoints
  - make sure to rename any you swap
  - make sure you replace the equivalent weapon
- make sure to include a cockpit, hidden in CT. Prevents combat drop alignment issues

- Armature tab on export; enable ''only deform bones', disable 'add leaf bones'
- Apply armature modifier to all parts?
- Apply rest pose to animation before export/
- In BTDebug, in Mechbay, search for MechParent_0 to find the first mechbay display. Can help identify not loading issues if the chrPrf gameObject doesn't appear under it

- buy blender exporter for FBX - http://www.mesh-online.net/fbx.html / https://blendermarket.com/products/better-fbx-importer--exporter
- Re-parent meshes under armature
- For each mesh part, add a vertex group with the *exact* same name as the bone you want to connect to
- For each mesh part, add an armature modifier targeting the armature + vertex group
- Select mesh part in object mode, go to edit mode, select all, click vertex group tab, click 'assign' to map very mesh to the vertex group

- Export settings
- Selected Objects only
- FBX_2018_00 works fine
- Only Deform Bones
- No animations
- Apply modifiers
- Include armature deform modifier

- Disable 'Reset Mesh Origin' to have weapons respect the cursor placement

- Weapons placement:
-   Set origin to bone end
-   Position weapons where you want
-   Apply transforms
-   Set object origin to the cursor on the bone end
-   Rotate objects x+180, z+90
  
- Torso dimensions in unity should be around center: [ 0.2, 1.5, -0.5], Extents: [ 3.0, 3.0, 3.5]
- Shortcuts: Ctrl + Shift + U -> combat, free camera
- Ctrl + U -> mechbay hide UI

- Add to ME Settings.json this to enable prefab logging:
- 	"BetterLog": {
		"Level" : "Debug"
	}

- Mechlab sorts by inventory size *first*, and finds the first prefab that matches
	+ I believe this also uses natural language sorting
	+ Mechlab is often *fucked* but generally drops in combat work fine
	+ Sort is defined in https://github.com/BattletechModders/MechEngineer/blob/4a4f9f775ea69cddf76cd82994ce1f52ce698f96/source/Features/HardpointFix/WeaponComponentPrefabCalculator.cs#L25

- Remember UI is z forward, y up
- Object seems to align to its armature
- https://github.com/egtwobits/mesh_mesh_align_plus

- For mechbay, aligning pivot to joint and then rotating the pivot seems to work fine.
- This doesn't seem to work as nicely in combat, where the objects tend to get shifted. 

- Mechbay seems to ONLY care about alignment? HOW?

- Torso weapons mount to j_COCKPIT
	+ Align, then adjust pivot to move them

- You MUST untick 'Always Deform' under advanced in the Skin modifier, when changing the pivot location. You MUST then re-enable it, or the mechbay will deform. Off = combat, on = mechbay. you MUST export the parts with it on!

- blanks work on the hardpoint numeric location... blank_bh4 replaces any _bh4 hardpoint that isn't defined. 
- ME sorts hardpoints by inventory crit size first, then type, when defaulting. So a LRM15 will look for lrm20 -> lrm15 -> lrm10 -> srm6 -> lrm5 -> srm4 -> srm2 when calculating prefabs to pull
- ME completely ignores location information 

- Do not call meshes chrprfweap_ ; this overwrites the GO in BIMP and causes a bundle load issue.


- Gunslinger:
- Only really two.
Both minor.
The RA central weapon (the gauss or the laser model in the center of the arm) is off-center visibly.
The ST missile boxes/blanks are also off center visibly. No one commented on either, but I noticed.




## UABE Vehicle Import<a name="import-uabe-vehicle"></a>

The UABE vehicle import works for vehicles, turrets, and aerospace fighters. It doesn't support animations (except from the donor) and doesn't (easily) support dynamic weapons. You'll be importing a single model with fixated weapons that won't change no matter what goes into the vehicledef.
	
### Common Setup

1. Extract APC bundle to path on disk. In UABE, uncompress the bundle. Then Export to save as .assets
2. Download [UABE](https://github.com/DerPopo/UABE/releases)

### Blender or Equivalent

1. Create model (see limitations above)
	1. You want a single model in Blender; BTG doesn't support importing multiples
2. UV Map the model (see texturing above)
3. Give the model a name reflective of your import. If you're importing the _Carrier Half Track SRM_, use an abbeviation like `carrierhtsrm`. Potentially add your initials to prevent collisions in the CAB, like `ircarrierhtsrm`.
	1. Make sure to use this base name for the Object and Object Data Properties in Blender.
	2. Everywhere below use this name where __<mymodel>__ is listed
4. Scale model to ~ 8.5m-9.5m long (for tanks)
7. Center unit on xyz origin. Treads/wheels slightly below x plane, slightly forward on Y. 
	Blender numpad 7 gives you the expected view in Unity
2. Make sure to __Apply All Transforms__ before your export!
1. Export model as FBX from blender
	7. __Make sure to apply all transforms!__
	3. Export a single object only
	4. Do not export the animation
	6. Unity works with +z forward, +y upward by default
	
### Substance Painter or Equivalent

1. Export your 6 textures. Most should be 1024 for vehicles, but you can use 2048 if you really need details. Names below don't strictly matter and are provided to link the various parts together.
	1. Albedo map should be RGBA, as `<texturename>_ALB`
	2. Ambient Occlusion map should be RGB, as `<texturename>_AO`
	3. Emissive map should be RGB, as `<texturename>_EMS`
	4. Specular (aka Metallics) should be RGBA, as `<texturename>_MTLS`
	5. Normals should be RGB, as `<texturename>_NRM`
	6. Mask should be RGBA, as `<texturename>_MSK`

### Unity Editor

Download via Unity Hub [https://store.unity.com/download-nuo]

1. In UnityEditor, create new folder for model - use __<mymodel>__ name (i.e. carrierhtsrm)
1. Create new GameObject named `chrprfvhcl_<mymodel>`. ie. `chrprfvhcl_carrierhtsrm`
	1. Must be all lowercase! 
1. Drag GO into your folder from step 1; should create a blue cube
	1. Click on the blue cube, go to Asset Labels in the lower left, click new and name it the same as your `chrprfvhcl<mymodel>`
1. In folder right-click to 'Import New Asset', select your FBX. It will import as `<mymodel>` (i.e. carrierhtsrm)
	1. Click your model
	1. Make sure to uncheck 'use file scale' and click __Apply__
		1. Warning: If you leave this enabled model will import but will be so small you can't see it.
	1. Orientation in the scene does not matter; orientation in the mesh preview *does*
		1. The model should be facing to the right, from a profile view
		2. The mesh should be facing to the left of the display, from slightly beneath
	1. In bottom right, change assetbundle name to `<mymodel>_parts`
1. Right click in folder, choose Asset Bundles -> Build Asset Bundles


### UABE

1. Make a models/mymodel folder with the following underneath it
	3. unity/ - contains the exported models and parts ready for the CAB
	1. unity/<mymodel>_0/ - contains your package for the CAB
	2. unity/parts/ - contains the extracted parts bundle from UE
1. Open UABE
1. File -> Open the location `Documents\Unity\HBS BT Import Project\HBS BT Import Project\Assets\AssetBundles\Windows`
	1. Choose the `chrprfvhcl_mymodel` bundle
	1. Choose to uncompress, save as `unity/chrprfvhcl_mymodel`
2. Click 'Import'
	1.  Choose the APC bundle you extracted above
	2.  Save as `unity/chrprfvhcl_mymodel_imported`
3. File -> Close
1. File -> Open the location `Documents\Unity\HBS BT Import Project\HBS BT Import Project\Assets\AssetBundles\Windows`
	1. Choose the `mymodel_parts` bundle
	1. Choose to uncompress, save as `unity/parts/mymodel_parts`
1. Click 'Info'
	1. Click asset with name `mymodel` AND type of `Mesh`. 
	2. Click _Export Raw_
	3. Save to unity/parts/<MESH_RANDOM_STRING>
3. File -> Close
1. File -> Open the `unity/chrprfvhcl_mymodel_imported`
	1. Click 'Container' twice
	2. Click `chrprfvhcl_apc` with type `AssetBundle`
	3. Click _Export Dump_
	4. Save to unity/<DUMP_RANDOM_STRING>
5. In a text editor, open unity/<DUMP_RANDOM_STRING>
	1. Replace all instances of __apc__ in manifest.txt with __mymodel__
	2. Should be 5 find/replace substitutions if you did it right
	2. Save file
3. In UABE, click _Import Dump_
	1. Select unity/<DUMP_RANDOM_STRING>
	2. Click 'Ok'
	3. Save as `unity/chrprfvhcl_mymodel_imported_manifest`
4. Click _Info_
	1. Click 'Size (Bytes)' to order by largest size
	2. Select `chrTxrVhcl_apc_amb`
	3. Click 'Name' twice
	4. Hit the up arrow; you should have -alb, -amb, -ems, -msk, -nrm, -spc files ordered
	5. Select all of the chrTxrVhcl_apc -alb, -amb, -ems, -msk, -nrm, -spc  files
	6. Click _Plugins_
	7. Click _Batch Import_
	8. Click _Ok_
	9. Choose your textures folder (from above)
	10. For each file (should be 6), click on the `chrTxrVhcl_apc` file and hit edit
		1. Click 'Load' and choose the texture you created with the same name.
		2. Click 'Ok', then 'Ok' when prompted for Multi-thread
	3. Click 'Ok' on the Batch Import dialog
	4. Save as `unity/chrprfvhcl_mymodel_imported_manifest_textured`
5. Click _Info_
	1. Click 'Size (Bytes)' to order by largest size
	2. Select 'chrMdlVhcl_apc' with type 'Mesh'
	3. Click _Import Raw_
	4. Choose unity/parts/<MESH_RANDOM_STRING>
	5. Click _Ok_
	6. Save as `unity/chrprfvhcl_mymodel_imported_manifest_textured_ready`
3. File -> Close
4. File -> Compress

	1. Select `unity/chrprfvhcl_mymodel_imported_manifest_textured_ready`
	2. Make sure 'LZ4' is selected (should be default)
	2. Click 'Ok'
	3. Save as `unity/chrprfvhcl_mymodel_imported_manifest_textured_compressed`
4. Copy `unity/chrprfvhcl_mymodel_imported_manifest_textured_ready` to `unity/<mymodel>_0/chrprfvhcl_mymodel`

### Text Editor

1. Create `unity/<mymodel>_0/fragment.mod.json`
	1. Contents should be as below. Replace mymodel with the name you've been using above
	2. Should be 5 find/replace substitutions if you did it right

```json
        { "Type": "Prefab", "Path": "assets/character/vehicle/prefabs/chrprfvhcl_mymodel.prefab", "AssetBundleName": "chrprfvhcl_mymodel" },
        { "Type": "Prefab", "Path": "assets/character/vehicle/prefabs/weapons/mymodel/chrprfweap_mymodel_turret_generic_eh1.prefab", "AssetBundleName": "chrprfvhcl_mymodel" },

```
	
1. Create `unity/<mymodel>_0/hardpointdatadef_mymodel`
 	1. Contents should be as below. Replace mymodel with the name you've been using above
	2. Should be 2 find/replace substitutions if you did it right

```json
{
    "ID" : "hardpointdatadef_mymodel",
    "HardpointData" : [
        {
            "location" : "turret",
            "weapons" : [
                [
                    "chrprfweap_mymodel_turret_generic_eh1"
                ]
            ],
            "blanks" : [
                
            ],
            "mountingPoints" : [
                
            ]
        }
    ]
}
```

### Testing
  
Following assumes you're testing on BTA

1. Copy `unity/<mymodel>_0/hardpointdatadef_mymodel` to `BATTLETECH\Mods\CAB-Tank\hardpoints`
2. Copy `unity/<mymodel>_0/chrprfvhcl_mymodel` to `BATTLETECH\Mods\CAB-Tank\assetbundles`
2. Edit `BATTLETECH\Mods\CAB-Tank\mod.json` and paste your lines from `unity/<mymodel>_0/fragment.mod.json` into it below the ` "Type": "SoundBankDef", "Path": "soundbanks" },` block
3. For a vehicle you have in your save, find the vehicledef in `BATTLETECH\Mods\VIPAdvanced`
	1. Example: BATTLETECH\Mods\VIPAdvanced\heavychassis\vehiclechassisdef_ZHUKOV.json
2. Edit the following lines, replacing with mymodel

From:
```
	"HardpointDataDefID": "hardpointdatadef_zhukov",
	"PrefabIdentifier": "chrprfvhcl_zhukov",
	"PrefabBase": "zhukov",
```

To:

```
	"HardpointDataDefID": "hardpointdatadef_mymodel",
	"PrefabIdentifier": "chrprfvhcl_mymodel",
	"PrefabBase": "mymodel",
```


# BTIRS Notes<a name="btirs"></a>

This section deals with imports using 3dsTax's BTIRS tooling, specifically version 003. Other versions may work differently, or have fixed known issues (shown below).  

BTIRS is a standalone application that can export donor AssetBundles, import source GLB meshes, and assemble a target AssetBundle by parasitically replacing donor meshes and information. To get it, contact 3dsTax on the Rougetech Discord. The download will extract into multiple folders:
  
  * BTIRS - the application itself. Config data is stored here as well.
  * GLTF - both exported donor bundles AND source meshes in glTF format. 
  * Raw - a working directory for the application
  * Screenshots - as it says
  * Workspace - output assetbundles will be created here.
  
Load the BTIRS/MechEditor.exe application. You'll get a screen with 4 mechbay pads, several options on the left, input fields along the top, and stats on the top right. The most important are the input fields in white, which default to `chrprfmech_battlemasterbase-001`.

From top to bottom, these are:  
  
* A source AssetBundle you want to load from the Battletech/Mods directory. This works for both Vanilla and modded assets, so long as moddable assets are loaded by Modtek? Defaults to `chrprfmech_battlemasterbase-001'`. The selected bundle will be loaded into bay #2 (second from left)
* A source parasite mesh that you want to load from the GLTF directory. Defaults to `../GLTF/chrprfmech_battlemasterbase-001`. The selected mesh is loaded into bay #4 (right-most bay)
* A MechDef, ChassisDef, UIName, and Variant name to use for the generated assetbundle, hardpointdef, and mod.json.fragment. Defaults to `chrprfmech_battlemasterbase-001`, `battlemaster`, `blr`.

## BTIRS Workflow

Before starting, enable the **glTF 2.0 format** plugin in Blender. You'll need it for all import and export actions from Blender. 

Here's a high level view of the import workflow for just the model meshes. Dynamic weapons are discussed shortly after. Assume we're taking chrprfmech_spiderbase-001 (donor) and creating chrprfmech_stardriveapollobase-001 (target). 
  
* BTIRS: Export the donor assetbundle (chrprfmech_spiderbase-001)from BattleTech/Mods using the tool. Change the 'Parts Bundle Name' from `chrprfmech_battlemaserbase-001` to `chrprfmech-spiderbase-001`, and hit 'Load'. Then click 'Export Donor'. This generates a directory and loose files in /GLTF/chrprfmech_spiderbase-001. It should also load the spider into the 2nd slot.
* BTIRS: Duplicate the generated /GLTF/chrprfmech_spiderbase-001 directory, renaming it to your new asssetbundle (GLTF/chrprfmech_stardriveapollobase-001). Remove the chrprfmech_spiderbase-001.lgb file, and all chrxrMech_* files. We'll add them back later
* Blender: Create the meshes for stardriveapollo
* Blender: Create a new collection called Donor. Import /GLTF/chrprfmech_spiderbase-001 using File -> Import -> glTF 2.0 (.glb/.gltf). If the donor doesn't import within the collection, click it, right-click 'Select Hierarchy' then move it into the Donor collection
* Blender: Expand the donor to find the mesh parent; for us that's chrPrfMech_spiderBase-001(Clone) / mesh. Expand each sub-node and delete the hierarchy of nodes your mesh doesn't include. Few of us include rear meshes or torso meshes, for instance. These will be blanked in the output.
* Blender: For each mesh you want to replace, go into Edit mode on the donor mesh and delete all the verts. DO NOT delete the object itself. Once the donor verts are deleted, return to object mode. Join your mesh object to the donor object. Then enter edit mode again, and move the mesh verts as you. DO NOT move the object itself, only your mesh!
* Blender: For each of your meshes, check their Data / Attributes values. Remove any `bevel_*` attributes; these cause the importer to fail.
* Blender: Once all your meshes are converted, select the donor chrPrfMech, then select it's entire hierarchy. Then File -> Export -> glTF (.glb/.gltf). Export the mesh as your *target assetbundle*, in this case chrprfmech_stardriveapollobase-001.
* Substance: Export your unit and weapon textures following the HBS format. You'll need `chrTxrMech_stardriveapollobase-*` for the alb, amb, ems, mtls, nrm, v01-msk, v02-msk, v03-msk, v04-msk, v05-msk, and v06-msk. You'll need `chrTxrMech_stardriveapollobase-weapons-*` for the alb, amb, ems, mtls, and nrm. I changed my Substance export fields to use the mesh name, and used 'stardriveapollobase' for the mesh name during texturing.
* Substance: Copy all the chrTxrMech* textures to GLTF/chrprfmech_stardriveapollobase-001/
* BTIRS: Assuming you didn't export to the BTIRS directory, copy chrprfmech_stardriveapollobase-001 to GLTF/chrprfmech_stardriveapollobase-001
* BTIRS: Change the 'View Bundle Name' input to use your new updated bundle path instead of the default. For us, change `../GLTF/chrprfmech_battlemasterbase-001` to `../GLTF/chrprfmech_stardriveapollobase-001`. Then hit 'Load'. Your mesh should load into the 4th slot. It will be using the donor textures, but you can check for positioning errors.
* BTIRS: Update the 'MechDef', 'ChassiDef', and 'UIName' fields with your target values. Then hit 'Create'. This will take 10-30 seconds and create a new timestamped directory in /Workspace that looks something like `/Workspace/stardriveapollo_20250226032227`
* Copy the *compressed* (.lz4) assetbundle and hardpointdef to the appropriate CAB directory (or you mod directory). Make sure to remove the `_lz4` suffix from the assetbundle. I encourage you to clean the hardpointdatadef to remove unnecessary or unused imports.
* Copy the contents of the manifestdef.json into the mod.json of your CAB or mod directory. **CRITICALLY IMPORTANT: You MUST lowercase the very first line in the file, for the base prefab. In our case, we MUST change `../mechs/prefabs/chrPrfMech_stardriveapollobase-001.prefab` to `../mechs/prefabs/chrprfmech_stardriveapollobase-001.prefab`. IT WILL NOT LOAD IF YOU SKIP THIS**
* Launch the game and checkout the model in skirmish. It frequently works on the first try for me.

One of the major benefits of this approach is that once your target assetbundle is in the game directory, you can load it in BTIRS and see it as the game will without loading HBS BT. Simply change the 'Parts Bundle Name' to your target assetbundle and hit 'load'. It should load in place, with it's textures AND weapons and every time it's exactly what I get in game. This cuts down cycle time immensely, especially when dealing with weapon positioning.  
  
**WARNING: If you load your target assetbundle, MAKE SURE to re-load your donor bundle before doing 'Create' again. I.e. if you loaded `chrprfmech_stardriveapollobase-001` and found, and error, make sure to load `chrprfmech_spiderbase-001` again before trying to create an updated export!**

### BTIRS Dynamic Weapons

BTIRS allows you to both replace and add new dynamic hardpoints. It does regex matching to find replacements, and is **extremely particular** about naming. That said, the process is fairly straightforward. You can either 1) replace existing weapons on the parent or 2) generate completely new ones.

Before getting into the process, it's important to understand some context. Weapons generally have 4 layers of hierarchy:
  
* chrPrfWeap is the top level in the hierarchy. It gets parented to J_COCKPIT, J_LForearm, J_RForearm, J_LTHigh, or J_RThigh. The Origin of the object MUST be the parented object. **CRITICAL INFO: For any objects you manually parent to a donor J_ bone, Blender creates a `Parent Inverse` matrix. We don't want this; make sure to hit Alt+P and choose 'Clear Parent Inverse' for manually parented chrPrfWeap objects. If you don't, your transforms will be all over the place.**
* chrMdlWeap is the next level in the hierarchy. It must be parented to chrPrfWeap, BUT have its object origin at the world origin (0,0,0). 
* The mesh is the next level in the hierarchy. It must be parented to the chrMdlWeap, BUT have its object origin at the target bone (J_COCKPIT, J_LForearm, etc).
* The next level has one or more `_fire` objects representing fire transform positions. The origin of these should b e where you want the fire effect.

Replacing meshes on existing weapons is trivial. As with donor body parts, DO NOT replace the objects. Go into the target weapon mesh and delete the vertices, then join your objects, edit the mesh and move your mesh to where you want it.   
  
Once you're done with your weapons, just follow the export process from the point you create the GLB file of your donor hierarchy in Blender. You should be able to see all the weapons overlapping each other in both the GLTF and assetbundle forms.

#### Creating New Weapons
You can create completely new weapons as well, instead of using just what the donor provides. All you need is the hierarchy described above *with proper origins and parenting*, which works almost every time for me. I've provided a script in RT's #modelling channel which will take a weapon mesh and create the hierarchy for you, as well as associating the mesh with the donor's material for weapons. The things to remember when using it are:  
  
* If you create the hierarchy outside the Donor collection, make sure to Select Hierarchy on the created weapon and copy it into the Donor collection first. Parenting across collections works oddly.
* Once you have the weapon in the Donor collection, ONLY parent the chrPrfWeap object to the target bone, not the entire hierarchy. 
* After parenting chrPrfWeapon, make sure to remove the parent inverse matrix with Alt+P
* Validate the origins are correct for each level of the hierarchy. For a torso weapon, the origins should be chrPrfWeap=J_COCKPIT, chrMdlWeap=(0,0,0), mesh=J_COCKPIT

**Note: With the apollo, parenting off the spider ran into a small complication with the left arm. It only had laser_eh2, not laser_eh1. I ended up using the eh2 parent as a target instead of creating a eh1. I think a new eh1 would work here, but I haven't tested it.**

  
## BTIRS Issues, Bugs, and Limitations

* Issue - Confusing UI: "Parts Bundle Name", "View Bundle Name", "MechDef (.json)", "ChassisDef (.json)", "UIName", and "VariantName" rows in the editor can be changed, but DO NOT do anything. They are just labels. Only fields in white (not grey) are actual fields. 
* Limitation - Damage Meshes: The exporter doesn't include damage meshes from the donor.  It's unclear if they would be matched if you add them. They won't be present in the GLTF 
* Limitation - Donor Weapons: Donor weapons aren't stripped during the export process, though they are overwritten. If you replace the meshes, the export gets your new meshes. If you do nothing with them, they are included in the assetbundle. I recommend manually cleaning the hardpointdef and mod.json.fragment to remove anything you don't modders to invoke. 
* Limitation - Donor Blips: Sensor blips aren't included during the AssetBundle export process. Exports made prior to this being fixed will probably need to be reimported once corrected. 
* Bug: Meshes with any `bevel_weight_*` attributes (in Blender) fail to import.
* Bug: Export manifest uses wrong case on base prefab (chrPrfMech, etc)
* Bug: Fire positions may not be matched by regex, resulting in them defaulting to the donor position

# Miscellaneous Notes<a name="misc"></a>

## CustomUnits

*  CU vehicleDefs will fail if MountedLocation is not specified  
*  CU prefabs cannot be reused across hardpointdefs; each instantiation needs it's own prefab. Tried to use the same prefab across 2 monster turrets, and it caused hardlocks

## Unity Editor
* The global/local toggle set to local will show the actual transform vectors, instead of the overall unit vector. This is extremely useful when doing hardpoint attaches. Remember that 'forward' for a Vector3 in Unity is the Z-axis (i.e. the blue).



## Modeling<a name="misc-modeling"></a>
  
  * The import model's vertex count needs to be 50k or less. Unity's import will increase the vert count slightly, and any model > 55k gets split by Unity 5 into multiple meshes. BTG doesn't support multiple meshes (for vehicles) so you're stuck with ~ 45-50k.
  * The Unity scene we have requires Unity 5.5. Don't use Unity 2018.4 (what BTG uses) because the export will break.
  * The model/mesh is starts with `chrMdlVhcle`. The materials start with `chrMatVhcle`  
  
The only real parts you need are the following:  
* Center Torso => mechname_centre_torso
* Pelvis => mechname_centre_torso_pelvis
* Upper arm (left and right) => mechname_left_arm_upperarm, mechname_right_arm_upperarm
* forearm (left and right) => mechname_left_arm_forearm, mechname_right_arm_forearm
* thigh (left and right) => mechname_left_leg_thigh, mechname_right_leg_thigh
* calf (left and right) => mechname_left_leg_calf, mechname_right_leg_calf
* feet (left and right) => mechname_left_leg_foot, mechname_right_leg_foot
* cockpit  => mechname_cockpit

I always put a cockpit object in my mechs now, even if it is a invisible object hidden in the torso.  The cockpit saves a ton of headache because your CT will align properly.  Without it you have to do some funky alignment stuff for the CT.
I almost always merge my RT/LT into the CT.  Hips to the Pelvis and shoulders to the upperarm.

Ctrl+Shift+U to hide / show screen in system

If meshes look shaded for no reason, go to Object Data Properties (triangle) -> Geometry Data -> Clear Custom Split Normals Data. Boxcutter seems bad in particular for adding these which results in shading that doesn't match the geometry. It will appear as shaded flat tris.

### Blender FBX Export
Blender's native FBX export is... lacking. [Better FBX Export](https://blendermarket.com/products/better-fbx-importer--exporter) exports native to Unity better, and supports ASCII as well as binary. (Blender dropped ASCII in version 2.6)


## Texturing<a name="misc-texturing"></a>

Make lenses with no emission, but a paint-dot on their tips with full occlusion for a 'shine'

* Substance doesn't an emissive layer by default; you need to do so yourself
* Need to set Min/Max occlusion distance to 0.004 / 0.01 in AO bake
* Need to set color source = Vertex colors in ID bake
* UV mapping - don't use Smart UV, using 'Box projection', then 'Average Islands' and 'Pack Islands'

### Substance Defaults
- Vehicles bake to a 1K map, mechs to 2k, 4k if you *really* need it
- Note that larger map sizes take up more and more GPU ram, which causes the pink mechs issue. So try to avoid tons of 4k maps if possible
- Transient bakes with defaults, except ambient occlusion min: 0.004 and max: 0.01

### Unit color mask

RGB mask, set a black fill as the base so it comes out correctly
- Primary color is Blue channel
- Secondary color is Green channel
- Accent color is Red channel
  
 
== Zhukov def ==
Vehicles

	"HardpointDataDefID": "hardpointdatadef_shamash",
	"PrefabIdentifier": "chrprfvhcl_shamash",
	"PrefabBase": "shamash",
	
VTOLS

	"HardpointDataDefID": "hardpointdatadef_rakirov",
	"PrefabIdentifier": "rakirov_body",
	"PrefabBase": "rakirov",

# Requests<a name="requests"></a>

Requests for imports that are still outstanding.

- Carriers in need of true models:
  	- Mixed LRM+Thunderbolt
	- There's a rough list of carriers that aren't just missile boxes

KMission
* https://www.sarna.net/wiki/Gossamer_(Combat_Vehicle)

Raza: 
* https://www.sarna.net/wiki/Minion
* https://www.sarna.net/wiki/Musketeer
* https://www.sarna.net/wiki/Maultier

BD
* https://www.sarna.net/wiki/Hammerhands
* https://www.sarna.net/wiki/Sturmblitz
* https://www.sarna.net/wiki/Stygian
* https://www.sarna.net/wiki/LB-X_Carrier
* https://www.sarna.net/wiki/%C5%9Eoarece_Superheavy_MBT
* https://www.sarna.net/wiki/Buster
* https://www.sarna.net/wiki/Caesar

Haree:
* https://www.sarna.net/wiki/Prowler_(Combat_Vehicle)
* https://www.sarna.net/wiki/Harasser

Either the Regulator or the Musketeer would be the preferred one since both have 

Fuchsy on BTA:
* Dougram The Nikolaev - https://i.ebayimg.com/images/g/-vMAAOSwbxtgtcv1/s-l500.jpg

BTA #TT Channel:
* Defiance
* Rabid Coyote
* Patriot - https://www.sarna.net/wiki/Patriot
* Bowman
* Blood Kite
* Rook
* Prefect
* Tenshi
* Night Wolf
* Arctic Fox
* Beowulf
* Hachiman_Fire_Support_Tank
* Sarath quad
* Jian Che - https://cdn.discordapp.com/attachments/720016022194880602/1098737584995311706/Jian_Che_art.jpg
* Stooping Hawk - https://cdn.discordapp.com/attachments/720016022194880602/1098737667761512498/Stooping_Hawk.png
* Predator - https://cdn.discordapp.com/attachments/720016022194880602/1098737675097358396/Predator.png
* Matador - https://cdn.discordapp.com/attachments/720016022194880602/1098737819150733353/Matador.pngw
* Icestorm - https://cdn.discordapp.com/attachments/720016022194880602/1098737829946855484/Icestorm.png
* Red Shift - https://cdn.discordapp.com/attachments/720016022194880602/1098738012512337980/Red_Shift.png
* Blood Hound - https://cdn.discordapp.com/attachments/720016022194880602/1098738188559847454/Bloodhound.png
* Eyleuka - https://cdn.discordapp.com/attachments/720016022194880602/1098738608464199680/Eyleuka.png
* https://www.sarna.net/wiki/Ambassador
ME:
* [Viking Mech](https://cdn.discordapp.com/attachments/565136849752948736/847916645971263498/saulo-brito-vikingrobot-bg.png)

Interesting VTOLs:  

* https://www.sarna.net/wiki/Anhur
* https://www.sarna.net/wiki/Gossamer
* https://www.sarna.net/wiki/Peacekeeper_(Combat_Vehicle)
 
## Sources
- [Project Zhukov](https://drive.google.com/file/d/1nZEhDHVnn-dLR8CmwTFdjsNj4hHu4P_M/view)
