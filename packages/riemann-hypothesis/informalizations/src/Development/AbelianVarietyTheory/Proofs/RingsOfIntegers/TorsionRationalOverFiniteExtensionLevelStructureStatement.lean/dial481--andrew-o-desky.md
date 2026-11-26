---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/TorsionRationalOverFiniteExtensionLevelStructureStatement.lean",
  "declarations": [
    "GlobalTheory.T.torsion_rational_over_finite_extension_level_structure"
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

## Rational torsion and an integral-module parametrization

[Theorem AV.0221](https://andrewodesky.com/rh/lean/GlobalTheory.T.torsion_rational_over_finite_extension_level_structure/)

Fix the unitary moduli datum of ([Powers of a theta-coordinate bundle and the Hodge bundle](https://andrewodesky.com/rh/lean/GlobalTheory.T.theta_map_pull_O1_power_hodge/)): a CM number field $E$ with its specified conjugation and polarizing data, a finite projective $\mathcal O_E$-module $\Lambda$ with its integral alternating pairing and signature data, and a permitted level and representing moduli scheme $X$. Let $x:\operatorname{Spec}K\to X$ be a field-valued point and $A_x$ its universal abelian variety with $\mathcal O_E$-action. Let $M\ge1$.

There is a finite field extension $L/K$ over which all $M$-torsion of $A_x$ is rational. If all $M$-torsion is already rational over $K$, this remains true after every field embedding $K\to L'$, and there is an additive $\mathcal O_E$-linear map $$e:\Lambda\longrightarrow A_x(K)$$ with $\ker e=M\Lambda$, whose image contains every $P\in A_x(K)$ satisfying $MP=0$.
