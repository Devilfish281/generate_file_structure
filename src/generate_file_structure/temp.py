    start_dir: Path = Field(  # Changed Code
        default_factory=lambda: Path(  # Changed Code
            c_setup_config.get_setting_value("START_DIR", ".").strip().strip("'\"")  # Changed Code
        ),  # Changed Code
        description="Path to the directory to generate file structure for.",  # Changed Code
    )  # Changed Code

    output_dir: Path = Field(  # Changed Code
        default_factory=lambda: Path(  # Changed Code
            c_setup_config.get_setting_value("OUTPUT_DIR", "./").strip().strip("'\"")  # Changed Code
        ),  # Changed Code
        description="Path to the output file for the generated file structure.",  # Changed Code
    )  # Changed Code

    output_file_name: str = Field(  # Changed Code
        default_factory=lambda: c_setup_config.get_setting_value(  # Changed Code
            "OUTPUT_FILE_NAME", "generated_file_structure.md"  # Changed Code
        ),  # Changed Code
        description="Name of the output file for the generated file structure.",  # Changed Code
    )  # Changed Code
