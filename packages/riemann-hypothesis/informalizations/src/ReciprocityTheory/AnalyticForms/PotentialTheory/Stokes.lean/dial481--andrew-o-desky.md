---
{
  "module": "src/ReciprocityTheory/AnalyticForms/PotentialTheory/Stokes.lean",
  "declarations": [
    "ReciprocityTheory.AnForm.M.byPartsSymm",
    "ReciprocityTheory.AnForm.M.massIndep"
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

## Symmetry of integration by parts for local potentials

[Theorem AG.0219](https://andrewodesky.com/rh/lean/ReciprocityTheory.AnForm.M.byPartsSymm/)

Let $X$ be a compact Hausdorff space with a finite holomorphic atlas of complex dimension $e+1$, where $e\ge0$. Let $v,w:X\to\mathbb R$ be smooth, and let $\Phi_1,\ldots,\Phi_e$ be systems of smooth real local potentials whose differences on overlaps are locally real parts of holomorphic functions. Then $$\int_X v\,dd^cw\wedge dd^c\Phi_1\wedge\cdots\wedge dd^c\Phi_e=\int_X w\,dd^cv\wedge dd^c\Phi_1\wedge\cdots\wedge dd^c\Phi_e.$$

## Mixed potential mass is unchanged by smooth perturbations

[Theorem AG.1188](https://andrewodesky.com/rh/lean/ReciprocityTheory.AnForm.M.massIndep/)

Let $X$ be a compact Hausdorff space with a finite holomorphic atlas of complex dimension $e\ge0$. Let $\Phi_1,\ldots,\Phi_e$ be systems of smooth real local potentials whose differences on overlaps are locally real parts of holomorphic functions, and let $u_1,\ldots,u_e:X\to\mathbb R$ be smooth. Write $\mathcal M(\Phi_1,\ldots,\Phi_e)$ for the integral of their mixed Levi density, with the mixed Levi-density normalization of ([Measure associated with positive mixed potentials](https://andrewodesky.com/rh/lean/ReciprocityTheory.AnForm.M.maMeasure_thm/)). Then $$\mathcal M(\Phi_1+u_1,\ldots,\Phi_e+u_e)=\mathcal M(\Phi_1,\ldots,\Phi_e).$$ Here adding a global function to a system of local potentials means adding it to every local representative.
