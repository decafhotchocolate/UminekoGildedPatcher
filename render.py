import dearpygui.dearpygui as dpg

def save_callback():
    print("Save Clicked")

def add_and_load_image(image_path, parent=None):
    width, height, channels, data = dpg.load_image(image_path)

    with dpg.texture_registry() as reg_id:
        texture_id = dpg.add_static_texture(width, height, data, parent=reg_id)

    if parent is None:
        return dpg.add_image(texture_id)
    else:
        return dpg.add_image(texture_id, parent=parent)
        

dpg.create_context()
dpg.create_viewport(title="Umineko Gilded Patcher", width=800)
dpg.setup_dearpygui()


def callback(sender, app_data):
    print('OK was clicked.')
    print("Sender: ", sender)
    print("App Data: ", app_data)
    if sender == "file_dialog_id":
        selected_directory = app_data["file_path_name"]

def cancel_callback(sender, app_data):
    print('Cancel was clicked.')
    print("Sender: ", sender)
    print("App Data: ", app_data)

dpg.add_file_dialog(
    directory_selector=True, show=False, callback=callback, tag="file_dialog_id",
    cancel_callback=cancel_callback, width=700 ,height=400)

with dpg.window(tag="main_window"):
    dpg.add_text("Umineko Project: Gilded Patcher (v000)")

    dpg.add_button(label="Select where your Umineko Project is located.\n(this folder contains onscripter-ru.exe)", callback=lambda: dpg.show_item("file_dialog_id"))


    dpg.add_text(" ")

    dpg.add_text("What spriteset would you like to use?\n(Note, sprites other than PS3 will require a sizable download.)")
    dpg.add_radio_button(label="spriteSelection", items=["Ryukishi/OG Sprites", "Alchemist/PS3 Sprites", "Panchiko/Mangagamer Sprites"], default_value="Alchemist/PS3 Sprites")

    dpg.add_text(" ")

    dpg.add_text("Font scale? (Default is 1.0)\n1.2 is recommended on the Umineko Project website.")
    dpg.add_input_text(label="Font scale", default_value="1.0", width=100)

    dpg.add_text(" ")

    # before uploading this get permission from umipro goat & discord guys

    dpg.add_text("Discord integration? (Provided by m3t4f1v3 on Github)")
    dpg.add_checkbox(label="Install Discord integration", default_value=True)
    dpg.add_text(" ")
    
    dpg.add_text("Enable smallcaps? By default in Umineko Project, BEATRICE will have her name displayed this way.\nIf it matters to you, this was not the case in the original WH/MangaGamer releases.\nHowever, it does emulate the fact BEATRICE's name is origianlly in katakana.")

    add_and_load_image("res/smallcaps_false.png")
    add_and_load_image("res/smallcaps_true.png")

    dpg.add_checkbox(label="Smallcaps for BEATRICE", default_value=True)


    dpg.add_text(" ")
    

    dpg.add_text("Would you like your fonts to have a small gradient on them? (Default Umineko Project behavior)")
    add_and_load_image("res/gradient_false.png")
    dpg.add_checkbox(label="Font gradient", default_value=True)

    dpg.add_text(" ")

    dpg.add_text("What spriteset would you like to use?\n(Note, sprites other than PS3 will require a sizable download.)")
    add_and_load_image("res/sprites.png")
    dpg.add_radio_button(label="spriteSelection", items=["Ryukishi/OG Sprites", "Alchemist/PS3 Sprites", "Panchiko/Mangagamer Sprites"], default_value="Alchemist/PS3 Sprites")

    dpg.add_text(" ")
    
    dpg.add_text("Install Umineko Project GOAT Edition?\nOptional patch by Pteryon on Github.\nContains new logos, replaces PS3 openings with less-spoilery original PC openings, more.")
    # note, UMIPROGOAT only provides ps3fication of og openings, need to add original openings
    dpg.add_button(label="Read more info here!", callback=lambda:webbrowser.open("https://github.com/Pteryon/umipro-goat"))
    dpg.add_checkbox(label="Install GOAT Edition ", default_value=True)

dpg.show_viewport()
dpg.set_primary_window("main_window", True)
dpg.start_dearpygui()
dpg.destroy_context()
