# src/generate_file_structure/setup_config.py

import logging
import os
import threading
from asyncio.log import logger
from pathlib import Path

# from logging import config
from typing import ClassVar, Optional

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, ConfigDict, Field

from generate_file_structure.my_utils.custom_settings_loader import (
    load_custom_settings_once,
)
from generate_file_structure.my_utils.directory_setup import (
    create_chat_gpt_directory_once,
)
from generate_file_structure.my_utils.env_loader import load_dotenv_once
from generate_file_structure.my_utils.llm_loader import get_llm_or_init
from generate_file_structure.my_utils.logger_setup import setup_logger
from generate_file_structure.my_utils.path_utils import validate_path

try:
    load_dotenv_once()
except Exception:
    pass

# from dataclasses_json import config


#  c_setup_config is a singleton class that holds configuration and runtime objects for the application.
# It uses Pydantic for data validation and management, and includes methods for masking sensitive information

LOGGER_PROJECT_NAME = "generate_file_structure"


class c_setup_config(BaseModel):
    """
    Singleton-style setup/config model for runtime configuration and shared objects.

    :ivar log_prompt_flag: Whether prompt logging is enabled.
    :vartype log_prompt_flag: bool
    :ivar llm: Cached LangChain OpenAI chat model instance.
    :vartype llm: Optional[ChatOpenAI]
    :ivar logger: Cached logger instance.
    :vartype logger: Optional[logging.Logger]
    :ivar max_chunk_size_bytes: Maximum chunk size for processing.
    :vartype max_chunk_size_bytes: int
    :ivar openai_model: Default OpenAI model name.
    :vartype openai_model: str
    :ivar testing_flag: Primary testing mode flag.
    :vartype testing_flag: bool
    :ivar testing_flag2: Secondary testing mode flag.
    :vartype testing_flag2: bool
    """

    ##########################################################################
    # Flags
    ###########################################################################

    ################################ Path Flags ################################

    start_dir: Path = Field(
        default=Path(os.getenv("START_DIR", ".").strip().strip("'\"")),
        description="Path to the directory to generate file structure for.",
    )

    output_dir: Path = Field(
        default=Path(os.getenv("OUTPUT_DIR", "./").strip().strip("'\"")),
        description="Path to the output file for the generated file structure.",
    )

    output_file_name: str = Field(
        default=os.getenv("OUTPUT_FILE_NAME", "generated_file_structure.md"),
        description="Name of the output file for the generated file structure.",
    )
    ################################ bool Flags ################################

    python_project_flag: bool = Field(
        default_factory=lambda: c_setup_config.env_bool("PYTHON_PROJECT_FLAG", True),
        description="Flag to indicate if the application is running as a Python project.",
    )

    next_js_project_flag: bool = Field(
        default_factory=lambda: c_setup_config.env_bool("NEXT_JS_PROJECT_FLAG", False),
        description="Flag to indicate if the application is running as a Next.js project.",
    )
    # CUSTOM_HEADER_NAME
    custom_header_name: str = Field(
        default=os.getenv("CUSTOM_HEADER_NAME", "custom_header.md"),
        description="Name of the custom header file to include at the top of the output file.",
    )

    # CUSTOM_HEADER_BEGINNINGNAME
    custom_header_beginning_name: str = Field(
        default=os.getenv("CUSTOM_HEADER_BEGINNING_NAME", "beginning.md"),
        description="Name of the custom header file to include at the top of the output file.",
    )
    ################################
    # OTHERS
    ################################
    # include the test directory
    include_tests_flag: bool = Field(
        default_factory=lambda: c_setup_config.env_bool("INCLUDE_TESTS_FLAG", False),
        description="Flag to indicate if the application should include test directories.",
    )

    log_prompt_flag: bool = Field(
        default=False, description="Enable logging of prompts."
    )

    llm: Optional[ChatOpenAI] = Field(default=None, description="LLM Configuration.")

    logger: Optional[logging.Logger] = Field(
        default=None, description="Logger Configuration."
    )

    # MAX_CHUNK_SIZE_BYTES = int(os.getenv("MAX_CHUNK_SIZE_BYTES", str(24 * 1024 * 1024)))
    max_chunk_size_bytes: int = Field(
        default=int(os.getenv("MAX_CHUNK_SIZE_BYTES", str(24 * 1024 * 1024))),
        description="Maximum chunk size in bytes for processing large files.",
    )

    # OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5.1")
    openai_model: str = Field(
        default=os.getenv("OPENAI_MODEL", "gpt-5.1"),
        description="Default OpenAI model to use for LLM interactions.",
    )

    testing_flag: bool = Field(
        default_factory=lambda: c_setup_config.env_bool("TESTING_FLAG", False),
        description="Flag to indicate if the application is running in testing mode.",
    )

    testing_flag2: bool = Field(
        default_factory=lambda: c_setup_config.env_bool("TESTING_FLAG2", False),
        description="Flag to indicate if the application is running in testing mode level 2.",
    )

    ###########################################################################
    # Thread Safety for Singleton: for a singleton pattern,
    # we need to ensure that only one instance of the class is created,
    # even in a multi-threaded environment.
    ###########################################################################
    _instance: ClassVar[Optional["c_setup_config"]] = None
    _lock: ClassVar[threading.Lock] = threading.Lock()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    ##########################################################################
    # method for loading custom settings from Custom_setting.md
    # with caching to avoid repeated file reads.
    ##########################################################################
    @classmethod
    def get_custom_settings_path(cls) -> Path:
        return Path.cwd() / "Custom_setting.md"

    @classmethod
    def get_custom_settings(cls) -> dict[str, str]:
        return load_custom_settings_once(cls.get_custom_settings_path())

    @classmethod
    def get_setting_value(cls, key: str, default: str = "") -> str:
        custom_settings = cls.get_custom_settings()
        if key in custom_settings:
            return custom_settings[key]
        return os.getenv(key, default)

    @classmethod
    def get_setting_bool(cls, key: str, default: bool = False) -> bool:
        raw_value = cls.get_setting_value(key, str(default))
        return raw_value.strip().lower() in {"1", "true", "yes", "y", "on"}

    ##########################################################################
    # Utility method to get required environment variables with error handling.
    ##########################################################################
    @staticmethod
    def get_required_env(key: str) -> str:
        """
        Return a required environment variable after trimming whitespace and quotes.

        :param key: Environment variable name.
        :type key: str
        :return: Cleaned environment variable value.
        :rtype: str
        :raises ValueError: If the environment variable is missing or empty.
        """
        value = os.getenv(key)
        if not value:
            raise ValueError(f"Missing required environment variable: {key}")
        return value.strip().strip("'\"")

    ###########################################################################
    # Utility method to convert common "truthy" strings to boolean values.
    ###########################################################################
    @staticmethod
    def env_bool(name: str, default: bool = False) -> bool:
        """
        Convert an environment variable to a boolean.

        :param name: Environment variable name.
        :type name: str
        :param default: Value to use if the variable is not set.
        :type default: bool
        :return: Parsed boolean value.
        :rtype: bool
        """
        raw = os.getenv(name)
        if raw is None:
            return default
        return raw.strip().lower() in {"1", "true", "yes", "y", "on"}

    ###################################################################
    # Utility method to mask sensitive information in logs and representations.
    ####################################################################
    @staticmethod
    def _mask_key(value: Optional[str]) -> Optional[str]:
        """
        Mask a sensitive string for safe display.

        :param value: Secret value to mask.
        :type value: Optional[str]
        :return: Masked value.
        :rtype: Optional[str]
        """
        if not value:
            return None
        s = str(value)
        return f"{s[:4]}...{s[-4:]}" if len(s) > 8 else "***"

    ##################################################################
    # set and get Functions
    ##################################################################
    def set_logger(self, logger: logging.Logger) -> None:
        self.logger = logger

    def get_logger(self) -> logging.Logger:
        if self.logger is None:

            # Avoid import-time failures: lazily create a logger the first time it's requested.
            self.logger = setup_logger(LOGGER_PROJECT_NAME)
            self.logger.info("logger Started!")
        return self.logger

    def get_llm(self) -> ChatOpenAI:
        """Return initialized LLM, initializing it once if needed."""

        return get_llm_or_init(
            self,
            temperature=0.0,
            streaming=True,
        )

    def get_program_working_root_dir(self) -> Path:
        return self.output_dir

    # main_dir = output_dir / "chat_gpt"
    def get_program_output_dir(self) -> Path:
        return self.output_dir / "chat_gpt"

    # chunks_dir = main_dir / "chunks"
    def get_chunks_dir(self) -> Path:
        return self.get_program_output_dir() / "chunks"

    # db_dir = main_dir / "db"
    def get_db_dir(self) -> Path:
        return self.get_program_output_dir() / "db"

    # main_dir = output_dir / "chat_gpt" / output_file_name
    def get_output_file_path(self) -> Path:
        return self.get_program_output_dir() / self.output_file_name

    # getcustom_header_path
    def get_custom_header_dir(self) -> Path:
        custom_header_path = self.get_program_output_dir() / "header"
        return custom_header_path

    def get_custom_header_location(self) -> Path:
        custom_header_location = self.get_custom_header_dir() / self.custom_header_name
        return custom_header_location

    def get_custom_header_beginning_location(self) -> Path:
        custom_header_location = (
            self.get_custom_header_dir() / self.custom_header_beginning_name
        )
        return custom_header_location

    # if setup_config.python_project_flag:
    #     if setup_config.include_tests_flag and "tests" in EXCLUDED_PYTHON_DIRS:
    #         EXCLUDED_PYTHON_DIRS.remove("tests")

    # get project type based on flags return "python" or "next_js" defalut to "python"
    def get_project_type(self) -> str:
        if self.python_project_flag:
            return "python"
        elif self.next_js_project_flag:
            return "next_js"
        else:
            return "python"

    """
    setup_config = c_setup_config.get_instance()
    print(setup_config)
    ##########################################
    setup_config = c_setup_config.get_instance()
    config_repr = repr(setup_config)
    print(config_repr)
    """

    def __repr__(self) -> str:
        """
        Return a readable string representation of the config object.

        :return: Readable configuration summary.
        :rtype: str
        """
        return (
            "c_setup_config("
            f"testing_flag={self.testing_flag!r}, "
            f"testing_flag2={self.testing_flag2!r}, "
            f"log_prompt_flag={self.log_prompt_flag!r}, "
            f"max_chunk_size_bytes={self.max_chunk_size_bytes!r}, "
            f"openai_model={self.openai_model!r}, "
            f"llm={'Initialized' if self.llm else 'Not Initialized'}, "
            f"logger={'Initialized' if self.logger else 'Not Initialized'}"
            ")"
        )

    # setup_config.logger.info(f"Configuration Status: {setup_config.to_dict()}")
    """
    import json

    config_json = json.dumps(setup_config.to_dict(), indent=4)
    print(config_json)
    #################################
    setup_config = c_setup_config.get_instance()
    config_dict = setup_config.to_dict()
    print(config_dict)

    """

    def to_dict(self) -> dict:
        """
        Convert the configuration object to a plain dictionary.

        :return: Dictionary view of current config and runtime state.
        :rtype: dict
        """
        return {
            "testing_flag": self.testing_flag,
            "testing_flag2": self.testing_flag2,
            "log_prompt_flag": self.log_prompt_flag,
            "max_chunk_size_bytes": self.max_chunk_size_bytes,
            "openai_model": self.openai_model,
            "llm_initialized": self.llm is not None,
            "logger_initialized": self.logger is not None,
        }

    # a validate_initialization method that is called after all necessary fields are set.
    def validate_initialization(self) -> None:
        """
        Validate that required runtime objects and environment values are initialized.

        :raises ValueError: If required dependencies are missing.
        """
        if self.logger is None:
            raise ValueError("logger must be initialized.")

        if self.llm is None:
            raise ValueError("llm must be initialized.")

        apikey = os.getenv("OPENAI_API_KEY", "").strip()
        if not apikey:
            self.logger.error("OPENAI_API_KEY environment variable not set")
            raise ValueError("OPENAI_API_KEY environment variable not set")

        if len(apikey) < 20:
            self.logger.error("OPENAI_API_KEY looks too short to be valid")
            raise ValueError("OPENAI_API_KEY looks too short to be valid")

    """
        Pydantic normally expects fields to be “pydantic-friendly” types (str/int/dict/BaseModel/etc). You have fields like:

        llm: Optional[ChatOpenAI]

        logger: Optional[logging.Logger]

        tavily_client: Optional[TavilyClient]

        Those are “arbitrary” Python objects. Setting arbitrary_types_allowed=True tells Pydantic: 
        “Don't try to validate/parse these types—just allow them as-is.” 
        This is the standard Pydantic v2 way to configure a model via model_config    
    """
    model_config = ConfigDict(arbitrary_types_allowed=True)
