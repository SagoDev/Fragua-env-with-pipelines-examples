"""Fragua Environment Configuration."""

import fragua as fg
import fragua_sets as fs

from fragua_env.functions.functions_config import add_transformation_set_to_registry

from .pipelines.pipelines_config import add_pipelines_set_to_registry

# Create fragua environment

env = fg.FraguaEnvironment("env-example")

# Get environment registry
registry = env.registry

# Add pre-configurated sets from fragua-sets
fs.add_sets_to_registry(fs.SETS_LIST, registry)


# The following functions were created in this project.

# Add pipelines set to registry
add_pipelines_set_to_registry(registry)

# Add transformation set to registry
add_transformation_set_to_registry(registry)


ENV = env
