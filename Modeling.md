# BT Developer Notes
This is my collection of random notes for use when modding the [HBS BattleTech](http://battletechgame.com/) game. I doubt anybody else would find them interesting.


under 50k or it spilts
100k total on import

chrMdlVhcle == model/mesh
chrMatVhcle == material

# Transient's Workflow
	
1. Create model
1. Export model as FBX from blender
1. Texture / UVMap model
1. Export textures (5 types; )
1. In UnityEditor, create new folder for model (lower-case name, i.e. ontosheat)
1. Create new GameObject named chrprfvhcl_<mymodel>
1. Drag GO into your folder; should create a blue cube
1. Click on the blue cube, go to Asset Labels in the lower left, click new and name it the same as your chrprfvhcl<mymodel>
1. In UE, right-click to 'Import New Asset', include your FBX
	1. Note: Name should be chrMdlVhcl_<mymodel>
	2. Meshes of > 50k will split; keep verts under 50k
1. In UE, game object should be linked to an assetbundle named chrmdlvhcl_<mymodel>
	1. chrmdlvhcl_<mymodel should be linked to an assetbundle named <mymodel>parts
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
