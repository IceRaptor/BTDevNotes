# BT Developer Notes
This is my collection of random notes for use when modding the [HBS BattleTech](http://battletechgame.com/) game. I doubt anybody else would find them interesting.


## Random notes  
  
  * The import model's vertex count needs to be 50k or less. Unity's import will increase the vert count slightly, and any model > 55k gets split by Unity 5 into multiple meshes. BTG doesn't support multiple meshes (for vehicles) so you're stuck with ~ 45-50k.
  * The Unity scene we have requires Unity 5.5. Don't use Unity 2018.4 (what BTG uses) because the export will break.
  * The model/mesh is starts with `chrMdlVhcle`. The materials start with `chrMatVhcle`  
  
The only real parts you need are the following:  
* Center Torso, 
* Pelvis, 
* Upper arm (left and right), 
* forearm (left and right), 
* thigh (left and right), 
* calf (left and right), 
* feet (left and right).  
* cockpit 

I always put a cockpit object in my mechs now, even if it is a invisible object hidden in the torso.  The cockpit saves a ton of headache because your CT will align properly.  Without it you have to do some funky alignment stuff for the CT.
I almost always merge my RT/LT into the CT.  Hips to the Pelvis and shoulders to the upperarm.

Ctrl+Shift+U to hide / show screen in system

## Texturing Notes

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

BD: 

Carriers in need of true models:

Flamer
Mixed LRM+Thunderbolt
There's a rough list of carriers that aren't just missile boxes

https://cfw.sarna.net/wiki/images/7/72/LB-X_Carrier.jpg

Raza: 
* https://www.sarna.net/wiki/Minion
* https://www.sarna.net/wiki/Musketeer
* https://www.sarna.net/wiki/File:Maultier.JPG

Haree:
* https://www.sarna.net/wiki/Prowler_(Combat_Vehicle)
* https://www.sarna.net/wiki/Harasser
* https://www.sarna.net/wiki/Pike_(combat_vehicle)
	**  (There is one that needs 3 barrels, and one that needs 2)

Shade:
* Loki loves melee things, so a hatchet would work well here
* https://www.sarna.net/wiki/Dig_King#/media/File%3ADig_Lord.jpg
* https://db4sgowjqfwig.cloudfront.net/images/636708/miningmek.gif
* https://s3.amazonaws.com/duxsite-battletech/87a2bcb6b597961044eddad891b7b10e3c79f6b30b1be3a26a4a77d32e41fd12u71.png
* https://www.ironwindmetals.com/images/com_hikashop/upload/thumbnails/300x300c000000/btindustrialmech/20-387.JPG
* https://cdnb.artstation.com/p/assets/images/images/019/977/873/large/longque-chen-timber-mech-17.jpg?1565822495
* http://2.bp.blogspot.com/-RDbza10lBYM/TmJIxj0LR6I/AAAAAAAAAz4/gwxk3HYvVno/s1600/IMECminer01.JPG1
* https://pbs.twimg.com/media/CHFuDvCWcAAaO8C.jpg


* https://sc01.alicdn.com/kf/HTB1r.jWKVXXXXb9XpXXq6xXFXXXi/Rock-Rotary-Drill-Head.jpg_350x350.jpg
* https://mining.komatsu/images/default-source/product-images/underground/room-and-pillar-entry-development/gpl5755.jpg?sfvrsn=40740a6b_48
* https://farm3.staticflickr.com/2905/14353629754_58dd5e443e_b.jpg
* http://www.saltassociation.co.uk/wp/wp-content/uploads/continuousdigger_lge.jpg

ME:  
* Viking Mech - https://cdn.discordapp.com/attachments/565136849752948736/847916645971263498/saulo-brito-vikingrobot-bg.png
* https://www.sarna.net/wiki/File:3055u_Gunslinger.jpg


Either the Regulator or the Musketeer would be the preferred one since both have

Interesting VTOLs:  

* https://www.sarna.net/wiki/Kamakiri
* https://www.sarna.net/wiki/Aeron
* https://www.sarna.net/wiki/Anhur
* https://www.sarna.net/wiki/Gossamer
* https://www.sarna.net/wiki/Peacekeeper_(VTOL)
* Robotech Beta fighter - https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/ad730f9f-28e3-4bef-a04c-6fcc3a4227ba/d6q6jwe-ac16c175-748c-44cc-88f7-fc1064c81c4b.jpg/v1/fill/w_1024,h_579,q_75,strp/shadow_beta_fighter_by_kevarin-d6q6jwe.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwic3ViIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl0sIm9iaiI6W1t7InBhdGgiOiIvZi9hZDczMGY5Zi0yOGUzLTRiZWYtYTA0Yy02ZmNjM2E0MjI3YmEvZDZxNmp3ZS1hYzE2YzE3NS03NDhjLTQ0Y2MtODhmNy1mYzEwNjRjODFjNGIuanBnIiwid2lkdGgiOiI8PTEwMjQiLCJoZWlnaHQiOiI8PTU3OSJ9XV19.jaId31uMnJB3DhYnqqptxjCW70zpQEC2X5I1vJHhovg

# Import Workflows

Everybody is different, but it seems. Some miscellaneous notes:

* Always lowercase the name
* Avoid name collisions where possible

# Mech Import Workflows

Notes:
- Make sure you use the 1.6 bundles from BT, not the current bundles. UABE can't export textures on current bundles, and will corrupt them when you make assets.
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

# Regular Vehicle Import Workflow

Largely from Transient and Shade. DO NOT COVER VTOLS
	
## Common Setup

1. Extract APC bundle to path on disk
2. Download [UABE](https://github.com/DerPopo/UABE/releases)

## Blender or Equivalent

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
	
## Substance Painter or Equivalent

1. Export your 6 textures. Most should be 1024 for vehicles, but you can use 2048 if you really need details. Names below don't strictly matter and are provided to link the various parts together.
	1. Albedo map should be RGBA, as `<texturename>_ALB`
	2. Ambient Occlusion map should be RGB, as `<texturename>_AO`
	3. Emissive map should be RGB, as `<texturename>_EMS`
	4. Specular (aka Metallics) should be RGBA, as `<texturename>_MTLS`
	5. Normals should be RGB, as `<texturename>_NRM`
	6. Mask should be RGBA, as `<texturename>_MSK`

## Unity Editor

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


## UABE

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

## Text Editor

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

## Testing
  
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