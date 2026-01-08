"""Fragua Environment Configuration."""

import fragua as fg
import fragua_sets as fs

# Create fragua environment
env = fg.FraguaEnvironment("env-example")

# Add pre-configurated sets from fragua-sets
pre_fg_sets = fs.FRAGUA_SETS
env.add_sets(*pre_fg_sets)

ENV = env
