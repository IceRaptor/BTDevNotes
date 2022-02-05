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
- CU animator will set 'in_battle', 'charge', 'forward' animator properties
- Animators have to be defined in json, like "Animators": [ "j_Body","LB","LF","RB","RF" ], 
- Animators should be attached to objects with distinct names. Don't use `body`!


- TODO
- Added paint mat 
- Add twist animations
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

__Step 3: Meshes and Materials__

Create the following new folders in the project view, for your mech:

* `Assets/characters/mechs/materials/XXX`
* `Assets/characters/mechs/models/XXX`
* `Assets/characters/mechs/textures/XXX`

Import your meshes into `/models`. Each mech component should have an origin at the center of the mesh geometry. 

Import your textures into `/textures/`. You need an albedo, ambient occlusion, emissive, specular (metallic), and normals as a minimum. You should also have 6 camo masks, RGBa masks (covered in Texturing up in this document). Click the normals texture and mark it as Texture Type: normal map in the top right, and hit save. 

Right click and choose Create -> Material. You MUST use the name of your PREFAB + `base` as the material name. For my `cuelemental` prefab, I used material `cuelementalbase`. Click the new material. Copy the albedo texture into the albedo block, the AO map into the occlusion block, enable emission and copy the emissive mask there. Copy the normals texture to the normal map block, and finally copy the speculars to the metallic block. 

If you have camo masks, create one material for each mask. It should be name prefix + `_camoX` where X is the camo ID (0 through 5). Copy ONLY the camo mask into the albedo block, and leave everything else blank. Example: `cuelemental_camo0`

Go back to your model's mesh/ hierarchy. Click-drag the meshes into the relevant section (i.e. the head into ``meshes/mesh_Head/Head_Whole`). For each part, right-click and choose 'Unpack Prefab Completely'. Once all your parts are imported, select them all. In the Inspector window, remove the `Mesh Filter` component by clicking the gear icon on the far right. Next, click 'Add Component' and add a `Skinned Mesh Renderer` component. Click the i button next to the `Materials/element 0` and choose the material you created above.

Note the 'mesh' and 'Root Bone' fields. CustomUnits works by finding all Skinned Mesh Render components, and trying to match their `Root Bone` with the same name on the parent skeleton. 

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