bl_info = {
    "name": "BT2018 Weapon Prefab Layout",
    "blender": (4, 3, 1),
    "category": "Object",
}


import bpy
#import mathutils 
from mathutils import Vector 


class ObjectBT2018WeaponPrefabLayout(bpy.types.Operator):
    """BT2018 Weapon Prefab Layout"""
    bl_idname = "object.bt2018_weapon_prefab_layout"
    bl_label = "BT Wep Prefab"
    bl_options = {'REGISTER', 'UNDO'}
    
    weapon_location = [
        ("CT", "CT", "", 1),
        ("LT", "LT", "", 2),
        ("RT", "RT", "", 3),
        ("LA", "LA", "", 4),
        ("LL", "LL", "", 5),
        ("RA", "RA", "", 6),
        ("RL", "RL", "", 7),
        ("HEAD", "Head", "", 8)
    ]
    
    # (parent_attach, chrPrfWeap loc string, chrMdlWeap loc string)
    attach_data = {
        "CT"    : ("J_COCKPIT", "centertorso", "centre_torso"),
        "LT"    : ("J_COCKPIT", "lefttorso", "left_torso"),
        "RT"    : ("J_COCKPIT", "righttorso", "right_torso"),
        "LA"    : ("J_LForearm", "leftarm", "left_arm_forearm"),
        "RA"    : ("J_RForearm", "rightarm", "right_arm_forearm"),
        "LL"    : ("J_LHip", "leftleg", "left_leg"),
        "RL"    : ("J_RHip", "rightleg", "right_leg"),
        "HEAD"  : ("J_COCKPIT", "head", "head")
    }
    
    def get_import_donors(self):
        for obj in bpy.data.objects:
            if obj.name.lower().startswith("chrprfmech_") and obj.type == 'EMPTY':
                return obj.name
        
    donor_prefab_name: bpy.props.StringProperty(
        name="Donor Prefab Id", 
        default="chrPrfMech_battlemasterBase-001",
        get=get_import_donors
    )
    
    new_prefab_id: bpy.props.StringProperty(name="New Prefab Id", default="changeme")
    location: bpy.props.EnumProperty(items=weapon_location)
    prefabid: bpy.props.StringProperty(name="Prefab Type", default="laser")
    
    hardpoint: bpy.props.StringProperty(name="Hardpoint Type", default="eh")

    hardpoint_index: bpy.props.IntProperty(name="Hardpoint Index", default=1, min=1, max=30)
    fire_emitter_count: bpy.props.IntProperty(name="Fire Emitters", default=1, min=1, max=30)

    
    def get_stripped_donor_name(self, donor_prefab_name):
        start_idx = donor_prefab_name.find("_")
        end_idx = donor_prefab_name.find("ase-001")
        sliced_name = donor_prefab_name[start_idx+1:end_idx-1]
        return sliced_name
    

    def isolate_to_donor_collection(self, obj, donor_collection):
        in_donor_collection = False
        for u_c in obj.users_collection:
            if donor_collection.name == u_c.name:
                in_donor_collection = True
            else:
                u_c.objects.unlink(obj)

        if not in_donor_collection:
            donor_collection.objects.link(obj)
            
    
    def execute(self, context):
        weapon_mesh = bpy.context.selected_objects[0]
        
        # Find donors
        donor = None
        for obj in bpy.data.objects:
            if obj.name == self.donor_prefab_name:
                donor = obj

        if donor is None:
            self.report({"ERROR"}, "Could not find donor prefab: %s" % self.donor_prefab_name)
            return {'CANCELLED'}
        
        # Validate donor is only in one collection
        if len(donor.users_collection) > 1:
            self.report({"ERROR"}, "Donor: %s linked to more than one collection, not supported!" % self.donor_prefab_name)
            return {'CANCELLED'}
                            
        donor_collection = donor.users_collection[0]
        
        # Get the base name (battlemaster) from the prefab                
        donor_prefab_base_name = self.get_stripped_donor_name(self.donor_prefab_name)               
        
        # Find the donor weapons material        
        target_mat_name = "chrMatMech_{0}_weapons".format(donor_prefab_base_name)
        target_mat = None
        for mat in bpy.data.materials:
            if mat.name == target_mat_name:
                target_mat = mat
                break
        if target_mat is None:
            self.report({"ERROR"}, "Could not find donor prefab weapons material: %s" % self.target_mat_name)
            return {'CANCELLED'}

        # Find the attach point
        attach_bone_name = self.attach_data[self.location][0].lower() 
        attach_bone = None
        for child in donor.children_recursive:
            print("Child: %s" % child.name.lower)
            if child.name.lower() == attach_bone_name:
                attach_bone = child

        if attach_bone is None:
            self.report({"ERROR"}, "Could not find attach bone: %s" % attach_bone_name)
            return {'CANCELLED'}

        # Create chrPrfWeap_
        chrPrfWeap_loc_str = self.attach_data[self.location][1]
        chrPrfWeap_obj_name = "chrPrfWeap_{0}_{1}_{2}_{3}{4}".format(self.new_prefab_id, chrPrfWeap_loc_str, self.prefabid, self.hardpoint, self.hardpoint_index)        
        chrPrfWeap_obj = bpy.data.objects.new(name=chrPrfWeap_obj_name, object_data=None)
        chrPrfWeap_obj.parent = attach_bone        
        donor_collection.objects.link(chrPrfWeap_obj)

        # create chrMdlWeap_
        chrMdlWeap_loc_str = self.attach_data[self.location][2]
        chrMdlWeap_obj_name = "chrMdlWeap_{0}_{1}_{2}_{3}{4}".format(self.new_prefab_id, chrMdlWeap_loc_str, self.prefabid, self.hardpoint, self.hardpoint_index)
        chrMdlWeap_obj = bpy.data.objects.new(name=chrMdlWeap_obj_name, object_data=None)

        # Set the weapon's location to the world origin via the attach_bone's world matrix
        chrMdlWeap_obj.location = attach_bone.matrix_world.inverted().translation
        chrMdlWeap_obj.parent = chrPrfWeap_obj
            
        donor_collection.objects.link(chrMdlWeap_obj)

        # Set the mesh parent
        weapon_mesh.name = "{0}_{1}_{2}_{3}{4}".format(self.new_prefab_id, chrMdlWeap_loc_str, self.prefabid, self.hardpoint, self.hardpoint_index)

        # Move the mesh to world origin so there's less work when positioning
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')
        weapon_mesh.location = chrMdlWeap_obj.matrix_local.inverted().translation
        weapon_mesh.parent = chrMdlWeap_obj
        
        # Set the weapon materials
        weapon_mesh.data.materials.clear()
        weapon_mesh.data.materials.append(target_mat)        
        
        self.isolate_to_donor_collection(weapon_mesh, donor_collection)

        # Create fire emitters
        for i in range (0, self.fire_emitter_count):
            fire_emitter_obj = bpy.data.objects.new(name=chrMdlWeap_obj_name, object_data=None)
            if (i == 0):
                fire_emitter_obj.name = "{0}_{1}_{2}_{3}{4}_fire".format(self.new_prefab_id, chrMdlWeap_loc_str, self.prefabid, self.hardpoint, self.hardpoint_index)
            else:        
                fire_emitter_obj.name = "{0}_{1}_{2}_{3}{4}_fire{5}".format(self.new_prefab_id, chrMdlWeap_loc_str, self.prefabid, self.hardpoint, self.hardpoint_index, i+1)
            fire_emitter_obj.parent = weapon_mesh
            
            self.isolate_to_donor_collection(fire_emitter_obj, donor_collection)

        return {'FINISHED'}
    
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
        

def menu_func(self, context):
    self.layout.operator(ObjectBT2018WeaponPrefabLayout.bl_idname)


def register():
    bpy.utils.register_class(ObjectBT2018WeaponPrefabLayout)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    bpy.utils.unregister_class(ObjectBT2018WeaponPrefabLayout)

    
if __name__ == "__main__":
    register()
