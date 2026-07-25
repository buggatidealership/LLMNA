#!/usr/bin/env python3
"""
memory_gp_bridge.py — GROSS-PROFIT BRIDGE for the memory complex (built 2026-07-10, user question:
'what must be true for GM reduction to be offset by unit-price increases, for DRAM/HBM and NAND?').

Identity: GP = Units x ASP x GM%, and GM = 1 - c/p (c = unit cost, p = ASP).
The identity forces every 'GM falls but profits hold' story into exactly one of two mechanisms:
  PRICE-DRIVEN (c constant, p falls): brutal — GM 88->70 means ASP -58%, GP/unit -67%, need 3x units.
  COST-DRIVEN  (p RISES, c rises faster — mix shift to HBM4/HBF class product): GM% falls as an
    ARTIFACT while GP dollars/unit GROW. This is the only benign path.
Adjudication per print: decompose each memory maker's ΔGP into Δunits x ΔASP x ΔGM and check the
SIGN OF ASP alongside the GM move. GM down + ASP down = commodity crack (Lens 2). GM down + ASP up
= mix/cost artifact (Lens 3) — do not sell the artifact.

Usage: python3 research/meta/scripts/memory_gp_bridge.py            (prints standard tables)
       import and call bridge(u, asp, gm) ratios per print for the decomposition.
"""

def rev_needed(g1, g2):
    """Revenue growth required to hold GP dollars flat through a GM slide g1 -> g2."""
    return g1 / g2 - 1

def price_driven(g1, g2):
    """Constant unit cost: implied ASP change, GP/unit change, units needed to offset."""
    pr = (1 - g1) / (1 - g2)          # ASP ratio
    gpu = pr * g2 / g1                # GP-per-unit ratio
    return pr - 1, gpu - 1, 1 / gpu

def cost_driven(g1, asp_up, cost_up):
    """ASP rises, unit cost rises faster (mix shift): resulting GM and GP/unit change."""
    gp_ratio = ((1 + asp_up) - (1 - g1) * (1 + cost_up)) / g1
    gm2 = 1 - (1 - g1) * (1 + cost_up) / (1 + asp_up)
    return gm2, gp_ratio - 1

def bridge(units_ratio, asp_ratio, gm1, gm2):
    """Full decomposition: returns (revenue ratio, GP ratio)."""
    rev = units_ratio * asp_ratio
    return rev, rev * gm2 / gm1

if __name__ == "__main__":
    print("LENS 1 — revenue growth to hold GP flat (GP flat <=> Rev2/Rev1 = g1/g2):")
    for g1, g2 in [(0.875, 0.80), (0.875, 0.70), (0.90, 0.70), (0.80, 0.70), (0.90, 0.60)]:
        print(f"  GM {g1:.0%}->{g2:.0%}: revenue {rev_needed(g1,g2):+.1%}")
    print("LENS 2 — price-driven (commodity) decline at constant cost:")
    for g1, g2 in [(0.875, 0.80), (0.875, 0.70), (0.90, 0.70)]:
        dp, dgpu, ux = price_driven(g1, g2)
        print(f"  GM {g1:.0%}->{g2:.0%}: ASP {dp:+.0%}, GP/unit {dgpu:+.0%}, units x{ux:.2f} to offset")
    print("LENS 3 — cost-driven (mix-shift) decline with ASP rising:")
    for g1, x, y in [(0.60, 0.40, 0.60), (0.60, 0.30, 0.50), (0.75, 0.25, 0.60), (0.70, 0.50, 0.80)]:
        gm2, dgp = cost_driven(g1, x, y)
        print(f"  g1={g1:.0%}, ASP {x:+.0%}, cost {y:+.0%}: GM->{gm2:.1%} but GP/unit {dgp:+.1%}")
