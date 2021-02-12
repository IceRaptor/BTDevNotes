# BT Developer Notes
This is my collection of random notes for use when modding the [HBS BattleTech](http://battletechgame.com/) game. I doubt anybody else would find them interesting.

under 50k or it splits
100k total on import

chrMdlVhcle == model/mesh
chrMatVhcle == material

Make lenses with no emission, but a paint-dot on their tips with full occlusion for a 'shine'

* Substance doesn't an emissive layer by default; you need to do so yourself
* Need to set Min/Max occlusion distance to 0.004 / 0.01 in AO bake
* Need to set color source = Vertex colors in ID bake

Unit color mask
======
RGB mask, set a black fill as the base so it comes out correctly
- Primary color is Green channel
- Secondary color is Blue channel
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
* https://www.sarna.net/wiki/Dixon_(law_enforcement)

Carriers in need of true models:

AC2/LBX2/Rifles
AC20
Thunderbolt5/10
Med Laser
Mortar
Flamer
Mixed LRM+Thunderbolt
There's a rough list of carriers that aren't just missile boxes

Raza: 
* https://www.sarna.net/wiki/Plainsman
* https://www.sarna.net/wiki/Minion
* https://www.sarna.net/wiki/Musketeer

Shade:
* https://www.sarna.net/wiki/Dig_King#/media/File%3ADig_Lord.jpg

Denadan
* https://cdn.discordapp.com/attachments/565136849752948736/806814292203667456/157555856919351749.png

Either the Regulator or the Musketeer would be the preferred one since both have

Interesting VTOLs:  

* https://www.sarna.net/wiki/Kamakiri
* https://www.sarna.net/wiki/Aeron
* https://www.sarna.net/wiki/Anhur
* https://www.sarna.net/wiki/Gossamer
* https://www.sarna.net/wiki/Peacekeeper_(VTOL)

# Transient's Workflow
	
1. Create model
1. Export model as FBX from blender
	1. UVMap model (smartUV + 0.10 islands)
	2. Vertex color model (use paint-> all to speed up)
	3. Export object only, no animation
	4. Scale model to ~ 8.5m long (for tanks)
	5. Make sure to apply all transforms
	6. Unity works with +z forward, +y upward by default
	7. Center unit on xyz origin. Treads slightly below x plane, slightly forward on Y. Blender numpad 7 gives you the expected view in Unity
	7. Make sure to apply all transforms!
1. Export textures (5 types; )
1. In UnityEditor, create new folder for model (lower-case name, i.e. ontosheat)
1. Create new GameObject named chrprfvhcl_<mymodel>
1. Drag GO into your folder; should create a blue cube
	1. Click on the blue cube, go to Asset Labels in the lower left, click new and name it the same as your chrprfvhcl<mymodel>
1. In UE, right-click to 'Import New Asset', include your FBX
	1. Note: Name should be chrMdlVhcl_<mymodel>
	1. Meshes of > 50k will split; keep verts under 50k
	1. Make sure to uncheck 'use file scale'; if checked the scale may be off
	1. Orientation in the scene does not matter; orientation in the mesh preview *does*
	1. FBX should be linked to an assetbundle named <mymodel>_parts
1. In UE, build your asset bundles
1. Uncompress assetbundle from unity
1. Import APC assets
1. save as `_import`
1. Open `_import`, save out AssetBundle as manifest.txt using UABE `Export Dump`
1. Replace all instances of apc in manifest.txt with your modelname
1. Update the AB using the new manifest.txt by using UABE 'Import Dump'
1. Save as `_manifest`
1. Find textures, update using plugin
	1. Links....
1. Save as `_texture`
1. Open mymodel_parts and find the mesh object. Export it using UABE 'Export raw'. Name it <TBD>
1. Close parts AB. Open `_texture` AB. Find the chrmdlvhcl_apc and 'Import Raw' the file from above.
1. Save the AB as `_ready`
1. Compress the file, save as `_compress` 
1. Build fragment.mod.json for CAB, add to CAB
1. Build hardpointdef
1. Edit vehiclechassisdef, setting <TBD> to new prefabs
