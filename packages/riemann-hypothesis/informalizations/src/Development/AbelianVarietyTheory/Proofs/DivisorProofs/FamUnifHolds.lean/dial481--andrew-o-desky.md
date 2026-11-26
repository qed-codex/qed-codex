---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/FamUnifHolds.lean",
  "declarations": [
    "GlobalTheory.PeriodFamily.famUnif_holds"
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

## Holomorphic variation of period lattices

[Theorem AV.1471](https://andrewodesky.com/rh/lean/GlobalTheory.PeriodFamily.famUnif_holds/)

Let $B$ be a finitely generated complex algebra, and let $\mathcal A\to\operatorname{Spec}B$ be an abelian scheme smooth of relative dimension $g$. Let $I$ be finite, $U\subset\mathbb C^I$ open with $0\in U$, and let $y_z:B\to\mathbb C$ be algebra homomorphisms such that $z\mapsto y_z(b)$ is holomorphic on $U$ for every $b\in B$. For every $z\in\mathbb C^I$, choose a group-scheme fibre $A_z$, its pullback map $\phi_z:A_z\to\mathcal A$, and a line bundle $L_z$ on $A_z$. Choose also a fibre $A_0'$ at $y_0$, with map $\phi_0'$, a line bundle $L_0'$ and a holomorphic uniformization $e_0:\mathbb C^g\to A_0'(\mathbb C)$ with lattice $\Lambda_0$ and a nowhere-zero holomorphic trivialization of $e_0^*L_0'$.

There exist $r>0$ with $B_r(0)\subseteq U$, holomorphic uniformizations $e_z:\mathbb C^g\to A_z(\mathbb C)$ with period lattices $\Lambda_z$ and holomorphic trivializations of $e_z^*L_z$, and additive isomorphisms $t_z:\Lambda_0\to\Lambda_z$, for all $z\in\mathbb C^I$, such that $(z,w)\mapsto\phi_z(e_z(w))$ is holomorphic on $B_r(0)\times\mathbb C^g$. The identity points of all fibres in this ball map into one affine open subset of $\mathcal A$; moreover, $$\phi_0e_0^{\mathrm{new}}=\phi_0'e_0,\qquad t_0(\lambda)=\lambda,$$ and $z\mapsto t_z(\lambda)\in\mathbb C^g$ is holomorphic on the ball for every $\lambda\in\Lambda_0$.

If a group endomorphism $\alpha$ of $\mathcal A$ has a complex-linear lift $M_0$ through $e_0$, then for every $z\in B_r(0)$ it has a complex-linear lift $M_z$ through $e_z$, and $$\lambda'=M_0\lambda\ \Longrightarrow\ t_z(\lambda')=M_zt_z(\lambda)\qquad(\lambda,\lambda'\in\Lambda_0).$$
