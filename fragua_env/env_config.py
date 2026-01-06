"""Fragua Environment Configuration."""

import fragua as fg
import fragua_sets as fs

from .pipelines.pipelines_config import add_pipelines_set_to_registry

# Create fragua environment

env = fg.FraguaEnvironment("env-example")

# Get environment registry
registry = env.registry

# Add pre-configurated sets from fragua-sets
fs.add_sets_to_registry(fs.SETS_LIST, registry)

# Add pipelines set to registry
# The function was created in this project.
add_pipelines_set_to_registry(registry)

ENV = env
