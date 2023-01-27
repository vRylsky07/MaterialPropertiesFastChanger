import unreal
unreal.log("Python Script Add Roughness Starts")
assets_mats = unreal.EditorUtilityLibrary.get_selected_assets()
filred_array = unreal.EditorFilterLibrary.by_class(assets_mats, unreal.Material, unreal.EditorScriptingFilterType.INCLUDE)
assets_mats = filred_array
for mat in assets_mats:
    current_roughness=unreal.MaterialEditingLibrary.get_material_property_input_node(mat, unreal.MaterialProperty.MP_ROUGHNESS)
    unreal.MaterialEditingLibrary.delete_material_expression(mat,current_roughness)
    roughness_expession=unreal.MaterialEditingLibrary.create_material_expression
    roughness_instance= roughness_expession(mat, unreal.MaterialExpressionConstant, -100, +100)
    roughness_instance.r = 1
    current_spec=unreal.MaterialEditingLibrary.get_material_property_input_node(mat, unreal.MaterialProperty.MP_SPECULAR)
    unreal.MaterialEditingLibrary.delete_material_expression(mat,current_spec)
    spec_expession=unreal.MaterialEditingLibrary.create_material_expression
    spec_instance= roughness_expession(mat, unreal.MaterialExpressionConstant, -100, 0)
    spec_instance.r = 1
    current_met=unreal.MaterialEditingLibrary.get_material_property_input_node(mat, unreal.MaterialProperty.MP_METALLIC)
    unreal.MaterialEditingLibrary.delete_material_expression(mat,current_met)
    met_expession=unreal.MaterialEditingLibrary.create_material_expression
    met_instance= roughness_expession(mat, unreal.MaterialExpressionConstant, -100, -100)
    met_instance.r = 1
    unreal.MaterialEditingLibrary.connect_material_property(roughness_instance,'', unreal.MaterialProperty.MP_ROUGHNESS)
    unreal.MaterialEditingLibrary.connect_material_property(spec_instance,'', unreal.MaterialProperty.MP_SPECULAR)
    unreal.MaterialEditingLibrary.connect_material_property(met_instance,'', unreal.MaterialProperty.MP_METALLIC)
    unreal.MaterialEditingLibrary.recompile_material(mat)



