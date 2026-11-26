---
{
  "module": "src/Formalism/SharpRestriction/GlobalSchurBounds/GeneralLinearActions/FrameTransport.lean",
  "declarations": [
    "Formalism.MainNotions.GlobalTheoryTheory.GenusMassVolumes.GaugeFam",
    "Formalism.MainNotions.GlobalTheoryTheory.GenusMassVolumes.GaugeFam.IsGauge"
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

## Compatible adelic unitary measures

[Definition / hypothesis ARAK.D121](https://andrewodesky.com/rh/lean/Formalism.MainNotions.GlobalTheoryTheory.GenusMassVolumes.GaugeFam/)

Hypothesis (compatible unitary measures). Let $E/F$ and its conjugation be as in ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)). For every size $M$ and matrix $J\in M_M(E)$, choose a measure $\mu_J$ on the adelic unitary group $G_J(\mathbb A_F)$. When $J$ is a nondegenerate Hermitian matrix, require $\mu_J$ to be Haar measure.

If $J$ is nondegenerate Hermitian, $P\in\mathrm{GL}_M(E)$ and $J'=\bar P^TJP$, there must exist group isomorphisms $e:G_J(\mathbb A_F)\to G_{J'}(\mathbb A_F)$ satisfying $gP=Pe(g)$. Every such isomorphism must satisfy $e_*\mu_J=\mu_{J'}$.

The following compatibility is required for every $M+1\ge3$, nondegenerate Hermitian $J$ of size $M+1$, vector $x\in E^{M+1}$ of nonzero norm $\beta\in F$, and matrix $B$ whose columns are perpendicular to $x$ and for which $J'=\bar B^TJB$ is nondegenerate. Write $H_x$ for the stabilizer of $x$ in $G_J(\mathbb A_F)$. There must exist continuous nontrivial unitary additive characters $\psi:\mathbb A_F/F\to\mathbb C^\times$. For every such $\psi$, there must exist measures $\nu_{\psi,\beta}$ on $(\mathbb A_F\otimes_FE)^{M+1}$ with the fiber normalization below. There must also exist group isomorphisms $e:H_x\to G_{J'}(\mathbb A_F)$ satisfying $gB=Be(g)$. For every such $e$, every normalized $\nu_{\psi,\beta}$, every nonnegative measurable $f$ and every orbit section $s$ with $s(y)x=y$ on the orbit of $x$, require $$\int_{G_J(\mathbb A_F)}f(g)\,d\mu_J(g)=\int_y\int_{H_x}f(s(y)h)\,d(e^{-1}_*\mu_{J'})(h)\,d\nu_{\psi,\beta}(y).$$ No measurability condition on the section is added to this assertion.
