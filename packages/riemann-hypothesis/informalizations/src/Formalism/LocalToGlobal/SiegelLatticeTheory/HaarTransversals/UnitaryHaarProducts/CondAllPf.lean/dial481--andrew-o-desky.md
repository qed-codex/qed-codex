---
{
  "module": "src/Formalism/LocalToGlobal/SiegelLatticeTheory/HaarTransversals/UnitaryHaarProducts/CondAllPf.lean",
  "declarations": [
    "Formalism.L2.SG.Pf.conductor_inverse_different"
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

## The conductor of a standard local additive character

[Theorem ANT.0822](https://andrewodesky.com/rh/lean/Formalism.L2.SG.Pf.conductor_inverse_different/)

Let $F$ be a totally real number field and $\psi:\mathbb A_F\to\mathbb C^\times$ a continuous nontrivial unitary additive character, trivial on $F$, with $$\psi_\infty((x_\tau)_\tau)=\exp\left(2\pi i\sum_{\tau:F\hookrightarrow\mathbb R}x_\tau\right).$$ For a finite place $v$, let $\psi_v$ be its local component and choose $d_v\in F_v$ generating the localization of the different of $F/\mathbb Q$. Then, for every $x\in F_v$, $$\bigl(\psi_v(xy)=1\text{ for every }y\in\mathcal O_{F_v}\bigr) \quad\Longleftrightarrow\quad d_vx\in\mathcal O_{F_v}.$$
