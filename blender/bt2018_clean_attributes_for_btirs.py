bl_info = {
    "name": "BT2018 Clean Attributes for BTIRS",
    "blender": (4, 3, 1),
    "category": "Object",
}

import bpy

class ObjectBT2018CleanObjectAttributes(bpy.types.Operator):
    """BT2018 Clean Attributes for BTIRS"""
    bl_idname = "object.bt2018_clean_for_btirs"
    bl_label = "BT Clean Attribs"
    bl_options = {'REGISTER', 'UNDO'}
    
    properties_to_clean = [ 
        "bevel_weight_edge",
        "bevel_weight_vert" 
    ]
    
    def execute(self, context):
        for obj in bpy.context.selected_objects:
            if hasattr(obj, "data") and hasattr(obj.data, "attributes"):
                for a in obj.data.attributes:
                    if a.name in self.properties_to_clean:
                        print("Removing: %s from object: %s" % (a.name, obj.name))
                        obj.data.attributes.remove(a)
                    # print("  attribute: %s" % a)

        return {'FINISHED'}
    
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)
        

def menu_func(self, context):
    self.layout.operator(ObjectBT2018CleanObjectAttributes.bl_idname)


def register():
    bpy.utils.register_class(ObjectBT2018CleanObjectAttributes)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    bpy.utils.unregister_class(ObjectBT2018CleanObjectAttributes)

    
if __name__ == "__main__":
    register()
