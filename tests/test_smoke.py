import numpy as np
from datetime import datetime


def test_infrared_display_creation_and_status():
    from infrared_nanoparticle_integration import (
        InfraredNanoparticleIntegration,
        DisplayType,
    )

    integration = InfraredNanoparticleIntegration()
    specs = integration.create_display_system(
        "Test_Display_01",
        DisplayType.CRYSTAL_TABLET,
        "advanced_ucnp",
        "enhanced_quartz",
        (320, 200),
        60.0,
    )

    status = integration.get_display_system_status("Test_Display_01")
    assert status["system_name"] == specs.system_name
    assert status["display_type"] == DisplayType.CRYSTAL_TABLET.value
    assert status["status"] == "active"


def test_glasssphere_os_touch_processing():
    from glasssphere_os import GlassSphereOS, TouchInputData, InterfaceMode

    os_system = GlassSphereOS()

    # Register user and set as current user
    user = os_system.register_user(
        "user_test",
        "Test User",
        {"alpha_wave": 0.6, "beta_wave": 0.4},
        {"fundamental_frequency": 180.0},
        biofield_resonance=0.8,
        spiritual_attunement=0.7,
    )
    os_system.current_user = user
    os_system.switch_interface_mode(InterfaceMode.STANDARD_VISUAL)

    # Minimal touch input
    touch = TouchInputData(
        timestamp=datetime.now(),
        position=(0.2, 0.8),
        pressure=0.5,
        energy_level=0.75,
        frequency_signature=293.66,  # within third_eye range
        resonance_pattern=np.array([0.1, 0.2, 0.3]),
        chakra_activation={},
    )
    processed = os_system.process_touch_input(touch)
    assert "interface_response" in processed
    assert 0.0 <= processed["energy_resonance"] <= 1.0


def test_ui_shell_render_small_frame():
    from glasssphere_ui_shell import (
        GlassSphereUIShell,
        UIMode,
        OverlayType,
    )

    ui = GlassSphereUIShell()
    # Use very small resolution to keep test fast
    ui.create_display("disp1", (64, 48), 30.0)
    ui.register_user_interface("user1", UIMode.NIGHT_VISION)
    ui.enable_night_vision_mode("disp1", "user1")

    thermal = np.random.normal(300, 5, (12, 16))
    ui.create_ir_overlay("ov1", OverlayType.THERMAL_MAP, thermal, "disp1")

    base = np.random.uniform(0, 1, (48, 64, 3))
    frame = ui.render_display_frame("disp1", base)

    assert frame is not None
    assert frame.shape == base.shape

