# BT Developer Notes
This is my collection of random notes for use when modding the [HBS BattleTech](http://battletechgame.com/) game. I doubt anybody else would find them interesting.

## Random notes
- CU vehicleDefs will fail if MountedLocation is not specified  
  

## Modeling
  
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

## Texturing

Make lenses with no emission, but a paint-dot on their tips with full occlusion for a 'shine'

* Substance doesn't an emissive layer by default; you need to do so yourself
* Need to set Min/Max occlusion distance to 0.004 / 0.01 in AO bake
* Need to set color source = Vertex colors in ID bake
* UV mapping - don't use Smart UV, using 'Box projection', then 'Average Islands' and 'Pack Isalnds'

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
	

# Requests

Carriers in need of true models:

Mixed LRM+Thunderbolt
There's a rough list of carriers that aren't just missile boxes

https://cfw.sarna.net/wiki/images/7/72/LB-X_Carrier.jpg

Raza: 
* https://www.sarna.net/wiki/Minion
* https://www.sarna.net/wiki/Musketeer
* https://www.sarna.net/wiki/File:Maultier.JPG

BD
* https://www.sarna.net/wiki/Sturmblitz
* https://www.sarna.net/wiki/Stygian
* https://www.sarna.net/wiki/LB-X_Carrier
* https://www.sarna.net/wiki/%C5%9Eoarece_Superheavy_MBT


Haree:
* https://www.sarna.net/wiki/Prowler_(Combat_Vehicle)
* https://www.sarna.net/wiki/Harasser

ME:  
* Viking Mech - https://cdn.discordapp.com/attachments/565136849752948736/847916645971263498/saulo-brito-vikingrobot-bg.png


Either the Regulator or the Musketeer would be the preferred one since both have

Interesting VTOLs:  

* https://www.sarna.net/wiki/Kamakiri
* https://www.sarna.net/wiki/Aeron
* https://www.sarna.net/wiki/Anhur
* https://www.sarna.net/wiki/Gossamer
* https://www.sarna.net/wiki/Peacekeeper_(VTOL)
* 
* Robotech Beta fighter - https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/ad730f9f-28e3-4bef-a04c-6fcc3a4227ba/d6q6jwe-ac16c175-748c-44cc-88f7-fc1064c81c4b.jpg/v1/fill/w_1024,h_579,q_75,strp/shadow_beta_fighter_by_kevarin-d6q6jwe.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwic3ViIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl0sIm9iaiI6W1t7InBhdGgiOiIvZi9hZDczMGY5Zi0yOGUzLTRiZWYtYTA0Yy02ZmNjM2E0MjI3YmEvZDZxNmp3ZS1hYzE2YzE3NS03NDhjLTQ0Y2MtODhmNy1mYzEwNjRjODFjNGIuanBnIiwid2lkdGgiOiI8PTEwMjQiLCJoZWlnaHQiOiI8PTU3OSJ9XV19.jaId31uMnJB3DhYnqqptxjCW70zpQEC2X5I1vJHhovg

Project Zhukov - https://drive.google.com/file/d/1nZEhDHVnn-dLR8CmwTFdjsNj4hHu4P_M/view

# Import Workflows

## Custom Units

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

- CU animator will set 'in_battle', 'charge', 'forward' animator properties
- Animators have to be defined in json, like "Animators": [ "j_Body","LB","LF","RB","RF" ], 
- Animators should be attached to objects with distinct names. Don't use `body`!
- 
in_battle - boolean
charge - trigger
forward - float

#### Twist Animations
TwistAnimators - it is different set of animators which can be triggered independently they are triggering next animator values
StartRandomIdle - bool
TwistR - float (0-1) used with StartRandomIdle = false
TwistL - float (0-1) used with StartRandomIdle = false
IdleTwistR - float (0-1) used with StartRandomIdle = true
IdleTwistL - float (0-1) used with StartRandomIdle = true
you can look at yellowjacket twist animator implementation for inspiration

### CU VTOL Import

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

### CU Mech Import

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

(!) CAUTION: This is currently speculative, I've not done an actual import with these yet. IMPORTER BEWARE

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

Inside this parent, create a new GameObject called 'body'. You'll use this object to make all your transformations of the position, scale, or rotation. Next, drag your mesh under 'body' to create a new child GameObject. Add the SkinnedMeshRenderer component to the child, but DO NOT associate it with a root bone. 

To adjust the position of the mesh, you will adjust the transform on the `body` element. It's not special, and you can technically go without it and adjust the transform on the GO with the SkinnedMeshRenderer. I prefer to keep them separate though.

Now we'll create the GameObject you'll use to position the weapon. Copy your chrprfweap GO into the location that will mount the weapon. Here's the breakdown of locations by bind-bone:

* `j_Root/j_Pelvis/j_Pitch/j_Spine/j_Spine1/j_Spine2/j_COCKPIT` - used for left, right, centre torso and head weapons 
* `j_Root/j_Pelvis/j_Pitch/j_Spine/j_Spine1/j_Spine2/j_LClavicle/j_LUpperArm/j_LForearm` - used for arm weapons
* `j_Root/j_Pelvis/j_LHip/j_LThigh/j_LCalf/`- used for leg weapons

**DO NOT** use the `_cu` GameObjects that you created for your parts as the parents for your weapons. Your weapons are always lashed up to the parent skeleton, not your derived parts. 

Once you have the new chrprfweap, align the weapon using the `body` transform. For arm weapons you may find the donor model as the forearms rotated at random degrees. Do you best to align them now, but it's trivial to correct the alignment with BTDebug later. Once the `body` transform for a weapon what you want it to be, copy the transform component (click the cog icon, then choose Copy Component). Then go back to the original `chrprfweap_cuYOURMECH_lefttorso_laser_eh1` at the top level, and copy those values onto it's `body` element (click the cog icon, then Paste Component Values).   
  
If you have done this correctly, the transform on `chrprfweap_cuYOURMECH_lefttorso_laser_eh1` should be 0,0,0 for position and rotation, and scale of 1. The `body` child has the same values on the top-level and your embedded chrprfweap GOs. Now, copy your top-level chrprfweap prefab into the project window, under the path assets/character/mech/prefabs/. 

I prefer to use a directory to hold all my assets for a model, so my path for the Rifleman3 was assets/character/mech/prefabs/rifleman3. You just need to remember this later when the hardpoints are being defined.

Next, associate the chrprfweap prefab with the parent model's assetbundle. Click the prefab and in the bottom right window, choose the mech's assetbundle. For my rifleman3, this meant `chrprfweap_curifleman3_leftarm_ac2_bh1` was embedded in AssetBundle `chrprfmech_curifleman3base-001`. Now, build your assetbundle and wait for Unit to do it's thing.

** Hardpoints and Prefab Loading**

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
		{"prefab": "chrprfweap_curifleman3_leftarm_gauss_bh1", "attachType": "Body", "shaderSrc": "chrPrfWeap_atlas_centertorso_laser_eh1", "emitters": [  ] },
		{"prefab": "chrprfweap_curifleman3_leftarm_ac20_bh1", "attachType": "Body", "shaderSrc": "chrPrfWeap_atlas_centertorso_laser_eh1", "emitters": [  ] },
		{"prefab": "chrprfweap_curifleman3_leftarm_ac10_bh1", "attachType": "Body", "shaderSrc": "chrPrfWeap_atlas_centertorso_laser_eh1", "emitters": [  ] },  
```

You can do A LOT with this, but the above is your basic binding. It will load the prefab, attaches to the body of the model, use a generic shader, and has no specific emitters. 

Emitters are GameObjects that are used as the origin for projectiles. If you omit them, the projectiles issue from the attach point of the weapon mesh (I think). If you want to go the extra mile and define then, add a body/fire game object, and define one or more emitters under this hierarchy. The emitter GameObject should have it's transform at the position you want the projectile to originate from. As an example, I have `chrprfweap_kamakiri_left_tbolt/body/fire/fire1` and `chrprfweap_kamakiri_left_tbolt/body/fire/fire2` defined. Fire1 and fire2 both have transforms at the end of the Thunderbolt launcher where I want the missile to originate from. The hardpoint def for the Kamakiri then has:

```
      { "prefab": "chrprfweap_kamakiri_left_tbolt", "shaderSrc": "chrPrfWeap_atlas_centertorso_laser_eh1", "emitters": [ "fire1", "fire2" ] },
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

* Model throwing an NRE that you can't figure out? Did you make sure to add a camoholder object, with 6 patterns? They can all be the same, but it needs to be present.
* Material not loading? Make sure you name it CUMODELNAMEbase and CUMODELNAMEweapons. For the `chrprfmech_curifleman3base-001` assetbundle, that means the names must be `curifleman3base` and `curifleman3weapons`. Camos are just `curifleman3_camo0`.
* Model not loading, but no NRES? Make sure your donor j_Root is under bones/. CU will look to match using the /bones object, so leaving it out will cause subtle weird errors.
* Top level under your assetbundle (i.e. `chrprfmech_curifleman3base-001`) needs to be bones/, mesh/, and camoholder. 

## Legacy Workflow 

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

### Mech Import

Notes:

- Weapons get only textures, no masks
- Mechs gets 6 masks
- You need to blank any parts you're not using, using a tiny mesh
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




### Standard Vehicle Import 

Largely from Transient and Shade. DOES NOT COVER VTOLS
	
#### Common Setup

1. Extract APC bundle to path on disk. In UABE, uncompress the bundle. Then Export to save as .assets
2. Download [UABE](https://github.com/DerPopo/UABE/releases)

#### Blender or Equivalent

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
	2. Select 'chrTxrVhcl_apc' with type 'Mesh'
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