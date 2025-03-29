import dearpygui.dearpygui as dpg

def save_callback():
    print("Save Clicked")

dpg.create_context()
dpg.create_viewport(resizable=False, title="Umineko Gilded Patcher", width=600, height=400)
dpg.setup_dearpygui()

with dpg.window(label="Example Window", no_title_bar=True,width=600, height=400):
    dpg.add_text("Hello world")
    dpg.add_button(label="Save", callback=save_callback)
    dpg.add_input_text(label="string")

    dpg.add_text("What spriteset would you like to use?\n(Note, sprites other than PS3 will require a sizable download.)")
    dpg.add_radio_button(label="spriteSelection", items=["Ryukishi/OG Sprites", "Alchemist/PS3 Sprites", "Panchiko/Mangagamer Sprites"], default_value="Alchemist/PS3 Sprites")

    dpg.add_text("Install Umineko Project GOAT Edition?\nOptional patch by Pteryon on Github.")
    dpg.add_checkbox(label="umiproGoatSelection", default_value=True)
    dpg.add_slider_float(label="float")

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()