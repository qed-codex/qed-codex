---
{
  "module": "src/Formalism/HermitianCurvature/HermitianCurvatureProofs/TwoByOneBlock.lean",
  "declarations": [
    "Formalism.FourierDecayAlt.P.rank_one_integration_formula"
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

## Integration on a rank-one unitary factor

[Theorem REP.0856](https://andrewodesky.com/rh/lean/Formalism.FourierDecayAlt.P.rank_one_integration_formula/)

Let $k\ge1$, $r\ge0$, and let $V=\mathbb C^{2r+k+1}$ have a Hermitian form consisting of $r$ hyperbolic planes and an orthogonal middle space $W=\mathbb C^{k+1}$ with Gram matrix $J=\operatorname{diag}(1_k,-1)$. Fix a hyperbolic basis outside $W$. Let $G_0$ be the subgroup of $U(V)$ fixing every vector in that basis, and let $\iota:U(J)\to G_0$ act as the identity outside $W$.

Choose $z,z'\in W$ with $$T=-z^*Jz>0,\qquad T'=-(z')^*Jz'>0,$$ and let $K_z,K_{z'}\subseteq G_0$ be their stabilizers. Let $\mu:\mathbb C\to M_{k+1}(\mathbb C)$ be smooth on $\{|\zeta|^2>TT'\}$ and satisfy, there, $$\mu(\zeta)^*J\mu(\zeta)=J,\qquad z^*J\mu(\zeta)z'=\zeta.$$ Give $G_0,K_z,K_{z'}$ measures $dg,dh,dh'$ as in the conventions. There is $C>0$ such that, for every nonnegative measurable function $f$ on the ambient matrix space, $$\int f(g)\,dg =C\int_{\mathbb C}w(\zeta)\int f\bigl(h^{-1}\iota(\mu(\zeta))h'\bigr)\,dh\,dh'\,d\zeta,$$ where $d\zeta$ is Lebesgue measure on $\mathbb C$ and $$w(\zeta)=\begin{cases}(|\zeta|^2-TT')^{k-1},&|\zeta|^2\ge TT',\\0,&|\zeta|^2<TT'.\end{cases}$$
