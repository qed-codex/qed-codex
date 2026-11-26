---
{
  "module": "src/Development/EtaleCohomology/EtaleSheaves/StrictHenselColimits/EtaleLiftToStrictLocalRingUniqueOnResidueField.lean",
  "declarations": [
    "LateralTheory.E.ColimPf.RigidPf.etale_lift_to_strict_local_ring_unique_on_residue_field"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Etale maps into a ring are determined by their residue map

[Theorem AG.0758](https://andrewodesky.com/rh/lean/LateralTheory.E.ColimPf.RigidPf.etale_lift_to_strict_local_ring_unique_on_residue_field/)

Let $A,B,O$ be commutative rings, let $\Omega$ be a field, and let $\psi:O\to\Omega$ be a ring homomorphism such that every $x\in O$ with $\psi(x)\ne0$ is a unit. Let $g:A\to B$ be etale. If ring homomorphisms $u,v:B\to O$ satisfy $$u\circ g=v\circ g,\qquad\psi\circ u=\psi\circ v,$$ then $u=v$.
