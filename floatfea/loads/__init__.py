"""Mapping FloatSim loads onto the FE mesh, and the equilibrium check (F4).

Never invent a load distribution. If a record carries no strip or panel data,
refuse to build the load case rather than assuming one.
"""
